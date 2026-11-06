"""Small exact matrix implementation of the unchanged length-two identities."""
from fractions import Fraction as F
from math import isqrt


def matrix(rows):
    return [[F(x) for x in row] for row in rows]


def identity():
    return matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])


def zero():
    return matrix([[0] * 3 for _ in range(3)])


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(k, a):
    return [[F(k) * x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(-1, b))


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def comm(a, b):
    return sub(mul(a, b), mul(b, a))


def trace(a):
    return sum(a[i][i] for i in range(3))


def outer(a, b):
    return [[x * y for y in b] for x in a]


def determinant(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def rotate_tensor(r, t):
    return mul(mul(r, t), transpose(r))


def apply(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))


def residual(t):
    return sub(scale(F(1, 2), add(t, transpose(t))), scale(trace(t) / 3, identity()))


def compression(t):
    # m2(e_i | e_j)=e_j e_i, with right-handed quaternion multiplication.
    return (-trace(t), t[2][1] - t[1][2], t[0][2] - t[2][0], t[1][0] - t[0][1])


def response(s):
    # Core note 04: A2(S)=-2S for S symmetric and trace free.
    assert s == transpose(s) and trace(s) == 0
    return scale(-2, s)


def frobenius2(a):
    return sum(x * x for row in a for x in row)


def exact_sqrt(value):
    value = F(value)
    if value < 0:
        raise ValueError("negative square root")
    p, q = isqrt(value.numerator), isqrt(value.denominator)
    if p * p != value.numerator or q * q != value.denominator:
        raise ArithmeticError("This exact-rational test has no rational square root for the requested value")
    return F(p, q)


def frame(a, b, c):
    # Rational unit quaternion by stereographic coordinates; SO(3) matrix below.
    v = tuple(F(x) for x in (a, b, c))
    rr = sum(x * x for x in v)
    w, x, y, z = ((1 - rr) / (1 + rr),) + tuple(2 * x / (1 + rr) for x in v)
    return [[w*w+x*x-y*y-z*z, 2*(x*y-w*z), 2*(x*z+w*y)],
            [2*(x*y+w*z), w*w-x*x+y*y-z*z, 2*(y*z-w*x)],
            [2*(x*z-w*y), 2*(y*z+w*x), w*w-x*x-y*y+z*z]]


def packed(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, (list, tuple)):
        return [packed(x) for x in value]
    if isinstance(value, dict):
        return {str(k): packed(v) for k, v in value.items()}
    return value
