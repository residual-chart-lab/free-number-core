#!/usr/bin/env python3
"""Exact certificate for the five generic reduced n=7 internal words.

After exterior spectators are stripped by Note 22, the two-spectator
n=7 problem has six spacing words. Note 21 handles the exceptional word
212. This certificate handles the remaining words

    113, 122, 131, 221, 311.

For each word, one n=6 chart block is transported through a spectator which
is exterior relative to that edge response. The 144-dimensional anchor has
a unique completion through the n=7 local matching relations.

Both the local matching and the completed quotient map are reconstructed
independently over F_1009 and F_1013. The two centered lifts agree. Exact
integer cancellation, SO(3)-equivariance, edge ranks, and Casimir profiles
then upgrade the complete generic reduced atlas to characteristic zero.

NumPy is used only for exact integer and finite-field operations.
"""

from itertools import combinations, product
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

from all_n_pairwise_terminal_descent_certificate import right_encoder
from n2_intrinsic_response_certificate import Mat, Q, V, qmul
from n6_response_4simplex_modular_certificate import (
    build_integer_response,
    rank_mod,
    right_inverse_data_mod,
)
from n6_spectator_chart_transition_certificate import reconstruct_charts
from n7_exceptional_core_decomposition_certificate import action_generators
from second_response_simplex_differential_certificate import left_nullspace_mod


PRIMES = (1009, 1013)
N = 7
GAPS = tuple(range(1, N))
FACE_DIMENSION = 4 * 3**5
EDGE_DIMENSION = 4 * 3**4
OLD_EDGE_DIMENSION = 4 * 3**3
CORE_DIMENSION = 4 * 4 * 3 * 3
MATCHING_RANK = 6 * EDGE_DIMENSION - CORE_DIMENSION

SUPPORTS = {
    (1, 1, 3): (1, 2, 3, 6),
    (1, 2, 2): (1, 2, 4, 6),
    (1, 3, 1): (1, 2, 5, 6),
    (2, 2, 1): (1, 3, 5, 6),
    (3, 1, 1): (1, 4, 5, 6),
}

# Each specification is
#   (new spectator, n=6 chart key, local edge index, exterior side).
# The old spectator and its compressed n=6 position are forced by support.
ANCHOR_SPECS = {
    (1, 1, 3): (5, (3, 4), 2, "right"),
    (1, 2, 2): (3, (3, 4), 0, "left"),
    (1, 3, 1): (3, (1, 2), 0, "left"),
    (2, 2, 1): (2, (1, 2), 0, "left"),
    (3, 1, 1): (2, (1, 2), 0, "left"),
}

FULL_PROFILE = (6, 39, 55, 35, 9)
STANDARD_EDGE_PROFILES = (
    FULL_PROFILE,
    (4, 27, 40, 28, 9),
    FULL_PROFILE,
    (2, 12, 15, 7, 0),
    (4, 27, 40, 28, 9),
    FULL_PROFILE,
)
CENTRAL_EDGE_PROFILES = (
    FULL_PROFILE,
    (4, 27, 40, 28, 9),
    (5, 33, 50, 35, 9),
    (2, 12, 15, 7, 0),
    (4, 27, 40, 28, 9),
    FULL_PROFILE,
)


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


