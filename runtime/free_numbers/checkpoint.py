"""Lossless, known-operation DAG checkpoints requiring a trusted outer hash.

This is a structural replay format, not a signature or a TE occurrence receipt.
Every retained exact value survives, including values unused by the last query.
"""
from fractions import Fraction as Q
from hashlib import sha256
import json
from .algebra import canonical
from .expression import Tensor, Circuit, Channel, Observation
from .retention import Vault


def _postorder(roots):
    seen, result = set(), []
    def visit(node):
        if node.digest in seen:
            return
        seen.add(node.digest)
        if type(node) is Circuit and node.kind == 'read':
            visit(node.data[0])
        for child in node.children:
            visit(child)
        result.append(node)
    for root in roots:
        if type(root) is not Circuit:
            raise ValueError('checkpoint roots must be observation circuits')
        visit(root)
    return result


def dumps(roots, vault):
    roots = tuple(roots)
    nodes = []
    for node in _postorder(roots):
        record = {'id':node.digest, 'type':'tensor' if type(node) is Tensor else 'circuit',
                  'kind':node.kind, 'children':[c.digest for c in node.children]}
        if type(node) is Tensor:
            record['grade'] = node.grade
            if node.kind == 'retained':
                vault.verify(node.data[0])
                record['data'] = [node.data[0].key]
            else:
                record['data'] = node.data
        elif node.kind == 'read':
            tensor, obs = node.data
            record['data'] = {'tensor':tensor.digest, 'grade':obs.grade,
                'channels':[(c.gaps,c.weight,c.left,c.right) for c in obs.channels]}
        else:
            record['data'] = node.data
        nodes.append(record)
    values = [(r.key,value,r.envelope,r.origin,r.digest) for r,value in vault._records()]
    payload = canonical({'format':'free-numbers-demand-dag-v1', 'nodes':nodes,
                         'roots':[r.digest for r in roots], 'retained':values})
    return payload, sha256(payload).hexdigest()


def _object(pairs):
    d = {}
    for key, value in pairs:
        if key in d:
            raise ValueError('duplicate JSON keys are not allowed')
        d[key] = value
    if set(d) == {'q'}:
        v = d['q']
        if type(v) is not list or len(v) != 2 or any(type(a) is not str for a in v):
            raise ValueError('invalid exact rational record')
        q = Q(int(v[0]),int(v[1]))
        if v != [str(q.numerator),str(q.denominator)]:
            raise ValueError('rational records must be normalized')
        return q
    return d


def _freeze(x):
    if type(x) is list:
        return tuple(_freeze(v) for v in x)
    return x


def loads(payload, expected_sha256):
    if type(payload) is not bytes or not isinstance(expected_sha256,str) or sha256(payload).hexdigest() != expected_sha256:
        raise ValueError('a matching externally trusted checkpoint hash is required')
    if len(payload) > 20_000_000:
        raise ValueError('checkpoint byte budget exceeded')
    def reject(value):
        raise ValueError('JSON floating values are not part of the exact format')
    doc = json.loads(payload.decode('utf-8'), object_pairs_hook=_object,
                     parse_float=reject, parse_constant=reject)
    if (type(doc) is not dict or set(doc) != {'format','nodes','roots','retained'} or
            doc['format'] != 'free-numbers-demand-dag-v1' or type(doc['nodes']) is not list or
            type(doc['roots']) is not list or type(doc['retained']) is not list or
            len(doc['nodes']) > 10000 or len(doc['retained']) > 10000):
        raise ValueError('unknown checkpoint schema or resource budget exceeded')
    vault, seen_keys = Vault(), set()
    for key,value,envelope,origin,digest in doc['retained']:
        if key in seen_keys:
            raise ValueError('duplicate retained reference')
        seen_keys.add(key)
        ref = vault.register(key,value,envelope,origin)
        if ref.digest != digest:
            raise ValueError('the exact value, bound or provenance changed')
    nodes = {}
    for record in doc['nodes']:
        expected_keys = {'id','type','kind','children','data'}
        if record.get('type') == 'tensor':
            expected_keys.add('grade')
        if set(record) != expected_keys or record['id'] in nodes:
            raise ValueError('invalid or duplicate graph record')
        try:
            children = tuple(nodes[key] for key in record['children'])
            kind, data = record['kind'], record['data']
            if record['type'] == 'tensor':
                if kind == 'retained':
                    if type(data) is not list or len(data) != 1:
                        raise ValueError('invalid retained node')
                    data = (vault.reference(data[0]),)
                else:
                    data = _freeze(data)
                node = Tensor(kind,record['grade'],data,children)
            elif record['type'] == 'circuit':
                if kind == 'read':
                    if type(data) is not dict or set(data) != {'tensor','grade','channels'}:
                        raise ValueError('invalid observation record')
                    obs = Observation(data['grade'],tuple(Channel(_freeze(g),w,_freeze(l),_freeze(r))
                        for g,w,l,r in data['channels']))
                    data = (nodes[data['tensor']],obs)
                else:
                    data = _freeze(data)
                node = Circuit(kind,data,children)
            else:
                raise ValueError('unknown graph type')
        except (KeyError, TypeError, IndexError) as exc:
            raise ValueError('invalid or non-topological operation graph') from exc
        if node.digest != record['id']:
            raise ValueError('ordered structure or retained observation changed')
        nodes[node.digest] = node
    try:
        roots = tuple(nodes[key] for key in doc['roots'])
    except KeyError as exc:
        raise ValueError('missing checkpoint root') from exc
    if any(type(root) is not Circuit for root in roots) or len(_postorder(roots)) != len(nodes):
        raise ValueError('all operation nodes must be reachable from declared roots')
    return roots,vault
