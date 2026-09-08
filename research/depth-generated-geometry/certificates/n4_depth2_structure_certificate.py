#!/usr/bin/env python3
"""Exact structural certificate for the length-four depth-two response."""

from fractions import Fraction
from itertools import combinations, product

from n2_intrinsic_response_certificate import Mat, Q, V, levi_civita, qmul


ONE = Q[0]
IMAG = V
WORDS = list(product(range(3), repeat=4))
PAIRS = list(combinations(range(1, 4), 2))
WORD_INDEX = {word: index for index, word in enumerate(WORDS)}


def qprod_reversed(letters):
    out = ONE
    for letter in reversed(letters):
        out = qmul(out, letter)
    return out


def qadd(left, right):
    return tuple(a + b for a, b in zip(left, right))


def qscale(scalar, value):
    return tuple(Fraction(scalar) * component for component in value)


def bilinear_index(first, second, component):
    return 4 * (3 * first + second) + component


def linear_index(argument, component):
    return 4 * argument + component


def response_matrix(slots):
    degree = len(slots)
    out = Mat.zeros(4 * 3**degree, len(WORDS))
    for col, word in enumerate(WORDS):
        base = [IMAG[index] for index in word]
        for probe_index, probe_word in enumerate(product(range(3), repeat=degree)):
            letters = list(base)
            for slot, value in sorted(zip(slots, probe_word), reverse=True):
                letters.insert(slot, IMAG[value])
            value = qprod_reversed(letters)
            for component in range(4):
                out[4 * probe_index + component, col] = value[component]
    return out


VALUE = response_matrix(())
DEPTH1_COMPONENTS = {slot: response_matrix((slot,)) for slot in range(1, 4)}
DEPTH2_COMPONENTS = {pair: response_matrix(pair) for pair in PAIRS}
def vstack(*matrices):
    if not matrices:
        return Mat([])
    ncols = matrices[0].ncols
    if any(matrix.ncols != ncols for matrix in matrices):
        raise ValueError("column counts differ")
    return Mat([row for matrix in matrices for row in matrix.data])


def add(left, right):
    if (left.nrows, left.ncols) != (right.nrows, right.ncols):
        raise ValueError("matrix shapes differ")
    return Mat(
        [
            [left[row, col] + right[row, col] for col in range(left.ncols)]
            for row in range(left.nrows)
        ]
    )


def shifted(matrix, scalar):
    out = Mat([row[:] for row in matrix.data])
    for index in range(min(out.nrows, out.ncols)):
        out[index, index] += scalar
    return out


def build_casimir():
    generators = []
    for axis in range(3):
        generator = Mat.zeros(len(WORDS), len(WORDS))
        for col, word in enumerate(WORDS):
            for position in range(4):
                old = word[position]
                for new in range(3):
                    coefficient = -levi_civita(axis, new, old)
                    if coefficient:
                        changed = list(word)
                        changed[position] = new
                        generator[WORD_INDEX[tuple(changed)], col] += coefficient
        generators.append(generator)

    casimir = Mat.zeros(len(WORDS), len(WORDS))
    for generator in generators:
        casimir = add(casimir, generator * generator)
    return casimir


CASIMIR = build_casimir()


def spin_projector_polynomial(spin):
    projector = Mat.eye(len(WORDS))
    for other_spin in range(5):
        if other_spin != spin:
            projector = shifted(CASIMIR, other_spin * (other_spin + 1)) * projector
    return projector


SPIN_PROJECTORS = {spin: spin_projector_polynomial(spin) for spin in range(5)}


DEPTH1 = vstack(VALUE, *DEPTH1_COMPONENTS.values())
DEPTH2 = vstack(DEPTH1, *DEPTH2_COMPONENTS.values())


def build_left_contraction_second():
    """H(x,y) -> (x -> sum_y e_y H(x,e_y))."""
    matrix = Mat.zeros(12, 36)
    for first in range(3):
        for second, e_second in enumerate(V):
            for component, basis_q in enumerate(Q):
                value = qmul(e_second, basis_q)
                for out_component in range(4):
                    matrix[linear_index(first, out_component), bilinear_index(first, second, component)] += value[out_component]
    return matrix


