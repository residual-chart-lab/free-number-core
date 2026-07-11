#!/usr/bin/env python3
"""
Exact certificate for core/08-all-grade-response-reconstruction.md.

Checks over exact integer arithmetic:
  1. Theta: V tensor H -> Hom(V,H) has determinant 256 and rank 12.
  2. The canonical all-gap response A_n has full column rank 3^n for n=1,...,5.
  3. The recursive last-slot identity holds on every basis word and basis probe
     for n=2,...,5.
  4. The composition factorisation holds on every basis word and basis probe
     for m,n >=1 with m+n <=5.

Expected final line:
    ALL CHECKS PASSED
"""

from itertools import product
import sympy as sp

Q = [
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
]
V = Q[1:]


def qmul(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return (
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    )


def qprod(seq):
    out = Q[0]
    for item in seq:
        out = qmul(out, item)
    return out


def vertical_value(word, probes):
    n = len(word)
    assert len(probes) == n - 1
    seq = []
    for pos in range(n - 1, -1, -1):
        seq.append(V[word[pos]])
        if pos > 0:
            seq.append(V[probes[pos - 1]])
    return qprod(seq)


def theta_matrix():
    M = sp.zeros(12, 12)
    for left_idx, left in enumerate(V):
        for h_idx, h in enumerate(Q):
            col = 4 * left_idx + h_idx
            for d_idx, d in enumerate(V):
                out = qmul(qmul(left, d), h)
                for comp in range(4):
                    M[4 * d_idx + comp, col] = out[comp]
    return M


def A_matrix(n):
    words = list(product(range(3), repeat=n))
    probes = list(product(range(3), repeat=n - 1))
    rows = []
    for probe_tuple in probes:
        for comp in range(4):
            rows.append([
                vertical_value(word, probe_tuple)[comp]
                for word in words
            ])
    return sp.Matrix(rows)


checks = []


def check(name, cond):
    checks.append((name, bool(cond)))


Theta = theta_matrix()
check("Theta determinant is 256", Theta.det() == 256)
check("Theta rank is 12", Theta.rank() == 12)

# Explicit inverse from Lemma 2.1:
# h_a = 1/2 * sum_{b,c} epsilon_{abc} e_b F(e_c).
Inv = sp.zeros(12, 12)
for a in range(3):
    for b in range(3):
        for c in range(3):
            eps = sp.LeviCivita(a, b, c)
            if eps == 0:
                continue
            # Left multiplication by e_b on the quaternion F(e_c).
            for in_comp, basis_h in enumerate(Q):
                out = qmul(V[b], basis_h)
                in_col = 4 * c + in_comp
                for out_comp in range(4):
                    Inv[4 * a + out_comp, in_col] += sp.Rational(1, 2) * eps * out[out_comp]

check("explicit inverse satisfies Inv*Theta=I", Inv * Theta == sp.eye(12))
check("explicit inverse satisfies Theta*Inv=I", Theta * Inv == sp.eye(12))

for n in range(1, 6):
    A = A_matrix(n)
    check(f"A_{n} rank is 3^{n}", A.rank() == 3**n)

for n in range(2, 6):
    ok = True
    for word in product(range(3), repeat=n):
        prefix = word[:-1]
        last = word[-1]
        for probes in product(range(3), repeat=n - 1):
            earlier = probes[:-1]
            d_last = probes[-1]
            lhs = vertical_value(word, probes)
            rhs = qmul(
                qmul(V[last], V[d_last]),
                vertical_value(prefix, earlier),
            )
            if lhs != rhs:
                ok = False
                break
        if not ok:
            break
    check(f"A_{n} recursive last-slot identity", ok)

for total in range(2, 6):
    for m in range(1, total):
        n = total - m
        ok = True
        for xword in product(range(3), repeat=m):
            for yword in product(range(3), repeat=n):
                for d in product(range(3), repeat=m - 1):
                    for bridge in range(3):
                        for e in product(range(3), repeat=n - 1):
                            lhs = vertical_value(
                                xword + yword,
                                d + (bridge,) + e,
                            )
                            rhs = qmul(
                                qmul(vertical_value(yword, e), V[bridge]),
                                vertical_value(xword, d),
                            )
                            if lhs != rhs:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break
                if not ok:
                    break
            if not ok:
                break
        check(f"composition factorisation m={m}, n={n}", ok)

all_ok = True
for name, passed in checks:
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    all_ok = all_ok and passed

print("ALL CHECKS PASSED" if all_ok else "SOME CHECK FAILED")
