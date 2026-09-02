#!/usr/bin/env python3
"""Certificate for the tetrahedral second response differential.

The pairwise terminal matching map partial_n has one target block for every
edge of the response simplex.  For every four vertices Q, restrict partial_n
to the four face blocks and the six edge blocks supported on Q and put

    Y_(n,Q) = coker(partial_(n,Q)).

The quotient maps to the Y_(n,Q) assemble to a canonical-by-construction
second map partial_n^(2).  This script checks the first two cases:

* n=5 over Q: one 16-dimensional tetrahedral quotient and exactness at C1;
* n=6 over F_1009 and F_1013: five 48-dimensional local quotients,
  rank(partial_6^(2))=176, and ker(partial_6^(2))=im(partial_6).

It also descends the SO(3) Casimir to the actual local quotients and the
second cokernel.  No floating-point arithmetic is used.
"""

from fractions import Fraction
from itertools import combinations

import numpy as np

from n2_intrinsic_response_certificate import Mat
from n5_response_tetrahedron_certificate import (
    build_pairwise_matching_operator,
    build_response_with_missing_gaps,
)
from n6_response_4simplex_modular_certificate import (
    build_integer_response,
    build_matching_operator_mod,
    rank_mod,
    right_inverse_data_mod,
)


PRIMES = (1009, 1013)


def transpose_exact(matrix):
    return Mat(
        [
            [matrix[row, column] for row in range(matrix.nrows)]
            for column in range(matrix.ncols)
        ]
    )


def fraction_mod(value, prime):
    value = Fraction(value)
    return (
        value.numerator * pow(value.denominator, -1, prime)
    ) % prime


def nullspace_exact(matrix):
    """Return a matrix whose columns are a Q-basis of ker(matrix)."""

    work = [row[:] for row in matrix.data]
    pivot_columns = []
    pivot_row = 0
    for column in range(matrix.ncols):
        pivot = next(
            (
                row
                for row in range(pivot_row, matrix.nrows)
                if work[row][column]
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(matrix.nrows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[row], work[pivot_row])
            ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == matrix.nrows:
            break

    free_columns = [
        column
        for column in range(matrix.ncols)
        if column not in set(pivot_columns)
    ]
    basis = Mat.zeros(matrix.ncols, len(free_columns))
    for basis_column, free_column in enumerate(free_columns):
        basis[free_column, basis_column] = 1
        for row, pivot_column in enumerate(pivot_columns):
            basis[pivot_column, basis_column] = -work[row][free_column]
    return basis


def left_nullspace_exact(matrix):
    return transpose_exact(nullspace_exact(transpose_exact(matrix)))


def nullspace_mod(matrix, prime):
    """Columns form a kernel basis, using echelon form and back-substitution."""

    work = np.asarray(matrix, dtype=np.int64).copy() % prime
    row_count, column_count = work.shape
    pivot_columns = []
    pivot_row = 0

    for column in range(column_count):
        candidates = np.flatnonzero(work[pivot_row:, column])
        if not candidates.size:
            continue
        source_row = pivot_row + int(candidates[0])
        if source_row != pivot_row:
            work[[pivot_row, source_row]] = work[[source_row, pivot_row]]
        inverse = pow(int(work[pivot_row, column]), -1, prime)
        work[pivot_row, column:] = (
            work[pivot_row, column:] * inverse
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
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == row_count:
            break

    pivot_set = set(pivot_columns)
    free_columns = [
        column for column in range(column_count) if column not in pivot_set
    ]
    basis = np.zeros(
        (column_count, len(free_columns)), dtype=np.int64
    )
    for index, column in enumerate(free_columns):
        basis[column, index] = 1

    for row in reversed(range(len(pivot_columns))):
        pivot_column = pivot_columns[row]
        if pivot_column + 1 < column_count:
            basis[pivot_column] = -(
                work[row, pivot_column + 1 :] @ basis[pivot_column + 1 :]
            ) % prime
    return basis


def left_nullspace_mod(matrix, prime):
    return nullspace_mod(np.asarray(matrix).T, prime).T


def select_local_operator(
    matching, gaps, face_dimension, shadow_dimension, four_subset
):
    """Select the four face columns and six edge rows supported on Q."""

    all_edges = list(combinations(gaps, 2))
    local_edges = list(combinations(four_subset, 2))
    row_indices = np.concatenate(
        [
            np.arange(
                all_edges.index(edge) * shadow_dimension,
                (all_edges.index(edge) + 1) * shadow_dimension,
            )
            for edge in local_edges
        ]
    )
    column_indices = np.concatenate(
        [
            np.arange(
                gaps.index(gap) * face_dimension,
                (gaps.index(gap) + 1) * face_dimension,
            )
            for gap in four_subset
        ]
    )
    return matching[np.ix_(row_indices, column_indices)], row_indices


def build_second_map_mod(
    matching, gaps, face_dimension, shadow_dimension, prime
):
    local_data = []
    embedded_quotients = []
    for four_subset in combinations(gaps, 4):
        local, row_indices = select_local_operator(
            matching,
            gaps,
            face_dimension,
            shadow_dimension,
            four_subset,
        )
        quotient = left_nullspace_mod(local, prime)
        embedded = np.zeros(
            (quotient.shape[0], matching.shape[0]), dtype=np.int64
        )
        embedded[:, row_indices] = quotient
        embedded_quotients.append(embedded)
        local_data.append((four_subset, local, quotient))
    return np.concatenate(embedded_quotients, axis=0) % prime, local_data


def vector_generators():
    return (
        np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=np.int64),
        np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0]], dtype=np.int64),
        np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0]], dtype=np.int64),
    )


