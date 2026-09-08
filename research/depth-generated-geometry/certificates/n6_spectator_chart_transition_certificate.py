#!/usr/bin/env python3
"""Exact certificate for the five-placement n=6 spectator atlas.

For each omitted gap s in {1,...,5}, let Q_s be the ordered four-gap
support.  Its local tetrahedral matching quotient has dimension 48.  The
three rank-16 seed edges 12, 14, and 34 provide possible direct coordinates
on

    T_6 = (H tensor H) tensor V.

The certificate determines exactly which direct seed normalizations extend
through the matching quotient.  The left chart (edge 12) and right chart
(edge 34) cover all five spectator placements.  On their overlaps the
transition is the identity at the exterior placement s=1, whereas at the
central placement s=3 it is

    G = id_H tensor theta,

where theta : H tensor V -> H tensor V has the closed formula

    theta(1 tensor w) = 1 tensor w + sum_a e_a tensor (e_a cross w),
    theta(a tensor w) = -w tensor a                    (a,w in V).

All local quotient maps are reconstructed as the same rational matrices
from two independent prime fields.  Their matching cancellation and all
transition identities are then checked over the integers.  Exact Fraction
ranks certify the direct-anchor incidence and the K_4/W_12 channel mixing.
"""

from itertools import combinations, product

import numpy as np

from n2_intrinsic_response_certificate import Mat, Q, V, qmul
from n5_central_channel_factorization_certificate import iota_operator
from n5_quaternionic_second_differential_certificate import (
    edge_operators,
    vector_generators,
)
from n6_response_4simplex_modular_certificate import (
    rank_mod,
    right_inverse_data_mod,
)
from n6_seed_cap_bridge_certificate import (
    EDGE_DIMENSION,
    GAPS,
    PRIMES,
    TARGET_DIMENSION,
    as_integer_array,
    beta_operator,
    local_matching_tensor,
)
from second_response_simplex_differential_certificate import (
    left_nullspace_mod,
)


LOCAL_EDGES = tuple(combinations((1, 2, 3, 4), 2))
FULL_SEED_EDGE_INDICES = (0, 2, 5)
EXPECTED_COVERAGE = {
    1: {(1, 2), (1, 4), (3, 4)},
    2: {(1, 2), (1, 4)},
    3: {(1, 2), (3, 4)},
    4: {(3, 4)},
    5: {(3, 4)},
}
EXPECTED_JOIN_RANKS = {
    # Exact ranks of [reference edge block ; direct seed anchor] for
    # local edges 12, 14, 34 respectively.
    1: (48, 48, 48),
    2: (48, 48, 80),
    3: (48, 80, 48),
    4: (56, 80, 48),
    5: (80, 80, 48),
}


def exact_rank(matrix):
    return Mat(matrix.tolist()).rank()


def fourfold_seed_anchor(support, edge_index):
    """Return four times the direct seed block on one local edge."""

    actual_edges = tuple(combinations(support, 2))
    actual_edge = actual_edges[edge_index]
    local_edge = LOCAL_EDGES[edge_index]
    operator = edge_operators()[local_edge]

    remaining = tuple(gap for gap in GAPS if gap not in actual_edge)
    active = tuple(gap for gap in support if gap not in actual_edge)
    spectator = next(gap for gap in GAPS if gap not in support)
    positions = {gap: index for index, gap in enumerate(remaining)}

    anchor4 = np.zeros((TARGET_DIMENSION, EDGE_DIMENSION), dtype=np.int64)
    for column, (h_index, *vectors) in enumerate(
        product(range(4), range(3), range(3), range(3))
    ):
        first = vectors[positions[active[0]]]
        second = vectors[positions[active[1]]]
        spectator_vector = vectors[positions[spectator]]
        source = 9 * h_index + 3 * first + second
        for pair_component in range(16):
            value = 4 * operator[pair_component, source]
            if value.denominator != 1:
                raise AssertionError("fourfold seed anchor is not integral")
            anchor4[3 * pair_component + spectator_vector, column] = value.numerator
    return anchor4


