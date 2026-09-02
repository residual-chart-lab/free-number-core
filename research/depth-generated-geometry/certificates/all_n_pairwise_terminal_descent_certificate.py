#!/usr/bin/env python3
"""Exact finite checks for all-n pairwise terminal descent.

The proof in Note 12 has two fixed algebraic ingredients.

First, actual deletions in an iterated right response encoder are related by
an invertible upper-triangular change of target coordinates to the simple
slot contractions

    M_j(h tensor v_1 tensor ... tensor v_m)
      = (h v_j) tensor v_1 tensor ... hat(v_j) ... tensor v_m.

The local move is the quaternion identity

    h x (v u) + (h v) x u = -2 <x,v> h u.

Second, the common simple-contraction kernel is

    ker(M_1,...,M_m) = S^m_0 V + S^{m+1}_0 V.

This certificate checks the fixed local decoders and their quadratic inverse
identities, the exact row-space triangularization through m=4, and the
explicit Cartan section through m=4.
It uses only fractions.Fraction arithmetic from the Python standard library.
The finite checks are evidence for the symbolic all-m proof, not a replacement
for it.
"""

from fractions import Fraction
from itertools import product

from all_n_terminal_boundary_certificate import (
    Mat,
    build_symmetric_trace_free_constraints,
    vstack,
)
from n2_intrinsic_response_certificate import Q, V, levi_civita, qmul
from n5_response_tetrahedron_certificate import inverse


def tuple_index(values, base):
    out = 0
    for value in values:
        out = base * out + value
    return out


def qadd(left, right):
    return tuple(a + b for a, b in zip(left, right))


def qscale(scalar, value):
    return tuple(scalar * entry for entry in value)


def dot(left, right):
    return sum(a * b for a, b in zip(left[1:], right[1:]))


def right_encoder(depth):
    """J_m(h,v_1,...,v_m)(x_1,...,x_m)=h x_m v_m ... x_1 v_1."""

    coefficients = list(product(range(4), *([range(3)] * depth)))
    probes = list(product(range(3), repeat=depth))
    matrix = Mat.zeros(4 * len(probes), len(coefficients))

    for column, (h_index, *vectors) in enumerate(coefficients):
        for probe_index, probe_word in enumerate(probes):
            value = Q[h_index]
            for probe, vector in zip(
                reversed(probe_word), reversed(vectors)
            ):
                value = qmul(qmul(value, V[probe]), V[vector])
            for component, entry in enumerate(value):
                matrix[4 * probe_index + component, column] = entry

    return matrix


def simple_contraction(depth, slot):
    """The coefficient contraction M_slot, with slots numbered from zero."""

    source = list(product(range(4), *([range(3)] * depth)))
    target = list(product(range(4), *([range(3)] * (depth - 1))))
    target_index = {word: index for index, word in enumerate(target)}
    matrix = Mat.zeros(len(target), len(source))

    for column, (h_index, *vectors) in enumerate(source):
        value = qmul(Q[h_index], V[vectors[slot]])
        remaining = vectors[:slot] + vectors[slot + 1 :]
        for component, entry in enumerate(value):
            matrix[target_index[(component, *remaining)], column] = entry

    return matrix


def actual_deletion(depth, slot):
    """Evaluate J_m after deleting probe x_slot from its product string."""

    source = list(product(range(4), *([range(3)] * depth)))
    remaining_slots = [index for index in range(depth) if index != slot]
    probes = list(product(range(3), repeat=depth - 1))
    matrix = Mat.zeros(4 * len(probes), len(source))

    for column, (h_index, *vectors) in enumerate(source):
        for probe_index, probe_word in enumerate(probes):
            assigned = dict(zip(remaining_slots, probe_word))
            value = Q[h_index]
            for index in reversed(range(depth)):
                if index != slot:
                    value = qmul(value, V[assigned[index]])
                value = qmul(value, V[vectors[index]])
            for component, entry in enumerate(value):
                matrix[4 * probe_index + component, column] = entry

    return matrix


