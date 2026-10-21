"""Rational quaternion coefficients and exact sparse parameter polynomials.

Parameters are real scalars, so their monomials commute. Quaternion coefficient
order does not commute. Cancelling complete monomials is essential: independent
first derivatives at a zero representative miss residual-residual interactions.
"""
from fractions import Fraction as Q
from hashlib import sha256
import json

ZERO = (Q(0),) * 4
ONE = (Q(1), Q(0), Q(0), Q(0))
BASIS = (ONE, (Q(0), Q(1), Q(0), Q(0)),
         (Q(0), Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(0), Q(1)))
TABLE = ((1, 2, 3, 4), (2, -1, 4, -3),
         (3, -4, -1, 2), (4, 3, -2, -1))


def rational(x):
    if type(x) not in (int, Q):
        raise TypeError('use integers or exact Fraction values, not floats')
    return Q(x)


def quat(x):
    v = tuple(map(rational, x))
    if len(v) != 4:
        raise ValueError('four rational quaternion coordinates are required')
    return v


def vector(x):
    v = tuple(map(rational, x))
    if len(v) != 3:
        raise ValueError('a three-dimensional rational probe is required')
    return v


def qadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def qscale(a, x):
    return tuple(a * b for b in x)


def qmul(x, y):
    out = [Q(0)] * 4
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            k = TABLE[i][j]
            out[abs(k)-1] += a * b * (1 if k > 0 else -1)
    return tuple(out)


def primitive(word, gaps):
    """Reversed compression, with an optional probe at each original gap."""
    out = ONE
    for i, a in enumerate(word):
        if i and gaps[i-1] is not None:
            out = qmul((Q(0),) + gaps[i-1], out)
        out = qmul(BASIS[a+1], out)
    return out


def encode(x):
    if type(x) is Q:
        return {'q': [str(x.numerator), str(x.denominator)]}
    if isinstance(x, (tuple, list)):
        return [encode(y) for y in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if x is None or type(x) in (str, int, bool):
        return x
    raise TypeError(type(x).__name__)


def canonical(x):
    return json.dumps(encode(x), sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False).encode('utf-8')


def fingerprint(x):
    return sha256(canonical(x)).hexdigest()


class ProofBudgetExceeded(Exception):
    pass


class Polynomial:
    """An exact quaternion-valued polynomial, bounded by a public work budget."""
    def __init__(self, terms=(), limit=4096):
        self.limit = limit
        d = {}
        for monomial, value in terms:
            m = tuple(sorted(monomial))
            d[m] = qadd(d.get(m, ZERO), value)
        self.terms = {m: v for m, v in d.items() if any(v)}
        if len(self.terms) > limit:
            raise ProofBudgetExceeded('symbolic monomial budget exhausted')

    @classmethod
    def constant(cls, value, limit=4096):
        return cls((((), value),), limit)

    @property
    def dependencies(self):
        return tuple(sorted({key for m in self.terms for key in m}))

    @property
    def digest(self):
        return fingerprint(tuple(sorted(self.terms.items())))

    def add(self, other):
        return Polynomial(tuple(self.terms.items()) + tuple(other.terms.items()), self.limit)

    def scaled(self, a):
        return Polynomial(((m, qscale(a, v)) for m, v in self.terms.items()), self.limit)

    def mul(self, other):
        if len(self.terms) * len(other.terms) > self.limit * 16:
            raise ProofBudgetExceeded('symbolic product work budget exhausted')
        return Polynomial(((a+b, qmul(x, y)) for a, x in self.terms.items()
                           for b, y in other.terms.items()), self.limit)

    def exact(self, values):
        out = ZERO
        for m, coeff in self.terms.items():
            a = Q(1)
            for key in m:
                a *= values[key]
            out = qadd(out, qscale(a, coeff))
        return out