def centered_scaled_lift(matrix, scale, prime):
    lifted = scale * matrix % prime
    lifted[lifted > prime // 2] -= prime
    return lifted.astype(np.int64)


def exact_rank(matrix):
    return Mat(matrix.tolist()).rank()


def sigma_plus_encoder():
    """V_new tensor R_3 -> R_4, (w,F) -> w z F, in right coordinates."""

    old_encoder = integer_array(right_encoder(3))
    old_probe_words = tuple(product(range(3), repeat=3))
    old_probe_index = {
        word: index for index, word in enumerate(old_probe_words)
    }
    result = np.zeros(
        (EDGE_DIMENSION, 3 * OLD_EDGE_DIMENSION),
        dtype=np.int64,
    )

    for new_vector, old_column in product(
        range(3), range(OLD_EDGE_DIMENSION)
    ):
        column = new_vector * OLD_EDGE_DIMENSION + old_column
        for probe_index, probe_word in enumerate(
            product(range(3), repeat=4)
        ):
            old_index = old_probe_index[probe_word[:3]]
            old_value = tuple(
                int(old_encoder[4 * old_index + component, old_column])
                for component in range(4)
            )
            value = qmul(
                qmul(V[new_vector], V[probe_word[3]]),
                old_value,
            )
            for component, entry in enumerate(value):
                result[4 * probe_index + component, column] = entry
    return result


def prepare_restrictions(prime):
    """Build every decoded face-to-edge restriction needed at n=7."""

    faces = {
        gap: build_integer_response(N, {gap})
        for gap in GAPS
    }
    shadows = {
        edge: build_integer_response(N, set(edge))
        for edge in combinations(GAPS, 2)
    }
    face_data = {
        gap: right_inverse_data_mod(face, prime)
        for gap, face in faces.items()
    }

    encoder = integer_array(right_encoder(4)) % prime
    encoder_pivots, decoder = right_inverse_data_mod(encoder, prime)
    if not np.array_equal(encoder_pivots, np.arange(EDGE_DIMENSION)):
        raise AssertionError("right encoder pivot order changed")

    restrictions = {}
    for edge, shadow_integer in shadows.items():
        shadow = shadow_integer % prime
        for endpoint in edge:
            pivots, inverse = face_data[endpoint]
            response_restriction = (
                shadow[:, pivots] @ inverse
            ) % prime
            if np.count_nonzero(
                (
                    response_restriction @ (faces[endpoint] % prime)
                    - shadow
                ) % prime
            ):
                raise AssertionError("face-to-shadow factorization failed")
            tensor_restriction = decoder @ response_restriction % prime
            restrictions[(edge, endpoint)] = tensor_restriction
    return restrictions, encoder


def local_matching(support, restrictions, prime):
    edges = tuple(combinations(support, 2))
    face_index = {gap: index for index, gap in enumerate(support)}
    matching = np.zeros(
        (6 * EDGE_DIMENSION, 4 * FACE_DIMENSION),
        dtype=np.int64,
    )

    for edge_index, edge in enumerate(edges):
        first, second = edge
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
        matching[rows, first_columns] = restrictions[(edge, first)]
        matching[rows, second_columns] = (
            -restrictions[(edge, second)]
        ) % prime
    return matching


def parent_data(support, new_spectator):
    spectators = tuple(gap for gap in GAPS if gap not in support)
    old_spectator = next(
        gap for gap in spectators if gap != new_spectator
    )
    base_gaps = tuple(
        gap for gap in GAPS if gap != new_spectator
    )
    parent_position = base_gaps.index(old_spectator) + 1
    return old_spectator, parent_position


def carry_leftmost(
    old_block,
    edge,
    old_spectator,
    new_spectator,
):
    """Carry the lowest remaining gap by the right suspension."""

    base_gaps = tuple(
        gap for gap in GAPS if gap != new_spectator
    )
    remaining = tuple(gap for gap in GAPS if gap not in edge)
    old_remaining = tuple(
        gap for gap in base_gaps if gap not in edge
    )
    if new_spectator != remaining[0]:
        raise AssertionError("new spectator is not leftmost on this edge")
    positions = {gap: index for index, gap in enumerate(remaining)}
    anchor = np.zeros(
        (CORE_DIMENSION, EDGE_DIMENSION),
        dtype=np.int64,
    )

    for h_index, vectors in product(
        range(4), product(range(3), repeat=4)
    ):
        source = tuple_index(
            (h_index, *vectors),
            (4, 3, 3, 3, 3),
        )
        old_vectors = tuple(
            vectors[positions[gap]]
            for gap in old_remaining
        )
        old_source = tuple_index(
            (h_index, *old_vectors),
            (4, 3, 3, 3),
        )
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
            anchor[target, source] += int(
                old_block[old_row, old_source]
            )
    return anchor


def carry_rightmost(old_block, desuspension, prime):
    """Carry the highest remaining gap by the left suspension."""

    carried = (
        np.kron(np.eye(3, dtype=np.int64), old_block % prime)
        @ desuspension
    ) % prime
    anchor = np.zeros_like(carried)
    for new_vector, old_row in product(range(3), range(48)):
        pair_component, old_vector = divmod(old_row, 3)
        carried_row = new_vector * 48 + old_row
        target_row = (
            pair_component * 9
            + old_vector * 3
            + new_vector
        )
        anchor[target_row] = carried[carried_row]
    return anchor


def transported_anchor(
    word,
    support,
    charts,
    desuspension,
    prime,
):
    new_spectator, chart_key, edge_index, side = ANCHOR_SPECS[word]
    old_spectator, parent_position = parent_data(
        support, new_spectator
    )
    chart = charts[parent_position][chart_key]
    old_block = chart[
        :,
        edge_index * OLD_EDGE_DIMENSION:
        (edge_index + 1) * OLD_EDGE_DIMENSION,
    ]
    edge = tuple(combinations(support, 2))[edge_index]

    if side == "left":
        anchor = carry_leftmost(
            old_block,
            edge,
            old_spectator,
            new_spectator,
        ) % prime
    else:
        remaining = tuple(gap for gap in GAPS if gap not in edge)
        if new_spectator != remaining[-1]:
            raise AssertionError(
                "new spectator is not rightmost on this edge"
            )
        anchor = carry_rightmost(
            old_block,
            desuspension,
            prime,
        )

    description = {
        "new": new_spectator,
        "old": old_spectator,
        "parent_position": parent_position,
        "chart": chart_key,
        "edge": edge,
        "side": side,
    }
    return anchor, edge_index, description


def complete_anchor(quotient, anchor, edge_index, prime):
    columns = slice(
        edge_index * EDGE_DIMENSION,
        (edge_index + 1) * EDGE_DIMENSION,
    )
    block = quotient[:, columns] % prime
    if rank_mod(block, prime) != CORE_DIMENSION:
        raise AssertionError("anchor edge does not see the full quotient")
    if rank_mod(
        np.concatenate((block, anchor % prime), axis=0),
        prime,
    ) != CORE_DIMENSION:
        raise AssertionError("transported anchor is incompatible")

    pivots, inverse = right_inverse_data_mod(block, prime)
    normalizer = anchor[:, pivots] % prime @ inverse % prime
    core = normalizer @ quotient % prime
    if np.count_nonzero(
        (core[:, columns] - anchor) % prime
    ):
        raise AssertionError("anchored completion failed")
    return core


def casimir_numerators():
    """Numerators of the five spectral projectors on the core target."""

    _, generators, _ = action_generators()
    casimir = -sum(
        generator @ generator for generator in generators
    )
    identity = np.eye(CORE_DIMENSION, dtype=np.int64)
    numerators = []
    for spin in range(5):
        projector = identity.copy()
        for other in range(5):
            if other == spin:
                continue
            projector = projector @ (
                casimir - other * (other + 1) * identity
            )
        numerators.append(projector)
    return tuple(numerators), generators


def exact_edge_profiles(core, projector_numerators):
    ranks = []
    profiles = []
    for edge_index in range(6):
        block = core[
            :,
            edge_index * EDGE_DIMENSION:
            (edge_index + 1) * EDGE_DIMENSION,
        ]
        ranks.append(exact_rank(block))
        profiles.append(tuple(
            exact_rank(projector @ block)
            for projector in projector_numerators
        ))
    return tuple(ranks), tuple(profiles)


def process_prime(prime, charts, temporary_directory):
    print(f"building all n=7 restrictions mod {prime}", flush=True)
    restrictions, encoder = prepare_restrictions(prime)
    plus_encoder = sigma_plus_encoder() % prime
    plus_pivots, plus_inverse = right_inverse_data_mod(
        plus_encoder, prime
    )
    if not np.array_equal(
        plus_pivots, np.arange(EDGE_DIMENSION)
    ):
        raise AssertionError("left suspension pivot order changed")
    desuspension = plus_inverse @ encoder % prime

    results = {}
    for word, support in SUPPORTS.items():
        print(f"  completing word {word} mod {prime}", flush=True)
        matching = local_matching(support, restrictions, prime)
        matching_rank = rank_mod(matching, prime)
        quotient = left_nullspace_mod(matching, prime)
        anchor, edge_index, description = transported_anchor(
            word,
            support,
            charts,
            desuspension,
            prime,
        )
        core = complete_anchor(
            quotient,
            anchor,
            edge_index,
            prime,
        )

        matching16 = centered_scaled_lift(matching, 16, prime)
        core_lift = centered_scaled_lift(core, 1, prime)
        anchor_lift = centered_scaled_lift(anchor, 1, prime)

        path = (
            Path(temporary_directory)
            / f"matching_{''.join(map(str, word))}_{prime}.npy"
        )
        np.save(path, matching16)
        results[word] = {
            "matching_path": path,
            "matching_rank": matching_rank,
            "quotient_dimension": quotient.shape[0],
            "core": core_lift,
            "anchor": anchor_lift,
            "edge_index": edge_index,
            "description": description,
            "core_rank_mod": rank_mod(core, prime),
        }
    return results


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    print("reconstructing exact n=6 chart atlas", flush=True)
    _, charts = reconstruct_charts()

    with TemporaryDirectory() as temporary_directory:
        modular = {
            prime: process_prime(
                prime,
                charts,
                temporary_directory,
            )
            for prime in PRIMES
        }

        integer_cores = {}
        descriptions = {}
        for word in SUPPORTS:
            first = modular[PRIMES[0]][word]
            second = modular[PRIMES[1]][word]
            first_matching = np.load(first["matching_path"])
            second_matching = np.load(second["matching_path"])

            check(
                f"word {word}: both primes lift the same 16*matching",
                np.array_equal(first_matching, second_matching),
            )
            check(
                f"word {word}: 16*matching has alphabet 0,+/-1,+/-2",
                set(int(value) for value in first_matching.reshape(-1))
                <= {-2, -1, 0, 1, 2},
            )
            check(
                f"word {word}: both primes lift the same integer anchor",
                np.array_equal(first["anchor"], second["anchor"]),
            )
            check(
                f"word {word}: both primes lift the same integer completion",
                np.array_equal(first["core"], second["core"]),
            )
            check(
                f"word {word}: completion coefficients have size at most 12",
                int(np.max(np.abs(first["core"]))) <= 12,
            )
            check(
                f"word {word}: integer completion kills 16*matching",
                not np.count_nonzero(
                    first["core"] @ first_matching
                ),
            )
            check(
                f"word {word}: the specified anchor is the completed block",
                np.array_equal(
                    first["core"][
                        :,
                        first["edge_index"] * EDGE_DIMENSION:
                        (first["edge_index"] + 1) * EDGE_DIMENSION,
                    ],
                    first["anchor"],
                ),
            )

            for prime in PRIMES:
                result = modular[prime][word]
                check(
                    f"word {word}: matching rank is 1800 mod {prime}",
                    result["matching_rank"] == MATCHING_RANK,
                )
                check(
                    f"word {word}: quotient dimension is 144 mod {prime}",
                    result["quotient_dimension"] == CORE_DIMENSION,
                )
                check(
                    f"word {word}: completion rank is 144 mod {prime}",
                    result["core_rank_mod"] == CORE_DIMENSION,
                )

            integer_cores[word] = first["core"]
            descriptions[word] = first["description"]

        crt_bound = EDGE_DIMENSION * FACE_DIMENSION * 2 + 16
        crt_modulus = PRIMES[0] * PRIMES[1]
        check(
            "the matching factorization bound fits below the CRT modulus",
            crt_bound < crt_modulus,
        )

    projector_numerators, target_generators = casimir_numerators()
    source_generators, _, _ = action_generators()
    target_profile = tuple(
        exact_rank(projector)
        for projector in projector_numerators
    )
    check(
        "the core target has the generic n=7 spin profile",
        target_profile == FULL_PROFILE,
    )

    edge_data = {}
    for word, core in integer_cores.items():
        check(
            f"word {word}: completion is SO(3)-equivariant over Z",
            all(
                not np.count_nonzero(
                    target @ core[
                        :,
                        edge_index * EDGE_DIMENSION:
                        (edge_index + 1) * EDGE_DIMENSION,
                    ]
                    - core[
                        :,
                        edge_index * EDGE_DIMENSION:
                        (edge_index + 1) * EDGE_DIMENSION,
                    ] @ source
                )
                for source, target in zip(
                    source_generators, target_generators
                )
                for edge_index in range(6)
            ),
        )
        edge_ranks, edge_profiles = exact_edge_profiles(
            core,
            projector_numerators,
        )
        expected_profiles = (
            CENTRAL_EDGE_PROFILES
            if word[1] > 1
            else STANDARD_EDGE_PROFILES
        )
        check(
            f"word {word}: exact edge Casimir profiles agree with the atlas",
            edge_profiles == expected_profiles,
        )
        check(
            f"word {word}: exact edge ranks are profile dimensions",
            edge_ranks == tuple(
                sum(profile) for profile in expected_profiles
            ),
        )
        edge_data[word] = (edge_ranks, edge_profiles)

    print("CRT bound/modulus:", crt_bound, crt_modulus)
    for word in SUPPORTS:
        core = integer_cores[word]
        print(
            "word",
            "".join(map(str, word)),
            "anchor",
            descriptions[word],
        )
        print(
            "  core alphabet:",
            sorted(set(int(value) for value in core.reshape(-1))),
        )
        print("  exact edge ranks:", edge_data[word][0])
        print("  exact edge profiles:", edge_data[word][1])

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
