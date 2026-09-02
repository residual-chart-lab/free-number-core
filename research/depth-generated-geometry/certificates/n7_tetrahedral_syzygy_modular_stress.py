#!/usr/bin/env python3
"""Two-prime n=7 stress test for tetrahedral generation of first syzygies.

This is the first case in which a four-vertex support can occupy genuinely
different positions inside the ordered six-vertex response simplex.  The
script constructs the full first and second differentials over a prime field,
checks exactness at C1, and descends the SO(3) Casimir to every local quotient
and to coker(partial_7^(2)).

The computation is exact finite-field linear algebra.  It is evidence for the
characteristic-zero conjecture, not by itself a theorem over Q.
"""

import argparse

import numpy as np

from second_response_simplex_differential_certificate import modular_case


PRIMES = (1009, 1013)
EXCEPTIONAL_SUPPORT = (1, 3, 4, 6)
GENERIC_TYPE = {0: 6, 1: 13, 2: 11, 3: 5, 4: 1}
EXCEPTIONAL_TYPE = {0: 7, 1: 14, 2: 11, 3: 5, 4: 1}
COKERNEL_TYPE = {0: 46, 1: 96, 2: 75, 3: 30, 4: 5}


def run(prime):
    result = modular_case(7, prime)
    supports = [support for support, _, _ in result["local_data"]]
    local_dimensions = [
        quotient.shape[0]
        for _, _, quotient in result["local_data"]
    ]
    local_types = dict(zip(supports, result["local_types"]))
    exceptional_indices = [
        index
        for index, dimension in enumerate(local_dimensions)
        if dimension != 144
    ]

    print(
        f"n=7 mod {prime}: first shape {result['matching'].shape}, "
        f"rank {result['matching_rank']}"
    )
    print(
        f"  second shape {result['second'].shape}, "
        f"rank {result['second_rank']}, "
        f"kernel {result['matching'].shape[0] - result['second_rank']}, "
        f"cokernel {result['cokernel_dimension']}"
    )
    for support, dimension in zip(supports, local_dimensions):
        marker = "  <interlaced>" if support == EXCEPTIONAL_SUPPORT else ""
        print(
            f"  Q={support}: dim {dimension}, "
            f"type {local_types[support]}{marker}"
        )
    print(f"  second-cokernel type: {result['cokernel_type']}")

    checks = [
        (
            "the first differential has shape 4860 x 5832",
            result["matching"].shape == (4860, 5832),
        ),
        (
            "the first differential has rank 3660",
            result["matching_rank"] == 3660,
        ),
        (
            "exactly one four-support is non-generic",
            exceptional_indices == [supports.index(EXCEPTIONAL_SUPPORT)],
        ),
        (
            "fourteen local quotients have dimension 144",
            local_dimensions.count(144) == 14,
        ),
        (
            "the interlaced quotient has dimension 148",
            local_dimensions[supports.index(EXCEPTIONAL_SUPPORT)] == 148,
        ),
        (
            "all generic local quotients have the predicted Casimir type",
            all(
                local_types[support] == GENERIC_TYPE
                for support in supports
                if support != EXCEPTIONAL_SUPPORT
            ),
        ),
        (
            "the interlaced quotient has one extra H=V0+V1",
            local_types[EXCEPTIONAL_SUPPORT] == EXCEPTIONAL_TYPE,
        ),
        (
            "the second target has dimension 2164",
            result["second"].shape[0] == 2164,
        ),
        (
            "the second differential kills the first image",
            not np.count_nonzero(
                (result["second"] @ result["matching"]) % prime
            ),
        ),
        (
            "the second differential has rank 1200",
            result["second_rank"] == 1200,
        ),
        (
            "the complex is exact at C1",
            result["matching"].shape[0] - result["second_rank"]
            == result["matching_rank"]
            == 3660,
        ),
        (
            "the second cokernel has dimension 964",
            result["cokernel_dimension"] == 964,
        ),
        (
            "the second cokernel has the measured Casimir type",
            result["cokernel_type"] == COKERNEL_TYPE,
        ),
    ]

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] mod {prime}: {name}")
    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED modulo {prime}: {', '.join(failed)}")
    print(f"ALL CHECKS PASSED MODULO {prime}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prime",
        type=int,
        choices=PRIMES,
        help="run one prime only (default: run both)",
    )
    arguments = parser.parse_args()
    primes = (arguments.prime,) if arguments.prime else PRIMES
    for prime in primes:
        run(prime)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
