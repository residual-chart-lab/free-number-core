#!/usr/bin/env python3
"""Exact certificate for the n=5 terminal response tetrahedron.

At length five there are four exact-depth-three terminal faces.  Every pair
of faces has a common exact-depth-two shadow.  This certificate constructs
the six intrinsic pairwise matching maps by factoring the common shadow
through either surjective terminal face, and checks over fractions.Fraction
that pairwise matching is already sufficient for global realizability.

The resulting compatibility operator has rank 200, kernel dimension 232,
and cokernel dimension 16.  Its kernel is exactly the image of the joint
terminal-boundary map.  Standard SO(3) character bookkeeping identifies the
16-dimensional syzygy module as 2V_0 + 3V_1 + V_2.
"""

from fractions import Fraction
from itertools import combinations, product

from all_n_terminal_boundary_certificate import (
    Mat,
    V,
    build_terminal_boundary_face,
    qprod_reversed,
    vstack,
)


def build_response_with_missing_gaps(n, missing_gaps):
    """Probe every internal gap except those in missing_gaps."""

    missing_gaps = set(missing_gaps)
    probed_gaps = [
        gap for gap in range(1, n) if gap not in missing_gaps
    ]
    words = list(product(range(3), repeat=n))
    response = Mat.zeros(4 * 3 ** len(probed_gaps), len(words))

    for column, word in enumerate(words):
        base_letters = [V[index] for index in word]
        for probe_index, probe_word in enumerate(
            product(range(3), repeat=len(probed_gaps))
        ):
            letters = list(base_letters)
            for gap, probe in sorted(
                zip(probed_gaps, probe_word), reverse=True
            ):
                letters.insert(gap, V[probe])
            value = qprod_reversed(letters)
            for component in range(4):
                response[4 * probe_index + component, column] = value[
                    component
                ]
    return response


def pivot_columns(matrix):
    """Return pivot columns of a matrix by exact row reduction."""

    work = [row[:] for row in matrix.data]
    pivots = []
    pivot_row = 0

    for column in range(matrix.ncols):
        pivot = next(
            (
                row
                for row in range(pivot_row, matrix.nrows)
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue

        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [
            value / pivot_value for value in work[pivot_row]
        ]

        for row in range(matrix.nrows):
            if row == pivot_row or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(
                    work[row], work[pivot_row]
                )
            ]

        pivots.append(column)
        pivot_row += 1
        if pivot_row == matrix.nrows:
            break

    return pivots


def inverse(matrix):
    """Invert a square matrix over fractions.Fraction."""

    if matrix.nrows != matrix.ncols:
        raise ValueError("inverse requires a square matrix")

    size = matrix.nrows
    work = [
        row[:]
        + [Fraction(int(row_index == column)) for column in range(size)]
        for row_index, row in enumerate(matrix.data)
    ]

    for column in range(size):
        pivot = next(
            row for row in range(column, size) if work[row][column] != 0
        )
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [value / pivot_value for value in work[column]]

        for row in range(size):
            if row == column or work[row][column] == 0:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(work[row], work[column])
            ]

    return Mat([row[size:] for row in work])


def right_inverse(matrix):
    """Construct a right inverse of a full-row-rank matrix."""

    pivots = pivot_columns(matrix)
    if len(pivots) != matrix.nrows:
        raise ValueError("matrix is not onto")

    pivot_minor = Mat(
        [
            [matrix[row, column] for column in pivots]
            for row in range(matrix.nrows)
        ]
    )
    pivot_inverse = inverse(pivot_minor)
    result = Mat.zeros(matrix.ncols, matrix.nrows)

    for pivot_index, source_row in enumerate(pivots):
        for column in range(matrix.nrows):
            result[source_row, column] = pivot_inverse[
                pivot_index, column
            ]

    return result


def build_pairwise_matching_operator(n):
    """Build all pairwise common-shadow differences among terminal faces."""

    gaps = list(range(1, n))
    faces = {
        gap: build_terminal_boundary_face(n, gap) for gap in gaps
    }
    right_inverses = {
        gap: right_inverse(face) for gap, face in faces.items()
    }

    face_dimension = 4 * 3 ** (n - 2)
    shadow_dimension = 4 * 3 ** (n - 3)
    pair_count = (n - 1) * (n - 2) // 2
    matching = Mat.zeros(
        pair_count * shadow_dimension,
        (n - 1) * face_dimension,
    )
    restrictions = {}

    row_offset = 0
    for first_gap, second_gap in combinations(gaps, 2):
        shadow = build_response_with_missing_gaps(
            n, {first_gap, second_gap}
        )
        first_restriction = shadow * right_inverses[first_gap]
        second_restriction = shadow * right_inverses[second_gap]

        if first_restriction * faces[first_gap] != shadow:
            raise AssertionError("first restriction does not factor")
        if second_restriction * faces[second_gap] != shadow:
            raise AssertionError("second restriction does not factor")

        restrictions[(first_gap, second_gap, first_gap)] = (
            first_restriction
        )
        restrictions[(first_gap, second_gap, second_gap)] = (
            second_restriction
        )

        first_offset = (first_gap - 1) * face_dimension
        second_offset = (second_gap - 1) * face_dimension
        for row in range(shadow_dimension):
            for column in range(face_dimension):
                matching[row_offset + row, first_offset + column] = (
                    first_restriction[row, column]
                )
                matching[row_offset + row, second_offset + column] = (
                    -second_restriction[row, column]
                )

        row_offset += shadow_dimension

    joint_faces = vstack(*(faces[gap] for gap in gaps))
    return matching, joint_faces, restrictions


