#!/usr/bin/env python3
"""Exact rank verification for the grade-four residual-depth filtration.

Requires SymPy.  All matrices are integer matrices; no floating-point rank
calculation is used.
"""

from __future__ import annotations

from itertools import combinations, product
from typing import Iterable, Sequence

import sympy as sp


IMAGINARY = (1, 2, 3)  # quaternion basis: 0=1, 1=i, 2=j, 3=k


def qmul_basis(a: int, b: int) -> tuple[int, int]:
    """Multiply quaternion basis elements and return (sign, basis_index)."""
    if a == 0:
        return 1, b
    if b == 0:
        return 1, a
    if a == b:
        return -1, 0

    cyclic = {(1, 2): 3, (2, 3): 1, (3, 1): 2}
    if (a, b) in cyclic:
        return 1, cyclic[(a, b)]
    return -1, cyclic[(b, a)]


def multiply_word(word: Iterable[int]) -> tuple[int, int]:
    sign = 1
    value = 0
    for letter in word:
        factor_sign, value = qmul_basis(value, letter)
        sign *= factor_sign
    return sign, value


def partial_response(
    word: Sequence[int], selected_gaps: Sequence[int], probes: Sequence[int]
) -> tuple[int, int]:
    """Evaluate reversed multiplication with probes in selected 1-based gaps."""
    probe_at = dict(zip(selected_gaps, probes, strict=True))
    expanded: list[int] = []

    for position, letter in enumerate(word, start=1):
        expanded.append(letter)
        if position < len(word) and position in probe_at:
            expanded.append(probe_at[position])

    return multiply_word(reversed(expanded))


def response_matrix(n: int, maximum_depth: int) -> sp.Matrix:
    words = list(product(IMAGINARY, repeat=n))
    rows: list[list[int]] = []

    for depth in range(maximum_depth + 1):
        for selected_gaps in combinations(range(1, n), depth):
            for probes in product(IMAGINARY, repeat=depth):
                values = [partial_response(word, selected_gaps, probes) for word in words]
                for output_coordinate in range(4):
                    rows.append(
                        [
                            sign if basis_index == output_coordinate else 0
                            for sign, basis_index in values
                        ]
                    )

    return sp.Matrix(rows)


def pair_basis_vector(a: int, b: int) -> sp.Matrix:
    vector = sp.zeros(9, 1)
    vector[3 * a + b] = 1
    return vector


def grade_two_sectors() -> tuple[list[sp.Matrix], list[sp.Matrix]]:
    """Return integer bases for P=R g + Lambda^2 V and R=S^2_0 V."""
    metric = sum(
        (pair_basis_vector(a, a) for a in range(3)),
        start=sp.zeros(9, 1),
    )

    visible = [metric]
    for a, b in ((0, 1), (1, 2), (2, 0)):
        visible.append(pair_basis_vector(a, b) - pair_basis_vector(b, a))

    residual = [
        pair_basis_vector(0, 0) - pair_basis_vector(1, 1),
        pair_basis_vector(1, 1) - pair_basis_vector(2, 2),
        pair_basis_vector(0, 1) + pair_basis_vector(1, 0),
        pair_basis_vector(1, 2) + pair_basis_vector(2, 1),
        pair_basis_vector(2, 0) + pair_basis_vector(0, 2),
    ]

    return visible, residual


def tensor_sector(left: Sequence[sp.Matrix], right: Sequence[sp.Matrix]) -> sp.Matrix:
    columns = [sp.kronecker_product(x, y) for x in left for y in right]
    return sp.Matrix.hstack(*columns)


def main() -> None:
    visible, residual = grade_two_sectors()
    sectors = {
        "P⊗P": tensor_sector(visible, visible),
        "P⊗R": tensor_sector(visible, residual),
        "R⊗P": tensor_sector(residual, visible),
        "R⊗R": tensor_sector(residual, residual),
    }

    expected_total = {
        0: (4, 77),
        1: (32, 49),
        2: (72, 9),
        3: (81, 0),
    }
    expected_sector_kernels = {
        0: {"P⊗P": 12, "P⊗R": 20, "R⊗P": 20, "R⊗R": 25},
        1: {"P⊗P": 0, "P⊗R": 12, "R⊗P": 12, "R⊗R": 25},
        2: {"P⊗P": 0, "P⊗R": 0, "R⊗P": 0, "R⊗R": 9},
        3: {"P⊗P": 0, "P⊗R": 0, "R⊗P": 0, "R⊗R": 0},
    }

    for depth in range(4):
        matrix = response_matrix(4, depth)
        rank = matrix.rank()
        kernel_dimension = 81 - rank
        assert (rank, kernel_dimension) == expected_total[depth]

        sector_kernels: dict[str, int] = {}
        for name, basis in sectors.items():
            sector_kernels[name] = basis.cols - (matrix * basis).rank()
        assert sector_kernels == expected_sector_kernels[depth]

        print(
            f"depth {depth}: rank={rank}, kernel={kernel_dimension}, "
            f"sectors={sector_kernels}"
        )

    print("grade-four residual-depth verification passed")


if __name__ == "__main__":
    main()