def build_right_contraction_first():
    """H(x,y) -> (y -> sum_x H(e_x,y)e_x)."""
    matrix = Mat.zeros(12, 36)
    for first, e_first in enumerate(V):
        for second in range(3):
            for component, basis_q in enumerate(Q):
                value = qmul(basis_q, e_first)
                for out_component in range(4):
                    matrix[linear_index(second, out_component), bilinear_index(first, second, component)] += value[out_component]
    return matrix


def build_h12_to_f1():
    """Decode the first variable on the right, contract the second, re-encode."""
    matrix = Mat.zeros(12, 36)
    for first_input in range(3):
        for second_input, e_second in enumerate(V):
            for component, basis_q in enumerate(Q):
                column = bilinear_index(first_input, second_input, component)
                decoded = [(0, 0, 0, 0) for _ in range(3)]
                for pure_index in range(3):
                    value = (0, 0, 0, 0)
                    for basis_index, e_basis in enumerate(V):
                        epsilon = levi_civita(pure_index, basis_index, first_input)
                        if epsilon:
                            term = qscale(Fraction(-epsilon, 2), qmul(basis_q, e_basis))
                            value = qadd(value, term)
                    decoded[pure_index] = value

                contracted = [qmul(value, e_second) for value in decoded]
                for output_argument, e_argument in enumerate(V):
                    output = (0, 0, 0, 0)
                    for pure_index, e_pure in enumerate(V):
                        term = qmul(qmul(contracted[pure_index], e_argument), e_pure)
                        output = qadd(output, term)
                    for out_component in range(4):
                        matrix[linear_index(output_argument, out_component), column] = output[out_component]
    return matrix


def build_h23_to_f3():
    """Decode the second variable on the left, contract the first, re-encode."""
    matrix = Mat.zeros(12, 36)
    for first_input, e_first in enumerate(V):
        for second_input in range(3):
            for component, basis_q in enumerate(Q):
                column = bilinear_index(first_input, second_input, component)
                decoded = [(0, 0, 0, 0) for _ in range(3)]
                for pure_index in range(3):
                    value = (0, 0, 0, 0)
                    for basis_index, e_basis in enumerate(V):
                        epsilon = levi_civita(pure_index, basis_index, second_input)
                        if epsilon:
                            term = qscale(Fraction(epsilon, 2), qmul(e_basis, basis_q))
                            value = qadd(value, term)
                    decoded[pure_index] = value

                contracted = [qmul(e_first, value) for value in decoded]
                for output_argument, e_argument in enumerate(V):
                    output = (0, 0, 0, 0)
                    for pure_index, e_pure in enumerate(V):
                        term = qmul(qmul(e_pure, e_argument), contracted[pure_index])
                        output = qadd(output, term)
                    for out_component in range(4):
                        matrix[linear_index(output_argument, out_component), column] = output[out_component]
    return matrix


PI_12_TO_1 = build_h12_to_f1()
PI_12_TO_2 = build_right_contraction_first()
PI_13_TO_1 = build_left_contraction_second()
PI_13_TO_3 = build_right_contraction_first()
PI_23_TO_2 = build_left_contraction_second()
PI_23_TO_3 = build_h23_to_f3()


def build_left_linear_contraction():
    matrix = Mat.zeros(4, 12)
    for argument, e_argument in enumerate(V):
        for component, basis_q in enumerate(Q):
            value = qmul(e_argument, basis_q)
            for out_component in range(4):
                matrix[out_component, linear_index(argument, component)] += value[out_component]
    return matrix


def build_right_linear_contraction():
    matrix = Mat.zeros(4, 12)
    for argument, e_argument in enumerate(V):
        for component, basis_q in enumerate(Q):
            value = qmul(basis_q, e_argument)
            for out_component in range(4):
                matrix[out_component, linear_index(argument, component)] += value[out_component]
    return matrix


LEFT_LINEAR_CONTRACTION = build_left_linear_contraction()
RIGHT_LINEAR_CONTRACTION = build_right_linear_contraction()


def build_pair_chart_constraints():
    constraints = Mat.zeros(36, 108)
    equalities = (
        (0, PI_12_TO_1, 1, PI_13_TO_1),
        (0, PI_12_TO_2, 2, PI_23_TO_2),
        (1, PI_13_TO_3, 2, PI_23_TO_3),
    )
    for block, (left_chart, left_map, right_chart, right_map) in enumerate(equalities):
        for row in range(12):
            for col in range(36):
                constraints[12 * block + row, 36 * left_chart + col] += left_map[row, col]
                constraints[12 * block + row, 36 * right_chart + col] -= right_map[row, col]
    return constraints


