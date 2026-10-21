"""Three strengthening demonstrations; standard library only.

Run with: python examples/strengthening_study.py --output .work/study.json
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'runtime'))
import argparse
from dataclasses import asdict
from fractions import Fraction as Q
import json
from free_numbers import *
from free_numbers.algebra import encode
from free_numbers.checkpoint import dumps,loads


def run():
    vault = Vault()
    e1,e2 = (Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0))
    s = matrix_block(((1,0,0),(0,-1,0),(0,0,0)))
    t = matrix_block(((0,1,0),(1,0,0),(0,0,0)))
    zero = block(2,())
    a = retained(vault,'alpha',Q(1,3),(-1,1),'retained-A',zero,s)
    b = retained(vault,'beta',Q(2,5),(0,1),'retained-B',zero,t)
    checks = []
    def check(name,passed,**details):
        if not passed:
            raise AssertionError(name)
        checks.append(dict(name=name,passed=True,**details))
    local_scope = Scope('entry-A','one-factor','compression')
    local = assess_replacement(read(a),read(zero),local_scope,vault)
    check('compression_skips_a_retained_nonzero_difference',local.status=='REPLACEABLE_IN_SCOPE')
    deep = Observation(4,(Channel((e1,None,e1)),))
    pair_read = read(a.then(b),deep)
    pair_scope = Scope('entry-A','ordered-pair','cross-boundary-D13')
    demand = plan(Query(pair_read,pair_scope),vault)
    meter = Meter()
    result = evaluate(Query(pair_read,pair_scope),vault,meter=meter)
    check('coupled_demand_finds_the_mixed_residual_term',
          demand.dependencies==('alpha','beta') and demand.interacting_monomials==(('alpha','beta'),)
          and result.value==(0,0,0,Q(-8,15)),
          dependencies=demand.dependencies,monomials=demand.interacting_monomials,value=result.value)
    blind = []
    for gap in range(3):
        for basis in ((1,0,0),(0,1,0),(0,0,1)):
            gaps = tuple(basis if i==gap else None for i in range(3))
            r = read(a.then(b),Observation(4,(Channel(gaps),)))
            p = plan(Query(r,pair_scope),vault)
            blind.append(not p.dependencies and evaluate(Query(r,pair_scope),vault).value==ZERO)
    check('all_nine_depth_one_basis_channels_remain_blind',all(blind),channels=len(blind))
    low_depth = evaluate(Query(pair_read,pair_scope),vault,Policy(max_depth=1,precisions=(1024,)))
    check('extra_bits_cannot_replace_a_missing_response_depth',low_depth.status=='UNDETERMINED_DEPTH_BUDGET')
    observed = read(a,Observation(2,(Channel((e1,)),)))
    broad_meter = Meter()
    broad = evaluate(Query(observed,local_scope,'within-l1',ZERO,Q(3)),vault,meter=broad_meter)
    check('a_predicate_can_skip_values_needed_by_an_exact_action_read',
          broad.decision is True and broad.value is None and broad_meter.exact_reads==0
          and meter.exact_reads==2,
          predicate_meter=asdict(broad_meter),exact_read_meter=asdict(meter))
    precise_meter = Meter()
    precise = evaluate(Query(observed,local_scope,'within-l1',(0,Q(-2,3),0,0),Q(1,10**12)),vault,
                       Policy(max_depth=1,precisions=(4,16,48),exact_fallback=False),precise_meter)
    check('requested_precision_increases_independently_of_response_depth',
          precise.decision is True and precise.stages[-1].bits==48 and precise_meter.exact_reads==0,
          final_bits=precise.stages[-1].bits,requested_depth=1,meter=asdict(precise_meter))
    raw,digest = dumps((read(a),pair_read),vault)
    (restored_local,restored_pair),archive = loads(raw,digest)
    later = evaluate(Query(restored_pair,pair_scope),archive)
    check('lossless_checkpoint_preserves_dormant_values_and_order',later==result
          and dumps((restored_local,restored_pair),archive)==(raw,digest),bytes=len(raw),sha256=digest)
    shared = matrix_block(((Q(1,3),0,0),(0,Q(1,3),0),(0,0,Q(1,3))))
    for _ in range(6):
        shared = shared.then(shared)
    shared_meter = Meter()
    shared_result = evaluate(Query(read(shared),local_scope),Vault(),Policy(max_depth=0),shared_meter)
    check('grade_128_reuses_seven_tensor_nodes_instead_of_dense_response_coordinates',
          shared_result.value==ONE and shared_meter.compiled_tensor_slices==7,
          grade=128,dense_coordinate_dimension=str(3**128),tensor_slices=shared_meter.compiled_tensor_slices)
    try:
        verify_certificate(Query(restored_pair,Scope('entry-A','different-pair','cross-boundary-D13')),archive,result)
        rejected = False
    except ValueError:
        rejected = True
    check('a_certificate_is_not_reused_in_a_new_scope',rejected)
    return dict(schema='free-numbers-demand-runtime-study-v1',checks=checks,groups=len(checks),
                runtime_is_a_core_extension=True,core_release_changed=False,
                response_depth_is_not_flower_count=True,global_speedup_claimed=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,default=Path('.work/study.json'))
    args = parser.parse_args()
    result = run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes((json.dumps(encode(result),ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    print(json.dumps({'groups':result['groups'],'passed':True,'output':str(args.output)}))
