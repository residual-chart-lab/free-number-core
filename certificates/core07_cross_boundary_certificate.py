#!/usr/bin/env python3
"""
Exact certificate for core/07-length-four-cross-boundary-propagation.md.

Checks, over exact integer/rational arithmetic:
  1. all pure-word factorisation formulas for B2 x B2 -> B4;
  2. full profile ranks at depths 0,1,2,3;
  3. sectorwise ranks for VV, VR, RV, RR;
  4. the residual-residual middle response has rank 16;
  5. adding the depth-3 response completes the RR sector to rank 25.

Run:
    python3 certificates/core07_cross_boundary_certificate.py

Expected final line:
    ALL CHECKS PASSED
"""

from itertools import combinations, product
import sympy as sp

# Quaternion basis order: 0=1, 1=i, 2=j, 3=k.
Q = [
    sp.Matrix([1, 0, 0, 0]),
    sp.Matrix([0, 1, 0, 0]),
    sp.Matrix([0, 0, 1, 0]),
    sp.Matrix([0, 0, 0, 1]),
]
IM = Q[1:]


def qmul(x, y):
    a0, a1, a2, a3 = list(x)
    b0, b1, b2, b3 = list(y)
    return sp.Matrix([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ])


def qprod(seq):
    out = Q[0]
    for x in seq:
        out = qmul(out, x)
    return out


def reversed_compression(letters):
    return qprod(list(reversed(letters)))


def insertion_matrix(n, gaps):
    """All probe values for one fixed tuple of original internal gaps."""
    words = list(product(range(3), repeat=n))
    mat = sp.zeros((3 ** len(gaps)) * 4, len(words))
    for col, word in enumerate(words):
        for probe_index, probes in enumerate(product(range(3), repeat=len(gaps))):
            letters = [IM[a] for a in word]
            for slot, probe in sorted(zip(gaps, probes), reverse=True):
                letters.insert(slot, IM[probe])
            out = reversed_compression(letters)
            for h in range(4):
                mat[4*probe_index + h, col] = out[h]
    return mat


def profile_matrix(n, depth):
    pieces = [insertion_matrix(n, ())]
    internal_gaps = list(range(1, n))
    for k in range(1, depth + 1):
        for gaps in combinations(internal_gaps, k):
            pieces.append(insertion_matrix(n, gaps))
    return sp.Matrix.vstack(*pieces)


checks = []


def check(name, condition):
    checks.append((name, bool(condition)))


# ---------------------------------------------------------------------------
# 1. Pure-word factorisation formulas.
# x=a|b, y=c|d, q=ba, p=dc.
# ---------------------------------------------------------------------------
for a, b, c, d in product(range(3), repeat=4):
    q = qprod([IM[b], IM[a]])
    p = qprod([IM[d], IM[c]])

    check(
        f"m4 factorisation {(a,b,c,d)}",
        qprod([IM[d], IM[c], IM[b], IM[a]]) == qmul(p, q),
    )

    for z in range(3):
        lx = qprod([IM[b], IM[z], IM[a]])
        ly = qprod([IM[d], IM[z], IM[c]])
        check(
            f"R1 factorisation {(a,b,c,d,z)}",
            qprod([IM[d], IM[c], IM[b], IM[z], IM[a]]) == qmul(p, lx),
        )
        check(
            f"R2 factorisation {(a,b,c,d,z)}",
            qprod([IM[d], IM[c], IM[z], IM[b], IM[a]]) == qmul(qmul(p, IM[z]), q),
        )
        check(
            f"R3 factorisation {(a,b,c,d,z)}",
            qprod([IM[d], IM[z], IM[c], IM[b], IM[a]]) == qmul(ly, q),
        )

    for z1, z2 in product(range(3), repeat=2):
        lx = qprod([IM[b], IM[z1], IM[a]])
        ly = qprod([IM[d], IM[z2], IM[c]])
        check(
            f"D12 factorisation {(a,b,c,d,z1,z2)}",
            qprod([IM[d], IM[c], IM[z2], IM[b], IM[z1], IM[a]])
            == qmul(qmul(p, IM[z2]), lx),
        )
        check(
            f"D13 factorisation {(a,b,c,d,z1,z2)}",
            qprod([IM[d], IM[z2], IM[c], IM[b], IM[z1], IM[a]])
            == qmul(ly, lx),
        )
        check(
            f"D23 factorisation {(a,b,c,d,z1,z2)}",
            qprod([IM[d], IM[z2], IM[c], IM[z1], IM[b], IM[a]])
            == qmul(qmul(ly, IM[z1]), q),
        )

    for z1, z2, z3 in product(range(3), repeat=3):
        lx = qprod([IM[b], IM[z1], IM[a]])
        ly = qprod([IM[d], IM[z3], IM[c]])
        check(
            f"A4 factorisation {(a,b,c,d,z1,z2,z3)}",
            qprod([IM[d], IM[z3], IM[c], IM[z2], IM[b], IM[z1], IM[a]])
            == qmul(qmul(ly, IM[z2]), lx),
        )


