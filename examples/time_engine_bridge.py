"""Optional integration check against the pinned, unchanged RR62 TE tree.

The core runtime never imports TE. This example adapts its small B2 boundary
readouts, then hands the resulting context to the existing exact TE executor.
It does not replace a TE source, decoder, occurrence receipt or upper demand.
"""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'runtime'))
from dataclasses import asdict
from fractions import Fraction as Q
from functools import reduce
from hashlib import sha1
import argparse,json
from free_numbers import *
from free_numbers.algebra import encode
from free_numbers.checkpoint import dumps,loads

AXES = ((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),(Q(0),Q(0),Q(1)))


def verify_te_tree(root):
    manifest = json.loads((ROOT/'research/demand-runtime-v001/TE-SOURCE.json').read_bytes())
    for path,wanted in manifest['blobs'].items():
        data = (root/path).read_bytes()
        got = sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if got != wanted:
            raise ValueError('the pinned TE input differs: '+path)
    return manifest


def kernel_observation(context):
    # join(X,Y) = sum_{c,d} Y_cd e_d A_2(X)(e_c).
    # This is an explicit observation adapter, not m2(X) or a new product law.
    return Observation(2,tuple(Channel((AXES[c],),Q(context[c][d]),BASIS[d+1])
        for c in range(3) for d in range(3) if context[c][d]))


def boundary_component(tensor,i,j):
    # This adapter is restricted to the authenticated symmetric trace-one TE
    # library. A2(X)(e_j) = (I-2X)e_j, hence X_ij=(delta_ij-R_i)/2.
    response = read(tensor,Observation(2,(Channel((AXES[j],)),)))
    return constant((Q(1,2),0,0,0)) * (constant((Q(i==j),0,0,0)) +
        constant((-1,0,0,0))*component(response,i+1))


