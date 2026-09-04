#!/usr/bin/env python3
"""Exact certificate for transport on the reduced n=7 spacing-word graph.

The six positive compositions of 5 into three parts label the reduced
two-spectator supports.  Adjacent words differ by sliding one internal
support vertex through one gap.  The two tetrahedra share a triangular face
and, inside that face, a stationary outer edge.

This certificate proves that the two 144-dimensional core coordinates have
the same full row space on that stationary edge.  Hence the shared edge
defines a unique integral SO(3)-equivariant core transport.  The only cycle
in the spacing graph has exactly trivial holonomy.

At the exceptional word 212 the full quotient is T_7 direct-sum H.  The
intrinsic kappa_212 coordinate vanishes on both stationary outer edges, so
both incident transports factor through the 144-dimensional core and have
the residual H as kernel.  Thus the complete atlas is a flat core system
with a four-dimensional vertex-supported defect, not a curved core system.

Every quotient coordinate and every slide is reconstructed independently
over F_1009 and F_1013.  Centered lifts agree; all transition, inverse,
holonomy, residual, polynomial, and equivariance identities are then checked
over the integers.  NumPy is used only for integer and finite-field
arithmetic; no floating-point computation occurs.
"""

from itertools import combinations
from tempfile import TemporaryDirectory

import numpy as np

from all_n_pairwise_terminal_descent_certificate import right_encoder
from n6_response_4simplex_modular_certificate import (
    rank_mod,
    right_inverse_data_mod,
)
from n6_spectator_chart_transition_certificate import reconstruct_charts
from n7_anchor_transition_groupoid_certificate import (
    ALL_SUPPORTS,
    EXCEPTIONAL_WORD,
    PRIMES,
    centered_lift,
    evaluate_polynomial_exact,
    minimal_polynomial_mod,
    process_prime,
)
from n7_exceptional_core_decomposition_certificate import (
    action_generators,
    integer_array,
    tensor_kappa,
)
from n7_internal_word_atlas_certificate import (
    CORE_DIMENSION,
    EDGE_DIMENSION,
)


W113 = (1, 1, 3)
W122 = (1, 2, 2)
W131 = (1, 3, 1)
W212 = EXCEPTIONAL_WORD
W221 = (2, 2, 1)
W311 = (3, 1, 1)

# Each entry is (source word, target word, stationary outer edge).
ADJACENCY = (
    (W113, W122, (1, 2)),
    (W122, W131, (1, 2)),
    (W122, W212, (4, 6)),
    (W131, W221, (5, 6)),
    (W212, W221, (1, 3)),
    (W221, W311, (5, 6)),
)

EXPECTED_MINIMAL_POLYNOMIALS = {
    (W113, W122): (-1, 1, 2, -2, -1, 1),
    (W122, W131): (-1, -1, 1, 1),
    (W122, W212): (1, 1),
    (W131, W221): (1, 1),
    (W212, W221): (-1, -1, 1, 1),
    (W221, W311): (1, 1),
}

EXPECTED_FACE_RANKS = {
    (W113, W122): (144, 144, 288),
    (W122, W131): (144, 144, 288),
    (W122, W212): (144, 148, 292),
    (W131, W221): (144, 144, 288),
    (W212, W221): (148, 144, 292),
    (W221, W311): (144, 144, 288),
}


def word_label(word):
    return "".join(map(str, word))


def edge_block(coordinate, support, edge):
    edges = tuple(combinations(support, 2))
    edge_index = edges.index(edge)
    columns = slice(
        edge_index * EDGE_DIMENSION,
        (edge_index + 1) * EDGE_DIMENSION,
    )
    return coordinate[:, columns]


def face_trace(coordinate, support, shared_vertices):
    return np.concatenate(
        tuple(
            edge_block(coordinate, support, edge)
            for edge in combinations(shared_vertices, 2)
        ),
        axis=1,
    )


def transition_mod(source, target, prime):
    pivots, inverse = right_inverse_data_mod(source, prime)
    if len(pivots) != CORE_DIMENSION:
        raise AssertionError("stationary edge stopped being a full anchor")
    transition = target[:, pivots] @ inverse % prime
    if np.count_nonzero((transition @ source - target) % prime):
        raise AssertionError("shared-edge transport failed to descend")
    return transition


