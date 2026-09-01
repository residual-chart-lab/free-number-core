#!/usr/bin/env python3
"""Exact certificate for the canonical terminal filling theorem at n=4.

The certificate works over fractions.Fraction and checks that the Casimir
spectral projector onto the unique top-spin V_4 is exactly the kernel of the
three pair-chart map.  Its complementary projector therefore gives the
canonical SO(3)-equivariant, top-spin-free filler.
"""

from fractions import Fraction
from itertools import product

from n4_depth2_structure_certificate import (
    DEPTH2_COMPONENTS,
    Mat,
    PAIR_CHARTS,
    PAIR_CHART_CONSTRAINTS,
    Q,
    SPIN_PROJECTORS,
    V,
    WORDS,
    kernel_spin_multiplicities,
    levi_civita,
    qmul,
    response_matrix,
)


TOP_SPIN_SCALE = Fraction(40320)  # 8!


def scale(matrix, scalar):
    return Mat([[scalar * value for value in row] for row in matrix.data])


def subtract(left, right):
    if (left.nrows, left.ncols) != (right.nrows, right.ncols):
        raise ValueError("matrix shapes differ")
    return Mat(
        [
            [left[row, col] - right[row, col] for col in range(left.ncols)]
            for row in range(left.nrows)
        ]
    )


def build_contraction_map():
    """T -> C_T, contracting the last three tensor factors.

    On the symmetric subspace the choice of the uncontracted factor is
    immaterial.  Quaternion component 0 is zero because C_T is V-valued.
    """

    contraction = Mat.zeros(108, 81)
    for column, word in enumerate(WORDS):
        output_vector = word[0]
        contracted = word[1:]
        for probe_index, probes in enumerate(product(range(3), repeat=3)):
            if probes == contracted:
                contraction[4 * probe_index + output_vector + 1, column] = 1
    return contraction


def terminal_index(x, y, z, component):
    return 4 * (9 * x + 3 * y + z) + component


def bilinear_index(first, second, component):
    return 4 * (3 * first + second) + component


def build_terminal_to_h12():
    """F(x,y,z) -> sum_a e_a F(x,y,e_a)."""

    face = Mat.zeros(36, 108)
    for x in range(3):
        for y in range(3):
            for z, e_z in enumerate(V):
                for component, basis_q in enumerate(Q):
                    value = qmul(e_z, basis_q)
                    for output_component in range(4):
                        face[
                            bilinear_index(x, y, output_component),
                            terminal_index(x, y, z, component),
                        ] += value[output_component]
    return face


def build_terminal_to_h23():
    """F(x,y,z) -> sum_a F(e_a,y,z)e_a."""

    face = Mat.zeros(36, 108)
    for x, e_x in enumerate(V):
        for y in range(3):
            for z in range(3):
                for component, basis_q in enumerate(Q):
                    value = qmul(basis_q, e_x)
                    for output_component in range(4):
                        face[
                            bilinear_index(y, z, output_component),
                            terminal_index(x, y, z, component),
                        ] += value[output_component]
    return face


def build_terminal_to_h13():
    """Decode the last variable once, contract the middle variable, re-encode."""

    face = Mat.zeros(36, 108)
    for x in range(3):
        for output_z, e_z in enumerate(V):
            for decoded_index, e_decoded in enumerate(V):
                for y, e_y in enumerate(V):
                    for decoder_left, e_left in enumerate(V):
                        for input_z in range(3):
                            epsilon = levi_civita(
                                decoded_index, decoder_left, input_z
                            )
                            if not epsilon:
                                continue
                            left_factor = qmul(
                                qmul(qmul(e_decoded, e_z), e_y), e_left
                            )
                            for component, basis_q in enumerate(Q):
                                value = qmul(left_factor, basis_q)
                                for output_component in range(4):
                                    face[
                                        bilinear_index(
                                            x, output_z, output_component
                                        ),
                                        terminal_index(
                                            x, y, input_z, component
                                        ),
                                    ] += (
                                        Fraction(epsilon, 2)
                                        * value[output_component]
                                    )
    return face


