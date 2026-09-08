#!/usr/bin/env python3
"""Exact certificate for the n=6 capped five-edge quaternionic residual.

For Q=(1,2,4,5), remove the long local edge 14, namely the actual edge
(1,5), and retain the five edges

    (1,2), (1,4), (2,4), (2,5), (4,5).

On R_3 define

    L(F) = sum_(a,b) e_b F(e_a,e_a,e_b),
    R(F) = sum_(a,b) F(e_b,e_a,e_a) e_b.

The block operator (-L,+L,0,-R,+R) kills the actual five-edge matching
map.  The collapse identities are checked over the integers.  Actual
response-side restrictions are then factored over F_1009 and F_1013, where
the matching rank is 536.  The four-dimensional rational annihilator and
either modular minor therefore prove that the five-edge cokernel over Q is
exactly H.
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
N = 6
SUPPORT = (1, 2, 4, 5)
KEPT_EDGES = ((1, 2), (1, 4), (2, 4), (2, 5), (4, 5))
FACE_DEPTH = N - 2
EDGE_DEPTH = N - 3
FACE_DIMENSION = 4 * 3**FACE_DEPTH
EDGE_DIMENSION = 4 * 3**EDGE_DEPTH


def tuple_index(values, base):
    result = 0
    for value in values:
        result = base * result + value
    return result


def left_cap_collapse_3():
    """L(F)=sum_(a,b) e_b F(e_a,e_a,e_b)."""

    matrix = Mat.zeros(4, EDGE_DIMENSION)
    for paired in range(3):
        for cap in range(3):
            probe_index = tuple_index((paired, paired, cap), 3)
            for component, coefficient in enumerate(Q):
                value = qmul(V[cap], coefficient)
                for output, entry in enumerate(value):
                    matrix[output, 4 * probe_index + component] += entry
    return matrix


def right_cap_collapse_3():
    """R(F)=sum_(a,b) F(e_b,e_a,e_a)e_b."""

    matrix = Mat.zeros(4, EDGE_DIMENSION)
    for paired in range(3):
        for cap in range(3):
            probe_index = tuple_index((cap, paired, paired), 3)
            for component, coefficient in enumerate(Q):
                value = qmul(coefficient, V[cap])
                for output, entry in enumerate(value):
                    matrix[output, 4 * probe_index + component] += entry
    return matrix


def decoded_cap_map(left):
    """Tensor-coordinate form of L or R after the right encoder J_3."""

    matrix = Mat.zeros(4, 4 * 3**EDGE_DEPTH)
    for column, (coefficient, *vectors) in enumerate(
        product(range(4), *([range(3)] * EDGE_DEPTH))
    ):
        value = Q[coefficient]
        if left:
            value = (-3 * value[0], value[1], value[2], value[3])
        for vector in reversed(vectors):
            value = qmul(value, V[vector])
        for component, entry in enumerate(value):
            matrix[component, column] = entry
    return matrix


def full_reverse_product():
    """Pi_6(v_1,...,v_6)=v_6...v_1."""

    matrix = np.zeros((4, 3**N), dtype=np.int64)
    for column, word in enumerate(product(range(3), repeat=N)):
        value = Q[0]
        for vector in reversed(word):
            value = qmul(value, V[vector])
        for component, entry in enumerate(value):
            matrix[component, column] = entry
    return matrix


def actual_five_edge_matching_mod(faces, shadows, prime):
    """Factor the five actual face-to-shadow maps and assemble the matching."""

    right_data = {
        gap: right_inverse_data_mod(face, prime)
        for gap, face in faces.items()
    }
    face_index = {gap: index for index, gap in enumerate(SUPPORT)}
    matrix = np.zeros(
        (5 * EDGE_DIMENSION, 4 * FACE_DIMENSION), dtype=np.int64
    )

    for edge_index, (first_gap, second_gap) in enumerate(KEPT_EDGES):
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


def omega_array(left, right):
    left_array = np.array(left.data, dtype=np.int64)
    right_array = np.array(right.data, dtype=np.int64)
    zero = np.zeros_like(left_array)
    return np.concatenate(
        (-left_array, left_array, zero, -right_array, right_array),
        axis=1,
    )


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    left = left_cap_collapse_3()
    right = right_cap_collapse_3()
    encoder = right_encoder(EDGE_DEPTH)
    check(
        "L J_3 is the left-capped reverse product",
        left * encoder == decoded_cap_map(left=True),
    )
    check(
        "R J_3 is ordinary reverse quaternion multiplication",
        right * encoder == decoded_cap_map(left=False),
    )
    check("L and R are onto H", left.rank() == right.rank() == 4)

    source_generators = response_generators(EDGE_DEPTH)
    target_generators = response_generators(0)
    left_array = np.array(left.data, dtype=np.int64)
    right_array = np.array(right.data, dtype=np.int64)
    check(
        "L and R are SO(3)-equivariant",
        all(
            np.array_equal(target @ operator, operator @ source)
            for operator in (left_array, right_array)
            for source, target in zip(source_generators, target_generators)
        ),
    )

    faces = {
        gap: build_integer_response(N, {gap}) for gap in SUPPORT
    }
    shadows = {
        edge: build_integer_response(N, set(edge))
        for edge in KEPT_EDGES
    }
    total_product = full_reverse_product()
    check(
        "the two left-capped actual shadows collapse to Pi_6 over Z",
        np.array_equal(left_array @ shadows[(1, 2)], total_product)
        and np.array_equal(left_array @ shadows[(1, 4)], total_product),
    )
    check(
        "the two right-capped actual shadows collapse to Pi_6 over Z",
        np.array_equal(right_array @ shadows[(2, 5)], total_product)
        and np.array_equal(right_array @ shadows[(4, 5)], total_product),
    )

    omega = omega_array(left, right)
    for prime in PRIMES:
        matching = actual_five_edge_matching_mod(faces, shadows, prime)
        matching_rank = rank_mod(matching, prime)
        print(
            f"mod {prime}: actual five-edge shape {matching.shape}, "
            f"rank {matching_rank}, "
            f"cokernel {matching.shape[0] - matching_rank}",
        )
        check(
            f"omega_6 kills the actual five-edge matching mod {prime}",
            not np.count_nonzero((omega @ matching) % prime),
        )
        check(
            f"the actual five-edge matching rank is 536 mod {prime}",
            matching_rank == 536,
        )
        check(
            f"omega_6 has rank four mod {prime}",
            rank_mod(omega, prime) == 4,
        )

    block_ranks = tuple(
        rank_mod(
            omega[:, index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION],
            PRIMES[0],
        )
        for index in range(5)
    )
    check(
        "the five labelled edge ranks are 4,4,0,4,4",
        block_ranks == (4, 4, 0, 4, 4),
    )

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED: {', '.join(failed)}")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