def response_generators(depth):
    """Infinitesimal SO(3) action on Hom(V^tensor-depth,H)."""

    generators = []
    vector_identity = np.eye(3, dtype=np.int64)
    domain_dimension = 3**depth
    for vector_generator in vector_generators():
        quaternion_generator = np.zeros((4, 4), dtype=np.int64)
        quaternion_generator[1:, 1:] = vector_generator
        domain_generator = np.zeros(
            (domain_dimension, domain_dimension), dtype=np.int64
        )
        for slot in range(depth):
            factors = [vector_identity] * depth
            factors[slot] = vector_generator
            term = factors[0]
            for factor in factors[1:]:
                term = np.kron(term, factor)
            domain_generator += term
        generators.append(
            np.kron(np.eye(domain_dimension, dtype=np.int64), quaternion_generator)
            - np.kron(domain_generator.T, np.eye(4, dtype=np.int64))
        )
    return generators


def apply_block_generator(rows, block_generator):
    block_dimension = block_generator.shape[0]
    blocks = rows.shape[1] // block_dimension
    return np.concatenate(
        [
            rows[:, index * block_dimension : (index + 1) * block_dimension]
            @ block_generator
            for index in range(blocks)
        ],
        axis=1,
    )


def induced_generators(quotient, block_generators, prime):
    pivots, inverse_minor = right_inverse_data_mod(quotient, prime)
    induced = []
    for generator in block_generators:
        acted = apply_block_generator(quotient, generator) % prime
        descended = (acted[:, pivots] @ inverse_minor) % prime
        if np.count_nonzero((descended @ quotient - acted) % prime):
            raise AssertionError("SO(3) action does not descend")
        induced.append(descended)
    return induced


def block_diagonal_action(rows, block_generators):
    pieces = []
    offset = 0
    for generators in block_generators:
        dimension = generators[0].shape[0]
        pieces.append(rows[:, offset : offset + dimension] @ generators)
        offset += dimension
    return np.concatenate(pieces, axis=1)


