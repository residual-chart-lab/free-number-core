#!/usr/bin/env python3
"""Audit Note 26 with component quaternion products and a third-prime rank.

Inputs are the defining matrices from the production certificate. This is
an independent check of their literal-response meaning and rank arithmetic,
not a second independent construction of the whole theory. No production
XOR/sign-table multiplication or C++ RREF is used by the comparison checks.
"""
from pathlib import Path
from itertools import combinations, product
import argparse
import hashlib
import json
import sys
import time

import numpy as np
from scipy import sparse

if not __debug__:
    raise RuntimeError('Audit requires assertions; omit -O and -OO.')

HERE = Path(__file__).resolve().parent
CANDIDATES = (HERE.parent/'certificates', HERE.parents[2]/'certificates')
CERT = next(p for p in CANDIDATES if p.is_dir())
sys.path.insert(0, str(CERT))
import n8_222_redetection_certificate as c
from n6_response_4simplex_modular_certificate import rank_mod

P = 1019
BASIS = np.eye(4, dtype=np.int64)

def log(*args):
    print(time.strftime('%H:%M:%S'), *args, flush=True)

def mul(x, y):
    """Expanded Hamilton product, with ordinary signed integer components."""
    a,b,d,e = np.moveaxis(x, -1, 0)
    f,g,h,k = np.moveaxis(y, -1, 0)
    return np.stack((a*f-b*g-d*h-e*k,
                     a*g+b*f+d*k-e*h,
                     a*h-b*k+d*f+e*g,
                     a*k+b*h-d*g+e*f), axis=-1)

def rank(a):
    # Forward-only NumPy elimination, Python modular inverse and opposite
    # row/column order distinguish this from the production C++ RREF.
    return rank_mod(a[::-1, ::-1], P)

def literal_factorizations(n, support, D):
    """All state basis tensors and all probe basis tensors, no sampling."""
    states = np.array(list(product(range(1,4), repeat=n)))
    probes = np.array(list(product(range(1,4), repeat=n-3)))
    ed,fd = 4*3**(n-3),4*3**(n-2)
    J = c.encoder(n-3)
    comparisons = 0
    for ei,edge in enumerate(combinations(support,2)):
        gaps = [g for g in range(1,n) if g not in edge]
        probed = {g:j for j,g in enumerate(gaps)}
        shadows = []
        for endpoint,sign in ((edge[0],1),(edge[1],-1)):
            ix = support.index(endpoint)
            block = D[ei*ed:(ei+1)*ed,ix*fd:(ix+1)*fd]
            shadows.append(sign*(sparse.csr_matrix(block).T @ J.T).T)
        for start in range(0,len(states),96):
            word = states[start:start+96]
            value = np.broadcast_to(BASIS[0], (len(probes),len(word),4)).copy()
            for i in range(n,0,-1):
                value = mul(value, BASIS[word[None,:,i-1]])
                if i-1 in probed:
                    value = mul(value, BASIS[probes[:,None,probed[i-1]]])
            for endpoint,shadow in zip(edge,shadows):
                pair = mul(BASIS[word[:,endpoint]],BASIS[word[:,endpoint-1]])
                h = np.argmax(np.abs(pair), axis=1)
                sign = pair[np.arange(len(word)),h]
                ix = h.copy()
                for state_index in range(n):
                    if state_index not in (endpoint-1,endpoint):
                        ix = 3*ix + word[:,state_index]-1
                expected = (shadow[:,ix]*sign).reshape(len(probes),4,len(word)).transpose(0,2,1)
                assert np.array_equal(value,expected), (n,edge,endpoint,start)
                comparisons += len(word)*len(probes)
        log('all literal state/probe products agree', n, edge)
    return comparisons