PAIR_CHARTS = vstack(*DEPTH2_COMPONENTS.values())
PAIR_CHART_CONSTRAINTS = build_pair_chart_constraints()


def rank_on_kernel(operator, constraints):
    return vstack(constraints, operator).rank() - constraints.rank()


def kernel_spin_multiplicities(constraints):
    multiplicities = {}
    for spin, projector in SPIN_PROJECTORS.items():
        isotypic_dimension = projector.rank()
        kernel_dimension = isotypic_dimension - (constraints * projector).rank()
        if kernel_dimension:
            if kernel_dimension % (2 * spin + 1):
                raise AssertionError("non-integral spin multiplicity")
            multiplicities[spin] = kernel_dimension // (2 * spin + 1)
    return multiplicities


def subtract_multiplicities(left, right):
    return {
        spin: left.get(spin, 0) - right.get(spin, 0)
        for spin in range(5)
        if left.get(spin, 0) != right.get(spin, 0)
    }


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    print(f"value rank: {VALUE.rank()}")
    for slot, matrix in DEPTH1_COMPONENTS.items():
        print(f"gap {slot} rank: {matrix.rank()}")
    print(f"depth <= 1 rank: {DEPTH1.rank()}")
    depth1_kernel_spins = kernel_spin_multiplicities(DEPTH1)
    print(f"depth <= 1 kernel spins: {depth1_kernel_spins}")
    for pair, matrix in DEPTH2_COMPONENTS.items():
        refined_constraints = vstack(DEPTH1, matrix)
        remaining_spins = kernel_spin_multiplicities(refined_constraints)
        print(
            f"pair {pair}: absolute rank {matrix.rank()}, "
            f"new rank over depth 1 {rank_on_kernel(matrix, DEPTH1)}, "
            f"detected spins {subtract_multiplicities(depth1_kernel_spins, remaining_spins)}, "
            f"remaining spins {remaining_spins}"
        )
    for pair_set_size in (2, 3):
        for pair_set in combinations(PAIRS, pair_set_size):
            matrix = vstack(*(DEPTH2_COMPONENTS[pair] for pair in pair_set))
            print(
                f"pairs {pair_set}: absolute rank {matrix.rank()}, "
                f"new rank over depth 1 {rank_on_kernel(matrix, DEPTH1)}"
            )
    print(f"depth <= 2 rank: {DEPTH2.rank()}")
    print(f"depth-two birth rank: {rank_on_kernel(vstack(*DEPTH2_COMPONENTS.values()), DEPTH1)}")

    h12 = DEPTH2_COMPONENTS[(1, 2)]
    h13 = DEPTH2_COMPONENTS[(1, 3)]
    h23 = DEPTH2_COMPONENTS[(2, 3)]
    f1 = DEPTH1_COMPONENTS[1]
    f2 = DEPTH1_COMPONENTS[2]
    f3 = DEPTH1_COMPONENTS[3]
    qf2 = vstack(VALUE, f2)

    print("row-space overlap identifications:")
    print(f"  F1 in H12: {vstack(h12, f1).rank() == h12.rank()}")
    print(f"  F1 in H13: {vstack(h13, f1).rank() == h13.rank()}")
    print(f"  intersection(H12,H13) = F1: {h12.rank() + h13.rank() - vstack(h12, h13).rank() == f1.rank()}")
    print(f"  (q,F2) in H12: {vstack(h12, qf2).rank() == h12.rank()}")
    print(f"  (q,F2) in H23: {vstack(h23, qf2).rank() == h23.rank()}")
    print(f"  intersection(H12,H23) = (q,F2): {h12.rank() + h23.rank() - vstack(h12, h23).rank() == qf2.rank()}")
    print(f"  F3 in H13: {vstack(h13, f3).rank() == h13.rank()}")
    print(f"  F3 in H23: {vstack(h23, f3).rank() == h23.rank()}")
    print(f"  intersection(H13,H23) = F3: {h13.rank() + h23.rank() - vstack(h13, h23).rank() == f3.rank()}")
    print(f"  q in all pair charts: {all(vstack(matrix, VALUE).rank() == matrix.rank() for matrix in (h12,h13,h23))}")

    print("explicit pair-chart gluing:")
    print(f"  H12 -> F1 factorization: {PI_12_TO_1 * h12 == f1}")
    print(f"  H12 -> F2 factorization: {PI_12_TO_2 * h12 == f2}")
    print(f"  H13 -> F1 factorization: {PI_13_TO_1 * h13 == f1}")
    print(f"  H13 -> F3 factorization: {PI_13_TO_3 * h13 == f3}")
    print(f"  H23 -> F2 factorization: {PI_23_TO_2 * h23 == f2}")
    print(f"  H23 -> F3 factorization: {PI_23_TO_3 * h23 == f3}")
    print(f"  three overlap equations have rank 36: {PAIR_CHART_CONSTRAINTS.rank() == 36}")
    print(f"  actual pair charts satisfy overlap equations: {PAIR_CHART_CONSTRAINTS * PAIR_CHARTS == Mat.zeros(36, 81)}")
    print(f"  actual pair-chart image equals intrinsic gluing space: {PAIR_CHARTS.rank() == 108 - PAIR_CHART_CONSTRAINTS.rank()}")

    a12_constraints = vstack(PI_12_TO_1, PI_12_TO_2)
    a13_constraints = vstack(PI_13_TO_1, PI_13_TO_3)
    a23_constraints = vstack(PI_23_TO_2, PI_23_TO_3)
    a_dimensions = tuple(36 - constraints.rank() for constraints in (a12_constraints, a13_constraints, a23_constraints))
    print(f"birth chart kernel dimensions: {a_dimensions}")

    check("each pair chart is onto the 36-dimensional bilinear response space", all(matrix.rank() == 36 for matrix in (h12, h13, h23)))
    check("H12 extraction recovers F1", PI_12_TO_1 * h12 == f1)
    check("H12 extraction recovers F2", PI_12_TO_2 * h12 == f2)
    check("H13 extraction recovers F1", PI_13_TO_1 * h13 == f1)
    check("H13 extraction recovers F3", PI_13_TO_3 * h13 == f3)
    check("H23 extraction recovers F2", PI_23_TO_2 * h23 == f2)
    check("H23 extraction recovers F3", PI_23_TO_3 * h23 == f3)
    check(
        "the H13 corner identity recovers one common quaternionic value",
        RIGHT_LINEAR_CONTRACTION * PI_13_TO_1
        == LEFT_LINEAR_CONTRACTION * PI_13_TO_3,
    )
    check("the three overlap equations have rank 36", PAIR_CHART_CONSTRAINTS.rank() == 36)
    check(
        "actual pair charts satisfy the overlap equations",
        PAIR_CHART_CONSTRAINTS * PAIR_CHARTS == Mat.zeros(36, 81),
    )
    check("the actual pair-chart map has rank 72", PAIR_CHARTS.rank() == 72)
    check(
        "actual pair charts equal the intrinsic gluing kernel",
        PAIR_CHARTS.rank() == 108 - PAIR_CHART_CONSTRAINTS.rank(),
    )
    check(
        "the pair-chart kernel is exactly one V4",
        kernel_spin_multiplicities(PAIR_CHARTS) == {4: 1},
    )
    check("the depth-two birth dimensions split as 12+16+12", a_dimensions == (12, 16, 12))
    check(
        "the three birth chart factors are jointly independent",
        rank_on_kernel(PAIR_CHARTS, DEPTH1) == sum(a_dimensions) == 40,
    )
    check(
        "H12 birth factor has spin V2+V3",
        subtract_multiplicities(
            depth1_kernel_spins,
            kernel_spin_multiplicities(vstack(DEPTH1, h12)),
        )
        == {2: 1, 3: 1},
    )
    check(
        "H13 birth factor has spin V0+V1+V2+V3",
        subtract_multiplicities(
            depth1_kernel_spins,
            kernel_spin_multiplicities(vstack(DEPTH1, h13)),
        )
        == {0: 1, 1: 1, 2: 1, 3: 1},
    )
    check(
        "H23 birth factor has spin V2+V3",
        subtract_multiplicities(
            depth1_kernel_spins,
            kernel_spin_multiplicities(vstack(DEPTH1, h23)),
        )
        == {2: 1, 3: 1},
    )

    print("certificate checks:")
    all_ok = True
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        all_ok = all_ok and passed
    print("ALL CHECKS PASSED" if all_ok else "SOME CHECK FAILED")


if __name__ == "__main__":
    report()
