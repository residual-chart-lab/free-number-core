#!/usr/bin/env python3
"""Exact certificate for the outer-normalized n=6 seed-to-cap bridge.

For the central-spectator support Q=(1,2,4,5), work in right-decoder tensor
coordinates.  The local matching map has shape

    648 x 1296

and its quotient has dimension 48.  Normalize the quotient coordinate

    Omega_6 : R_3^6 -> (H tensor H) tensor V

by requiring its outer edge 34 to be the direct spectator extension of the
n=5 block Lambda_34=P.

Two independent modular constructions recover the same matrix 4 Omega_6
with small integer entries.  All defining identities are then verified over
the integers, so Omega_6 is an exact rational operator.

The closed contraction

    beta((x tensor y) tensor w) = x w conjugate(y)

satisfies

    beta Omega_6 = chi_6.

It kills iota(H) tensor V, while the long edge image is exactly ker(beta).
Thus the n=6 cap residual is born from W_12 tensor V, not from the direct
spectator extension of the seed channel K_4=iota(H).
"""

from itertools import combinations, product

import numpy as np

from all_n_pairwise_terminal_descent_certificate import right_encoder
from n2_intrinsic_response_certificate import Mat, Q, V, qmul
from n5_central_channel_factorization_certificate import iota_operator
from n5_quaternionic_second_differential_certificate import edge_operators
from n5_response_tetrahedron_certificate import inverse
from n6_capped_five_edge_operator_certificate import decoded_cap_map
from n6_response_4simplex_modular_certificate import (
    build_integer_response,
    rank_mod,
    right_inverse_data_mod,
)
from second_response_simplex_differential_certificate import (
    left_nullspace_mod,
)


PRIMES = (1009, 1013)
GAPS = (1, 2, 3, 4, 5)
SUPPORT = (1, 2, 4, 5)
EDGES = tuple(combinations(SUPPORT, 2))
FACE_DEPTH = 4
EDGE_DEPTH = 3
FACE_DIMENSION = 4 * 3**FACE_DEPTH
EDGE_DIMENSION = 4 * 3**EDGE_DEPTH
TARGET_DIMENSION = 16 * 3


def as_integer_array(matrix):
    result = np.empty((matrix.nrows, matrix.ncols), dtype=np.int64)
    for row in range(matrix.nrows):
        for column in range(matrix.ncols):
            value = matrix[row, column]
            if value.denominator != 1:
                raise AssertionError("expected an integral exact matrix")
            result[row, column] = value.numerator
    return result


