"""Pull a concrete observation back through an ordered retained expression.

The exact dependency object is a polynomial, not a local Jacobian. It includes
mixed residual terms and repeated references. Finite symbolic or depth budgets
produce UNDETERMINED, never an assertion that a difference can be discarded.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from .algebra import (ZERO, ONE, Polynomial, ProofBudgetExceeded, primitive,
                      qmul, qscale, rational, quat, fingerprint)
from .expression import Tensor, Circuit
from .retention import Meter


@dataclass(frozen=True)
class Scope:
    entry: str
    continuation: str
    observer: str

    def __post_init__(self):
        if any(type(v) is not str or not v for v in (self.entry,self.continuation,self.observer)):
            raise ValueError('bind an entry, a declared continuation and an observer')

    @property
    def digest(self):
        return fingerprint((self.entry,self.continuation,self.observer))


@dataclass(frozen=True)
class Query:
    expression: Circuit
    scope: Scope
    purpose: str = 'exact-value'
    target: tuple = ZERO
    tolerance: Q = Q(0)

    def __post_init__(self):
        if type(self.expression) is not Circuit or type(self.scope) is not Scope:
            raise ValueError('a retained expression and an explicit scope are required')
        object.__setattr__(self, 'target', quat(self.target))
        object.__setattr__(self, 'tolerance', rational(self.tolerance))
        if self.purpose not in ('exact-value','within-l1') or (self.purpose == 'within-l1' and self.tolerance <= 0):
            raise ValueError('choose an exact read or a positive strict L1 tolerance')
        if self.purpose == 'exact-value' and (self.target != ZERO or self.tolerance):
            raise ValueError('exact reads have no acceptance target')

    @property
    def digest(self):
        return fingerprint((self.expression.digest,self.scope.digest,self.purpose,self.target,self.tolerance))


@dataclass(frozen=True)
class Policy:
    max_depth: int = 8
    precisions: tuple = (16, 32, 64, 128)
    exact_fallback: bool = True
    max_terms: int = 4096
    max_channels: int = 4096
    max_nodes: int = 10000

    def __post_init__(self):
        if type(self.max_depth) is not int or self.max_depth < 0:
            raise ValueError('a nonnegative observation-depth budget is required')
        if (type(self.precisions) is not tuple or not self.precisions or
                any(type(b) is not int or not 1 <= b <= 4096 for b in self.precisions) or
                tuple(sorted(set(self.precisions))) != self.precisions):
            raise ValueError('a finite strictly increasing dyadic precision schedule is required')
        if type(self.exact_fallback) is not bool or any(type(x) is not int or x < 1 for x in (self.max_terms,self.max_channels,self.max_nodes)):
            raise ValueError('positive finite work budgets are required')


@dataclass(frozen=True)
class Plan:
    query_digest: str
    status: str
    requested_depth: int
    coefficients: tuple = ()

    @property
    def dependencies(self):
        return tuple(sorted({key for m, _ in self.coefficients for key in m}))

    @property
    def interacting_monomials(self):
        return tuple(m for m, _ in self.coefficients if len(m) > 1)

    @property
    def digest(self):
        return fingerprint((self.query_digest,self.status,self.requested_depth,self.coefficients))


def graph_metadata(root, vault, policy):
    seen, depth, channels = set(), 0, 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node.digest in seen:
            continue
        seen.add(node.digest)
        if len(seen) > policy.max_nodes:
            raise ProofBudgetExceeded('retained DAG node budget exhausted')
        if type(node) is Circuit and node.kind == 'read':
            tensor, obs = node.data
            stack.append(tensor)
            depth = max(depth, obs.depth)
            channels += len(obs.channels)
            if channels > policy.max_channels:
                raise ProofBudgetExceeded('response channel budget exhausted')
        elif type(node) is Tensor and node.kind == 'retained':
            vault.verify(node.data[0])
        stack.extend(node.children)
    return depth


class Compiler:
    def __init__(self, vault, policy, meter):
        self.vault, self.policy, self.meter = vault, policy, meter
        self.tensor_cache, self.circuit_cache = {}, {}

    def constant(self, value):
        return Polynomial.constant(value, self.policy.max_terms)

    def tensor(self, node, gaps):
        key = (node.digest,gaps)
        if key in self.tensor_cache:
            self.meter.compile_cache_hits += 1
            return self.tensor_cache[key]
        self.meter.compiled_tensor_slices += 1
        if node.kind == 'block':
            result = self.constant(ZERO)
            for word, a in node.data:
                result = result.add(self.constant(qscale(a, primitive(word,gaps))))
        elif node.kind == 'sum':
            result = self.tensor(node.children[0],gaps).add(self.tensor(node.children[1],gaps))
        elif node.kind == 'scale':
            result = self.tensor(node.children[0],gaps).scaled(node.data[0])
        elif node.kind == 'retained':
            ref = node.data[0]
            self.vault.verify(ref)
            variable = Polynomial((((ref.key,),ONE),), self.policy.max_terms)
            result = self.tensor(node.children[0],gaps).add(variable.mul(self.tensor(node.children[1],gaps)))
        elif node.kind == 'concat':
            left, right = node.children
            a = self.tensor(left,gaps[:left.grade-1])
            b = self.tensor(right,gaps[left.grade:])
            bridge = gaps[left.grade-1]
            # A_{m+n}(x|y) = A_n(y) * bridge * A_m(x).
            result = b.mul(self.constant(ONE if bridge is None else (Q(0),)+bridge)).mul(a)
        else:
            raise ValueError('unregistered tensor operation')
        self.tensor_cache[key] = result
        return result

    def circuit(self, node):
        if node.digest in self.circuit_cache:
            self.meter.compile_cache_hits += 1
            return self.circuit_cache[node.digest]
        if node.kind == 'constant':
            result = self.constant(node.data[0])
        elif node.kind == 'read':
            tensor, obs = node.data
            result = self.constant(ZERO)
            for c in obs.channels:
                part = self.constant(c.left).mul(self.tensor(tensor,c.gaps)).mul(self.constant(c.right))
                result = result.add(part.scaled(c.weight))
        elif node.kind == 'add':
            result = self.circuit(node.children[0]).add(self.circuit(node.children[1]))
        elif node.kind == 'mul':
            result = self.circuit(node.children[0]).mul(self.circuit(node.children[1]))
        else:
            raise ValueError('unregistered observation operation')
        self.circuit_cache[node.digest] = result
        return result


def plan(query, vault, policy=Policy(), meter=None):
    if type(query) is not Query or type(policy) is not Policy:
        raise TypeError('an explicit query and policy are required')
    meter = Meter() if meter is None else meter
    depth = 0
    try:
        depth = graph_metadata(query.expression,vault,policy)
        if depth > policy.max_depth:
            return Plan(query.digest,'DEPTH_BUDGET',depth)
        poly = Compiler(vault,policy,meter).circuit(query.expression)
    except ProofBudgetExceeded:
        return Plan(query.digest,'PROOF_BUDGET',depth)
    return Plan(query.digest,'AVAILABLE',depth,tuple(sorted(poly.terms.items())))


def verify_plan(query, vault, policy, proof):
    if type(proof) is not Plan or proof != plan(query,vault,policy):
        raise ValueError('the scope, retained expression, observer or dependency witness changed')
    return True
