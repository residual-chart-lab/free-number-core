#!/usr/bin/env python3
from __future__ import annotations
import sympy as sp

def qmul(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return sp.Matrix([
        a0*b0-a1*b1-a2*b2-a3*b3,
        a0*b1+a1*b0+a2*b3-a3*b2,
        a0*b2-a1*b3+a2*b0+a3*b1,
        a0*b3+a1*b2-a2*b1+a3*b0,
    ])

def theta_matrix() -> sp.Matrix:
    basis_h=[sp.eye(4)[:,r] for r in range(4)]
    basis_v=basis_h[1:]
    M=sp.zeros(12,12)
    for a,e_a in enumerate(basis_v):
        for mu,h_mu in enumerate(basis_h):
            col=4*a+mu
            for c,e_c in enumerate(basis_v):
                M[4*c:4*c+4,col]=qmul(qmul(e_a,e_c),h_mu)
    return M

if __name__=='__main__':
    M=theta_matrix()
    assert M.rank()==12
    assert M.det()==256
    B=sp.Matrix([[-1,2],[1,0]])
    assert B.det()==-2
    assert B.det()**3*(-2)**5==256
    print('theta certificate passed:', M.rank(), M.det())
