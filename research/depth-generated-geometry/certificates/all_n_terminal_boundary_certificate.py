#!/usr/bin/env python3
"""Exact finite checks for the all-n terminal-boundary theorem.

For each internal gap r, the exact-depth-(n-2) face leaves only that gap
unprobed.  The theorem factors this face through the adjacent reversed
quaternion product

    V tensor V -> H,  u tensor v -> v*u.

The surrounding response encoder is invertible.  Hence the common kernel of
all codimension-one faces is the intersection of the adjacent S^2_0 V pair
conditions, which is S^n_0 V.

This certificate checks the factorization at the level of exact row spaces and
the final kernel equality for n=2,3,4,5 over fractions.Fraction.
"""

from itertools import product

from n2_intrinsic_response_certificate import Mat, Q, V, qmul


def vstack(*matrices):
    if not matrices:
        return Mat([])
    ncols = matrices[0].ncols
    if any(matrix.ncols != ncols for matrix in matrices):
        raise ValueError("column counts differ")
    return Mat([row for matrix in matrices for row in matrix.data])


def qprod_reversed(letters):
    out = Q[0]
    for letter in reversed(letters):
        out = qmul(out, letter)
    return out


def words_of_length(n):
    return list(product(range(3), repeat=n))


def tuple_index(values, base=3):
    out = 0
    for value in values:
        out = base * out + value
    return out


def build_terminal_boundary_face(n, missing_gap):
    """All internal gaps are probed except missing_gap in {1,...,n-1}."""

    words = words_of_length(n)
    probed_gaps = [
        gap for gap in range(1, n) if gap != missing_gap
    ]
    face = Mat.zeros(4 * 3 ** (n - 2), len(words))

    for column, word in enumerate(words):
        base_letters = [V[index] for index in word]
        for probe_index, probe_word in enumerate(
            product(range(3), repeat=n - 2)
        ):
            letters = list(base_letters)
            for gap, probe in sorted(
                zip(probed_gaps, probe_word), reverse=True
            ):
                letters.insert(gap, V[probe])
            value = qprod_reversed(letters)
            for component in range(4):
                face[4 * probe_index + component, column] = value[component]
    return face


def build_terminal_response(n):
    """Probe every internal gap."""

    words = words_of_length(n)
    terminal = Mat.zeros(4 * 3 ** (n - 1), len(words))

    for column, word in enumerate(words):
        base_letters = [V[index] for index in word]
        for probe_index, probe_word in enumerate(
            product(range(3), repeat=n - 1)
        ):
            letters = list(base_letters)
            for gap, probe in sorted(
                zip(range(1, n), probe_word), reverse=True
            ):
                letters.insert(gap, V[probe])
            value = qprod_reversed(letters)
            for component in range(4):
                terminal[4 * probe_index + component, column] = value[
                    component
                ]
    return terminal


def build_contraction_map(n):
    """Contract the last n-1 tensor factors and leave the first V factor."""

    words = words_of_length(n)
    contraction = Mat.zeros(4 * 3 ** (n - 1), len(words))
    for column, word in enumerate(words):
        probe_index = tuple_index(word[1:])
        contraction[4 * probe_index + word[0] + 1, column] = 1
    return contraction


def build_adjacent_collapse(n, gap):
    """Replace tensor factors gap-1,gap by their reversed product."""

    words = words_of_length(n)
    post_length = n - gap - 1
    collapse = Mat.zeros(4 * 3 ** (n - 2), len(words))

    for column, word in enumerate(words):
        prefix = word[: gap - 1]
        suffix = word[gap + 1 :]
        prefix_index = tuple_index(prefix)
        suffix_index = tuple_index(suffix)
        value = qmul(V[word[gap]], V[word[gap - 1]])

        for component in range(4):
            row = (
                (prefix_index * 4 + component) * 3**post_length
                + suffix_index
            )
            collapse[row, column] = value[component]
    return collapse