def run(te_root):
    source = verify_te_tree(te_root)
    sys.path.insert(0,str(te_root/'integrations/inquiry'))
    import demand_filter as f
    import internal_port as port
    d,prior,te = f.d,f.prior,f.te
    inputs = json.loads((te_root/'integrations/inquiry/RR62-inputs.json').read_bytes())
    vault = Vault()
    local_rows,future_rows,port_rows,roots = [],[],[],[]
    chosen_delivery = None
    original_digests = []
    checks = []
    def check(name,ok,**detail):
        if not ok:
            raise AssertionError(name)
        checks.append(dict(name=name,passed=True,**detail))
    for mode in ('keep','erase','restore'):
        flight = prior.previous.begin(mode,1,0)
        original_digests.append((mode,flight.digest))
        head,geometry,axis,library = prior.data(flight)
        base = matrix_block(d.tensor(flight.pair.representative))
        direction = matrix_block(tuple(tuple(sum(v*op.source.endpoint[i][j] for v,op in zip(axis,library))
            for j in range(3)) for i in range(3)))
        value = retained(vault,mode,geometry.shift,(Q(-1,1024),Q(1,1024)),flight.digest,base,direction)
        y = flight.first.residue.internal_context
        current = read(value,kernel_observation(y))
        roots.append(current)
        q = Query(current,Scope(flight.digest,'current-flower','TE-kernel'))
        p,meter = plan(q,vault),Meter()
        result = evaluate(q,vault,meter=meter)
        check(mode+'_current_kernel_matches_without_exact_retained_read',
              result.value==flight.pair.original.kernel(y) and not p.dependencies and meter.exact_reads==0)
        local_rows.append(dict(mode=mode,dependencies=p.dependencies,value=result.value,meter=asdict(meter)))
        for frame in inputs['future_frames']:
            y = prior.diagonal(Q(frame['x']))
            expression = read(value,kernel_observation(y))
            q = Query(expression,Scope(flight.digest,'C='+frame['x'],'TE-kernel'))
            p,meter = plan(q,vault),Meter()
            result = evaluate(q,vault,meter=meter)
            if result.value != flight.pair.original.kernel(y):
                raise AssertionError('future B2 response differs from original exact TE kernel')
            future_rows.append(dict(mode=mode,x=frame['x'],dependencies=p.dependencies,
                                    exact_reads=meter.exact_reads,value=result.value))
        spec = te.pair.ConnectionSpec()
        for strength in (Q(0),spec.strength):
            cfg = te.pair.ConnectionSpec(strength=strength)
            leaves,positions,mass = port.leaf_view(flight)
            denominator = Q(len(leaves)*(len(leaves)+1),2)
            parts = tuple((value if k in positions else matrix_block(d.tensor(leaf))).scaled(Q(k)/denominator)
                          for k,leaf in enumerate(leaves,1))
            raw_tensor = reduce(lambda x,y:x+y,parts)
            anchor = te.pair.boundary_readout(flight.first.closed_engine.designated_head)
            expressions = tuple(constant((anchor[i][j]-strength*Q(i==j,3),0,0,0))+
                constant((strength,0,0,0))*boundary_component(raw_tensor,i,j)
                for i in range(3) for j in range(3))
            roots.extend(expressions)
            coordinates,dependencies = [],set()
            meter = Meter()
            for n,expression in enumerate(expressions):
                q = Query(expression,Scope(flight.digest,'RR53-strength='+str(strength),'next-context-'+str(n)))
                dependencies.update(plan(q,vault).dependencies)
                cert = evaluate(q,vault,meter=meter)
                if any(cert.value[1:]):
                    raise AssertionError('boundary readout must be a real coordinate')
                coordinates.append(cert.value[0])
            computed = tuple(tuple(coordinates[3*i:3*i+3]) for i in range(3))
            raw,wanted = te.pair.connection_context(flight.first,cfg)
            if computed != wanted:
                raise AssertionError('demand-directed next context differs from original RR53 connector')
            if not strength and dependencies:
                raise AssertionError('a disconnected port must not depend on a retained difference')
            port_rows.append(dict(mode=mode,strength=str(strength),dependencies=tuple(sorted(dependencies)),
                                  context=computed,meter=asdict(meter)))
            if mode=='keep' and strength==spec.strength:
                request = port.request_connection(flight,cfg)
                emitted = te.port.event(request.waiting,'rr53-terminal-residue-port-emitted')
                arrived = te.accept_context(emitted,computed)
                scope_ = d.Scope((computed,),entry='RR60-internally-arrived-kernel')
                exposure = port.probe.initiate(flight.pair,scope_)
                chosen_delivery = port.Delivery(request,raw,computed,arrived,exposure)
    check('42_future_context_reads_match_the_unchanged_exact_TE_operator',len(future_rows)==42)
    check('six_ordered_ports_match_RR53_including_zero_coupling_controls',len(port_rows)==6)
    check('same_current_response_needs_retained_data_at_the_next_port',
          all(not row['dependencies'] for row in local_rows) and
          all(bool(row['dependencies'])==bool(Q(row['strength'])) for row in port_rows))
    second,certificate = port.continue_one(chosen_delivery,branch=0,petal=0)
    first = chosen_delivery.flight.first
    check('the_context_computed_by_the_new_runtime_drives_a_real_second_flower',
          second.closed_engine.phase=='IDLE' and second.closed_engine.pending is None and
          second.closed_engine.events[:len(first.closed_engine.events)]==first.closed_engine.events and
          second.closed_engine.stock[:len(first.closed_engine.stock)]==first.closed_engine.stock and
          second.closure_error<second.tolerance/2,
          closure_error=str(second.closure_error),stock_before=len(first.closed_engine.stock),stock_after=len(second.closed_engine.stock))
    raw,h = dumps(roots,vault)
    restored,archive = loads(raw,h)
    check('all_TE_readout_roots_and_three_histories_survive_exact_restore',
          tuple(r.digest for r in restored)==tuple(r.digest for r in roots) and dumps(restored,archive)==(raw,h),
          roots=len(roots),bytes=len(raw),sha256=h)
    check('the_three_original_TE_histories_remain_unchanged',all(prior.previous.begin(mode,1,0).digest==digest
        for mode,digest in original_digests))
    return dict(schema='free-numbers-demand-runtime-TE-bridge-v1',TE_commit=source['commit'],
        TE_verified_blobs=len(source['blobs']),groups=len(checks),checks=checks,
        local_rows=local_rows,future_rows=future_rows,port_rows=port_rows,actual_second_flowers=1,
        source_authentication_and_TE_execution_excluded_from_read_counters=True,
        TE_sources_decoders_and_occurrence_certificates_unchanged=True,
        new_bundle_wide_future_requirement_derived=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--time-engine',type=Path,required=True)
    parser.add_argument('--output',type=Path,default=Path('.work/te-bridge.json'))
    args = parser.parse_args()
    result = run(args.time_engine.resolve())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_bytes((json.dumps(encode(result),ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    print(json.dumps({'groups':result['groups'],'passed':True,'actual_second_flowers':1,'output':str(args.output)}))
