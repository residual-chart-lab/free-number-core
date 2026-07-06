#!/usr/bin/env python3
"""
Certificate for Note 11: The Spin-Depth Filtration (n = 2, 3, 4).
Exact rational arithmetic. Verifies:
  - kernel dimensions and spin multiplicities at each probe depth,
  - top-spin S^n_0 V is the last survivor, detected at canonical vertical depth n-1,
  - for n=4, the V_2 multiplicity (6 copies) splits as 3+3 as genuine SO(3)-subreps
    (subspace containment, not merely a dimension count).
Run:  python3 note11_certificate.py   ->   ALL CHECKS PASSED
"""
import sympy as sp
from itertools import product, permutations, combinations
import numpy as np

def qmul(x, y):
    a0,a1,a2,a3 = x; b0,b1,b2,b3 = y
    return sp.Matrix([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                      a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
E = [sp.Matrix([1,0,0,0]),sp.Matrix([0,1,0,0]),sp.Matrix([0,0,1,0]),sp.Matrix([0,0,0,1])]
IMAG = [E[1],E[2],E[3]]
def prod(seq):
    v = E[0]
    for q in seq: v = qmul(v, q)
    return v
eps = np.zeros((3,3,3)); eps[0,1,2]=eps[1,2,0]=eps[2,0,1]=1; eps[0,2,1]=eps[2,1,0]=eps[1,0,2]=-1
Lgen = [np.array([[-eps[a,b,c] for c in range(3)] for b in range(3)]) for a in range(3)]

checks = []
def check(name, cond): checks.append((name, bool(cond)))

def build(n):
    words = list(product(range(3), repeat=n)); idx = {w:i for i,w in enumerate(words)}; N = len(words)
    def m_of(word, probes=None, slots=None):
        letters = [IMAG[a] for a in word]
        if probes:
            for s,p in sorted(zip(slots,probes), reverse=True): letters.insert(s, p)
        return prod(list(reversed(letters)))
    M = sp.zeros(4, N)
    for c,w in enumerate(words):
        o = m_of(w)
        for h in range(4): M[h,c] = o[h]
    internal = list(range(1, n))
    def profile(d):
        mats = [M]
        for k in range(1, d+1):
            for combo in combinations(internal, k):
                Md = sp.zeros((3**k)*4, N)
                for c,w in enumerate(words):
                    for pi,probes in enumerate(product(range(3), repeat=k)):
                        o = m_of(w, [IMAG[x] for x in probes], list(combo))
                        for h in range(4): Md[pi*4+h, c] = o[h]
                mats.append(Md)
        return sp.Matrix.vstack(*mats)
    def lift(La):
        Mx = np.zeros((N,N))
        for c,w in enumerate(words):
            for pos in range(n):
                for nl in range(3):
                    v = La[nl, w[pos]]
                    if v != 0:
                        nw = list(w); nw[pos] = nl; Mx[idx[tuple(nw)], c] += v
        return Mx
    Cas = sp.Matrix(np.rint(sum(lift(La)@lift(La) for La in Lgen)).astype(int))
    def isotypic(kb, s):
        if not kb: return None
        Kb = sp.Matrix.hstack(*kb); X = (Kb.T*Kb).inv()*(Kb.T*Cas*Kb)
        P = X + s*(s+1)*sp.eye(X.shape[0]); ns = P.nullspace()
        return Kb*sp.Matrix.hstack(*ns) if ns else None
    def spinmult(kb):
        if not kb: return {}
        Kb = sp.Matrix.hstack(*kb); X = (Kb.T*Kb).inv()*(Kb.T*Cas*Kb); out = {}
        for s in range(n+1):
            d = len((X + s*(s+1)*sp.eye(X.shape[0])).nullspace())
            if d: out[s] = d//(2*s+1)
        return out
    return words, idx, N, M, profile, isotypic, spinmult

# expected tables
expected = {
    2: {0:[0,0,1], 1:[0,0,0]},
    3: {0:[0,2,2,1], 1:[0,0,0,1], 2:[0,0,0,0]},
    4: {0:[2,5,6,3,1], 1:[1,1,3,3,1], 2:[0,0,0,0,1], 3:[0,0,0,0,0]},
}
for n in [2,3,4]:
    words, idx, N, M, profile, isotypic, spinmult = build(n)
    for d in range(n):
        kb = profile(d).nullspace()
        row = spinmult(kb)
        rowv = [row.get(s,0) for s in range(n+1)]
        check(f"n={n} depth<={d} spin multiplicities {rowv}", rowv == expected[n][d])
    # top spin is last survivor = S^n_0 V, detected exactly at depth n-1
    kb_top = profile(n-2).nullspace()
    # S^n_0 V basis
    eqs = []
    for w in words:
        for p in set(permutations(w)):
            if w < p:
                r = [0]*N; r[idx[w]] = 1; r[idx[p]] = -1; eqs.append(r)
    for tail in product(range(3), repeat=n-2):
        r = [0]*N
        for a in range(3): r[idx[(a,a)+tail]] += 1
        eqs.append(r)
    S0 = sp.Matrix(eqs).nullspace()
    Ik = sp.Matrix.hstack(*kb_top); Is = sp.Matrix.hstack(*S0)
    check(f"n={n}: ker(depth<={n-2}) = S^{n}_0 V as subspaces",
          sp.Matrix.hstack(Ik, Is).rank() == len(kb_top) == len(S0))

# --- n=4: V_2 splits 3+3 as genuine SO(3)-subreps (subspace containment) ---
words, idx, N, M, profile, isotypic, spinmult = build(4)
K4 = M.nullspace()
F1 = profile(1).nullspace()
V2_K4 = isotypic(K4, 2)
V2_F1 = isotypic(F1, 2)
check("n=4: V_2 in K_4 has dim 30 (6 copies)", V2_K4.shape[1] == 30)
check("n=4: V_2 in ker(D<=1) has dim 15 (3 copies)", V2_F1.shape[1] == 15)
check("n=4: V_2(depth-1-invisible) is a subspace of V_2(K_4)",
      sp.Matrix.hstack(V2_K4, V2_F1).rank() == 30)
check("n=4: V_2 splits as 3+3 SO(3)-subreps (not just dim count)",
      V2_K4.shape[1] - V2_F1.shape[1] == 15)

ok = True
for name, passed in checks:
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    ok = ok and passed
print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
