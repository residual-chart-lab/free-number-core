#!/usr/bin/env python3
"""Exact low-grade certificate for the depth-one outer-gluing pattern.

For n >= 3, let a depth-one profile be

    (q, F_1, ..., F_{n-1}) in H + Hom(V,H)^(n-1).

Every actual profile satisfies

    q = r(F_1),
    q = ell(F_{n-1}),

where r(F)=sum F(e_a)e_a and ell(F)=sum e_aF(e_a).

The conjectural all-n statement is that these are the only universal linear
constraints.  This script exact-checks equality of the actual image and this
intrinsic outer-gluing space for n=3,...,7.
"""

from itertools import product

from n2_intrinsic_response_certificate import Mat, Q, V, qmul


def qprod(items):
    out = Q[0]
    for item in items:
        out = qmul(out, item)
    return out


def map_index(d_idx, q_comp):
    return 4 * d_idx + q_comp


def build_right_contraction():
    matrix = Mat.zeros(4, 12)
    for d_idx, e_d in enumerate(V):
        for in_comp, basis_q in enumerate(Q):
            out = qmul(basis_q, e_d)
            for out_comp in range(4):
                matrix[out_comp, map_index(d_idx, in_comp)] += out[out_comp]
    return matrix


def build_left_contraction():
    matrix = Mat.zeros(4, 12)
    for d_idx, e_d in enumerate(V):
        for in_comp, basis_q in enumerate(Q):
            out = qmul(e_d, basis_q)
            for out_comp in range(4):
                matrix[out_comp, map_index(d_idx, in_comp)] += out[out_comp]
    return matrix


def build_depth1_profile(n):
    words = list(product(range(3), repeat=n))
    profile = Mat.zeros(4 + 12 * (n - 1), len(words))

    for col, word in enumerate(words):
        letters = [V[idx] for idx in word]

        compressed = qprod(reversed(letters))
        for comp in range(4):
            profile[comp, col] = compressed[comp]

        for slot in range(1, n):
            for d_idx, d in enumerate(V):
                inserted = letters[:slot] + [d] + letters[slot:]
                response = qprod(reversed(inserted))
                offset = 4 + 12 * (slot - 1) + map_index(d_idx, 0)
                for comp in range(4):
                    profile[offset + comp, col] = response[comp]

    return profile


def build_outer_constraints(n, right, left):
    target_dim = 4 + 12 * (n - 1)
    constraints = Mat.zeros(8, target_dim)

    for comp in range(4):
        constraints[comp, comp] = 1
        constraints[4 + comp, comp] = 1

    for row in range(4):
        for col in range(12):
            constraints[row, 4 + col] -= right[row, col]
            last_offset = 4 + 12 * (n - 2)
            constraints[4 + row, last_offset + col] -= left[row, col]

    return constraints


def main():
    right = build_right_contraction()
    left = build_left_contraction()
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    check("right contraction has rank 4", right.rank() == 4)
    check("left contraction has rank 4", left.rank() == 4)

    for n in range(3, 8):
        profile = build_depth1_profile(n)
        constraints = build_outer_constraints(n, right, left)
        predicted_rank = 12 * n - 16

        check(f"n={n}: outer constraints have rank 8", constraints.rank() == 8)
        check(
            f"n={n}: actual profiles satisfy outer gluing",
            constraints * profile == Mat.zeros(8, 3**n),
        )
        check(
            f"n={n}: actual rank is 12n-16",
            profile.rank() == predicted_rank,
        )
        check(
            f"n={n}: actual image equals intrinsic outer-gluing space",
            profile.rank() == profile.nrows - constraints.rank(),
        )

    all_ok = True
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        all_ok = all_ok and passed

    print("ALL CHECKS PASSED" if all_ok else "SOME CHECK FAILED")


if __name__ == "__main__":
    main()

