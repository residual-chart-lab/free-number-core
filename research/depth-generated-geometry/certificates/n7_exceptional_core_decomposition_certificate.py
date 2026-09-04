#!/usr/bin/env python3
"""Exact certificate for the full exceptional n=7 local quotient.

Let Q=(1,3,4,6), with spectators 2 and 5.  Its six decoded edge spaces
form (H tensor V^4)^6.  The certificate transports the n=6 right chart
with spectator 5 through the new left spectator 2 on the maximal cross
edge (1,6).  Local compatibility extends that 144-dimensional anchor
uniquely to an integral core operator C on all six edges.

The same C and the same integral lift 16*partial_(7,Q) are reconstructed
independently over F_1009 and F_1013.  A CRT coefficient bound promotes the
lift to the rational matching map.  Integer multiplication then proves

    C partial_(7,Q) = 0,
    kappa_212 partial_(7,Q) = 0.

The stacked operator (C,kappa_212) has rank 148, while the matching has
rank 1796.  Hence it gives the exact quotient

    Y_(7,Q) ~= ((H tensor H) tensor V tensor V) direct-sum H.

The 144-dimensional summand is canonical relative to the stated transported
right-chart anchor.  The H-valued kappa_212 quotient is intrinsic.
"""

from itertools import combinations, product

import numpy as np

from all_n_pairwise_terminal_descent_certificate import right_encoder
from n6_response_4simplex_modular_certificate import (
    build_integer_response,
    rank_mod,
    right_inverse_data_mod,
)
from n2_intrinsic_response_certificate import Mat
from n5_quaternionic_second_differential_certificate import vector_generators
from n6_spectator_chart_transition_certificate import reconstruct_charts
from n7_exceptional_square_operator_certificate import (
    CROSS_EDGES,
    KAPPA_SIGNS,
    paired_collapse_4,
)
from second_response_simplex_differential_certificate import left_nullspace_mod


PRIMES = (1009, 1013)
N = 7
GAPS = tuple(range(1, N))
SUPPORT = (1, 3, 4, 6)
EDGES = tuple(combinations(SUPPORT, 2))
ANCHOR_EDGE = (1, 6)
ANCHOR_EDGE_INDEX = EDGES.index(ANCHOR_EDGE)
FACE_DEPTH = 5
EDGE_DEPTH = 4
FACE_DIMENSION = 4 * 3**FACE_DEPTH
EDGE_DIMENSION = 4 * 3**EDGE_DEPTH
CORE_DIMENSION = 4 * 4 * 3 * 3
QUOTIENT_DIMENSION = CORE_DIMENSION + 4
MATCHING_RANK = 6 * EDGE_DIMENSION - QUOTIENT_DIMENSION


def integer_array(matrix):
    result = np.empty((matrix.nrows, matrix.ncols), dtype=np.int64)
    for row in range(matrix.nrows):
        for column in range(matrix.ncols):
            value = matrix[row, column]
            if value.denominator != 1:
                raise AssertionError("expected an integral exact matrix")
            result[row, column] = value.numerator
    return result


def tuple_index(values, bases):
    index = 0
    for value, base in zip(values, bases):
        index = base * index + value
    return index


def carried_long_cross_anchor(chart4):
    """Carry the n=6 spectator-5 right chart through spectator 2.

    Removing gap 2 identifies (1,3,4,5,6) with the five-gap n=6 atlas.
    Gap 5 is then spectator position 4 and Q becomes (1,2,3,5).  We use
    its right chart and carry the newly inserted gap 2 on actual edge
    (1,6).  The target spectator order is (2,5).
    """

    old_spectator = 5
    new_spectator = 2
    base_gaps = tuple(gap for gap in GAPS if gap != new_spectator)
    edge = ANCHOR_EDGE
    old_edge_dimension = 4 * 3**3
    old_block = chart4[
        :,
        ANCHOR_EDGE_INDEX * old_edge_dimension:
        (ANCHOR_EDGE_INDEX + 1) * old_edge_dimension,
    ]
    remaining = tuple(gap for gap in GAPS if gap not in edge)
    old_remaining = tuple(gap for gap in base_gaps if gap not in edge)
    positions = {gap: index for index, gap in enumerate(remaining)}
    anchor = np.zeros((CORE_DIMENSION, EDGE_DIMENSION), dtype=np.int64)

    for h_index, vectors in product(range(4), product(range(3), repeat=4)):
        source = tuple_index((h_index, *vectors), (4, 3, 3, 3, 3))
        old_vectors = tuple(vectors[positions[gap]] for gap in old_remaining)
        old_source = tuple_index((h_index, *old_vectors), (4, 3, 3, 3))
        new_vector = vectors[positions[new_spectator]]
        for old_row in np.flatnonzero(old_block[:, old_source]):
            pair_component, old_vector = divmod(int(old_row), 3)
            target = tuple_index(
                (
                    pair_component // 4,
                    pair_component % 4,
                    new_vector,
                    old_vector,
                ),
                (4, 4, 3, 3),
            )
            anchor[target, source] += int(old_block[old_row, old_source])
    return anchor


