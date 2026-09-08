#!/usr/bin/env python3
"""Modular stress check for the first local descent rung beyond m <= 4.

Note 12 proves symbolically that actual last-face deletions and simple slot
contractions have the same common kernel for every m.  The exact rational
certificate checks every suffix row space through m=4.  This auxiliary check
builds the next case m=5 (the local model for n=7) directly and compares the
full actual, simple, and joined row spaces over two independent prime fields.

This is a falsification/stress check, not a substitute for the all-m proof.
NumPy is used only for integer matrix storage and modular row operations.
"""

from itertools import product

import numpy as np

from n2_intrinsic_response_certificate import Q, V, qmul
from n6_response_4simplex_modular_certificate import rank_mod


DEPTH = 5
PRIMES = (1009, 1013)


def build_local_stacks(depth):
    source = list(product(range(4), *([range(3)] * depth)))
    probes = list(product(range(3), repeat=depth - 1))
    actual_blocks = []
    simple_blocks = []

    for slot in range(depth):
        remaining = [index for index in range(depth) if index != slot]
        actual = np.zeros(
            (4 * len(probes), len(source)), dtype=np.int64
        )
        simple = np.zeros_like(actual)

        for column, (h_index, *vectors) in enumerate(source):
            contracted = qmul(Q[h_index], V[vectors[slot]])

            for probe_index, probe_word in enumerate(probes):
                assigned = dict(zip(remaining, probe_word))

                actual_value = Q[h_index]
                for index in reversed(range(depth)):
                    if index != slot:
                        actual_value = qmul(
                            actual_value, V[assigned[index]]
                        )
                    actual_value = qmul(
                        actual_value, V[vectors[index]]
                    )

                simple_value = contracted
                for index in reversed(remaining):
                    simple_value = qmul(
                        simple_value, V[assigned[index]]
                    )
                    simple_value = qmul(
                        simple_value, V[vectors[index]]
                    )

                row = 4 * probe_index
                actual[row : row + 4, column] = actual_value
                simple[row : row + 4, column] = simple_value

        actual_blocks.append(actual)
        simple_blocks.append(simple)

    return (
        np.concatenate(actual_blocks, axis=0),
        np.concatenate(simple_blocks, axis=0),
    )


def report():
    actual, simple = build_local_stacks(DEPTH)
    joined = np.concatenate([actual, simple], axis=0)
    source_dimension = 4 * 3**DEPTH
    expected_kernel = 4 * (DEPTH + 1)
    expected_rank = source_dimension - expected_kernel
    checks = []

    def check(name, condition):
        checks.append((name, bool(condition)))

    for prime in PRIMES:
        actual_rank = rank_mod(actual % prime, prime)
        simple_rank = rank_mod(simple % prime, prime)
        joined_rank = rank_mod(joined % prime, prime)
        print(
            f"mod {prime}: actual rank {actual_rank}, "
            f"simple rank {simple_rank}, joined rank {joined_rank}, "
            f"kernel {source_dimension - simple_rank}"
        )
        check(
            f"m=5 actual/simple/joined row spaces agree modulo {prime}",
            actual_rank == simple_rank == joined_rank == expected_rank,
        )
        check(
            f"m=5 common kernel has dimension 24 modulo {prime}",
            source_dimension - simple_rank == expected_kernel == 24,
        )

    for name, passed in checks:
        print(f"[{'PASS' if passed else 'FAIL'}] {name}")

    failed = [name for name, passed in checks if not passed]
    if failed:
        raise SystemExit(f"FAILED: {', '.join(failed)}")

    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    report()
