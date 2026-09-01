#!/usr/bin/env python3
"""Exact modular certificate for the n=6 terminal response 4-simplex.

At length six there are five exact-depth-four terminal faces and ten
pairwise exact-depth-three common shadows.  The resulting matching operator
has shape 1080 x 1620.

Direct fractions.Fraction elimination at this size obscures the structure
with unnecessary coefficient growth.  This certificate instead performs
deterministic Gaussian elimination over the exact prime fields F_1009 and
F_1013.  The response and matching matrices are reductions of rational
matrices whose decoder denominators are powers of two, so both reductions are
well defined.

The all-n terminal theorem gives the rational upper bound

    rank_Q(partial_6) <= 1620 - (3^6 - 13) = 904.

Finding rank 904 after reduction modulo either prime exhibits a nonzero
904-minor over Q.  Hence the rational rank is exactly 904.  Pairwise matching
is therefore sufficient at n=6, and the compatibility cokernel has dimension
176 and SO(3)-type 10V0 + 21V1 + 15V2 + 4V3.

NumPy is used only as a vectorized storage and row-operation backend.  Every
entry and every operation is exact finite-field arithmetic; no floating-point
calculation is used.
"""

from itertools import combinations, product

try:
    import numpy as np
except ImportError as exc:  # pragma: no cover - environment diagnostic
    raise SystemExit(
        "This large exact modular certificate requires NumPy."
    ) from exc

from n2_intrinsic_response_certificate import Q, V, qmul
from n5_response_tetrahedron_certificate import (
    module_dimension,
    syzygy_multiplicities,
)


PRIMES = (1009, 1013)


def qprod_reversed(letters):
    out = Q[0]
    for letter in reversed(letters):
        out = qmul(out, letter)
    return out


def build_integer_response(n, missing_gaps):
    """Build a signed integer response matrix before prime reduction."""

    missing_gaps = set(missing_gaps)
    probed_gaps = [
        gap for gap in range(1, n) if gap not in missing_gaps
    ]
    words = list(product(range(3), repeat=n))
    probe_words = list(product(range(3), repeat=len(probed_gaps)))
    response = np.zeros(
        (4 * len(probe_words), len(words)), dtype=np.int64
    )

    for column, word in enumerate(words):
        base_letters = [V[index] for index in word]
        for probe_index, probe_word in enumerate(probe_words):
            letters = list(base_letters)
            for gap, probe in sorted(
                zip(probed_gaps, probe_word), reverse=True
            ):
                letters.insert(gap, V[probe])
            value = qprod_reversed(letters)
            for component in range(4):
                response[4 * probe_index + component, column] = (
                    value[component]
                )

    return response


def right_inverse_data_mod(matrix, prime):
    """Return pivot columns and the inverse pivot minor modulo prime."""

    row_count, column_count = matrix.shape
    augmented = np.concatenate(
        [
            matrix.copy() % prime,
            np.eye(row_count, dtype=np.int64),
        ],
        axis=1,
    )
    pivots = []
    pivot_row = 0

    for column in range(column_count):
        candidates = np.flatnonzero(augmented[pivot_row:, column])
        if not candidates.size:
            continue

        source_row = pivot_row + int(candidates[0])
        if source_row != pivot_row:
            augmented[[pivot_row, source_row]] = augmented[
                [source_row, pivot_row]
            ]

        pivot_inverse = pow(
            int(augmented[pivot_row, column]), -1, prime
        )
        augmented[pivot_row] = (
            augmented[pivot_row] * pivot_inverse
        ) % prime

        affected = np.flatnonzero(augmented[:, column])
        affected = affected[affected != pivot_row]
        if affected.size:
            factors = augmented[affected, column].copy()
            augmented[affected] = (
                augmented[affected]
                - factors[:, None] * augmented[pivot_row]
            ) % prime

        pivots.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    if pivot_row != row_count:
        raise AssertionError(
            f"terminal face rank dropped modulo {prime}: "
            f"{pivot_row} != {row_count}"
        )

    inverse_minor = augmented[:, column_count:]
    pivot_minor = matrix[:, pivots] % prime
    identity = np.eye(row_count, dtype=np.int64)
    if not np.array_equal(
        (pivot_minor @ inverse_minor) % prime, identity
    ):
        raise AssertionError("right-inverse construction failed")

    return np.asarray(pivots, dtype=np.int64), inverse_minor


def rank_mod(matrix, prime):
    """Deterministic row rank over a prime field."""

    work = matrix.copy() % prime
    row_count, column_count = work.shape
    pivot_row = 0

    for column in range(column_count):
        candidates = np.flatnonzero(work[pivot_row:, column])
        if not candidates.size:
            continue

        source_row = pivot_row + int(candidates[0])
        if source_row != pivot_row:
            work[[pivot_row, source_row]] = work[
                [source_row, pivot_row]
            ]

        pivot_inverse = pow(
            int(work[pivot_row, column]), -1, prime
        )
        work[pivot_row, column:] = (
            work[pivot_row, column:] * pivot_inverse
        ) % prime

        affected = pivot_row + 1 + np.flatnonzero(
            work[pivot_row + 1 :, column]
        )
        if affected.size:
            factors = work[affected, column].copy()
            work[affected, column:] = (
                work[affected, column:]
                - factors[:, None] * work[pivot_row, column:]
            ) % prime

        pivot_row += 1
        if pivot_row == row_count:
            break

    return pivot_row