def simple_response(depth, slot):
    return right_encoder(depth - 1) * simple_contraction(depth, slot)


def metric_decoder():
    """Coordinates of Psi(c x v)=-2<x,v>c in the right encoder basis."""

    evaluated = Mat.zeros(12, 12)
    for h_index, coefficient in enumerate(Q):
        for vector_index, vector in enumerate(V):
            column = 3 * h_index + vector_index
            for probe_index, probe in enumerate(V):
                value = qscale(-2 * dot(probe, vector), coefficient)
                for component, entry in enumerate(value):
                    evaluated[4 * probe_index + component, column] = entry
    return inverse(right_encoder(1)) * evaluated


def antisymmetric_decoder():
    """M_1 on H tensor Lambda^2 V, in epsilon coordinates."""

    matrix = Mat.zeros(12, 12)
    for h_index, coefficient in enumerate(Q):
        for axis in range(3):
            column = 3 * h_index + axis
            for remaining in range(3):
                value = (0, 0, 0, 0)
                for contracted in range(3):
                    epsilon = levi_civita(contracted, remaining, axis)
                    if epsilon:
                        value = qadd(
                            value,
                            qscale(
                                epsilon,
                                qmul(coefficient, V[contracted]),
                            ),
                        )
                for component, entry in enumerate(value):
                    # Use the same H-major ordering on source and target:
                    # (quaternion component, V index).
                    matrix[3 * component + remaining, column] = entry
    return matrix


def subtract_polynomial(linear, square, linear_coefficient, scalar):
    """Return square + a*linear + b*I for a square exact matrix."""

    result = Mat([row[:] for row in square.data])
    for row in range(result.nrows):
        for column in range(result.ncols):
            result[row, column] += linear_coefficient * linear[row, column]
            if row == column:
                result[row, column] += scalar
    return result


def joint_simple_contractions(depth):
    return vstack(
        *(simple_contraction(depth, slot) for slot in range(depth))
    )


def lift_coefficient_constraints(constraints, word_count):
    """Apply V-tensor constraints independently to four H coefficients."""

    lifted = Mat.zeros(4 * constraints.nrows, 4 * word_count)
    for component in range(4):
        for row in range(constraints.nrows):
            for column in range(word_count):
                lifted[
                    component * constraints.nrows + row,
                    component * word_count + column,
                ] = constraints[row, column]
    return lifted


def scalar_projection(depth):
    word_count = 3**depth
    projection = Mat.zeros(word_count, 4 * word_count)
    for word in range(word_count):
        projection[word, word] = 1
    return projection


def cartan_section(depth):
    """The explicit section A -> 1 tensor A + vector part B(A)."""

    words = list(product(range(3), repeat=depth))
    index = {word: position for position, word in enumerate(words)}
    word_count = len(words)
    section = Mat.zeros(4 * word_count, word_count)

    for word, column in index.items():
        section[column, column] = 1

    coefficient = Fraction(-1, depth + 1)
    for output_word, output_index in index.items():
        for vector_component in range(3):
            row = (vector_component + 1) * word_count + output_index
            for slot, input_value in enumerate(output_word):
                for replacement in range(3):
                    epsilon = levi_civita(
                        vector_component, input_value, replacement
                    )
                    if epsilon == 0:
                        continue
                    source_word = list(output_word)
                    source_word[slot] = replacement
                    section[row, index[tuple(source_word)]] += (
                        coefficient * epsilon
                    )

    return section


def vector_stf_embedding(depth):
    """Embed a degree-(m+1) tensor as the vector coefficient of H tensor V^m."""

    source_words = list(product(range(3), repeat=depth + 1))
    target_words = list(product(range(3), repeat=depth))
    target_index = {word: position for position, word in enumerate(target_words)}
    embedding = Mat.zeros(4 * len(target_words), len(source_words))

    for column, word in enumerate(source_words):
        vector_component, *inputs = word
        row = (vector_component + 1) * len(target_words) + target_index[
            tuple(inputs)
        ]
        embedding[row, column] = 1

    return embedding


