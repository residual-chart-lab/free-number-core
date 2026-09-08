#!/usr/bin/env python3
"""Exact factorization certificate for the central n=5 quaternion channel.

The rank-four edge operator Lambda_23 from Note 14 factors through the
canonical Frobenius embedding

    iota(q) = sum_alpha e_alpha tensor q e_alpha.

More precisely,

    A(h,u,v) = iota(u v conjugate(h)),
    C(h,u,v) = iota(u v h),
    Lambda_23(h,u,v)
        = iota(-1/4 u v (conjugate(h) + 2 h)).

The normalized adjoint nu=(1/4)iota^* is the canonical coordinate on this
channel.  It kills the common rank-twelve edge image and gives closed
coordinates for all six edge blocks.  Consequently

    H tensor H = ker(nu) orthogonal-direct-sum iota(H),

and P_K=(1/4)iota iota^* is the orthogonal projector onto the central
quaternionic channel.

All calculations use fractions.Fraction only.
"""

from fractions import Fraction
from itertools import product

from n2_intrinsic_response_certificate import Mat, Q, V, qmul
from n5_quaternionic_second_differential_certificate import (
    add,
    edge_operators,
    equivariance_checks,
    kron,
    outer,
    primitive_operators,
    quaternion_generator,
    scale,
    vector_generators,
)


def transpose(matrix):
    return Mat(
        [
            [matrix[row, column] for row in range(matrix.nrows)]
            for column in range(matrix.ncols)
        ]
    )


def conjugate(quaternion):
    return (
        quaternion[0],
        -quaternion[1],
        -quaternion[2],
        -quaternion[3],
    )


def iota_operator():
    """iota(q)=sum_alpha e_alpha tensor q e_alpha."""

    matrix = Mat.zeros(16, 4)
    for column, quaternion in enumerate(Q):
        value = [0] * 16
        for basis in Q:
            term = outer(basis, qmul(quaternion, basis))
            value = [left + right for left, right in zip(value, term)]
        for row, entry in enumerate(value):
            matrix[row, column] = entry
    return matrix


def product_parameter(conjugated=False):
    """(h,u,v) maps to u v h or u v conjugate(h)."""

    matrix = Mat.zeros(4, 36)
    for column, (coefficient, first, second) in enumerate(
        product(range(4), range(3), range(3))
    ):
        h = conjugate(Q[coefficient]) if conjugated else Q[coefficient]
        value = qmul(qmul(V[first], V[second]), h)
        for row, entry in enumerate(value):
            matrix[row, column] = entry
    return matrix


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    iota = iota_operator()
    adjoint = transpose(iota)
    normalized_adjoint = scale(adjoint, Fraction(1, 4))
    identity_h = Mat.eye(4)
    identity_target = Mat.eye(16)
    check("iota is injective", iota.rank() == 4)
    check(
        "iota star iota equals 4 id_H",
        adjoint * iota == scale(identity_h, 4),
    )
    projector = iota * normalized_adjoint
    check("the central projector is idempotent", projector * projector == projector)
    check("the central projector is self-adjoint", transpose(projector) == projector)

    target_identity = Mat.eye(4)
    iota_equivariant = True
    for vector_generator in vector_generators():
        h_generator = quaternion_generator(vector_generator)
        target_generator = add(
            kron(h_generator, target_identity),
            kron(target_identity, h_generator),
        )
        iota_equivariant &= (
            target_generator * iota == iota * h_generator
        )
    check("iota is SO(3)-equivariant", iota_equivariant)

    primitive = primitive_operators()
    edge = edge_operators()
    uv_h = product_parameter(conjugated=False)
    uv_h_bar = product_parameter(conjugated=True)
    sigma_parameter = add(
        scale(uv_h_bar, -Fraction(1, 4)),
        scale(uv_h, -Fraction(1, 2)),
    )
    zero_parameter = Mat.zeros(4, 36)
    expected_primitive_coordinates = {
        "P": scale(uv_h_bar, Fraction(1, 4)),
        "A": uv_h_bar,
        "B": zero_parameter,
        "C": uv_h,
        "D": scale(uv_h, Fraction(1, 2)),
    }
    expected_central_coordinates = {
        (1, 2): scale(uv_h_bar, Fraction(1, 4)),
        (1, 3): zero_parameter,
        (1, 4): scale(uv_h_bar, -Fraction(1, 4)),
        (2, 3): sigma_parameter,
        (2, 4): zero_parameter,
        (3, 4): scale(uv_h_bar, Fraction(1, 4)),
    }

    check("A equals iota of u v conjugate(h)",
          primitive["A"] == iota * uv_h_bar)
    check("C equals iota of u v h",
          primitive["C"] == iota * uv_h)
    check(
        "Lambda_23 has the closed iota factorization",
        edge[(2, 3)] == iota * sigma_parameter,
    )
    check("the quaternion parameter map is onto", sigma_parameter.rank() == 4)
    check(
        "A, C, and Lambda_23 have the same four-dimensional image",
        primitive["A"].rank()
        == primitive["C"].rank()
        == edge[(2, 3)].rank()
        == Mat(
            [
                primitive["A"].data[row]
                + primitive["C"].data[row]
                + edge[(2, 3)].data[row]
                for row in range(16)
            ]
        ).rank()
        == 4,
    )
    check(
        "one-quarter iota star recovers the central quaternion parameter",
        normalized_adjoint * edge[(2, 3)] == sigma_parameter,
    )
    check(
        "the five primitive central coordinates are closed",
        all(
            normalized_adjoint * primitive[name]
            == expected_primitive_coordinates[name]
            for name in expected_primitive_coordinates
        ),
    )
    check(
        "the normalized central coordinates of all six edges are closed",
        all(
            normalized_adjoint * edge[item]
            == expected_central_coordinates[item]
            for item in expected_central_coordinates
        ),
    )
    check(
        "the common rank-twelve edge image is orthogonal to iota(H)",
        adjoint * edge[(1, 3)] == zero_parameter
        and adjoint * edge[(2, 4)] == zero_parameter,
    )
    check(
        "the central projector fixes Lambda_23 and kills the rank-twelve edges",
        projector * edge[(2, 3)] == edge[(2, 3)]
        and projector * edge[(1, 3)] == Mat.zeros(16, 36)
        and projector * edge[(2, 4)] == Mat.zeros(16, 36),
    )
    check(
        "ker(nu) is the common rank-twelve edge image",
        normalized_adjoint.rank() == 4
        and edge[(1, 3)].rank() == edge[(2, 4)].rank() == 12
        and Mat(
            [
                edge[(1, 3)].data[row] + edge[(2, 4)].data[row]
                for row in range(16)
            ]
        ).rank() == 12,
    )
    check(
        "the complementary projector has rank twelve",
        add(identity_target, scale(projector, -1)).rank() == 12,
    )

    # The primitive maps used above are already checked globally in the
    # omega_5 certificate. Keep a local guard against import drift.
    check(
        "A and C remain SO(3)-equivariant",
        all(
            passed
            for name, passed in equivariance_checks(
                {"A": primitive["A"], "C": primitive["C"]}
            )
        ),
    )

    print("rank iota:", iota.rank())
    print("rank central parameter:", sigma_parameter.rank())
    print("rank Lambda_23:", edge[(2, 3)].rank())
    print(
        "central coordinate ranks:",
        {item: (normalized_adjoint * edge[item]).rank() for item in edge},
    )
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
