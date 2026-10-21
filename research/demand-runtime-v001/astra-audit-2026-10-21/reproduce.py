"""Reproduce three runtime-boundary findings without modifying the runtime.

Run from any directory. Prints observations as JSON, not an approval result.
After repair the expected outcomes are documented in REVIEW.md.
"""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'runtime'))
from free_numbers import Vault, Scope, Query, Policy, constant, plan, evaluate
from free_numbers.checkpoint import dumps, loads


def outcome(call):
    try:
        value = call()
        return dict(returned=True, **value)
    except Exception as exc:
        return dict(returned=False, exception=type(exc).__name__, message=str(exc))


def run():
    # A writer can return a valid digest for a file rejected by its own reader.
    archive = Vault()
    for i in range(10001):
        archive.register(str(i), 0, (0, 0), 'origin')
    raw, digest = dumps((constant((1, 0, 0, 0)),), archive)
    def reload():
        roots, restored = loads(raw, digest)
        return dict(roots=len(roots), retained=len(restored._records()))
    checkpoint = dict(retained=10001, roots=1, bytes=len(raw), writer_returned=True,
                      digest_matches=hashlib.sha256(raw).hexdigest() == digest,
                      reader=outcome(reload))

    # The expression is well inside max_nodes; observation depth is zero.
    one = constant((1, 0, 0, 0))
    chain = one
    for _ in range(1200):
        chain = chain + one
    query = Query(chain, Scope('audit', 'finite-addition-chain', 'exact'))
    def read_chain():
        c = evaluate(query, Vault())
        return dict(status=c.status, equals_expected=c.value == (1201, 0, 0, 0))
    def save_chain():
        payload, h = dumps((chain,), Vault())
        (restored,), v = loads(payload, h)
        return dict(root_digest_preserved=restored.digest == chain.digest)
    long_graph = dict(unique_nodes=1201, max_nodes=Policy().max_nodes,
        required_observation_depth=0,
        deliberate_lower_budget=evaluate(query, Vault(), Policy(max_nodes=1000)).status,
        evaluation=outcome(read_chain), checkpoint=outcome(save_chain))

    # Small inputs and 16 shared nodes produce a single exact coefficient.
    power = constant((2, 0, 0, 0))
    for _ in range(15):
        power = power * power
    query = Query(power, Scope('audit', 'fifteen-squarings', 'exact'))
    p = plan(query, Vault())
    def read_power():
        c = evaluate(query, Vault())
        return dict(status=c.status, equals_expected=c.value == (2**32768, 0, 0, 0))
    big_integer = dict(unique_nodes=16, monomials=len(p.coefficients), plan_status=p.status,
        coefficient_bits=p.coefficients[0][1][0].numerator.bit_length(),
        evaluation=outcome(read_power))
    return dict(audited_commit='f7837c4e3a1fa3ef095da2bad59ae59ff10a9ea0',
        python=sys.version, recursion_limit=sys.getrecursionlimit(),
        integer_string_limit=getattr(sys, 'get_int_max_str_digits', lambda: None)(),
        checkpoint_writer_reader=checkpoint, long_expression=long_graph,
        exact_integer_serialization=big_integer)


if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2))