RAW_TOP_PROJECTOR = SPIN_PROJECTORS[4]
TOP_PROJECTOR = scale(RAW_TOP_PROJECTOR, Fraction(1, TOP_SPIN_SCALE))
LOWER_PROJECTOR = subtract(Mat.eye(81), TOP_PROJECTOR)
TERMINAL_RESPONSE = response_matrix((1, 2, 3))
CONTRACTION = build_contraction_map()
TERMINAL_TO_H12 = build_terminal_to_h12()
TERMINAL_TO_H13 = build_terminal_to_h13()
TERMINAL_TO_H23 = build_terminal_to_h23()


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    spin_dimensions = {
        spin: projector.rank() for spin, projector in SPIN_PROJECTORS.items()
    }
    spin_multiplicities = {
        spin: dimension // (2 * spin + 1)
        for spin, dimension in spin_dimensions.items()
    }

    print(f"spin dimensions in V^tensor4: {spin_dimensions}")
    print(f"spin multiplicities in V^tensor4: {spin_multiplicities}")
    print(f"top projector rank: {TOP_PROJECTOR.rank()}")
    print(f"top-spin-free projector rank: {LOWER_PROJECTOR.rank()}")
    print(f"pair-boundary rank on top-spin-free sector: {(PAIR_CHARTS * LOWER_PROJECTOR).rank()}")
    print(f"terminal response rank: {TERMINAL_RESPONSE.rank()}")
    print(f"terminal top-spin rank: {(TERMINAL_RESPONSE * TOP_PROJECTOR).rank()}")

    check(
        "V^tensor4 has multiplicities 3V0+6V1+6V2+3V3+V4",
        spin_multiplicities == {0: 3, 1: 6, 2: 6, 3: 3, 4: 1},
    )
    check(
        "the unnormalized Casimir polynomial squares to 8! times itself",
        RAW_TOP_PROJECTOR * RAW_TOP_PROJECTOR
        == scale(RAW_TOP_PROJECTOR, TOP_SPIN_SCALE),
    )
    check(
        "the normalized V4 Casimir projector is idempotent",
        TOP_PROJECTOR * TOP_PROJECTOR == TOP_PROJECTOR,
    )
    check("the V4 projector has rank 9", TOP_PROJECTOR.rank() == 9)
    check(
        "the complementary top-spin-free projector is idempotent",
        LOWER_PROJECTOR * LOWER_PROJECTOR == LOWER_PROJECTOR,
    )
    check(
        "the top-spin-free complement has rank 72",
        LOWER_PROJECTOR.rank() == 72,
    )
    check(
        "the two Casimir projectors are complementary",
        TOP_PROJECTOR * LOWER_PROJECTOR == Mat.zeros(81, 81)
        and LOWER_PROJECTOR * TOP_PROJECTOR == Mat.zeros(81, 81),
    )
    check(
        "the pair-chart kernel is exactly one V4",
        kernel_spin_multiplicities(PAIR_CHARTS) == {4: 1},
    )
    check(
        "all pair boundaries annihilate the V4 projector",
        PAIR_CHARTS * TOP_PROJECTOR == Mat.zeros(108, 81),
    )
    check(
        "the intrinsic compatible pair-boundary space has dimension 72",
        PAIR_CHART_CONSTRAINTS.rank() == 36
        and PAIR_CHART_CONSTRAINTS * PAIR_CHARTS == Mat.zeros(36, 81),
    )
    check(
        "discarding top spin leaves every pair boundary unchanged",
        PAIR_CHARTS * LOWER_PROJECTOR == PAIR_CHARTS,
    )
    check(
        "the pair map restricts to an isomorphism onto compatible boundaries",
        (PAIR_CHARTS * LOWER_PROJECTOR).rank()
        == 108 - PAIR_CHART_CONSTRAINTS.rank()
        == 72,
    )
    check(
        "the terminal all-gap response separates all 81 state directions",
        TERMINAL_RESPONSE.rank() == 81,
    )
    check(
        "the direct terminal face formula recovers H12",
        TERMINAL_TO_H12 * TERMINAL_RESPONSE == DEPTH2_COMPONENTS[(1, 2)],
    )
    check(
        "the one-layer decoded terminal face formula recovers H13",
        TERMINAL_TO_H13 * TERMINAL_RESPONSE == DEPTH2_COMPONENTS[(1, 3)],
    )
    check(
        "the direct terminal face formula recovers H23",
        TERMINAL_TO_H23 * TERMINAL_RESPONSE == DEPTH2_COMPONENTS[(2, 3)],
    )
    check(
        "terminal response splits into 72 lower-spin and 9 top-spin directions",
        (TERMINAL_RESPONSE * LOWER_PROJECTOR).rank() == 72
        and (TERMINAL_RESPONSE * TOP_PROJECTOR).rank() == 9,
    )
    check(
        "the terminal top-spin coefficient is A4=-8C",
        TERMINAL_RESPONSE * TOP_PROJECTOR
        == scale(CONTRACTION * TOP_PROJECTOR, -8),
    )

    print("certificate checks:")
    all_ok = True
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        all_ok = all_ok and passed
    print("ALL CHECKS PASSED" if all_ok else "SOME CHECK FAILED")


if __name__ == "__main__":
    report()
