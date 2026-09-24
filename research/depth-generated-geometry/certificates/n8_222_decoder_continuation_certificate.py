#!/usr/bin/env python3
"""Note 28: central right-decoder readouts and minimal retained child state.

Caps are constructed from quaternion products and probe evaluations before
their inverse relation with Note 26's suspension is checked. Old result JSONs
are not inputs. All mathematical checks use exact arithmetic.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import argparse
import hashlib
import json
import platform
import time

import numpy as np
import scipy
from scipy import sparse

import n8_222_redetection_certificate as base
from n8_222_minimal_refinement_certificate import exact_product, exact_row_factor, graded_rank

if not __debug__:
    raise RuntimeError("Certificate checks require assertions; do not use -O or -OO.")

BASE_COMMIT = "3e479034f1834542eb8679cca6638eeee7d82e0c"
PRIMES = base.PRIMES


def right_multiplication(a):
    out = np.zeros((4, 4), dtype=np.int64)
    for h in range(4):
        out[h ^ a, h] = base.SIGNS[h, a]
    return out


def cap_primitive():
    """Twice the inverse of h tensor w -> (z -> h z w), built from (2.1)."""
    numerator = np.zeros((12, 12), dtype=np.int64)
    for a, (b, c) in enumerate(((2, 3), (3, 1), (1, 2))):
        rows = np.arange(a, 12, 3)
        numerator[np.ix_(rows, np.arange(4*(b-1), 4*b))] = right_multiplication(c)
        numerator[np.ix_(rows, np.arange(4*(c-1), 4*c))] = -right_multiplication(b)
    identity = 2 * np.eye(12, dtype=np.int64)
    assert np.array_equal(exact_product(numerator, base.encoder(1)), identity)
    assert np.array_equal(exact_product(base.encoder(1), numerator), identity)
    return numerator


@lru_cache(None)
def direct_caps(pos):
    """Decode the selected probe pointwise, then use the old four-probe basis.

    Returns (den, matrix); output order is (parent decoded coefficient, i/j/k).
    No inversion of Sigma is used in this construction.
    """
    primitive = cap_primitive()
    old_den, old_inverse = base.lift(base.decoder(4, PRIMES[0]), base.decoder(4, PRIMES[1]))
    assert np.array_equal(exact_product(old_inverse, base.encoder(4)), old_den * np.eye(324, dtype=np.int64))
    child_evaluations = base.encoder(5)
    cap_evaluations = [np.zeros((324, 972), dtype=np.int64) for _ in range(3)]
    for old_ix, old_args in enumerate(base.words(4)):
        rows = []
        for z in (1, 2, 3):
            args = list(old_args)
            args.insert(pos, z)
            ix = 0
            for a in args:
                ix = 3 * ix + int(a) - 1
            rows.extend(range(4*ix, 4*ix+4))
        values = exact_product(primitive, child_evaluations[rows])
        for a in range(3):
            cap_evaluations[a][4*old_ix:4*old_ix+4] = values[a::3]
    out = np.zeros((972, 972), dtype=np.int64)
    for a in range(3):
        out[a::3] = exact_product(old_inverse, cap_evaluations[a])
    den = 2 * old_den
    divisor = int(np.gcd(den, np.gcd.reduce(np.abs(out).ravel())))
    return den // divisor, out // divisor


def certify_joint_rank(child_q, readout, grades, obstruction_rank):
    """Exact upper bound from restriction to ker(child_q), modular lower bound.

    ker(child_q) = im(child_d) was certified by exact_quotient. Thus the
    joint rank is at most 444 + the independently bounded obstruction rank.
    Nonzero minors modulo a prime certify the matching rational lower bound.
    """
    joint = np.concatenate([child_q, readout])
    supports = (joint != 0).astype(np.int64)
    row_grade = np.full(joint.shape[0], -1, dtype=np.int64)
    for grade in range(4):
        touched = np.any(supports[:, grades == grade], axis=1)
        assert np.all(row_grade[touched] == -1)
        row_grade[touched] = grade
    profiles = []
    for prime in PRIMES:
        ranks = [len(base.rref(joint[np.ix_(row_grade == g, grades == g)], prime)[1])
                 for g in range(4)]
        assert sum(ranks) == 444 + obstruction_rank
        profiles.append(ranks)
    assert profiles[0] == profiles[1]
    return sum(profiles[0]), profiles[0]


def certificate(output=None):
    started = time.monotonic()
    base.primitive_checks()
    cap_primitive()
    parent_q, parent_d = base.exact_quotient(7, (1, 3, 4, 6))
    child_q, child_d = base.exact_quotient(8, (1, 3, 5, 7))
    assert parent_q.shape == (148, 1944)
    assert child_q.shape == (444, 5832)
    k, big_k = base.residual(4), base.residual(5)
    parent_den, parent_res = exact_row_factor(k, parent_q)
    child_den, child_res = exact_row_factor(big_k, child_q)
    assert base.certified_rank(parent_res) == 4
    assert base.certified_rank(child_res) == 12
    eye_v = np.eye(3, dtype=np.int64)
    q = np.kron(parent_q, eye_v)
    alpha_num = exact_product(base.encoder(1), np.kron(parent_res, eye_v))
    assert base.certified_rank(alpha_num) == 12

    edges = list(combinations((1, 3, 5, 7), 2))
    cap_blocks, suspension_blocks = [], []
    checked_positions = set()
    for edge in edges:
        pos = [g for g in range(1, 8) if g not in edge].index(4)
        cap_den, cap = direct_caps(pos)
        sigma_den, sigma = base.exact_suspension(pos, "right")
        if pos not in checked_positions:
            expected = cap_den * sigma_den * np.eye(972, dtype=np.int64)
            assert np.array_equal(exact_product(cap, sigma), expected)
            assert np.array_equal(exact_product(sigma, cap), expected)
            checked_positions.add(pos)
        cap_blocks.append((cap_den, cap))
        suspension_blocks.append((sigma_den, sigma))
    cap_common = int(np.lcm.reduce([d for d, _ in cap_blocks]))
    sigma_common = int(np.lcm.reduce([d for d, _ in suspension_blocks]))
    readout_blocks, forward_blocks = [], []
    for ei, ((cd, cap), (sd, sigma)) in enumerate(zip(cap_blocks, suspension_blocks)):
        selected = slice(ei*972, (ei+1)*972)
        readout = exact_product(q[:, selected], (cap_common // cd) * cap)
        forward = exact_product(child_q[:, selected], (sigma_common // sd) * sigma)
        readout_blocks.append(readout)
        forward_blocks.append(forward)
        # Inverse-loop identities are checked over the integers, block by block.
        assert np.array_equal(exact_product(readout, sigma), cap_common * sd * q[:, selected])
        assert np.array_equal(exact_product(forward, cap), sigma_common * cd * child_q[:, selected])
    readout_num = np.concatenate(readout_blocks, axis=1)
    forward_num = np.concatenate(forward_blocks, axis=1)
    # alpha R = beta q_t, expressed with positive integer denominators.
    assert np.array_equal(
        child_den * exact_product(alpha_num, readout_num),
        parent_den * cap_common * exact_product(child_res, child_q),
    )
    base.log("direct cap construction and both encode/decode identities passed")

    child_grades = np.tile(base.grades(5), 6)
    source_grades = np.repeat(np.tile(base.grades(4), 6), 3) ^ np.tile(np.arange(1, 4), 1944)
    assert graded_rank(child_q, child_grades)[0] == 444
    assert graded_rank(readout_num, child_grades)[0] == 444
    assert graded_rank(np.concatenate([q, forward_num]), source_grades)[0] == 876

    obstruction = exact_product(readout_num, child_d)
    assert base.iszero(exact_product(alpha_num, obstruction))
    for prime in PRIMES:
        assert len(base.rref(obstruction, prime)[1]) == 432
    # Rank 12 of alpha supplies the exact rational upper bound 444-12.
    profiles = [{"channels": [], "readout_obstruction_rank": 0, "minimal_child_dimension": 444}]
    for size in range(1, 4):
        for channels in combinations(range(3), size):
            rows = np.array([3*h+a for h in range(148) for a in channels])
            selected_obstruction = obstruction[rows]
            annihilator = np.kron(parent_res, np.eye(size, dtype=np.int64))
            assert base.iszero(exact_product(annihilator, selected_obstruction))
            # Annihilator has rank 4*size; modular minors attain the bound.
            expected = 144 * size
            for prime in PRIMES:
                assert len(base.rref(selected_obstruction, prime)[1]) == expected
            total_rank, grade_ranks = certify_joint_rank(child_q, readout_num[rows], child_grades, expected)
            assert total_rank == 444 + expected
            profiles.append({"channels": ["ijk"[a] for a in channels],
                             "readout_obstruction_rank": expected,
                             "minimal_child_dimension": total_rank,
                             "joint_rank_by_quaternion_grade": grade_ranks})
            base.log("readout profile certified", ["ijk"[a] for a in channels], total_rank)

    # Compatible-pair realization of the full child refinement.
    child_joint = np.concatenate([child_q, readout_num])
    constraint = np.concatenate([-parent_den * cap_common * child_res, child_den * alpha_num], axis=1)
    assert base.certified_rank(constraint) == 12
    assert base.iszero(exact_product(constraint, child_joint))
    assert certify_joint_rank(child_q, readout_num, child_grades, 432)[0] == child_joint.shape[0] - 12 == 876

    row, col = map(int, np.argwhere(obstruction != 0)[0])
    delta = child_d[:, col:col+1]
    readout_delta = exact_product(readout_num, delta)
    assert base.iszero(exact_product(child_q, delta))
    assert not base.iszero(readout_delta)
    assert base.iszero(exact_product(alpha_num, readout_delta))
    assert int(readout_delta[row, 0]) == int(obstruction[row, col])

    here = Path(__file__).resolve()
    sources = [here, Path(base.__file__).resolve(),
               base.HERE / "n8_222_minimal_refinement_certificate.py",
               base.HERE / "n8_222_exact_backend.cpp"]
    result = {
        "base_commit": BASE_COMMIT,
        "field": "Q and R: exact integer identities and certified rational ranks",
        "primes": list(PRIMES),
        "sources_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "continuations": "central-probe i,j,k coefficient readouts from the existing right local decoder",
        "caps_built_from_probe_evaluations_before_inverse_check": True,
        "local_decoder_denominator": 2,
        "raw_cap_common_denominator": cap_common,
        "raw_suspension_common_denominator": sigma_common,
        "checked_central_probe_positions_zero_based": sorted(checked_positions),
        "raw_source_dimension": 5832,
        "coarse_child_dimension": 444,
        "readout_target_dimension": 444,
        "discarded_subspace_dimension": 432,
        "readout_rank_on_discarded_subspace": 432,
        "full_decoder_readout_descends_to_coarse_child": False,
        "channel_profiles": profiles,
        "minimum_full_retention_dimensions": 432,
        "refined_child_dimension": 876,
        "refined_source_dimension": 876,
        "refined_encode_decode_are_inverse": True,
        "all_alternating_encode_decode_loops_identity": True,
        "child_relation_witness": {
            "matching_column": col,
            "nonzero_readout_row": row,
            "coefficient_channel": "ijk"[row % 3],
            "readout_numerator": int(readout_delta[row, 0]),
            "readout_denominator": cap_common,
            "raw_relation_nonzero_coordinates": [[int(i), int(delta[i, 0])] for i in np.flatnonzero(delta[:, 0])],
            "coarse_child_zero": True,
            "decoder_readout_nonzero": True,
            "parent_residual_zero": True,
        },
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "scope": "Full recovery of the Note 27 update kernel for the specified local decoder readouts, using retained data. A forward-only next-spectator insertion atlas is a separate remaining target.",
        "all_checks_passed": True,
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if output:
        Path(output).write_text(rendered)
    print(rendered, end="", flush=True)
    base.log("ALL CHECKS PASSED")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output")
    args = parser.parse_args()
    certificate(args.output)