def descend_from_blocks(quotient, block_generator_triples, prime):
    pivots, inverse_minor = right_inverse_data_mod(quotient, prime)
    induced = []
    for axis in range(3):
        block_generators = [triple[axis] for triple in block_generator_triples]
        acted = block_diagonal_action(quotient, block_generators) % prime
        descended = (acted[:, pivots] @ inverse_minor) % prime
        if np.count_nonzero((descended @ quotient - acted) % prime):
            raise AssertionError("block SO(3) action does not descend")
        induced.append(descended)
    return induced


def casimir_type(generators, maximum_spin, prime):
    dimension = generators[0].shape[0]
    casimir = -sum(
        (generator @ generator) % prime for generator in generators
    ) % prime
    identity = np.eye(dimension, dtype=np.int64)
    multiplicities = {}
    for spin in range(maximum_spin + 1):
        eigenspace_dimension = dimension - rank_mod(
            (casimir - spin * (spin + 1) * identity) % prime,
            prime,
        )
        if eigenspace_dimension:
            if eigenspace_dimension % (2 * spin + 1):
                raise AssertionError("invalid Casimir eigenspace dimension")
            multiplicities[spin] = eigenspace_dimension // (2 * spin + 1)
    recovered_dimension = sum(
        (2 * spin + 1) * count
        for spin, count in multiplicities.items()
    )
    if recovered_dimension != dimension:
        raise AssertionError("Casimir eigenspaces do not exhaust quotient")
    return multiplicities


def exact_n5():
    matching, _, _ = build_pairwise_matching_operator(5)
    quotient = left_nullspace_exact(matching)
    zero = quotient * matching
    gaps = list(range(1, 5))
    edges = list(combinations(gaps, 2))
    failed_naive_restrictions = []
    for triple in combinations(gaps, 3):
        triple_response = build_response_with_missing_gaps(5, triple)
        for edge in combinations(triple, 2):
            pair_response = build_response_with_missing_gaps(5, edge)
            stacked = Mat(pair_response.data + triple_response.data)
            if stacked.rank() != pair_response.rank():
                failed_naive_restrictions.append((edge, triple))

    triangle_ranks = []
    face_dimension = 108
    shadow_dimension = 36
    for triple in combinations(gaps, 3):
        local_rows = []
        for edge in combinations(triple, 2):
            edge_index = edges.index(edge)
            for row in range(
                edge_index * shadow_dimension,
                (edge_index + 1) * shadow_dimension,
            ):
                local_rows.append(
                    [
                        matching[row, (gap - 1) * face_dimension + column]
                        for gap in triple
                        for column in range(face_dimension)
                    ]
                )
        triangle_ranks.append(Mat(local_rows).rank())
    return {
        "matching": matching,
        "quotient": quotient,
        "annihilates": zero == Mat.zeros(quotient.nrows, matching.ncols),
        "second_rank": quotient.rank(),
        "second_kernel": matching.nrows - quotient.rank(),
        "failed_naive_restrictions": failed_naive_restrictions,
        "triangle_ranks": triangle_ranks,
    }


