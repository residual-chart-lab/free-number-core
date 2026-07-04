#!/usr/bin/env python3
"""
Exact certificate for:  K_3 ∩ ker D_3 = S^3_0 V   (Depth-One Detection in Length Three)

All arithmetic is exact (integer/rational via SymPy). No floating point.
Run:  python3 depth_one_detection_certificate.py
Expected final line:  ALL CHECKS PASSED
"""

import sympy as sp
from itertools import product, permutations

# Quaternion multiplication, basis order (1, i, j, k) as 4-vectors.
def qmul(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return sp.Matrix([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ])

E = [sp.Matrix([1,0,0,0]), sp.Matrix([0,1,0,0]),
     sp.Matrix([0,0,1,0]), sp.Matrix([0,0,0,1])]
IMAG = [E[1], E[2], E[3]]            # i, j, k

def prod(seq):
    v = E[0]
    for q in seq:
        v = qmul(v, q)
    return v

triples = list(product(range(3), repeat=3))   # ordered basis of V^{⊗3}
idx = {t: n for n, t in enumerate(triples)}

# --- m_3(a|b|c) = c b a  -----------------------------------------------------
M3 = sp.zeros(4, 27)
for col, (a, b, c) in enumerate(triples):
    o = prod([IMAG[c], IMAG[b], IMAG[a]])
    for h in range(4):
        M3[h, col] = o[h]

# --- depth-one profile: D^(1)(a|b|c)(x)=c b x a, D^(2)(a|b|c)(x)=c x b a ------
def Dblock(which):
    Md = sp.zeros(12, 27)
    for col, (a, b, c) in enumerate(triples):
        qa, qb, qc = IMAG[a], IMAG[b], IMAG[c]
        for xi in range(3):
            x = IMAG[xi]
            o = prod([qc, qb, x, qa]) if which == 1 else prod([qc, x, qb, qa])
            for h in range(4):
                Md[xi*4 + h, col] = o[h]
    return Md

D3 = sp.Matrix.vstack(Dblock(1), Dblock(2))

# --- S^3_0 V : symmetric + trace-free ---------------------------------------
eqs = []
for t in triples:
    for p in set(permutations(t)):
        if t < p:
            r = [0]*27; r[idx[t]] = 1; r[idx[p]] = -1; eqs.append(r)
for c in range(3):
    r = [0]*27
    for a in range(3):
        r[idx[(a, a, c)]] += 1
    eqs.append(r)
S30 = sp.Matrix(eqs).nullspace()

# --- checks ------------------------------------------------------------------
checks = []

checks.append(("m_3(i|j|k) = 1",  prod([IMAG[2],IMAG[1],IMAG[0]]) == sp.Matrix([1,0,0,0])))
checks.append(("m_3(i|i|i) = -i", prod([IMAG[0],IMAG[0],IMAG[0]]) == sp.Matrix([0,-1,0,0])))

checks.append(("rank m_3 = 4",  M3.rank() == 4))
checks.append(("dim K_3 = 23",  27 - M3.rank() == 23))

K3 = sp.Matrix.hstack(*M3.nullspace())               # 27 x 23
checks.append(("rank D_3|K_3 = 16", (D3 * K3).rank() == 16))
checks.append(("dim(K_3 ∩ ker D_3) = 7", 23 - (D3 * K3).rank() == 7))

checks.append(("dim S^3_0 V = 7", len(S30) == 7))

# subspace equality: intersection == S^3_0 V
inter = sp.Matrix.vstack(M3, D3).nullspace()         # ker m_3 ∩ ker D_3
Im = sp.Matrix.hstack(*inter)
Is = sp.Matrix.hstack(*S30)
union = sp.Matrix.hstack(Im, Is)
checks.append(("K_3 ∩ ker D_3 = S^3_0 V (subspace)",
               len(inter) == 7 and len(S30) == 7 and union.rank() == 7))

# depth-1 injective on V_2-isotypic part: nullity on K_3 is exactly the 7-dim V_3
checks.append(("depth-1 injective on K_3 / V_3",
               (D3 * K3).rank() == 16 and 23 - (D3 * K3).rank() == 7))

ok = True
for name, passed in checks:
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    ok = ok and passed

print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
