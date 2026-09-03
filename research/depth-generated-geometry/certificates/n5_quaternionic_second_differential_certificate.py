#!/usr/bin/env python3
"""Exact certificate for the closed quaternionic n=5 second differential.

The 16-dimensional tetrahedral quotient in Note 13 was first obtained as a
left-nullspace basis.  This certificate replaces that basis by five explicit
SO(3)-natural quaternionic operators P,A,B,C,D on

    H tensor V tensor V  ~=  R_2.

Six fixed linear combinations Lambda_ij assemble to

    omega_5 : R_2^6 -> H tensor H.

Everything below is checked over fractions.Fraction.  In particular,
omega_5 partial_5=0, rank(omega_5)=16, and rank(partial_5)=200, so
ker(omega_5)=im(partial_5).  No external library is used.
"""

from fractions import Fraction
from itertools import combinations, product

from all_n_pairwise_terminal_descent_certificate import right_encoder
from n2_intrinsic_response_certificate import Mat, Q, V, qmul
from n5_response_tetrahedron_certificate import (
    build_pairwise_matching_operator,
    inverse,
)


EDGES = list(combinations((1, 2, 3, 4), 2))


def qword(tokens, values):
    result = Q[0]
    for token in tokens:
        result = qmul(result, values[token])
    return result


def outer(left, right):
    return tuple(x * y for x in left for y in right)


def direct_operator(left_tokens, right_tokens):
    """Map h,u,v to word(left) tensor word(right)."""

    matrix = Mat.zeros(16, 36)
    for column, (h_index, u_index, v_index) in enumerate(
        product(range(4), range(3), range(3))
    ):
        values = {
            "h": Q[h_index],
            "u": V[u_index],
            "v": V[v_index],
        }
        value = outer(
            qword(left_tokens, values),
            qword(right_tokens, values),
        )
        for row, entry in enumerate(value):
            matrix[row, column] = entry
    return matrix


def frobenius_operator(left_tokens, right_tokens):
    """Insert Xi=sum_a e_a tensor e_a into two quaternion words."""

    matrix = Mat.zeros(16, 36)
    for column, (h_index, u_index, v_index) in enumerate(
        product(range(4), range(3), range(3))
    ):
        base = {
            "h": Q[h_index],
            "u": V[u_index],
            "v": V[v_index],
        }
        for basis in Q:
            values = dict(base)
            values["e"] = basis
            values["f"] = basis
            value = outer(
                qword(left_tokens, values),
                qword(right_tokens, values),
            )
            for row, entry in enumerate(value):
                matrix[row, column] += entry
    return matrix


def scale(matrix, scalar):
    scalar = Fraction(scalar)
    return Mat([[scalar * value for value in row] for row in matrix.data])


def add(*matrices):
    return Mat(
        [
            [sum(matrix[row, column] for matrix in matrices)
             for column in range(matrices[0].ncols)]
            for row in range(matrices[0].nrows)
        ]
    )


def hstack(*matrices):
    return Mat(
        [
            [value for matrix in matrices for value in matrix.data[row]]
            for row in range(matrices[0].nrows)
        ]
    )


def kron(left, right):
    return Mat(
        [
            [
                left[left_row, left_column]
                * right[right_row, right_column]
                for left_column in range(left.ncols)
                for right_column in range(right.ncols)
            ]
            for left_row in range(left.nrows)
            for right_row in range(right.nrows)
        ]
    )


def primitive_operators():
    """Return the five closed quaternionic operators P,A,B,C,D."""

    return {
        "P": direct_operator(("h",), ("u", "v")),
        "A": frobenius_operator(("h", "e"), ("u", "v", "f")),
        "B": frobenius_operator(("h", "e"), ("u", "f", "v")),
        "C": frobenius_operator(("e",), ("u", "v", "h", "f")),
        "D": frobenius_operator(("e", "h", "f", "v"), ("u",)),
    }


def edge_operators():
    """The six Lambda_ij in lexicographic edge order."""

    operator = primitive_operators()
    p = operator["P"]
    a = operator["A"]
    b = operator["B"]
    c = operator["C"]
    d = operator["D"]
    return {
        (1, 2): add(p, scale(b, -Fraction(1, 2)),
                    scale(c, Fraction(1, 2)), scale(d, -1)),
        (1, 3): add(p, scale(a, -Fraction(1, 4)),
                    scale(b, -Fraction(1, 2)),
                    scale(c, Fraction(1, 2)), scale(d, -1)),
        (1, 4): add(scale(a, -Fraction(1, 4)),
                    scale(b, -Fraction(1, 2))),
        (2, 3): add(scale(a, -Fraction(1, 4)),
                    scale(c, -Fraction(1, 2))),
        (2, 4): add(p, scale(a, -Fraction(1, 4))),
        (3, 4): p,
    }