def vanishes_on_constraint_kernel(operator, constraints):
    return vstack(constraints, operator).rank() == constraints.rank()


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    # The fixed slide identity that drives every triangularization step.
    local_identity = True
    for h, u, v, x in product(Q, V, V, V):
        left = qadd(
            qmul(qmul(h, x), qmul(v, u)),
            qmul(qmul(qmul(h, v), x), u),
        )
        right = qscale(-2 * dot(x, v), qmul(h, u))
        local_identity = local_identity and left == right

    psi = metric_decoder()
    antisymmetric = antisymmetric_decoder()
    psi_polynomial = subtract_polynomial(psi, psi * psi, 1, -2)
    antisymmetric_polynomial = subtract_polynomial(
        antisymmetric,
        antisymmetric * antisymmetric,
        -1,
        -2,
    )
    check("the quaternion slide identity holds on the full basis", local_identity)
    check("the metric decoder Psi is invertible with determinant 16", psi.det() == 16)
    check(
        "Psi satisfies Psi^2+Psi-2I=0, so Psi inverse is (Psi+I)/2",
        psi_polynomial == Mat.zeros(12, 12),
    )
    check(
        "the antisymmetric decoder is invertible with determinant 16",
        antisymmetric.det() == 16,
    )
    check(
        "kappa satisfies kappa^2-kappa-2I=0, so kappa inverse is (kappa-I)/2",
        antisymmetric_polynomial == Mat.zeros(12, 12),
    )

    for depth in range(1, 5):
        simple_blocks = [
            simple_response(depth, slot) for slot in range(depth)
        ]
        actual_blocks = [
            actual_deletion(depth, slot) for slot in range(depth)
        ]

        # The proof gives equality for every suffix.  Checking each suffix is
        # stronger finite evidence than comparing only the full common kernel.
        for first_slot in range(depth):
            actual_suffix = vstack(*actual_blocks[first_slot:])
            simple_suffix = vstack(*simple_blocks[first_slot:])
            common_rank = simple_suffix.rank()
            check(
                f"m={depth}, suffix={first_slot + 1}: actual and simple row spaces agree",
                actual_suffix.rank() == common_rank
                and vstack(actual_suffix, simple_suffix).rank() == common_rank,
            )

        contractions = joint_simple_contractions(depth)
        expected_kernel = 4 * (depth + 1)
        check(
            f"m={depth}: the common simple-contraction kernel has dimension 4(m+1)",
            contractions.ncols - contractions.rank() == expected_kernel,
        )

        # Every coefficient tensor in the kernel is symmetric trace-free in
        # its m input slots.  For m=1 this is automatic.
        if depth >= 2:
            stf = build_symmetric_trace_free_constraints(depth)
            lifted_stf = lift_coefficient_constraints(stf, 3**depth)
            check(
                f"m={depth}: the contraction equations force input STF symmetry",
                vstack(contractions, lifted_stf).rank()
                == contractions.rank(),
            )

        section = cartan_section(depth)
        scalar = scalar_projection(depth)
        check(
            f"m={depth}: the Cartan section has scalar part equal to its input",
            scalar * section == Mat.eye(3**depth),
        )

        if depth == 1:
            section_is_closed = (contractions * section).rank() == 0
        else:
            stf = build_symmetric_trace_free_constraints(depth)
            section_is_closed = vanishes_on_constraint_kernel(
                contractions * section, stf
            )
        check(
            f"m={depth}: the explicit Cartan section lands in the common kernel on S^m_0 V",
            section_is_closed,
        )

        next_stf = build_symmetric_trace_free_constraints(depth + 1)
        vector_embedding = vector_stf_embedding(depth)
        check(
            f"m={depth}: S^(m+1)_0 V embeds in the zero-scalar kernel",
            vanishes_on_constraint_kernel(
                contractions * vector_embedding, next_stf
            ),
        )

    print("certificate checks:")
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")

    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED: {', '.join(failed)}")

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