def modular_case(n, prime):
    gaps = list(range(1, n))
    faces = {gap: build_integer_response(n, {gap}) for gap in gaps}
    shadows = {
        pair: build_integer_response(n, set(pair))
        for pair in combinations(gaps, 2)
    }
    matching, _, _ = build_matching_operator_mod(faces, shadows, prime)
    face_dimension = 4 * 3 ** (n - 2)
    shadow_dimension = 4 * 3 ** (n - 3)
    second, local_data = build_second_map_mod(
        matching,
        gaps,
        face_dimension,
        shadow_dimension,
        prime,
    )
    local_generators = []
    response_action = response_generators(n - 3)
    for _, _, quotient in local_data:
        local_generators.append(
            induced_generators(quotient, response_action, prime)
        )
    second_cokernel = left_nullspace_mod(second, prime)
    cokernel_generators = descend_from_blocks(
        second_cokernel, local_generators, prime
    )
    return {
        "matching": matching,
        "matching_rank": rank_mod(matching, prime),
        "second": second,
        "second_rank": rank_mod(second, prime),
        "local_data": local_data,
        "local_types": [
            casimir_type(generators, n - 3, prime)
            for generators in local_generators
        ],
        "cokernel_dimension": second_cokernel.shape[0],
        "cokernel_type": casimir_type(
            cokernel_generators, n - 3, prime
        ),
    }


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    n5 = exact_n5()
    print(
        "n=5 over Q: "
        f"local quotient {n5['quotient'].nrows}, "
        f"second rank {n5['second_rank']}, "
        f"second kernel {n5['second_kernel']}"
    )
    check("n=5 quotient annihilates the first differential exactly", n5["annihilates"])
    check("n=5 tetrahedral quotient has dimension 16", n5["quotient"].nrows == 16)
    check(
        "n=5 second kernel equals the 200-dimensional first image",
        n5["second_kernel"] == n5["matching"].rank() == 200,
    )
    expected_failures = [
        ((1, 3), (1, 2, 3)),
        ((1, 4), (1, 2, 4)),
        ((1, 4), (1, 3, 4)),
        ((2, 4), (2, 3, 4)),
    ]
    check(
        "the naive pair-to-triple restrictions fail in exactly four long-edge cases",
        n5["failed_naive_restrictions"] == expected_failures,
    )
    check(
        "every three-face matching subsystem is onto",
        n5["triangle_ranks"] == [108] * 4,
    )

    n5_quotient_mod = np.array(
        [
            [fraction_mod(value, PRIMES[0]) for value in row]
            for row in n5["quotient"].data
        ],
        dtype=np.int64,
    )
    n5_type = casimir_type(
        induced_generators(
            n5_quotient_mod,
            response_generators(2),
            PRIMES[0],
        ),
        2,
        PRIMES[0],
    )
    print(f"n=5 local Casimir type: {n5_type}")
    check(
        "n=5 tetrahedral quotient has type 2V0+3V1+V2",
        n5_type == {0: 2, 1: 3, 2: 1},
    )

    expected_local = {0: 3, 1: 6, 2: 4, 3: 1}
    expected_cokernel = {0: 5, 1: 9, 2: 5, 3: 1}
    for prime in PRIMES:
        n6 = modular_case(6, prime)
        local_dimensions = [
            quotient.shape[0]
            for _, _, quotient in n6["local_data"]
        ]
        print(
            f"n=6 mod {prime}: local quotients {local_dimensions}, "
            f"second rank {n6['second_rank']}, "
            f"kernel {n6['matching'].shape[0] - n6['second_rank']}, "
            f"cokernel {n6['cokernel_dimension']}"
        )
        print(f"  local Casimir types: {n6['local_types']}")
        print(f"  second-cokernel Casimir type: {n6['cokernel_type']}")
        check(
            f"n=6 has five 48-dimensional quotients mod {prime}",
            local_dimensions == [48] * 5,
        )
        check(
            f"n=6 second differential kills the first image mod {prime}",
            not np.count_nonzero(
                (n6["second"] @ n6["matching"]) % prime
            ),
        )
        check(
            f"n=6 second differential has rank 176 mod {prime}",
            n6["second_rank"] == 176,
        )
        check(
            f"n=6 is exact at C1 mod {prime}",
            n6["matching"].shape[0] - n6["second_rank"]
            == n6["matching_rank"]
            == 904,
        )
        check(
            f"n=6 local quotient type is H^2 tensor V mod {prime}",
            n6["local_types"] == [expected_local] * 5,
        )
        check(
            f"n=6 second cokernel has dimension 64 mod {prime}",
            n6["cokernel_dimension"] == 64,
        )
        check(
            f"n=6 second cokernel type is H^3 mod {prime}",
            n6["cokernel_type"] == expected_cokernel,
        )

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED: {', '.join(failed)}")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