def report():
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    print("reconstructing exact n=6 parent charts", flush=True)
    _, charts = reconstruct_charts()
    kappa = tensor_kappa(integer_array(right_encoder(4)))

    modular_cores = {}
    modular_slides = {}
    modular_reverse_slides = {}

    with TemporaryDirectory() as temporary_directory:
        for prime in PRIMES:
            data = process_prime(prime, charts, temporary_directory)
            cores = {
                word: item["groups"][0]["core"] % prime
                for word, item in data.items()
            }
            modular_cores[prime] = cores
            slides = {}
            reverse_slides = {}

            for source_word, target_word, hinge in ADJACENCY:
                source_support = ALL_SUPPORTS[source_word]
                target_support = ALL_SUPPORTS[target_word]
                shared_vertices = tuple(
                    sorted(set(source_support) & set(target_support))
                )
                check(
                    f"{word_label(source_word)}-{word_label(target_word)}: "
                    "the supports share one triangular face",
                    len(shared_vertices) == 3,
                )

                source_block = edge_block(
                    cores[source_word], source_support, hinge
                ) % prime
                target_block = edge_block(
                    cores[target_word], target_support, hinge
                ) % prime
                check(
                    f"{word_label(source_word)}->{word_label(target_word)} "
                    f"mod {prime}: source hinge rank 144",
                    rank_mod(source_block, prime) == CORE_DIMENSION,
                )
                check(
                    f"{word_label(source_word)}->{word_label(target_word)} "
                    f"mod {prime}: target hinge rank 144",
                    rank_mod(target_block, prime) == CORE_DIMENSION,
                )
                check(
                    f"{word_label(source_word)}->{word_label(target_word)} "
                    f"mod {prime}: hinge row spaces agree",
                    rank_mod(
                        np.concatenate((source_block, target_block), axis=0),
                        prime,
                    ) == CORE_DIMENSION,
                )

                slide = transition_mod(source_block, target_block, prime)
                reverse = transition_mod(target_block, source_block, prime)
                identity = np.eye(CORE_DIMENSION, dtype=np.int64)
                check(
                    f"{word_label(source_word)}->{word_label(target_word)} "
                    f"mod {prime}: forward and reverse slides are inverse",
                    np.array_equal(slide @ reverse % prime, identity)
                    and np.array_equal(reverse @ slide % prime, identity),
                )
                slides[(source_word, target_word)] = slide
                reverse_slides[(source_word, target_word)] = reverse

                full_source = cores[source_word]
                full_target = cores[target_word]
                if source_word == W212:
                    full_source = np.concatenate(
                        (full_source, kappa % prime), axis=0
                    )
                if target_word == W212:
                    full_target = np.concatenate(
                        (full_target, kappa % prime), axis=0
                    )
                source_face = face_trace(
                    full_source, source_support, shared_vertices
                ) % prime
                target_face = face_trace(
                    full_target, target_support, shared_vertices
                ) % prime
                face_ranks = (
                    rank_mod(source_face, prime),
                    rank_mod(target_face, prime),
                    rank_mod(
                        np.concatenate((source_face, target_face), axis=0),
                        prime,
                    ),
                )
                check(
                    f"{word_label(source_word)}-{word_label(target_word)} "
                    f"mod {prime}: common-face traces are transverse",
                    face_ranks
                    == EXPECTED_FACE_RANKS[(source_word, target_word)],
                )

            modular_slides[prime] = slides
            modular_reverse_slides[prime] = reverse_slides

    integer_cores = {}
    for word in ALL_SUPPORTS:
        first = centered_lift(modular_cores[PRIMES[0]][word], PRIMES[0])
        second = centered_lift(modular_cores[PRIMES[1]][word], PRIMES[1])
        check(
            f"word {word_label(word)}: selected core lift is prime-independent",
            np.array_equal(first, second),
        )
        integer_cores[word] = first

    integer_slides = {}
    integer_reverse_slides = {}
    _, target_generators, _ = action_generators()
    identity = np.eye(CORE_DIMENSION, dtype=np.int64)

    for source_word, target_word, hinge in ADJACENCY:
        key = (source_word, target_word)
        first_slide = centered_lift(
            modular_slides[PRIMES[0]][key], PRIMES[0]
        )
        second_slide = centered_lift(
            modular_slides[PRIMES[1]][key], PRIMES[1]
        )
        first_reverse = centered_lift(
            modular_reverse_slides[PRIMES[0]][key], PRIMES[0]
        )
        second_reverse = centered_lift(
            modular_reverse_slides[PRIMES[1]][key], PRIMES[1]
        )
        label = f"{word_label(source_word)}->{word_label(target_word)}"
        check(
            f"{label}: integral slide lift is prime-independent",
            np.array_equal(first_slide, second_slide),
        )
        check(
            f"{label}: integral reverse lift is prime-independent",
            np.array_equal(first_reverse, second_reverse),
        )
        check(
            f"{label}: slide alphabet is 0,+/-1",
            set(int(value) for value in first_slide.reshape(-1))
            <= {-1, 0, 1},
        )

        source_block = edge_block(
            integer_cores[source_word], ALL_SUPPORTS[source_word], hinge
        )
        target_block = edge_block(
            integer_cores[target_word], ALL_SUPPORTS[target_word], hinge
        )
        check(
            f"{label}: exact stationary-edge transition",
            np.array_equal(first_slide @ source_block, target_block),
        )
        check(
            f"{label}: exact inverse transition",
            np.array_equal(first_reverse @ target_block, source_block)
            and np.array_equal(first_slide @ first_reverse, identity)
            and np.array_equal(first_reverse @ first_slide, identity),
        )
        check(
            f"{label}: exact SO(3)-equivariance",
            all(
                not np.count_nonzero(
                    generator @ first_slide - first_slide @ generator
                )
                for generator in target_generators
            ),
        )

        polynomial = EXPECTED_MINIMAL_POLYNOMIALS[key]
        check(
            f"{label}: exact annihilating polynomial",
            not np.count_nonzero(
                evaluate_polynomial_exact(first_slide, polynomial)
            ),
        )
        for prime in PRIMES:
            check(
                f"{label}: minimal polynomial mod {prime}",
                minimal_polynomial_mod(
                    modular_slides[prime][key], prime
                ) == polynomial,
            )

        integer_slides[key] = first_slide
        integer_reverse_slides[key] = first_reverse

    R = integer_slides[(W122, W131)]
    check(
        "the two horizontal central slides are the same R",
        np.array_equal(R, integer_slides[(W212, W221)]),
    )
    check(
        "the three vertical/right-tail slides are -identity",
        all(
            np.array_equal(integer_slides[key], -identity)
            for key in (
                (W122, W212),
                (W131, W221),
                (W221, W311),
            )
        ),
    )

    # 122 -> 131 -> 221 -> 212 -> 122.
    holonomy = (
        integer_reverse_slides[(W122, W212)]
        @ integer_reverse_slides[(W212, W221)]
        @ integer_slides[(W131, W221)]
        @ integer_slides[(W122, W131)]
    )
    check(
        "the unique spacing-word cycle has exact identity holonomy",
        np.array_equal(holonomy, identity),
    )

    # The two hinges incident to 212 are its local outer edges 12 and 34.
    exceptional_support = ALL_SUPPORTS[W212]
    for neighbor, hinge, outward in (
        (W122, (4, 6), integer_reverse_slides[(W122, W212)]),
        (W221, (1, 3), integer_slides[(W212, W221)]),
    ):
        kappa_block = edge_block(kappa, exceptional_support, hinge)
        exceptional_core_block = edge_block(
            integer_cores[W212], exceptional_support, hinge
        )
        neighbor_block = edge_block(
            integer_cores[neighbor], ALL_SUPPORTS[neighbor], hinge
        )
        check(
            f"212->{word_label(neighbor)}: kappa vanishes on the hinge",
            not np.count_nonzero(kappa_block),
        )
        check(
            f"212->{word_label(neighbor)}: full transport factors through core",
            np.array_equal(outward @ exceptional_core_block, neighbor_block),
        )
        full_outward = np.concatenate(
            (outward, np.zeros((CORE_DIMENSION, 4), dtype=np.int64)),
            axis=1,
        )
        check(
            f"212->{word_label(neighbor)}: defect kernel has dimension four",
            rank_mod(full_outward % PRIMES[0], PRIMES[0])
            == CORE_DIMENSION
            and not np.count_nonzero(full_outward[:, CORE_DIMENSION:]),
        )

    print("spacing-word graph:")
    print("  113--122--131")
    print("       |     |")
    print("      212--221--311")
    print("stationary-edge slides:")
    for source_word, target_word, hinge in ADJACENCY:
        key = (source_word, target_word)
        print(
            " ",
            f"{word_label(source_word)}->{word_label(target_word)}",
            "hinge",
            hinge,
            "minpoly",
            EXPECTED_MINIMAL_POLYNOMIALS[key],
        )
    print("central square holonomy: identity")
    print("exceptional full fiber: flat core direct-sum vertex H defect")
    print("common-face intersections: zero on all six graph edges")

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit("FAILED: " + ", ".join(failed))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