def vector_generators():
    return (
        Mat([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
        Mat([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
        Mat([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
    )


def quaternion_generator(vector_generator):
    result = Mat.zeros(4, 4)
    for row in range(3):
        for column in range(3):
            result[row + 1, column + 1] = vector_generator[row, column]
    return result


def equivariance_checks(operators):
    identity_h = Mat.eye(4)
    identity_v = Mat.eye(3)
    checks = []
    for vector_generator in vector_generators():
        h_generator = quaternion_generator(vector_generator)
        source_generator = add(
            kron(kron(h_generator, identity_v), identity_v),
            kron(kron(identity_h, vector_generator), identity_v),
            kron(kron(identity_h, identity_v), vector_generator),
        )
        target_generator = add(
            kron(h_generator, identity_h),
            kron(identity_h, h_generator),
        )
        for name, operator in operators.items():
            checks.append(
                (name, target_generator * operator == operator * source_generator)
            )
    return checks


def target_casimir_projectors():
    """Spin 0,1,2 projectors on H tensor H for diagonal SO(3)."""

    identity_h = Mat.eye(4)
    target_generators = []
    for vector_generator in vector_generators():
        h_generator = quaternion_generator(vector_generator)
        target_generators.append(
            add(kron(h_generator, identity_h), kron(identity_h, h_generator))
        )
    casimir = Mat.zeros(16, 16)
    for generator in target_generators:
        casimir = add(casimir, scale(generator * generator, -1))
    identity = Mat.eye(16)
    c_minus_two = add(casimir, scale(identity, -2))
    c_minus_six = add(casimir, scale(identity, -6))
    return (
        scale(c_minus_two * c_minus_six, Fraction(1, 12)),
        scale(casimir * c_minus_six, -Fraction(1, 8)),
        scale(casimir * c_minus_two, Fraction(1, 24)),
    )


def report():
    primitive = primitive_operators()
    edge = edge_operators()
    encoder_inverse = inverse(right_encoder(2))
    omega_tensor = hstack(*(edge[item] for item in EDGES))
    omega_response = hstack(
        *(edge[item] * encoder_inverse for item in EDGES)
    )
    matching, _, _ = build_pairwise_matching_operator(5)
    composition = omega_response * matching

    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    primitive_equivariance = equivariance_checks(primitive)
    check(
        "P,A,B,C,D are SO(3)-equivariant on all three generators",
        all(passed for _, passed in primitive_equivariance),
    )
    check(
        "omega_5 kills the first matching image exactly over Q",
        composition == Mat.zeros(16, matching.ncols),
    )
    check("omega_5 has rank 16", omega_response.rank() == 16)
    check("partial_5 has rank 200", matching.rank() == 200)
    check(
        "ker(omega_5)=im(partial_5) by inclusion and dimension",
        matching.nrows - omega_response.rank() == matching.rank() == 200,
    )

    block_ranks = [edge[item].rank() for item in EDGES]
    check(
        "edge ranks are 16,12,16,4,12,16",
        block_ranks == [16, 12, 16, 4, 12, 16],
    )
    check(
        "the outer normalization is Lambda_34(h,u,v)=h tensor uv",
        edge[(3, 4)] == primitive["P"],
    )
    projectors = target_casimir_projectors()
    image_spin_dimensions = {
        item: tuple((projector * edge[item]).rank() for projector in projectors)
        for item in EDGES
    }
    check(
        "full edge images have spin dimensions 2,9,5",
        all(
            image_spin_dimensions[item] == (2, 9, 5)
            for item in ((1, 2), (1, 4), (3, 4))
        ),
    )
    check(
        "rank-12 edge images have spin dimensions 1,6,5",
        all(
            image_spin_dimensions[item] == (1, 6, 5)
            for item in ((1, 3), (2, 4))
        ),
    )
    check(
        "the central edge image has spin dimensions 1,3,0 = H",
        image_spin_dimensions[(2, 3)] == (1, 3, 0),
    )
    check(
        "the two rank-12 edge images coincide",
        hstack(edge[(1, 3)], edge[(2, 4)]).rank() == 12,
    )
    check(
        "the central H is complementary to the common rank-12 image",
        hstack(edge[(1, 3)], edge[(2, 3)]).rank()
        == hstack(edge[(2, 4)], edge[(2, 3)]).rank()
        == 16,
    )

    print("omega_5 response shape:", omega_response.nrows, "x", omega_response.ncols)
    print("partial_5 shape:", matching.nrows, "x", matching.ncols)
    print("edge ranks:", dict(zip(EDGES, block_ranks)))
    print("edge image spin dimensions:", image_spin_dimensions)
    print("rank omega_5:", omega_response.rank())
    print("rank partial_5:", matching.rank())
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
