#!/usr/bin/env python3
"""Exact certificate for the intrinsic n=3, depth-1 response space.

For a length-three state x, let

    q = m_3(x),
    F(d) = R_3^(1)(x)(d),
    G(d) = R_3^(2)(x)(d).

The intrinsic presentation proved in Note 04 is

    q = sum_a F(e_a) e_a,
    q = sum_a e_a G(e_a).

Equivalently, Q_{3,1} is the fiber product of two copies of Hom(V,H)
over H, using the right and left contraction maps.  This script checks the
claim over exact integer arithmetic.
"""

from n2_intrinsic_response_certificate import Mat, Q, V, qmul


def tensor_index(first_idx, middle_idx, last_idx):
    return 9 * first_idx + 3 * middle_idx + last_idx


def map_index(d_idx, q_comp):
    return 4 * d_idx + q_comp


def build_right_contraction():
    """r(F) = sum_a F(e_a) e_a."""
    matrix = Mat.zeros(4, 12)
    for d_idx, e_d in enumerate(V):
        for in_comp, basis_q in enumerate(Q):
            out = qmul(basis_q, e_d)
            for out_comp in range(4):
                matrix[out_comp, map_index(d_idx, in_comp)] += out[out_comp]
    return matrix


def build_left_contraction():
    """ell(G) = sum_a e_a G(e_a)."""
    matrix = Mat.zeros(4, 12)
    for d_idx, e_d in enumerate(V):
        for in_comp, basis_q in enumerate(Q):
            out = qmul(e_d, basis_q)
            for out_comp in range(4):
                matrix[out_comp, map_index(d_idx, in_comp)] += out[out_comp]
    return matrix


def build_depth1_profile():
    """Rows are q (4), F (12), G (12); columns are length-three words."""
    profile = Mat.zeros(28, 27)

    for first_idx, first in enumerate(V):
        for middle_idx, middle in enumerate(V):
            for last_idx, last in enumerate(V):
                col = tensor_index(first_idx, middle_idx, last_idx)

                value = qmul(qmul(last, middle), first)
                for comp in range(4):
                    profile[comp, col] = value[comp]

                for d_idx, d in enumerate(V):
                    # Internal slot 1: first | d | middle | last.
                    response_1 = qmul(qmul(qmul(last, middle), d), first)
                    # Internal slot 2: first | middle | d | last.
                    response_2 = qmul(qmul(qmul(last, d), middle), first)

                    for comp in range(4):
                        profile[4 + map_index(d_idx, comp), col] = response_1[comp]
                        profile[16 + map_index(d_idx, comp), col] = response_2[comp]

    return profile


def build_fiber_product_constraints(right, left):
    """C(q,F,G) = (q-r(F), q-ell(G))."""
    constraints = Mat.zeros(8, 28)

    for comp in range(4):
        constraints[comp, comp] = 1
        constraints[4 + comp, comp] = 1

    for row in range(4):
        for col in range(12):
            constraints[row, 4 + col] -= right[row, col]
            constraints[4 + row, 16 + col] -= left[row, col]

    return constraints


def build_pair_projection():
    """Forget q and retain the pair (F,G)."""
    projection = Mat.zeros(24, 28)
    for idx in range(24):
        projection[idx, 4 + idx] = 1
    return projection


def main():
    right = build_right_contraction()
    left = build_left_contraction()
    profile = build_depth1_profile()
    constraints = build_fiber_product_constraints(right, left)
    pair_projection = build_pair_projection()
    response_pair = pair_projection * profile

    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    check("right contraction is onto H", right.rank() == 4)
    check("left contraction is onto H", left.rank() == 4)
    check("the two quaternion compatibility equations have rank 8", constraints.rank() == 8)
    check("all depth-one profiles satisfy the compatibility equations", constraints * profile == Mat.zeros(8, 27))
    check("the actual n=3 depth-one profile has rank 20", profile.rank() == 20)
    check("the response pair (F,G) already has rank 20", response_pair.rank() == 20)
    check("the intrinsic fiber product has dimension 20", 28 - constraints.rank() == 20)
    check("actual profiles equal the intrinsic fiber product", profile.rank() == 28 - constraints.rank())
    check("the depth-one invisible layer has dimension 7", 27 - profile.rank() == 7)

    all_ok = True
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        all_ok = all_ok and passed

    print("ALL CHECKS PASSED" if all_ok else "SOME CHECK FAILED")


if __name__ == "__main__":
    main()