def add_multiplicities(*terms):
    spins = set().union(*(term for term in terms))
    return {
        spin: sum(term.get(spin, 0) for term in terms)
        for spin in spins
        if sum(term.get(spin, 0) for term in terms)
    }


def scale_multiplicities(multiplicities, scalar):
    return {
        spin: scalar * multiplicity
        for spin, multiplicity in multiplicities.items()
        if scalar * multiplicity
    }


def tensor_with_vector(multiplicities):
    """Clebsch-Gordan multiplication by the spin-one module V."""

    result = {}
    for spin, multiplicity in multiplicities.items():
        targets = (1,) if spin == 0 else (spin - 1, spin, spin + 1)
        for target in targets:
            result[target] = result.get(target, 0) + multiplicity
    return result


def tensor_power_multiplicities(length):
    result = {0: 1}
    for _ in range(length):
        result = tensor_with_vector(result)
    return result


def response_multiplicities(depth):
    """SO(3)-type of Hom(V^tensor-depth,H), with H=V0+V1."""

    domain = tensor_power_multiplicities(depth)
    return add_multiplicities(domain, tensor_with_vector(domain))


def terminal_boundary_multiplicities(n):
    result = tensor_power_multiplicities(n)
    result[n] -= 1
    if result[n] == 0:
        del result[n]
    return result


def syzygy_multiplicities(n):
    """Virtual character of coker(partial_n), assuming middle exactness."""

    face_count = n - 1
    pair_count = face_count * (face_count - 1) // 2
    pair_shadows = scale_multiplicities(
        response_multiplicities(n - 3), pair_count
    )
    faces = scale_multiplicities(
        response_multiplicities(n - 2), -face_count
    )
    boundary = terminal_boundary_multiplicities(n)
    return add_multiplicities(pair_shadows, faces, boundary)


def module_dimension(multiplicities):
    return sum(
        multiplicity * (2 * spin + 1)
        for spin, multiplicity in multiplicities.items()
    )


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    triangle, n4_faces, n4_restrictions = (
        build_pairwise_matching_operator(4)
    )
    tetrahedron, n5_faces, n5_restrictions = (
        build_pairwise_matching_operator(5)
    )

    triangle_rank = triangle.rank()
    tetrahedron_rank = tetrahedron.rank()
    n4_boundary_rank = n4_faces.rank()
    n5_boundary_rank = n5_faces.rank()
    n5_syzygies = syzygy_multiplicities(5)

    print(
        "n=4 response triangle: "
        f"matching rank {triangle_rank}, "
        f"kernel {triangle.ncols - triangle_rank}, "
        f"cokernel {triangle.nrows - triangle_rank}"
    )
    print(
        "n=5 response tetrahedron: "
        f"matching rank {tetrahedron_rank}, "
        f"kernel {tetrahedron.ncols - tetrahedron_rank}, "
        f"cokernel {tetrahedron.nrows - tetrahedron_rank}"
    )
    print(f"n=5 terminal-boundary rank: {n5_boundary_rank}")
    print(f"n=5 syzygy spins: {n5_syzygies}")

    check(
        "the generic restriction construction recovers the n=4 triangle rank",
        triangle_rank == 36,
    )
    check(
        "the n=4 pairwise matching operator is onto",
        triangle.nrows - triangle_rank == 0,
    )
    check(
        "the n=4 response triangle has the established 72-dimensional kernel",
        triangle.ncols - triangle_rank == n4_boundary_rank == 72,
    )
    check(
        "all twelve oriented n=5 face-to-shadow restrictions are onto",
        len(n5_restrictions) == 12
        and all(
            restriction.rank() == 36
            for restriction in n5_restrictions.values()
        ),
    )
    check(
        "the joint n=5 terminal boundary has rank 232",
        n5_boundary_rank == 232,
    )
    check(
        "every actual n=5 boundary satisfies pairwise matching",
        tetrahedron * n5_faces == Mat.zeros(216, 243),
    )
    check(
        "the n=5 pairwise matching operator has rank 200",
        tetrahedron_rank == 200,
    )
    check(
        "pairwise matching is sufficient for n=5 terminal realizability",
        tetrahedron.ncols - tetrahedron_rank == n5_boundary_rank == 232,
    )
    check(
        "the n=5 matching equations have a 16-dimensional syzygy space",
        tetrahedron.nrows - tetrahedron_rank == 16,
    )
    check(
        "SO(3) character bookkeeping gives 2V0+3V1+V2",
        n5_syzygies == {0: 2, 1: 3, 2: 1},
    )
    check(
        "the syzygy character has dimension 16",
        module_dimension(n5_syzygies) == 16,
    )

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")

    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED: {', '.join(failed)}")

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
