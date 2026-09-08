#!/usr/bin/env python3
"""Finite-field certificate for spectator-placement residual fingerprints.

For every four-face support Q at n=6 and n=7, form the canonical local
tetrahedral quotient Y_(n,Q).  The quotient map has six edge blocks.  This
script measures the SO(3)-Casimir profile of the image of each block, not
only the abstract type of Y_(n,Q).

The checks isolate two placement effects:

* at n=6, the central-spectator support (1,2,4,5) makes the long edge image
  lose one H = V0 + V1;
* at n=7, a spectator in the central interval makes the long edge image lose
  H tensor V, while the unique 2-1-2 support gains a canonical H quotient
  seen by exactly the four cross edges.

All arithmetic is exact over the stated prime fields.  Agreement at two
primes is evidence for the characteristic-zero pattern, not a proof over Q.
"""

import argparse
from itertools import combinations

import numpy as np

from n6_response_4simplex_modular_certificate import (
    build_integer_response,
    build_matching_operator_mod,
    rank_mod,
)
from second_response_simplex_differential_certificate import (
    induced_generators,
    left_nullspace_mod,
    response_generators,
    select_local_operator,
)


PRIMES = (1009, 1013)
LENGTHS = (6, 7)

N6_FULL = (3, 18, 20, 7)
N6_STANDARD = (
    N6_FULL,
    (2, 12, 15, 7),
    N6_FULL,
    (1, 6, 5, 0),
    (2, 12, 15, 7),
    N6_FULL,
)
N6_CENTRAL = N6_STANDARD[:2] + ((2, 15, 20, 7),) + N6_STANDARD[3:]

N7_FULL = (6, 39, 55, 35, 9)
N7_EXCEPTIONAL_FULL = (7, 42, 55, 35, 9)
N7_STANDARD = (
    N7_FULL,
    (4, 27, 40, 28, 9),
    N7_FULL,
    (2, 12, 15, 7, 0),
    (4, 27, 40, 28, 9),
    N7_FULL,
)
N7_CENTRAL = N7_STANDARD[:2] + ((5, 33, 50, 35, 9),) + N7_STANDARD[3:]
N7_EXCEPTIONAL = (
    N7_FULL,
    (5, 30, 40, 28, 9),
    N7_EXCEPTIONAL_FULL,
    (3, 15, 15, 7, 0),
    (5, 30, 40, 28, 9),
    N7_FULL,
)


def casimir_projectors(generators, maximum_spin, prime):
    dimension = generators[0].shape[0]
    identity = np.eye(dimension, dtype=np.int64)
    casimir = -sum(
        (generator @ generator) % prime for generator in generators
    ) % prime
    eigenvalues = [spin * (spin + 1) for spin in range(maximum_spin + 1)]
    projectors = []
    for eigenvalue in eigenvalues:
        projector = identity.copy()
        denominator = 1
        for other in eigenvalues:
            if other == eigenvalue:
                continue
            projector = (
                projector @ ((casimir - other * identity) % prime)
            ) % prime
            denominator = denominator * (eigenvalue - other) % prime
        projectors.append(
            projector * pow(denominator, -1, prime) % prime
        )
    if sum(rank_mod(projector, prime) for projector in projectors) != dimension:
        raise AssertionError("Casimir projectors do not exhaust the quotient")
    return projectors


def spin_profile(block, projectors, prime):
    return tuple(
        rank_mod((projector @ block) % prime, prime)
        for projector in projectors
    )