def run(output):
    records = []
    quotients = {}
    for n,support,dimension in (
        (7,(1,2,4,6),144), (7,(1,3,4,6),148),
        (7,(1,3,5,6),144), (8,(1,3,5,7),444),
    ):
        L,D = c.exact_quotient(n,support)
        assert len(L)==dimension
        cg,fg = np.tile(c.grades(n-3),6),np.tile(c.grades(n-2),4)
        blocks = []
        for g in range(4):
            rows,cols = np.flatnonzero(cg==g),np.flatnonzero(fg==g)
            assert not np.count_nonzero(D[np.ix_(rows,np.flatnonzero(fg!=g))])
            blocks.append(rank(D[np.ix_(rows,cols)]))
        assert sum(blocks)==D.shape[0]-dimension
        assert rank(L)==dimension
        log('independent matching lower bound', n,support,blocks,sum(blocks))
        count = literal_factorizations(n,support,D)
        records.append({'n':n,'support':list(support),'quotient_dimension':dimension,
                        'matching_rank_mod_1019':sum(blocks),'graded_ranks':blocks,
                        'literal_quaternion_value_comparisons':count})
        quotients[support] = L,D

    l,d = quotients[(1,3,4,6)]
    L,D = quotients[(1,3,5,7)]
    edges = tuple(combinations((1,3,5,7),2))
    er = [rank(L[:,972*i:972*(i+1)]) for i in range(6)]
    assert er==[432,336,408,120,336,432]
    assert rank(np.concatenate((L[:,:972],L[:,5*972:]),axis=1))==432
    k,K = c.residual(4),c.residual(5)
    assert rank(k)==4 and rank(K)==12
    assert not np.count_nonzero((sparse.csr_matrix(K)@sparse.csr_matrix(D)).toarray())
    comparisons = []
    for parent,new,ei,hand in (((1,2,4,6),2,0,'right'),((1,3,5,6),6,5,'left')):
        lp,_ = quotients[parent]
        pos = [g for g in range(1,8) if g not in edges[ei]].index(new)
        scale,I = c.exact_suspension(pos,hand)
        A = (sparse.csr_matrix(L[:,972*ei:972*(ei+1)])@sparse.csr_matrix(I)).toarray()
        B = np.kron(lp[:,324*ei:324*(ei+1)],np.eye(3,dtype=np.int64))
        values = [rank(A),rank(B),rank(np.concatenate((A,B)))]
        assert values==[432,432,432]
        comparisons.append({'parent':list(parent),'ranks_mod_1019':values})
    suspensions = [c.exact_suspension([g for g in range(1,8) if g not in e].index(4),'right') for e in edges]
    scale = int(np.lcm.reduce([s for s,I in suspensions]))
    A = np.concatenate([(sparse.csr_matrix(L[:,972*i:972*(i+1)])@sparse.csr_matrix((scale//s)*I)).toarray()
                        for i,(s,I) in enumerate(suspensions)],axis=1)
    O = (sparse.csr_matrix(A)@sparse.kron(sparse.csr_matrix(d),sparse.eye(3,dtype=np.int64))).toarray()
    assert rank(O)==432
    log('independent edge, parent comparison and obstruction ranks agree')
    result = {'status':'passed','third_prime':P,
        'rank_algorithm':'NumPy forward elimination, reversed rows/columns; Python modular inverse',
        'quaternion_algorithm':'four expanded Hamilton components; all basis states and probes',
        'input_boundary':'Production defining matrices; independently checked literal meaning and arithmetic. Not an external referee report.',
        'certificate_source_sha256':c.SOURCE_HASH,
        'audit_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'objects':records,'edge_ranks_mod_1019':er,'parent_comparisons':comparisons,
        'full_suspension_obstruction_rank_mod_1019':432,
        'literal_quaternion_value_comparisons':sum(r['literal_quaternion_value_comparisons'] for r in records)}
    Path(output).write_text(json.dumps(result,indent=2)+'\n')
    log('ALL CHECKS PASSED')

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='audit-independent-result.json')
    run(p.parse_args().output)