def build_local_matching_mod(faces, shadows, encoder, prime):
    """Build partial_(7,Q) in decoded H tensor V^4 edge coordinates."""

    face_right_data = {
        gap: right_inverse_data_mod(face, prime)
        for gap, face in faces.items()
    }
    encoder_mod = encoder % prime
    encoder_pivots, decoder = right_inverse_data_mod(encoder_mod, prime)
    if not np.array_equal(encoder_pivots, np.arange(EDGE_DIMENSION)):
        raise AssertionError("right encoder pivot order changed")
    if np.count_nonzero(
        (decoder @ encoder_mod - np.eye(EDGE_DIMENSION, dtype=np.int64)) % prime
    ):
        raise AssertionError("right decoder construction failed")

    face_index = {gap: index for index, gap in enumerate(SUPPORT)}
    matching = np.zeros(
        (len(EDGES) * EDGE_DIMENSION, len(SUPPORT) * FACE_DIMENSION),
        dtype=np.int64,
    )

    for edge_index, (first, second) in enumerate(EDGES):
        shadow = shadows[(first, second)] % prime
        oriented_blocks = []
        for gap in (first, second):
            pivots, inverse = face_right_data[gap]
            restriction = shadow[:, pivots] @ inverse % prime
            if np.count_nonzero(
                (restriction @ (faces[gap] % prime) - shadow) % prime
            ):
                raise AssertionError("face-to-shadow factorization failed")
            tensor_restriction = decoder @ restriction % prime
            if np.count_nonzero(
                (encoder_mod @ tensor_restriction - restriction) % prime
            ):
                raise AssertionError("decoded restriction failed")
            oriented_blocks.append(tensor_restriction)

        rows = slice(
            edge_index * EDGE_DIMENSION,
            (edge_index + 1) * EDGE_DIMENSION,
        )
        first_columns = slice(
            face_index[first] * FACE_DIMENSION,
            (face_index[first] + 1) * FACE_DIMENSION,
        )
        second_columns = slice(
            face_index[second] * FACE_DIMENSION,
            (face_index[second] + 1) * FACE_DIMENSION,
        )
        matching[rows, first_columns] = oriented_blocks[0]
        matching[rows, second_columns] = -oriented_blocks[1] % prime
    return matching


def solve_anchored_core(quotient, anchor, prime):
    """Return the unique quotient map with the prescribed full cross block."""

    columns = slice(
        ANCHOR_EDGE_INDEX * EDGE_DIMENSION,
        (ANCHOR_EDGE_INDEX + 1) * EDGE_DIMENSION,
    )
    block = quotient[:, columns] % prime
    block_pivots, block_inverse = right_inverse_data_mod(block, prime)
    normalizer = anchor[:, block_pivots] % prime @ block_inverse % prime
    core = normalizer @ quotient % prime
    if np.count_nonzero((core[:, columns] - anchor) % prime):
        raise AssertionError("transported anchor did not extend")
    return core