def centered_scaled_lift(matrix, scale, prime):
    lifted = scale * matrix % prime
    lifted[lifted > prime // 2] -= prime
    return lifted.astype(np.int64)


def exact_face_right_inverse(face):
    """Recover a certified rational right inverse from two modular lifts."""

    lifts = []
    pivot_sets = []
    for prime in PRIMES:
        pivots, inverse_mod = right_inverse_data_mod(face % prime, prime)
        pivot_sets.append(pivots)
        lifts.append(centered_scaled_lift(inverse_mod, 16, prime))

    if not np.array_equal(pivot_sets[0], pivot_sets[1]):
        raise AssertionError("pivot columns changed between the two primes")
    if not np.array_equal(lifts[0], lifts[1]):
        raise AssertionError("right-inverse lifts changed between the primes")

    pivots = pivot_sets[0]
    inverse16 = lifts[0]
    if not set(int(value) for value in inverse16.reshape(-1)) <= {-1, 0, 1}:
        raise AssertionError("unexpected right-inverse coefficient")
    if not np.array_equal(
        face[:, pivots] @ inverse16,
        16 * np.eye(FACE_DIMENSION, dtype=np.int64),
    ):
        raise AssertionError("lifted face right inverse failed over Z")
    return pivots, inverse16


def local_matching_tensor(support=SUPPORT):
    """Return 128 times the matching map in edge tensor coordinates."""

    edges = tuple(combinations(support, 2))
    faces = {
        gap: build_integer_response(6, {gap})
        for gap in support
    }
    shadows = {
        edge: build_integer_response(6, set(edge))
        for edge in edges
    }
    right_inverse_data = {
        gap: exact_face_right_inverse(face)
        for gap, face in faces.items()
    }

    decoder = inverse(right_encoder(EDGE_DEPTH))
    decoder8 = np.empty((EDGE_DIMENSION, EDGE_DIMENSION), dtype=np.int64)
    for row in range(EDGE_DIMENSION):
        for column in range(EDGE_DIMENSION):
            value = 8 * decoder[row, column]
            if value.denominator != 1:
                raise AssertionError("unexpected J_3 inverse denominator")
            decoder8[row, column] = value.numerator
    encoder = as_integer_array(right_encoder(EDGE_DEPTH))
    if not np.array_equal(
        decoder8 @ encoder,
        8 * np.eye(EDGE_DIMENSION, dtype=np.int64),
    ):
        raise AssertionError("the lifted J_3 inverse failed over Z")

    face_index = {gap: index for index, gap in enumerate(support)}
    matching = np.zeros(
        (6 * EDGE_DIMENSION, 4 * FACE_DIMENSION),
        dtype=np.int64,
    )

    for edge_index, (first, second) in enumerate(edges):
        shadow = shadows[(first, second)]
        first_pivots, first_inverse16 = right_inverse_data[first]
        second_pivots, second_inverse16 = right_inverse_data[second]
        first_restriction16 = shadow[:, first_pivots] @ first_inverse16
        second_restriction16 = shadow[:, second_pivots] @ second_inverse16

        if not np.array_equal(
            first_restriction16 @ faces[first],
            16 * shadow,
        ):
            raise AssertionError("first exact shadow factorization failed")
        if not np.array_equal(
            second_restriction16 @ faces[second],
            16 * shadow,
        ):
            raise AssertionError("second exact shadow factorization failed")

        # J_3^{-1} contributes 1/8 and the response restriction 1/16.
        # Thus these integral blocks are 128 times the desired maps.
        first_restriction = decoder8 @ first_restriction16
        second_restriction = decoder8 @ second_restriction16

        row_slice = slice(
            edge_index * EDGE_DIMENSION,
            (edge_index + 1) * EDGE_DIMENSION,
        )
        first_slice = slice(
            face_index[first] * FACE_DIMENSION,
            (face_index[first] + 1) * FACE_DIMENSION,
        )
        second_slice = slice(
            face_index[second] * FACE_DIMENSION,
            (face_index[second] + 1) * FACE_DIMENSION,
        )
        matching[row_slice, first_slice] = first_restriction
        matching[row_slice, second_slice] = -second_restriction

    return matching


def outer_anchor(support=SUPPORT):
    """Direct spectator extension of local Lambda_34=P."""

    operator = edge_operators()[(3, 4)]
    operator = as_integer_array(operator)
    anchor = np.zeros(
        (TARGET_DIMENSION, EDGE_DIMENSION),
        dtype=np.int64,
    )

    outer_edge = support[2:]
    remaining = tuple(gap for gap in GAPS if gap not in outer_edge)
    active = support[:2]
    spectator_gap = next(gap for gap in GAPS if gap not in support)
    positions = {gap: index for index, gap in enumerate(remaining)}

    for column, (h_index, *vectors) in enumerate(
        product(range(4), range(3), range(3), range(3))
    ):
        first = vectors[positions[active[0]]]
        second = vectors[positions[active[1]]]
        spectator = vectors[positions[spectator_gap]]
        active_column = 9 * h_index + 3 * first + second
        for pair_component in range(16):
            anchor[
                3 * pair_component + spectator,
                column,
            ] = operator[pair_component, active_column]
    return anchor


def normalized_operator_mod(matching, anchor, prime):
    quotient = left_nullspace_mod(matching % prime, prime)
    if quotient.shape != (TARGET_DIMENSION, 6 * EDGE_DIMENSION):
        raise AssertionError("unexpected local quotient dimension")

    quotient_anchor = quotient[:, -EDGE_DIMENSION:]
    pivots, inverse_minor = right_inverse_data_mod(
        quotient_anchor,
        prime,
    )
    normalizer = (
        anchor[:, pivots] % prime @ inverse_minor
    ) % prime
    omega = normalizer @ quotient % prime

    if not np.array_equal(
        omega[:, -EDGE_DIMENSION:],
        anchor % prime,
    ):
        raise AssertionError("outer normalization failed")
    if np.count_nonzero(omega @ (matching % prime) % prime):
        raise AssertionError("normalized quotient does not kill matching")
    return omega


def centered_fourfold_lift(omega, prime):
    lifted = 4 * omega % prime
    lifted[lifted > prime // 2] -= prime
    allowed = {-8, -4, -3, -1, 0, 1, 3, 4, 9}
    if not set(int(value) for value in lifted.reshape(-1)) <= allowed:
        raise AssertionError("the normalized lift left the small alphabet")
    return lifted.astype(np.int64)


def conjugate(value):
    return (value[0], -value[1], -value[2], -value[3])


def beta_operator():
    """beta((x tensor y) tensor w)=x w conjugate(y)."""

    beta = np.zeros((4, TARGET_DIMENSION), dtype=np.int64)
    for x_index, y_index, w_index in product(range(4), range(4), range(3)):
        value = qmul(
            qmul(Q[x_index], V[w_index]),
            conjugate(Q[y_index]),
        )
        column = 12 * x_index + 3 * y_index + w_index
        beta[:, column] = value
    return beta


def cap_operator_tensor():
    """Six-edge form of chi_6 in right-decoder tensor coordinates."""

    left = as_integer_array(decoded_cap_map(left=True))
    right = as_integer_array(decoded_cap_map(left=False))
    zero = np.zeros_like(left)
    return np.concatenate(
        (-left, left, zero, zero, -right, right),
        axis=1,
    )


def channel_data_mod(omega4, prime):
    iota = as_integer_array(iota_operator()) % prime
    identity_v = np.eye(3, dtype=np.int64)
    nu = iota.T * pow(4, -1, prime) % prime
    projector_k = iota @ nu % prime
    projector_kv = np.kron(projector_k, identity_v) % prime
    projector_wv = (
        np.eye(TARGET_DIMENSION, dtype=np.int64) - projector_kv
    ) % prime
    coordinate_kv = np.kron(nu, identity_v) % prime

    full_ranks = []
    w_ranks = []
    k_ranks = []
    beta_ranks = []
    beta = beta_operator() % prime
    for index in range(6):
        block = omega4[
            :,
            index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION,
        ] % prime
        full_ranks.append(rank_mod(block, prime))
        w_ranks.append(rank_mod(projector_wv @ block % prime, prime))
        k_ranks.append(rank_mod(coordinate_kv @ block % prime, prime))
        beta_ranks.append(rank_mod(beta @ block % prime, prime))

    return (
        tuple(full_ranks),
        tuple(w_ranks),
        tuple(k_ranks),
        tuple(beta_ranks),
        np.kron(iota, identity_v) % prime,
    )


def exact_rank(matrix):
    return Mat(matrix.tolist()).rank()


def channel_profiles_exact(omega4):
    iota = as_integer_array(iota_operator())
    iota_v = np.kron(iota, np.eye(3, dtype=np.int64))
    projector_w_numerator = (
        4 * np.eye(TARGET_DIMENSION, dtype=np.int64)
        - iota_v @ iota_v.T
    )
    beta = beta_operator()

    profiles = [[], [], [], []]
    for index in range(6):
        block = omega4[
            :,
            index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION,
        ]
        profiles[0].append(exact_rank(block))
        profiles[1].append(exact_rank(projector_w_numerator @ block))
        profiles[2].append(exact_rank(iota_v.T @ block))
        profiles[3].append(exact_rank(beta @ block))
    return tuple(tuple(profile) for profile in profiles)


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    matching = local_matching_tensor()
    anchor = outer_anchor()
    lifted = []

    for prime in PRIMES:
        omega_mod = normalized_operator_mod(matching, anchor, prime)
        omega4 = centered_fourfold_lift(omega_mod, prime)
        lifted.append(omega4)
        check(
            f"local matching has rank 600 mod {prime}",
            rank_mod(matching, prime) == 600,
        )
        check(
            f"outer anchor has rank 48 mod {prime}",
            rank_mod(anchor, prime) == TARGET_DIMENSION,
        )

    omega4 = lifted[0]
    check(
        "both primes reconstruct the same integer matrix 4 Omega_6",
        np.array_equal(lifted[0], lifted[1]),
    )
    check(
        "4 Omega_6 kills the tensor-coordinate matching over Z",
        not np.count_nonzero(omega4 @ matching),
    )
    check(
        "the edge-34 block is exactly four times the outer anchor",
        np.array_equal(
            omega4[:, -EDGE_DIMENSION:],
            4 * anchor,
        ),
    )

    beta = beta_operator()
    chi = cap_operator_tensor()
    check(
        "beta Omega_6 equals chi_6 exactly over Q",
        np.array_equal(beta @ omega4, 4 * chi),
    )

    iota = as_integer_array(iota_operator())
    iota_v = np.kron(iota, np.eye(3, dtype=np.int64))
    check(
        "beta kills iota(H) tensor V over Z",
        not np.count_nonzero(beta @ iota_v),
    )
    check(
        "beta is onto H",
        all(rank_mod(beta, prime) == 4 for prime in PRIMES),
    )

    expected_profiles = (
        (48, 36, 44, 12, 36, 48),
        (36, 36, 32, 12, 36, 36),
        (12, 12, 12, 0, 12, 12),
        (4, 4, 0, 0, 4, 4),
    )
    check(
        "all four labelled channel profiles hold exactly over Q",
        channel_profiles_exact(omega4) == expected_profiles,
    )
    for prime in PRIMES:
        full, w_part, k_part, beta_part, iota_v_mod = channel_data_mod(
            omega4,
            prime,
        )
        check(
            f"the four labelled channel profiles hold mod {prime}",
            (full, w_part, k_part, beta_part) == expected_profiles,
        )
        long_edge = omega4[
            :,
            2 * EDGE_DIMENSION:3 * EDGE_DIMENSION,
        ] % prime
        check(
            f"the long edge contains K_4 tensor V mod {prime}",
            rank_mod(
                np.concatenate((long_edge, iota_v_mod), axis=1),
                prime,
            ) == 44,
        )

    long_edge = omega4[
        :,
        2 * EDGE_DIMENSION:3 * EDGE_DIMENSION,
    ]
    check(
        "the long edge lies in ker beta over Z",
        not np.count_nonzero(beta @ long_edge),
    )

    print("tensor matching shape:", matching.shape)
    print("normalized quotient shape:", omega4.shape)
    print("entries of 4 Omega_6:", sorted(set(omega4.reshape(-1))))
    print("full edge ranks:", expected_profiles[0])
    print("W tensor V projection ranks:", expected_profiles[1])
    print("K tensor V coordinate ranks:", expected_profiles[2])
    print("beta edge ranks:", expected_profiles[3])
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