def normalized_chart4_mod(quotient, anchor4, edge_index, prime):
    """Return 4 Omega modulo prime, or None if this anchor is incompatible."""

    block = quotient[
        :,
        edge_index * EDGE_DIMENSION:(edge_index + 1) * EDGE_DIMENSION,
    ]
    if rank_mod(block, prime) != TARGET_DIMENSION:
        return None
    if rank_mod(np.concatenate((block, anchor4 % prime), axis=0), prime) != 48:
        return None

    pivots, inverse = right_inverse_data_mod(block, prime)
    normalizer4 = anchor4[:, pivots] % prime @ inverse % prime
    omega4 = normalizer4 @ quotient % prime
    if not np.array_equal(
        omega4[
            :,
            edge_index * EDGE_DIMENSION:(edge_index + 1) * EDGE_DIMENSION,
        ],
        anchor4 % prime,
    ):
        raise AssertionError("direct seed normalization failed")
    return omega4


def centered_lift(matrix, prime):
    lifted = matrix.copy()
    lifted[lifted > prime // 2] -= prime
    return lifted.astype(np.int64)


def reconstruct_charts():
    """Reconstruct every compatible 4 Omega over Z from two primes."""

    matchings = {}
    modular = {prime: {} for prime in PRIMES}
    for spectator in GAPS:
        support = tuple(gap for gap in GAPS if gap != spectator)
        matching = local_matching_tensor(support)
        matchings[spectator] = matching
        anchors = {
            index: fourfold_seed_anchor(support, index)
            for index in FULL_SEED_EDGE_INDICES
        }
        for prime in PRIMES:
            if rank_mod(matching, prime) != 600:
                raise AssertionError("local matching rank changed")
            quotient = left_nullspace_mod(matching % prime, prime)
            if quotient.shape != (48, 648):
                raise AssertionError("unexpected local quotient shape")
            charts = {}
            for edge_index, anchor4 in anchors.items():
                omega4 = normalized_chart4_mod(
                    quotient,
                    anchor4,
                    edge_index,
                    prime,
                )
                if omega4 is not None:
                    charts[LOCAL_EDGES[edge_index]] = omega4
            modular[prime][spectator] = charts

    exact = {}
    for spectator in GAPS:
        first = modular[PRIMES[0]][spectator]
        second = modular[PRIMES[1]][spectator]
        if set(first) != set(second):
            raise AssertionError("direct-anchor coverage changed between primes")
        exact[spectator] = {}
        for edge in first:
            lift_first = centered_lift(first[edge], PRIMES[0])
            lift_second = centered_lift(second[edge], PRIMES[1])
            if not np.array_equal(lift_first, lift_second):
                raise AssertionError("chart lift changed between primes")
            if np.max(np.abs(lift_first)) > 12:
                raise AssertionError("unexpectedly large chart coefficient")
            if np.count_nonzero(lift_first @ matchings[spectator]):
                raise AssertionError("lifted chart does not kill matching over Z")
            exact[spectator][edge] = lift_first
    return matchings, exact


def cross_basis(first, second):
    """Coordinates of e_first cross e_second in V."""

    value = qmul(V[first], V[second])
    return value[1:]


def theta_operator():
    """Closed central wall map on H tensor V."""

    theta = np.zeros((12, 12), dtype=np.int64)
    for w in range(3):
        # 1 tensor w -> 1 tensor w + delta(w).
        theta[w, w] = 1
        for basis in range(3):
            cross = cross_basis(basis, w)
            for component, coefficient in enumerate(cross):
                theta[3 * (basis + 1) + component, w] += coefficient

        # a tensor w -> -w tensor a for a in V.
        for a in range(3):
            source = 3 * (a + 1) + w
            target = 3 * (w + 1) + a
            theta[target, source] = -1
    return theta


def theta_decomposition():
    """Return the scalar V, alternating V, and symmetric V tensor V bases."""

    scalar = np.zeros((12, 3), dtype=np.int64)
    delta = np.zeros((12, 3), dtype=np.int64)
    for w in range(3):
        scalar[w, w] = 1
        for basis in range(3):
            cross = cross_basis(basis, w)
            for component, coefficient in enumerate(cross):
                delta[3 * (basis + 1) + component, w] += coefficient

    symmetric = np.zeros((12, 6), dtype=np.int64)
    for a in range(3):
        symmetric[3 * (a + 1) + a, a] = 1
    for column, (a, b) in enumerate(combinations(range(3), 2), start=3):
        symmetric[3 * (a + 1) + b, column] = 1
        symmetric[3 * (b + 1) + a, column] = 1
    return scalar, delta, symmetric


def target_generators():
    """Infinitesimal diagonal SO(3) action on H tensor H tensor V."""

    identity_h = np.eye(4, dtype=np.int64)
    identity_v = np.eye(3, dtype=np.int64)
    generators = []
    for vector_generator in vector_generators():
        vector = as_integer_array(vector_generator)
        quaternion = np.zeros((4, 4), dtype=np.int64)
        quaternion[1:, 1:] = vector
        generators.append(
            np.kron(np.kron(quaternion, identity_h), identity_v)
            + np.kron(np.kron(identity_h, quaternion), identity_v)
            + np.kron(np.kron(identity_h, identity_h), vector)
        )
    return tuple(generators)


def conjugate(value):
    return (value[0], -value[1], -value[2], -value[3])


def left_beta_operator():
    """beta_L(x,y,w)=x(2y+conjugate(y))w."""

    result = np.zeros((4, 48), dtype=np.int64)
    for x_index, y_index, w_index in product(range(4), range(4), range(3)):
        y = Q[y_index]
        y_weighted = tuple(2 * y[index] + conjugate(y)[index] for index in range(4))
        value = qmul(qmul(Q[x_index], y_weighted), V[w_index])
        result[:, 12 * x_index + 3 * y_index + w_index] = value
    return result


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    seed_ranks = tuple(edge_operators()[edge].rank() for edge in LOCAL_EDGES)
    check(
        "the seed edge ranks are 16,12,16,4,12,16",
        seed_ranks == (16, 12, 16, 4, 12, 16),
    )

    matchings, charts = reconstruct_charts()
    coverage = {
        spectator: set(local_charts)
        for spectator, local_charts in charts.items()
    }
    check("the exact direct-seed coverage table holds", coverage == EXPECTED_COVERAGE)

    # Choose one exact quotient coordinate for each support, then certify the
    # compatibility and incompatibility ranks over Q rather than only mod p.
    references = {
        spectator: local_charts[(1, 2)] if (1, 2) in local_charts
        else local_charts[(3, 4)]
        for spectator, local_charts in charts.items()
    }
    exact_join_ranks = {}
    for spectator in GAPS:
        support = tuple(gap for gap in GAPS if gap != spectator)
        reference = references[spectator]
        ranks = []
        for edge_index in FULL_SEED_EDGE_INDICES:
            block = reference[
                :,
                edge_index * EDGE_DIMENSION:(edge_index + 1) * EDGE_DIMENSION,
            ]
            anchor4 = fourfold_seed_anchor(support, edge_index)
            ranks.append(exact_rank(np.concatenate((block, anchor4), axis=0)))
        exact_join_ranks[spectator] = tuple(ranks)
    check(
        "all direct-anchor incidence ranks hold exactly over Q",
        exact_join_ranks == EXPECTED_JOIN_RANKS,
    )

    # The middle 14-chart is redundant wherever it exists.
    check(
        "the edge-14 chart equals the left chart at spectators 1 and 2",
        all(np.array_equal(charts[s][(1, 4)], charts[s][(1, 2)]) for s in (1, 2)),
    )

    theta = theta_operator()
    identity_theta = np.eye(12, dtype=np.int64)
    transition = np.kron(np.eye(4, dtype=np.int64), theta)
    identity_transition = np.eye(48, dtype=np.int64)
    check(
        "the exterior left/right transition is the identity",
        np.array_equal(charts[1][(1, 2)], charts[1][(3, 4)]),
    )
    check(
        "the central transition is id_H tensor theta over Z",
        np.array_equal(
            charts[3][(1, 2)],
            transition @ charts[3][(3, 4)],
        ),
    )

    scalar, delta, symmetric = theta_decomposition()
    check(
        "scalar, alternating, and symmetric channels span H tensor V",
        exact_rank(np.concatenate((scalar, delta, symmetric), axis=1)) == 12,
    )
    check("theta sends scalar V to scalar V plus delta V",
          np.array_equal(theta @ scalar, scalar + delta))
    check("theta fixes the alternating V channel",
          np.array_equal(theta @ delta, delta))
    check("theta negates Sym^2 V",
          np.array_equal(theta @ symmetric, -symmetric))

    theta_minus = theta - identity_theta
    theta_plus = theta + identity_theta
    check(
        "theta obeys (theta-I)^2(theta+I)=0 over Z",
        not np.count_nonzero(theta_minus @ theta_minus @ theta_plus),
    )
    check(
        "theta has exact ranks 9,6,6 for theta-I,(theta-I)^2,theta+I",
        (
            exact_rank(theta_minus),
            exact_rank(theta_minus @ theta_minus),
            exact_rank(theta_plus),
        ) == (9, 6, 6),
    )
    check(
        "the repeated +1 factor is necessary",
        np.count_nonzero(theta_minus @ theta_plus) > 0,
    )

    # Canonical reflection-plus-shear decomposition theta=R+N.
    theta_minus_square = theta_minus @ theta_minus
    shear_numerator = 2 * theta_minus + theta_minus_square
    check("the shear numerator is even",
          all(int(value) % 2 == 0 for value in shear_numerator.reshape(-1)))
    shear = shear_numerator // 2
    reflection = theta - shear
    check("the shear has rank three", exact_rank(shear) == 3)
    check("the shear squares to zero", not np.count_nonzero(shear @ shear))
    check("the reflection is involutive",
          np.array_equal(reflection @ reflection, identity_theta))
    check("the reflection fixes the shear on both sides",
          np.array_equal(reflection @ shear, shear)
          and np.array_equal(shear @ reflection, shear))

    check(
        "the central transition has exact ranks 36 and 24 after one and two differences",
        (
            exact_rank(transition - identity_transition),
            exact_rank((transition - identity_transition) @ (transition - identity_transition)),
        ) == (36, 24),
    )
    check(
        "the central transition is SO(3)-equivariant over Z",
        all(
            not np.count_nonzero(generator @ transition - transition @ generator)
            for generator in target_generators()
        ),
    )

    # The transition does not preserve the seed K_4/W_12 splitting.
    iota = as_integer_array(iota_operator())
    iota_v = np.kron(iota, np.eye(3, dtype=np.int64))
    projector_k4 = iota_v @ iota_v.T
    projector_w4 = 4 * identity_transition - projector_k4
    channel_ranks = (
        exact_rank(projector_k4 @ transition @ iota_v),
        exact_rank(projector_w4 @ transition @ iota_v),
        exact_rank(projector_k4 @ transition @ projector_w4),
        exact_rank(projector_w4 @ transition @ projector_w4),
    )
    check(
        "the K/W transition block ranks are 12,12,12,24",
        channel_ranks == (12, 12, 12, 24),
    )
    check(
        "G(K_4 tensor V) meets K_4 tensor V trivially",
        exact_rank(np.concatenate((transition @ iota_v, iota_v), axis=1)) == 24,
    )
    check(
        "G(W_12 tensor V) contains K_4 tensor V",
        exact_rank(np.concatenate((transition @ projector_w4, iota_v), axis=1)) == 36,
    )

    # The cap decoder is independent of which central chart is used.
    beta_right = beta_operator()
    transition_inverse = -transition @ transition + transition + identity_transition
    check("the polynomial inverse is exact",
          np.array_equal(transition @ transition_inverse, identity_transition))
    beta_left = left_beta_operator()
    check("beta_R G^{-1}=beta_L",
          np.array_equal(beta_right @ transition_inverse, beta_left))
    check(
        "left and right central charts give the same cap residual",
        np.array_equal(
            beta_left @ charts[3][(1, 2)],
            beta_right @ charts[3][(3, 4)],
        ),
    )

    print("spectator coverage:", {
        spectator: tuple(sorted(local_charts))
        for spectator, local_charts in charts.items()
    })
    print("exact direct-anchor join ranks (12,14,34):", exact_join_ranks)
    print("theta entry alphabet:", sorted(set(int(value) for value in theta.reshape(-1))))
    print("theta minimal polynomial: (t-1)^2(t+1)")
    print("central transition ranks rank(G-I), rank((G-I)^2):", (36, 24))
    print("central K/W block ranks:", channel_ranks)
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
