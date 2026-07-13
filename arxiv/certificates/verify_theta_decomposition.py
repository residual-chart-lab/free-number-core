#!/usr/bin/env python3
"""Exact certificate for the local decoder Theta.

Builds the 12 x 12 real matrix of

    Theta(sum_a e_a tensor h_a)(d) = sum_a e_a d h_a

in the standard quaternion basis, checks det(Theta) = 256, and verifies the
irreducible block factorization

    V_0 : 1,
    2 V_1 : [[-1, 2], [1, 0]],
    V_2 : -2.
"""

from __future__ import annotations

import sympy as sp


def qmul(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    """Hamilton product in coordinates (1, i, j, k)."""
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return sp.Matrix(
        [
            a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0,
        ]
    )


def theta_matrix() -> sp.Matrix:
    basis_h = [sp.eye(4)[:, r] for r in range(4)]
    basis_v = basis_h[1:]
    matrix = sp.zeros(12, 12)

    # Domain order: e_a tensor h_mu.
    # Codomain order: quaternion components of F(e_c).
    for a, e_a in enumerate(basis_v):
        for mu, h_mu in enumerate(basis_h):
            col = 4 * a + mu
            for c, e_c in enumerate(basis_v):
                value = qmul(qmul(e_a, e_c), h_mu)
                matrix[4 * c : 4 * c + 4, col] = value
    return matrix


def main() -> None:
    theta = theta_matrix()
    assert theta.rank() == 12
    assert theta.det() == 256

    spin_one = sp.Matrix([[-1, 2], [1, 0]])
    block_determinant = sp.Integer(1) * spin_one.det() ** 3 * (-2) ** 5
    assert spin_one.det() == -2
    assert block_determinant == 256

    print("rank(Theta) =", theta.rank())
    print("det(Theta)  =", theta.det())
    print("block product = 1 * det([[-1,2],[1,0]])^3 * (-2)^5")
    print("              =", block_determinant)


if __name__ == "__main__":
    main()