# ---------------------------------------------------------------------------
# 2. Exact profile ranks on B4.
# ---------------------------------------------------------------------------
expected_full = {
    0: (4, 77),
    1: (32, 49),
    2: (72, 9),
    3: (81, 0),
}
profiles = {}
for depth in range(4):
    prof = profile_matrix(4, depth)
    profiles[depth] = prof
    rank = prof.rank()
    check(
        f"full B4 profile depth<={depth}: rank/kernel",
        (rank, 81-rank) == expected_full[depth],
    )


# ---------------------------------------------------------------------------
# 3. Exact length-two value/residual bases.
# W = Rg + Lambda^2 V (dimension 4), U = S^2_0 V (dimension 5).
# ---------------------------------------------------------------------------
pairs = list(product(range(3), repeat=2))
pair_index = {pair: i for i, pair in enumerate(pairs)}

w_basis = []
g = sp.zeros(9, 1)
for a in range(3):
    g[pair_index[(a, a)], 0] = 1
w_basis.append(g)
for a, b in [(0, 1), (1, 2), (2, 0)]:
    v = sp.zeros(9, 1)
    v[pair_index[(a, b)], 0] = 1
    v[pair_index[(b, a)], 0] = -1
    w_basis.append(v)
W = sp.Matrix.hstack(*w_basis)

u_basis = []
for a, b in [(0, 1), (0, 2), (1, 2)]:
    v = sp.zeros(9, 1)
    v[pair_index[(a, b)], 0] = 1
    v[pair_index[(b, a)], 0] = 1
    u_basis.append(v)
v = sp.zeros(9, 1)
v[pair_index[(0, 0)], 0] = 1
v[pair_index[(1, 1)], 0] = -1
u_basis.append(v)
v = sp.zeros(9, 1)
v[pair_index[(0, 0)], 0] = 1
v[pair_index[(1, 1)], 0] = 1
v[pair_index[(2, 2)], 0] = -2
u_basis.append(v)
U = sp.Matrix.hstack(*u_basis)

check("dim W=4", W.rank() == 4)
check("dim U=5", U.rank() == 5)
check("B2=W direct-sum U", sp.Matrix.hstack(W, U).rank() == 9)

sectors = {
    "VV": sp.kronecker_product(W, W),
    "VR": sp.kronecker_product(W, U),
    "RV": sp.kronecker_product(U, W),
    "RR": sp.kronecker_product(U, U),
}
expected_sector_kernel = {
    0: {"VV": 12, "VR": 20, "RV": 20, "RR": 25},
    1: {"VV": 0,  "VR": 12, "RV": 12, "RR": 25},
    2: {"VV": 0,  "VR": 0,  "RV": 0,  "RR": 9},
    3: {"VV": 0,  "VR": 0,  "RV": 0,  "RR": 0},
}
for depth, prof in profiles.items():
    for name, basis in sectors.items():
        restricted_rank = (prof * basis).rank()
        kernel_dim = basis.shape[1] - restricted_rank
        check(
            f"sector {name} depth<={depth}: kernel dimension",
            kernel_dim == expected_sector_kernel[depth][name],
        )


# ---------------------------------------------------------------------------
# 4. RR sector: the middle depth-two component and depth-three completion.
# ---------------------------------------------------------------------------
D13 = insertion_matrix(4, (1, 3))
A4 = insertion_matrix(4, (1, 2, 3))
RR = sectors["RR"]
check("D13 rank on RR is 16", (D13 * RR).rank() == 16)
check(
    "D13 plus A4 is injective on RR",
    (sp.Matrix.vstack(D13, A4) * RR).rank() == 25,
)


ok = True
for name, passed in checks:
    if not passed:
        print(f"[FAIL] {name}")
        ok = False

if ok:
    print(f"{len(checks)} exact checks passed")
    print("ALL CHECKS PASSED")
else:
    print("SOME CHECK FAILED")
    raise SystemExit(1)