def centered_scaled_lift(matrix, scale, prime):
    lifted = scale * matrix % prime
    lifted[lifted > prime // 2] -= prime
    return lifted.astype(np.int64)


def tensor_kappa(encoder):
    epsilon_response = integer_array(paired_collapse_4())
    epsilon_tensor = epsilon_response @ encoder
    blocks = []
    for edge in EDGES:
        if edge in CROSS_EDGES:
            sign = KAPPA_SIGNS[CROSS_EDGES.index(edge)]
            blocks.append(sign * epsilon_tensor)
        else:
            blocks.append(np.zeros_like(epsilon_tensor))
    return np.concatenate(blocks, axis=1)


def exact_rank(matrix):
    return Mat(matrix.tolist()).rank()


def action_generators():
    """Diagonal SO(3) generators on source, core target, and H."""

    identity_h = np.eye(4, dtype=np.int64)
    identity_v = np.eye(3, dtype=np.int64)
    source = []
    core_target = []
    quaternion_target = []
    for vector_generator in vector_generators():
        vector = integer_array(vector_generator)
        quaternion = np.zeros((4, 4), dtype=np.int64)
        quaternion[1:, 1:] = vector
        source.append(
            np.kron(np.kron(np.kron(np.kron(quaternion, identity_v), identity_v), identity_v), identity_v)
            + np.kron(np.kron(np.kron(np.kron(identity_h, vector), identity_v), identity_v), identity_v)
            + np.kron(np.kron(np.kron(np.kron(identity_h, identity_v), vector), identity_v), identity_v)
            + np.kron(np.kron(np.kron(np.kron(identity_h, identity_v), identity_v), vector), identity_v)
            + np.kron(np.kron(np.kron(np.kron(identity_h, identity_v), identity_v), identity_v), vector)
        )
        core_target.append(
            np.kron(np.kron(np.kron(quaternion, identity_h), identity_v), identity_v)
            + np.kron(np.kron(np.kron(identity_h, quaternion), identity_v), identity_v)
            + np.kron(np.kron(np.kron(identity_h, identity_h), vector), identity_v)
            + np.kron(np.kron(np.kron(identity_h, identity_h), identity_v), vector)
        )
        quaternion_target.append(quaternion)
    return tuple(source), tuple(core_target), tuple(quaternion_target)


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    faces = {
        gap: build_integer_response(N, {gap})
        for gap in SUPPORT
    }
    shadows = {
        edge: build_integer_response(N, set(edge))
        for edge in EDGES
    }
    encoder = integer_array(right_encoder(EDGE_DEPTH))
    check("the right encoder is integral with entries 0,+/-1",
          set(int(x) for x in encoder.reshape(-1)) <= {-1, 0, 1})
    check("all face matrices have entries 0,+/-1", all(
        set(int(x) for x in face.reshape(-1)) <= {-1, 0, 1}
        for face in faces.values()
    ))

    print("reconstructing the n=6 transported anchor", flush=True)
    _, charts = reconstruct_charts()
    anchor = carried_long_cross_anchor(charts[4][(3, 4)])
    check("the transported long-cross anchor has rank 144",
          rank_mod(anchor, PRIMES[0]) == CORE_DIMENSION)

    matching_lifts = []
    core_lifts = []
    modular_results = {}
    for prime in PRIMES:
        print(f"building exceptional local matching mod {prime}", flush=True)
        matching = build_local_matching_mod(faces, shadows, encoder, prime)
        matching_rank = rank_mod(matching, prime)
        quotient = left_nullspace_mod(matching, prime)
        anchor_block = quotient[
            :,
            ANCHOR_EDGE_INDEX * EDGE_DIMENSION:
            (ANCHOR_EDGE_INDEX + 1) * EDGE_DIMENSION,
        ]
        anchor_block_rank = rank_mod(anchor_block, prime)
        core = solve_anchored_core(quotient, anchor, prime)
        core_rank = rank_mod(core, prime)
        matching_lifts.append(centered_scaled_lift(matching, 16, prime))
        core_lifts.append(centered_scaled_lift(core, 1, prime))
        modular_results[prime] = {
            "matching_rank": matching_rank,
            "quotient_dimension": quotient.shape[0],
            "anchor_block_rank": anchor_block_rank,
            "core_rank": core_rank,
            "core_annihilates": not np.count_nonzero(core @ matching % prime),
        }

    matching16 = matching_lifts[0]
    core = core_lifts[0]
    check("both primes reconstruct the same integral 16*matching",
          np.array_equal(matching_lifts[0], matching_lifts[1]))
    check("16*matching has alphabet 0,+/-1,+/-2",
          set(int(x) for x in matching16.reshape(-1)) <= {-2, -1, 0, 1, 2})
    check("both primes reconstruct the same integral core operator",
          np.array_equal(core_lifts[0], core_lifts[1]))
    check("the core entry alphabet is the expected nine values",
          set(int(x) for x in core.reshape(-1))
          == {-4, -3, -1, 0, 1, 3, 4, 8, 9})
    check("the core has the transported anchor over Z", np.array_equal(
        core[
            :,
            ANCHOR_EDGE_INDEX * EDGE_DIMENSION:
            (ANCHOR_EDGE_INDEX + 1) * EDGE_DIMENSION,
        ],
        anchor,
    ))

    # The two modular factorizations promote matching16 to the exact
    # rational matching.  Every entry of J_4 matching16 face - 16 shadow
    # has absolute value at most the bound below.  Since it vanishes modulo
    # both primes and the bound is smaller than their product, it is zero
    # over Z by the Chinese remainder theorem.
    crt_bound = EDGE_DIMENSION * FACE_DIMENSION * 2 + 16
    crt_modulus = PRIMES[0] * PRIMES[1]
    check("the factorization coefficient bound fits below the CRT modulus",
          crt_bound < crt_modulus)

    kappa = tensor_kappa(encoder)
    check("the integral core kills 16*matching over Z",
          not np.count_nonzero(core @ matching16))
    check("the integral square residual kills 16*matching over Z",
          not np.count_nonzero(kappa @ matching16))

    source_action, core_action, quaternion_action = action_generators()
    check("the integral core is SO(3)-equivariant over Z", all(
        not np.count_nonzero(target @ core[:, index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION]
                             - core[:, index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION] @ source)
        for source, target in zip(source_action, core_action)
        for index in range(len(EDGES))
    ))
    check("the integral square residual is SO(3)-equivariant over Z", all(
        not np.count_nonzero(target @ kappa[:, index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION]
                             - kappa[:, index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION] @ source)
        for source, target in zip(source_action, quaternion_action)
        for index in range(len(EDGES))
    ))

    stacked = np.concatenate((core, kappa), axis=0)
    core_edge_ranks = tuple(
        exact_rank(core[:, index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION])
        for index in range(len(EDGES))
    )
    exceptional_edge_ranks = tuple(
        exact_rank(stacked[:, index * EDGE_DIMENSION:(index + 1) * EDGE_DIMENSION])
        for index in range(len(EDGES))
    )
    check("the core has the generic six-edge rank profile",
          core_edge_ranks == (144, 108, 144, 36, 108, 144))
    check("kappa adds four dimensions on exactly the four cross edges",
          exceptional_edge_ranks == (144, 112, 148, 40, 112, 144))
    for prime, result in modular_results.items():
        check(f"the matching has rank 1796 mod {prime}",
              result["matching_rank"] == MATCHING_RANK)
        check(f"the local quotient has dimension 148 mod {prime}",
              result["quotient_dimension"] == QUOTIENT_DIMENSION)
        check(f"the anchor edge sees the full quotient dual mod {prime}",
              result["anchor_block_rank"] == QUOTIENT_DIMENSION)
        check(f"the anchored core has rank 144 mod {prime}",
              result["core_rank"] == CORE_DIMENSION)
        check(f"the anchored core kills matching mod {prime}",
              result["core_annihilates"])
        check(f"core plus kappa has rank 148 mod {prime}",
              rank_mod(stacked, prime) == QUOTIENT_DIMENSION)

    print("support:", SUPPORT, "spectators:", (2, 5))
    print("transport anchor edge:", ANCHOR_EDGE)
    print("16*matching alphabet:", sorted(set(int(x) for x in matching16.reshape(-1))))
    print("core alphabet:", sorted(set(int(x) for x in core.reshape(-1))))
    print("CRT bound/modulus:", crt_bound, crt_modulus)
    print("ranks: matching/core/kappa/stacked =",
          MATCHING_RANK, CORE_DIMENSION, 4, QUOTIENT_DIMENSION)
    print("core edge ranks:", core_edge_ranks)
    print("exceptional edge ranks:", exceptional_edge_ranks)
    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