def build_matching_operator_mod(faces, shadows, prime):
    """Construct partial_6 and the joint terminal boundary modulo prime."""

    gaps = sorted(faces)
    face_dimension = next(iter(faces.values())).shape[0]
    shadow_dimension = next(iter(shadows.values())).shape[0]
    right_data = {
        gap: right_inverse_data_mod(faces[gap], prime)
        for gap in gaps
    }
    blocks = []
    restriction_ranks = []

    for first_gap, second_gap in combinations(gaps, 2):
        shadow = shadows[(first_gap, second_gap)] % prime
        first_pivots, first_inverse = right_data[first_gap]
        second_pivots, second_inverse = right_data[second_gap]

        first_restriction = (
            shadow[:, first_pivots] @ first_inverse
        ) % prime
        second_restriction = (
            shadow[:, second_pivots] @ second_inverse
        ) % prime

        if not np.array_equal(
            (first_restriction @ faces[first_gap]) % prime,
            shadow,
        ):
            raise AssertionError("first common-shadow factorization failed")
        if not np.array_equal(
            (second_restriction @ faces[second_gap]) % prime,
            shadow,
        ):
            raise AssertionError("second common-shadow factorization failed")

        restriction_ranks.extend(
            [
                rank_mod(first_restriction, prime),
                rank_mod(second_restriction, prime),
            ]
        )

        block = np.zeros(
            (shadow_dimension, len(gaps) * face_dimension),
            dtype=np.int64,
        )
        first_offset = (first_gap - 1) * face_dimension
        second_offset = (second_gap - 1) * face_dimension
        block[
            :, first_offset : first_offset + face_dimension
        ] = first_restriction
        block[
            :, second_offset : second_offset + face_dimension
        ] = (-second_restriction) % prime
        blocks.append(block)

    matching = np.concatenate(blocks, axis=0)
    joint_faces = np.concatenate(
        [faces[gap] for gap in gaps], axis=0
    )
    return matching, joint_faces, restriction_ranks


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    n = 6
    gaps = list(range(1, n))
    faces = {
        gap: build_integer_response(n, {gap}) for gap in gaps
    }
    shadows = {
        pair: build_integer_response(n, set(pair))
        for pair in combinations(gaps, 2)
    }

    expected_face_shape = (324, 729)
    expected_shadow_shape = (108, 729)
    check(
        "all five terminal faces have shape 324 x 729",
        all(face.shape == expected_face_shape for face in faces.values()),
    )
    check(
        "all ten common shadows have shape 108 x 729",
        all(
            shadow.shape == expected_shadow_shape
            for shadow in shadows.values()
        ),
    )

    modular_results = {}
    for prime in PRIMES:
        matching, joint_faces, restriction_ranks = (
            build_matching_operator_mod(faces, shadows, prime)
        )
        matching_rank = rank_mod(matching, prime)
        boundary_rank = rank_mod(joint_faces, prime)
        annihilates = not np.count_nonzero(
            (matching @ joint_faces) % prime
        )
        modular_results[prime] = {
            "matching_rank": matching_rank,
            "boundary_rank": boundary_rank,
            "kernel_dimension": matching.shape[1] - matching_rank,
            "cokernel_dimension": matching.shape[0] - matching_rank,
            "restriction_ranks": restriction_ranks,
            "annihilates": annihilates,
        }

        print(
            f"mod {prime}: matching rank {matching_rank}, "
            f"kernel {matching.shape[1] - matching_rank}, "
            f"cokernel {matching.shape[0] - matching_rank}, "
            f"boundary rank {boundary_rank}"
        )

    for prime, result in modular_results.items():
        check(
            f"all twenty oriented restrictions are onto modulo {prime}",
            len(result["restriction_ranks"]) == 20
            and all(rank == 108 for rank in result["restriction_ranks"]),
        )
        check(
            f"actual boundaries satisfy pairwise matching modulo {prime}",
            result["annihilates"],
        )
        check(
            f"the joint terminal boundary has rank 716 modulo {prime}",
            result["boundary_rank"] == 716,
        )
        check(
            f"the pairwise matching operator has rank 904 modulo {prime}",
            result["matching_rank"] == 904,
        )
        check(
            f"the compatible kernel has dimension 716 modulo {prime}",
            result["kernel_dimension"] == 716,
        )
        check(
            f"the compatibility cokernel has dimension 176 modulo {prime}",
            result["cokernel_dimension"] == 176,
        )

    rational_rank_upper_bound = 1620 - (3**6 - 13)
    check(
        "the all-n terminal theorem gives rational rank upper bound 904",
        rational_rank_upper_bound == 904,
    )
    check(
        "a modular 904-minor forces rational rank exactly 904",
        any(
            result["matching_rank"] == rational_rank_upper_bound
            for result in modular_results.values()
        ),
    )

    n6_syzygies = syzygy_multiplicities(6)
    print(f"n=6 syzygy spins: {n6_syzygies}")
    check(
        "SO(3) character bookkeeping gives 10V0+21V1+15V2+4V3",
        n6_syzygies == {0: 10, 1: 21, 2: 15, 3: 4},
    )
    check(
        "the n=6 syzygy character has dimension 176",
        module_dimension(n6_syzygies) == 176,
    )

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")

    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED: {', '.join(failed)}")

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
