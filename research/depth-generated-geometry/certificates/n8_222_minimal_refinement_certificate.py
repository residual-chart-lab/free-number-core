#!/usr/bin/env python3
"""Note 27: exact certificate for the specified central update refinement.

Reconstructs Note 26 operators; no result JSON is trusted as input.
Finite-field elimination is used only with exact identities/upper bounds
to certify rational ranks. No floating-point linear algebra is used.
"""
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import json
import platform
import time

import numpy as np
import scipy
from scipy import sparse

import n8_222_redetection_certificate as base

if not __debug__:
    raise RuntimeError("Certificate checks require assertions; do not use -O or -OO.")

BASE_COMMIT = "bf26e5f2681096b0a15549f0edebdcc452128705"
PRIMES = base.PRIMES


def exact_product(a, b):
    """Integer product with a conservative pre-multiplication overflow bound."""
    a, b = sparse.csr_matrix(a, dtype=np.int64), sparse.csr_matrix(b, dtype=np.int64)
    assert a.shape[1] == b.shape[0]
    max_a = max((abs(int(x)) for x in a.data), default=0)
    max_b = max((abs(int(x)) for x in b.data), default=0)
    assert a.shape[1] * max_a * max_b < 2**63
    return (a @ b).toarray()


def exact_row_factor(response, quotient):
    """Return (den, num) with num @ quotient == den * response over Z."""
    factors = []
    for prime in PRIMES:
        _, pivots = base.rref(quotient, prime)
        assert len(pivots) == quotient.shape[0]
        factors.append(response[:, pivots] @ base.inverse(quotient[:, pivots], prime) % prime)
    den, num = base.lift(*factors)
    assert np.array_equal(exact_product(num, quotient), den * response)
    return den, num


def graded_rank(matrix, column_grades):
    """Certify the full rational rank after verifying the exact grading split."""
    row_grades = []
    for row in matrix:
        grades = np.unique(column_grades[np.flatnonzero(row)])
        assert len(grades) <= 1
        row_grades.append(-1 if not len(grades) else int(grades[0]))
    row_grades = np.array(row_grades)
    ranks = []
    for grade in range(4):
        rows = np.flatnonzero(row_grades == grade)
        cols = np.flatnonzero(column_grades == grade)
        ranks.append(base.certified_rank(matrix[np.ix_(rows, cols)]))
    return sum(ranks), ranks


def continuation_check():
    """A one-step-invisible difference becomes visible after two operations.

    This is a negative control for interpreting one-step refinement as
    closure under every future continuation. All matrices are integers.
    """
    q = np.array([[1, 0, 0]], dtype=np.int64)
    j = np.array([[0, 1, 0], [0, 0, 1], [0, 0, 0]], dtype=np.int64)
    e3 = np.array([[0], [0], [1]], dtype=np.int64)
    qj = exact_product(q, j)
    qjj = exact_product(qj, j)
    assert base.iszero(exact_product(q, e3))
    assert base.iszero(exact_product(qj, e3))
    assert np.array_equal(exact_product(qjj, e3), np.ones((1, 1), dtype=np.int64))
    ranks = [base.certified_rank(np.concatenate([q, qj, qjj][:h])) for h in (1, 2, 3)]
    assert ranks == [1, 2, 3]
    return {"state_dimension": 3, "relation_dimensions_by_horizon": [3-r for r in ranks],
            "one_step_refinement_closed_under_continuation": False}


