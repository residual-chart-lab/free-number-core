#!/usr/bin/env python3
"""Exact certificate for the exceptional n=7 quaternionic square residual.

For Q=(1,3|4,6), discard the within-part edges (1,3) and (4,6) and
retain the four cross edges.  The paired response collapse

    epsilon_4(F) = sum_(a,b) F(e_a,e_a,e_b,e_b)

has the same value on all four actual odd-even common-shadow responses.
Consequently its +,-,-,+ edge sum kills the intrinsic cross matching map.

The collapse and shadow identities are checked over the integers.  Actual
response-side restriction maps are then factored over F_1009 and F_1013.
Their cross matching matrix has rank 1292 over both fields.  Together with
the four-dimensional rational annihilator, either modular minor proves that
the cross-square cokernel over Q is exactly H.
"""

from itertools import product

import numpy as np

from all_n_pairwise_terminal_descent_certificate import right_encoder
from n2_intrinsic_response_certificate import Mat, Q, V, qmul
from n6_response_4simplex_modular_certificate import (
    build_integer_response,
    rank_mod,
    right_inverse_data_mod,
)
from second_response_simplex_differential_certificate import (
    response_generators,
)


PRIMES = (1009, 1013)
N = 7
SUPPORT = (1, 3, 4, 6)
CROSS_EDGES = ((1, 4), (1, 6), (3, 4), (3, 6))
KAPPA_SIGNS = (1, -1, -1, 1)
FACE_DEPTH = N - 2
EDGE_DEPTH = N - 3
FACE_DIMENSION = 4 * 3**FACE_DEPTH
EDGE_DIMENSION = 4 * 3**EDGE_DEPTH


def tuple_index(values, base):
    result = 0
    for value in values:
        result = base * result + value
    return result


def reverse_product_map(depth):
    """mu_m(h,v_1,...,v_m)=h v_m ... v_1."""

    matrix = Mat.zeros(4, 4 * 3**depth)
    for column, (coefficient, *vectors) in enumerate(
        product(range(4), *([range(3)] * depth))
    ):
        value = Q[coefficient]
        for vector in reversed(vectors):
            value = qmul(value, V[vector])
        for component, entry in enumerate(value):
            matrix[component, column] = entry
    return matrix


def paired_collapse_4():
    """epsilon_4(F)=sum_(a,b) F(e_a,e_a,e_b,e_b)."""

    matrix = Mat.zeros(4, EDGE_DIMENSION)
    for first in range(3):
        for second in range(3):
            probe_index = tuple_index(
                (first, first, second, second), 3
            )
            for component in range(4):
                matrix[component, 4 * probe_index + component] = 1
    return matrix


def actual_cross_matching_mod(faces, shadows, prime):
    """Factor the four actual face-to-shadow maps and assemble the square."""

    right_data = {
        gap: right_inverse_data_mod(face, prime)
        for gap, face in faces.items()
    }
    face_index = {gap: index for index, gap in enumerate(SUPPORT)}
    matrix = np.zeros(
        (4 * EDGE_DIMENSION, 4 * FACE_DIMENSION), dtype=np.int64
    )

    for edge_index, (first_gap, second_gap) in enumerate(CROSS_EDGES):
        shadow = shadows[(first_gap, second_gap)] % prime
        first_pivots, first_inverse = right_data[first_gap]
        second_pivots, second_inverse = right_data[second_gap]
        first_restriction = (
            shadow[:, first_pivots] @ first_inverse
        ) % prime
        second_restriction = (
            shadow[:, second_pivots] @ second_inverse
        ) % prime

        if np.count_nonzero(
            (first_restriction @ faces[first_gap] - shadow) % prime
        ):
            raise AssertionError("first shadow factorization failed")
        if np.count_nonzero(
            (second_restriction @ faces[second_gap] - shadow) % prime
        ):
            raise AssertionError("second shadow factorization failed")

        row_slice = slice(
            edge_index * EDGE_DIMENSION,
            (edge_index + 1) * EDGE_DIMENSION,
        )
        first_index = face_index[first_gap]
        second_index = face_index[second_gap]
        first_slice = slice(
            first_index * FACE_DIMENSION,
            (first_index + 1) * FACE_DIMENSION,
        )
        second_slice = slice(
            second_index * FACE_DIMENSION,
            (second_index + 1) * FACE_DIMENSION,
        )
        matrix[row_slice, first_slice] = first_restriction
        matrix[row_slice, second_slice] = (-second_restriction) % prime
    return matrix


def kappa_array(epsilon):
    block = np.array(epsilon.data, dtype=np.int64)
    return np.concatenate(
        [sign * block for sign in KAPPA_SIGNS], axis=1
    )


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    epsilon = paired_collapse_4()
    mu_4 = reverse_product_map(4)
    check(
        "epsilon_4 J_4 is reverse quaternion multiplication",
        epsilon * right_encoder(4) == mu_4,
    )
    check("epsilon_4 and kappa_212 are onto H", epsilon.rank() == 4)

    source_generators = response_generators(EDGE_DEPTH)
    target_generators = response_generators(0)
    epsilon_array = np.array(epsilon.data, dtype=np.int64)
    check(
        "epsilon_4 is SO(3)-equivariant",
        all(
            np.array_equal(
                target @ epsilon_array,
                epsilon_array @ source,
            )
            for source, target in zip(source_generators, target_generators)
        ),
    )

    faces = {
        gap: build_integer_response(N, {gap}) for gap in SUPPORT
    }
    shadows = {
        edge: build_integer_response(N, set(edge))
        for edge in CROSS_EDGES
    }
    collapsed_shadows = {
        edge: epsilon_array @ shadow for edge, shadow in shadows.items()
    }
    first_collapse = collapsed_shadows[CROSS_EDGES[0]]
    check(
        "all four actual odd-even shadows have the same collapse over Z",
        all(
            np.array_equal(collapse, first_collapse)
            for collapse in collapsed_shadows.values()
        ),
    )

    # For the square signs +,-,-,+, the two incident edge signs cancel at
    # each of the four face vertices.
    vertex_sign_sums = (
        KAPPA_SIGNS[0] + KAPPA_SIGNS[1],
        KAPPA_SIGNS[2] + KAPPA_SIGNS[3],
        -KAPPA_SIGNS[0] - KAPPA_SIGNS[2],
        -KAPPA_SIGNS[1] - KAPPA_SIGNS[3],
    )
    check(
        "the four vertex sign sums vanish",
        vertex_sign_sums == (0, 0, 0, 0),
    )

    kappa = kappa_array(epsilon)
    for prime in PRIMES:
        matching = actual_cross_matching_mod(
            faces, shadows, prime
        )
        matching_rank = rank_mod(matching, prime)
        print(
            f"mod {prime}: actual square shape {matching.shape}, "
            f"rank {matching_rank}, "
            f"cokernel {matching.shape[0] - matching_rank}",
        )
        check(
            f"kappa_212 kills the actual square matching map mod {prime}",
            not np.count_nonzero((kappa @ matching) % prime),
        )
        check(
            f"the actual square matching rank is 1292 mod {prime}",
            matching_rank == 1292,
        )
        check(
            f"kappa_212 has rank four mod {prime}",
            rank_mod(kappa, prime) == 4,
        )

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED: {', '.join(failed)}")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