def build_profiles(n, prime):
    gaps = list(range(1, n))
    faces = {gap: build_integer_response(n, {gap}) for gap in gaps}
    shadows = {
        edge: build_integer_response(n, set(edge))
        for edge in combinations(gaps, 2)
    }
    matching, _, _ = build_matching_operator_mod(faces, shadows, prime)
    face_dimension = 4 * 3 ** (n - 2)
    edge_dimension = 4 * 3 ** (n - 3)
    response_action = response_generators(n - 3)
    profiles = {}

    for support in combinations(gaps, 4):
        local, _ = select_local_operator(
            matching,
            gaps,
            face_dimension,
            edge_dimension,
            support,
        )
        quotient = left_nullspace_mod(local, prime)
        generators = induced_generators(quotient, response_action, prime)
        projectors = casimir_projectors(generators, n - 3, prime)
        blocks = tuple(
            quotient[
                :,
                index * edge_dimension:(index + 1) * edge_dimension,
            ]
            for index in range(6)
        )
        profiles[support] = {
            "dimension": quotient.shape[0],
            "full": tuple(rank_mod(projector, prime) for projector in projectors),
            "edges": tuple(
                spin_profile(block, projectors, prime) for block in blocks
            ),
            "blocks": blocks,
        }
    return profiles


def check_n6(profiles, prime):
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    exceptional = (1, 2, 4, 5)
    check("all five n=6 local quotients have dimension 48", all(
        data["dimension"] == 48 for data in profiles.values()
    ))
    check("all five n=6 local quotients have the same Casimir profile", all(
        data["full"] == N6_FULL for data in profiles.values()
    ))
    check("the central-spectator support has the H-defective edge profile",
          profiles[exceptional]["edges"] == N6_CENTRAL)
    check("the other four n=6 supports have the standard edge profile", all(
        data["edges"] == N6_STANDARD
        for support, data in profiles.items()
        if support != exceptional
    ))

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] mod {prime}: {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED n=6 mod {prime}: {', '.join(failed)}")


def check_n7(profiles, prime):
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    exceptional = (1, 3, 4, 6)
    central_supports = {
        support
        for support in profiles
        if support[2] - support[1] > 1
    }
    ordinary_supports = set(profiles) - central_supports - {exceptional}

    check("there are five central-interval supports", len(central_supports) == 5)
    check("there are nine ordinary supports", len(ordinary_supports) == 9)
    check("fourteen n=7 quotients have dimension 144", sum(
        data["dimension"] == 144 for data in profiles.values()
    ) == 14)
    check("the 2-1-2 quotient has dimension 148",
          profiles[exceptional]["dimension"] == 148)
    check("all generic quotients have the standard Casimir profile", all(
        data["full"] == N7_FULL
        for support, data in profiles.items()
        if support != exceptional
    ))
    check("the 2-1-2 quotient has one extra H",
          profiles[exceptional]["full"] == N7_EXCEPTIONAL_FULL)
    check("all central-interval supports lose H tensor V on edge 14", all(
        profiles[support]["edges"] == N7_CENTRAL
        for support in central_supports
    ))
    check("all ordinary supports have the standard edge profile", all(
        profiles[support]["edges"] == N7_STANDARD
        for support in ordinary_supports
    ))
    check("the 2-1-2 support has the cross-edge H profile",
          profiles[exceptional]["edges"] == N7_EXCEPTIONAL)

    blocks = profiles[exceptional]["blocks"]
    outer_join = rank_mod(
        np.concatenate((blocks[0], blocks[5]), axis=1), prime
    )
    core_joins = tuple(
        rank_mod(np.concatenate((blocks[0], block), axis=1), prime)
        for block in blocks
    )
    check("the two outer edge images are the same 144-dimensional core",
          outer_join == 144)
    check("exactly the four cross edges surject onto the residual quotient",
          core_joins == (144, 148, 148, 148, 148, 144))

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] mod {prime}: {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED n=7 mod {prime}: {', '.join(failed)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prime", type=int, choices=PRIMES,
        help="run one prime only (default: both)",
    )
    parser.add_argument(
        "--length", type=int, choices=LENGTHS,
        help="run one tensor length only (default: n=6 and n=7)",
    )
    arguments = parser.parse_args()
    primes = (arguments.prime,) if arguments.prime else PRIMES
    lengths = (arguments.length,) if arguments.length else LENGTHS

    for prime in primes:
        for n in lengths:
            print(f"building n={n} placement profiles mod {prime}", flush=True)
            profiles = build_profiles(n, prime)
            if n == 6:
                check_n6(profiles, prime)
            else:
                check_n7(profiles, prime)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