def certificate(output=None):
    started = time.monotonic()
    base.primitive_checks()
    parent, child = (1, 3, 4, 6), (1, 3, 5, 7)
    parent_q, parent_d = base.exact_quotient(7, parent)
    child_q, child_d = base.exact_quotient(8, child)
    assert parent_q.shape == (148, 1944)
    assert child_q.shape == (444, 5832)
    k, big_k = base.residual(4), base.residual(5)
    assert base.iszero(exact_product(k, parent_d))
    assert base.iszero(exact_product(big_k, child_d))
    assert base.certified_rank(k) == 4
    assert base.certified_rank(big_k) == 12
    parent_den, parent_res = exact_row_factor(k, parent_q)
    child_den, child_res = exact_row_factor(big_k, child_q)

    identity_v = np.eye(3, dtype=np.int64)
    q = np.kron(parent_q, identity_v)
    relations = sparse.kron(sparse.csr_matrix(parent_d), sparse.eye(3, dtype=np.int64), format="csr")
    assert base.iszero(exact_product(q, relations))
    theta = base.encoder(1)
    alpha_num = exact_product(theta, np.kron(parent_res, identity_v))
    assert base.certified_rank(alpha_num) == 12
    assert base.certified_rank(child_res) == 12

    edges = list(combinations(child, 2))
    suspensions = []
    invertibility_checked = set()
    for edge in edges:
        pos = [g for g in range(1, 8) if g not in edge].index(4)
        den, integer_sigma = base.exact_suspension(pos, "right")
        # exact_suspension checks encoder * integer_sigma == den * literal
        # suspension evaluation. A full-size modular minor proves invertibility.
        if pos not in invertibility_checked:
            for prime in PRIMES:
                assert len(base.rref(integer_sigma, prime)[1]) == 972
            invertibility_checked.add(pos)
        suspensions.append((den, integer_sigma))
    common = int(np.lcm.reduce([d for d, _ in suspensions]))
    blocks = []
    for ei, (den, integer_sigma) in enumerate(suspensions):
        scaled_sigma = (common // den) * integer_sigma
        child_slice = slice(972 * ei, 972 * (ei + 1))
        parent_slice = slice(324 * ei, 324 * (ei + 1))
        # Check the literal residual square, independently of quotient factors.
        lhs = exact_product(big_k[:, child_slice], scaled_sigma)
        rhs = common * exact_product(theta, np.kron(k[:, parent_slice], identity_v))
        assert np.array_equal(lhs, rhs)
        blocks.append(exact_product(child_q[:, child_slice], scaled_sigma))
    f_num = np.concatenate(blocks, axis=1)  # actual F = f_num / common
    assert f_num.shape == (444, 5832)
    base.log("literal suspension, invertibility and residual square certified")

    # C(q, common*F)=0 is the fiber-product constraint in integer coordinates.
    constraint = np.concatenate([common * child_den * alpha_num, -parent_den * child_res], axis=1)
    joint = np.concatenate([q, f_num], axis=0)
    assert constraint.shape == (12, 888)
    assert base.iszero(exact_product(constraint, joint))
    constraint_rank = base.certified_rank(constraint)
    assert constraint_rank == 12

    source_grades = np.repeat(np.tile(base.grades(4), 6), 3) ^ np.tile(np.arange(1, 4), 1944)
    parent_rank, _ = graded_rank(q, source_grades)
    update_rank, _ = graded_rank(f_num, source_grades)
    joint_rank, joint_grade_ranks = graded_rank(joint, source_grades)
    assert parent_rank == update_rank == 444
    assert joint_rank == joint.shape[0] - constraint_rank == 876
    assert joint_grade_ranks == [219] * 4
    base.log("joint state/output rank certified", joint_rank)

    obstruction = exact_product(f_num, relations)
    # Exact 12-dimensional annihilator gives the rational upper bound 432.
    assert base.iszero(exact_product(child_res, obstruction))
    for prime in PRIMES:
        assert len(base.rref(obstruction, prime)[1]) == 432
    obstruction_rank = 432
    assert joint_rank == parent_rank + obstruction_rank

    witness_row, witness_col = map(int, np.argwhere(obstruction != 0)[0])
    delta = relations[:, witness_col].toarray()
    delta_child = exact_product(f_num, delta)
    assert base.iszero(exact_product(q, delta))
    assert not base.iszero(delta_child)
    assert base.iszero(exact_product(child_res, delta_child))
    assert int(delta_child[witness_row, 0]) == int(obstruction[witness_row, witness_col])

    # A known outer edge spans the 432-dimensional core, so the obstruction
    # has exactly that image, not merely a subspace with a guessed dimension.
    outer_core_rank = base.certified_rank(child_q[:, :972])
    assert outer_core_rank == 432
    assert base.iszero(exact_product(child_res, child_q[:, :972]))

    original_relation_dimension = q.shape[1] - parent_rank
    safe_relation_dimension = q.shape[1] - joint_rank
    assert original_relation_dimension == 5388
    assert safe_relation_dimension == 4956
    assert original_relation_dimension - safe_relation_dimension == obstruction_rank
    assert joint_rank - update_rank == 432

    negative_control = continuation_check()
    here = Path(__file__).resolve()
    source_files = [here, Path(base.__file__).resolve(), base.HERE / "n8_222_exact_backend.cpp"]
    result = {
        "base_commit": BASE_COMMIT,
        "field": "Q and R: exact integer identities plus certified rational ranks",
        "primes": list(PRIMES),
        "operation": "Note 26 central-slot right decoder Sigma_4^R; tensor-extended over V",
        "sources_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files},
        "environment": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "raw_source_dimension": q.shape[1],
        "original_parent_dimension": parent_rank,
        "child_dimension": update_rank,
        "original_relation_dimension": original_relation_dimension,
        "safe_relation_dimension": safe_relation_dimension,
        "obstruction_rank": obstruction_rank,
        "minimum_additional_linear_dimensions": obstruction_rank,
        "refined_dimension": joint_rank,
        "joint_rank_by_quaternion_grade": joint_grade_ranks,
        "common_residual_dimension": constraint_rank,
        "fiber_product_ambient_dimension": joint.shape[0],
        "fiber_product_constraint_rank": constraint_rank,
        "fiber_product_constraint_times_joint_map_is_zero": True,
        "joint_image_equals_fiber_product": True,
        "parent_projection_kernel_dimension": joint_rank - parent_rank,
        "update_kernel_dimension": joint_rank - update_rank,
        "joint_parent_and_update_kernel_dimension": 0,
        "update_surjective": True,
        "update_injective": False,
        "residual_preserved": True,
        "operation_common_denominator": common,
        "old_relation_witness": {
            "relation_column": witness_col,
            "nonzero_child_row": witness_row,
            "scaled_child_value": int(delta_child[witness_row, 0]),
            "raw_relation_nonzero_coordinates": [[int(i), int(delta[i, 0])] for i in np.flatnonzero(delta[:, 0])],
            "parent_output_zero": True,
            "child_output_nonzero": True,
            "child_residual_zero": True,
        },
        "continuation_negative_control": negative_control,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "claim_boundary": "Coarsest linear source refinement for fixed q and Sigma_4^R full child output. The 876-to-444 update still loses a 432-dimensional subspace. No decoder-independent operation, lossless full update, time law, or backward causal force is proved.",
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