def build_symmetric_trace_free_constraints(n):
    """Kernel is S^n_0 V: adjacent symmetry plus one pair trace."""

    words = words_of_length(n)
    index = {word: column for column, word in enumerate(words)}
    rows = []

    # Adjacent transpositions generate the full symmetric group.
    for position in range(n - 1):
        for word in words:
            swapped = list(word)
            swapped[position], swapped[position + 1] = (
                swapped[position + 1],
                swapped[position],
            )
            swapped = tuple(swapped)
            if word < swapped:
                row = [0] * len(words)
                row[index[word]] = 1
                row[index[swapped]] = -1
                rows.append(row)

    # Once symmetry is imposed, tracing the first pair is every pair trace.
    for tail in product(range(3), repeat=n - 2):
        row = [0] * len(words)
        for value in range(3):
            row[index[(value, value) + tail]] += 1
        rows.append(row)

    return Mat(rows)


def build_pair_product():
    product_map = Mat.zeros(4, 9)
    for first_index, first in enumerate(V):
        for second_index, second in enumerate(V):
            value = qmul(second, first)
            column = 3 * first_index + second_index
            for component in range(4):
                product_map[component, column] = value[component]
    return product_map


def subtract_scaled(left, right, scalar):
    if (left.nrows, left.ncols) != (right.nrows, right.ncols):
        raise ValueError("matrix shapes differ")
    return Mat(
        [
            [
                left[row, column] - scalar * right[row, column]
                for column in range(left.ncols)
            ]
            for row in range(left.nrows)
        ]
    )


def rank_on_kernel(operator, constraints):
    return vstack(constraints, operator).rank() - constraints.rank()


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    pair_product = build_pair_product()
    check(
        "the reversed pair product V tensor V -> H has rank 4",
        pair_product.rank() == 4,
    )
    check(
        "the reversed pair-product kernel has dimension 5",
        9 - pair_product.rank() == 5,
    )

    for n in range(2, 6):
        faces = []
        expected_face_rank = 4 * 3 ** (n - 2)

        for gap in range(1, n):
            face = build_terminal_boundary_face(n, gap)
            collapse = build_adjacent_collapse(n, gap)
            faces.append(face)

            check(
                f"n={n}, gap={gap}: terminal boundary face is onto",
                face.rank() == expected_face_rank,
            )
            check(
                f"n={n}, gap={gap}: face and adjacent collapse have the same kernel",
                collapse.rank() == expected_face_rank
                and vstack(face, collapse).rank() == expected_face_rank,
            )

        joint_faces = vstack(*faces)
        stf_constraints = build_symmetric_trace_free_constraints(n)
        expected_joint_rank = 3**n - (2 * n + 1)

        print(
            f"n={n}: joint face rank {joint_faces.rank()}, "
            f"kernel dimension {3**n - joint_faces.rank()}, "
            f"expected top-spin dimension {2*n+1}"
        )

        check(
            f"n={n}: common face kernel has dimension 2n+1",
            joint_faces.rank() == expected_joint_rank,
        )
        check(
            f"n={n}: STF constraint kernel has dimension 2n+1",
            stf_constraints.rank() == expected_joint_rank,
        )
        check(
            f"n={n}: common face kernel equals S^n_0 V",
            vstack(joint_faces, stf_constraints).rank()
            == expected_joint_rank,
        )

    # The first new rung beyond the previous n<=4 certificates.
    n = 5
    stf_constraints = build_symmetric_trace_free_constraints(n)
    terminal = build_terminal_response(n)
    contraction = build_contraction_map(n)
    coefficient = (-2) ** (n - 1)
    difference = subtract_scaled(terminal, contraction, coefficient)

    check(
        "n=5: C is injective on the 11-dimensional S^5_0 V",
        rank_on_kernel(contraction, stf_constraints) == 11,
    )
    check(
        "n=5: the terminal coefficient is A5=16C on S^5_0 V",
        vstack(stf_constraints, difference).rank()
        == stf_constraints.rank(),
    )

    print("certificate checks:")
    all_ok = True
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
        all_ok = all_ok and passed
    print("ALL CHECKS PASSED" if all_ok else "SOME CHECK FAILED")


if __name__ == "__main__":
    report()
