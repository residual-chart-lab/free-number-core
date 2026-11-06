"""Generate a conditional connection from B2 residual-response data.

Exact-rational construction plus obstruction certificates. An ambient frame and
minimum-twist rule are explicit extra inputs; do not call this unique Core law.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import argparse
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from b2 import (matrix, identity, zero, add, sub, scale, transpose, mul, trace,
                outer, determinant, rotate_tensor, apply, residual, compression,
                response, frobenius2, exact_sqrt, frame, packed, comm)

HERE = Path(__file__).resolve().parent
I = identity()


class Underdetermined(ValueError):
    pass


def line_projector(s):
    if s != transpose(s) or trace(s) != 0:
        raise Underdetermined("NOT_A_RESIDUAL")
    invariant2, invariant3 = trace(mul(s, s)), trace(mul(mul(s, s), s))
    if invariant2 == 0:
        raise Underdetermined("ZERO_RESIDUAL_HAS_NO_SELECTED_LINE")
    if invariant3 == 0 or 6 * invariant3 ** 2 != invariant2 ** 3:
        raise Underdetermined("OUTSIDE_TESTED_UNIAXIAL_FAMILY")
    amplitude = exact_sqrt(F(3,2) * invariant2)
    if invariant3 < 0:
        amplitude = -amplitude
    p = add(scale(1 / amplitude, s), scale(F(1,3), I))
    assert p == transpose(p) and mul(p, p) == p and trace(p) == 1
    return p, amplitude


def generated_link(source, target, reference=None):
    reference = I if reference is None else reference
    source_in_target_frame = rotate_tensor(reference, source)
    p, a = line_projector(source_in_target_frame)
    q, b = line_projector(target)
    overlap2 = F(1,3) + trace(mul(target, source_in_target_frame)) / (a * b)
    assert overlap2 == trace(mul(q, p)) and 0 <= overlap2 <= 1
    if overlap2 == 0:
        raise Underdetermined("ORTHOGONAL_STEP_NEEDS_PATH_REFINEMENT")
    cosine = exact_sqrt(overlap2)
    # This uses compositions of the unchanged Core response operators.
    response_commutator = comm(response(target), response(source_in_target_frame))
    projector_commutator = scale(1 / (4 * a * b), response_commutator)
    skew = scale(1 / cosine, projector_commutator)
    correction = add(add(I, skew), scale(1 / (1 + cosine), mul(skew, skew)))
    rotation = mul(correction, reference)
    assert mul(transpose(rotation), rotation) == I and determinant(rotation) == 1
    original_projector = line_projector(source)[0]
    assert rotate_tensor(rotation, original_projector) == q
    return rotation, {"overlap_cosine": cosine, "response_commutator": response_commutator,
                      "rotation": rotation, "source_amplitude": a, "target_amplitude": b}


def direct_axis_check(p, q):
    # Independent conventional Rodrigues formula, using recovered axes only here.
    def axis(projector):
        k = next(k for k in range(3) if projector[k][k] > 0)
        denom = exact_sqrt(projector[k][k])
        return tuple(projector[i][k] / denom for i in range(3))
    n, m = axis(p), axis(q)
    dot = sum(a * b for a, b in zip(n, m))
    if dot < 0:
        m = tuple(-x for x in m)
        dot = -dot
    cross = (n[1]*m[2]-n[2]*m[1], n[2]*m[0]-n[0]*m[2], n[0]*m[1]-n[1]*m[0])
    vx, vy, vz = cross
    k = matrix([[0,-vz,vy],[vz,0,-vx],[-vy,vx,0]])
    return add(add(I, k), scale(1 / (1 + dot), mul(k, k)))


def transport_path(tensors, cargo, references=None):
    sources = [residual(t) for t in tensors]
    total, steps, history = I, [], []
    for i in range(len(sources) - 1):
        reference = None if references is None else references[i]
        r, record = generated_link(sources[i], sources[i+1], reference)
        total = mul(r, total)
        steps.append(record)
        history.append({"step": i, "driver_value": compression(tensors[i+1]),
                        "carried_residual": rotate_tensor(total, cargo)})
    return total, steps, history


def rank(rows):
    rows = [[F(x) for x in row] for row in rows]
    pivot = 0
    for column in range(len(rows[0])):
        choice = next((i for i in range(pivot, len(rows)) if rows[i][column]), None)
        if choice is None:
            continue
        rows[pivot], rows[choice] = rows[choice], rows[pivot]
        scale0 = rows[pivot][column]
        rows[pivot] = [x / scale0 for x in rows[pivot]]
        for i in range(len(rows)):
            if i != pivot:
                fac = rows[i][column]
                rows[i] = [x - fac*y for x,y in zip(rows[i],rows[pivot])]
        pivot += 1
        if pivot == len(rows):
            break
    return pivot


def run(out):
    protocol_bytes, input_bytes = (HERE/'PROTOCOL.json').read_bytes(), (HERE/'INPUT.json').read_bytes()
    protocol = json.loads(protocol_bytes)
    cases = {name: [matrix(t) for t in series] for name, series in json.loads(input_bytes)['cases'].items()}
    cargo, probe, analyzer = matrix(protocol['cargo']), tuple(map(F,protocol['probe'])), tuple(map(F,protocol['analyzer']))
    out.mkdir(parents=True,exist_ok=False)
    checks, records, holonomies = {}, {}, {}
    rx_plus = matrix([[1,0,0],[0,0,-1],[0,1,0]])
    rx_minus = transpose(rx_plus)
    for name, tensors in cases.items():
        h, steps, history = transport_path(tensors,cargo)
        holonomies[name] = h
        carried = rotate_tensor(h,cargo)
        measured = sum(a*b for a,b in zip(analyzer,apply(response(carried),probe)))
        records[name] = {'holonomy': h, 'steps': steps, 'history': history,
                         'driver_returns': tensors[0] == tensors[-1],
                         'driver_values': [compression(t) for t in tensors],
                         'cargo_final': carried, 'cargo_value': compression(carried),
                         'response': measured}
        checks[name+'_SO3'] = mul(transpose(h),h)==I and determinant(h)==1
        checks[name+'_cargo_stays_zero_valued'] = all(compression(row['carried_residual']) == (0,0,0,0) for row in history)
        checks[name+'_cargo_norm_preserved'] = frobenius2(carried)==frobenius2(cargo)
    checks['forward_quarter_turn'] = holonomies['forward_triangle']==rx_plus
    checks['reverse_quarter_turn'] = holonomies['reverse_triangle']==rx_minus
    checks['opposite_zero_value_cargo_response'] = (records['forward_triangle']['response'],records['reverse_triangle']['response']) == (F(-2),F(2))
    checks['source_returns_but_cargo_changes'] = records['forward_triangle']['driver_returns'] and records['forward_triangle']['cargo_final'] != cargo
    checks['backtrack_identity'] = holonomies['backtrack']==I
    checks['same_arcs_other_subdivision'] = holonomies['other_subdivision']==rx_plus
    checks['amplitude_does_not_choose_rotation'] = holonomies['varying_amplitude']==holonomies['negative_amplitude']==rx_plus
    checks['amplitude_only_no_geometric_rotation'] = holonomies['constant_axis']==I
    checks['axis_sign_not_hidden_input'] = cases['sign_flipped_directions']==cases['forward_triangle'] and holonomies['sign_flipped_directions']==rx_plus
    checks['repeated_sample_invariant'] = holonomies['repeated_sample']==rx_plus
    checks['opposite_refinements_resolve_orthogonal_pair_differently'] = holonomies['arc_upper'] != holonomies['arc_lower'] and cases['arc_upper'][0] == cases['arc_lower'][0] and cases['arc_upper'][-1] == cases['arc_lower'][-1]
    independent_steps=[]
    series=cases['forward_triangle']
    for i in range(len(series)-1):
        r,_=generated_link(residual(series[i]),residual(series[i+1]))
        independent_steps.append(r==direct_axis_check(line_projector(residual(series[i]))[0],line_projector(residual(series[i+1]))[0]))
    checks['independent_axis_Rodrigues_comparison']=all(independent_steps)
    rejected={}
    for name,s,t in [
        ('zero_residual',zero(),residual(series[0])),
        ('orthogonal_pair',residual(series[0]),residual(series[2])),
        ('generic_triaxial',matrix([[1,0,0],[0,0,0],[0,0,-1]]),residual(series[0]))]:
        try:
            generated_link(s,t)
            rejected[name]='UNEXPECTEDLY_ACCEPTED'
        except Underdetermined as error:
            rejected[name]=str(error)
    checks['underdetermined_inputs_are_explicit']=all(v!='UNEXPECTEDLY_ACCEPTED' for v in rejected.values())
    # Minimum-norm generator, and an explicit family left free by compatibility.
    p=line_projector(residual(series[0]))[0]
    dp=matrix([[0,1,0],[1,0,0],[0,0,0]])
    omega=comm(dp,p)
    twist=matrix([[0,0,0],[0,0,-1],[0,1,0]])
    checks['minimal_generator_transports_projector']=comm(omega,p)==dp
    checks['minimum_twist_norm_decomposition']=all(comm(add(omega,scale(lam,twist)),p)==dp and frobenius2(add(omega,scale(lam,twist)))==frobenius2(omega)+lam*lam*frobenius2(twist) for lam in [F(-3,2),F(-1,2),F(0),F(1,2),F(3,2)])
    s=residual(series[0]);chosen,_=generated_link(s,s)
    checks['compatibility_does_not_fix_transport']=chosen==I and rotate_tensor(rx_plus,s)==s and rx_plus!=chosen
    minimum_cargo_readout=sum(a*b for a,b in zip(analyzer,apply(response(cargo),probe)))
    twisted_cargo_readout=sum(a*b for a,b in zip(analyzer,apply(response(rotate_tensor(rx_plus,cargo)),probe)))
    checks['same_driver_allows_different_cargo_if_twist_not_fixed']=(minimum_cargo_readout,twisted_cargo_readout)==(F(0),F(-2))
    # Local endpoint data can remain identical under a nontrivial endpoint stabilizer.
    local_without_reference,_=generated_link(s,rotate_tensor(rx_plus,s))
    checks['local_gauge_obstruction_without_reference']=local_without_reference != mul(rx_plus,chosen)
    # All three skew directions occur among commutators of the five Core responses.
    basis=[matrix(x) for x in [[[1,0,0],[0,-1,0],[0,0,0]],[[0,0,0],[0,1,0],[0,0,-1]],[[0,1,0],[1,0,0],[0,0,0]],[[0,0,1],[0,0,0],[1,0,0]],[[0,0,0],[0,0,1],[0,1,0]]]]
    commutators=[comm(response(basis[j]),response(basis[i])) for i in range(5) for j in range(i+1,5)]
    dimension=rank([[c[0][1],c[0][2],c[1][2]] for c in commutators])
    checks['response_commutators_skew']=all(c==scale(-1,transpose(c)) for c in commutators)
    checks['response_commutators_span_so3']=dimension==3
    gauge_records=[]
    for trial in range(protocol['gauge_trials']):
        g=frame(F(trial+1,7),F(trial-2,9),F(trial+3,11))
        global_series=[rotate_tensor(g,t) for t in series]
        transformed,_,_=transport_path(global_series,rotate_tensor(g,cargo))
        checks['global_frame_'+str(trial)]=transformed==rotate_tensor(g,rx_plus)
        frames=[frame(F(trial+i+1,13),F(trial-i,17),F(i+2,19)) for i in range(len(series))]
        frames[-1]=frames[0]
        local_series=[rotate_tensor(g,t) for g,t in zip(frames,series)]
        references=[mul(frames[i+1],transpose(frames[i])) for i in range(len(series)-1)]
        local_h,local_steps,_=transport_path(local_series,rotate_tensor(frames[0],cargo),references)
        expected=rotate_tensor(frames[0],rx_plus)
        predicates=[local_h==expected]
        for i,step in enumerate(local_steps):
            raw=records['forward_triangle']['steps'][i]['rotation']
            predicates.append(step['rotation']==mul(mul(frames[i+1],raw),transpose(frames[i])))
        checks['local_frames_with_reference_'+str(trial)]=all(predicates)
        gauge_records.append({'trial':trial,'local_frame_equalities':len(predicates),'all_pass':all(predicates)})
    certificates={
        'cases':records,'rejected':rejected,'generator':{'P':p,'dP':dp,'minimum_omega':omega,'free_twist':twist},
        'nonuniqueness':{'same_residual':s,'minimal_link':I,'another_compatible_link':rx_plus,'minimum_cargo_response':minimum_cargo_readout,'compatible_twisted_cargo_response':twisted_cargo_readout},
        'local_frame_obstruction':{'source_and_target_residual':s,'target_frame_stabilizer':rx_plus,'generated_without_reference':local_without_reference,'required_covariant_link':rx_plus},
        'response_commutator_span_dimension':dimension,'response_commutators':commutators}
    results={'id':protocol['id'],'status':'PASS' if all(checks.values()) else 'FAIL',
             'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
             'algebra_sha256':sha256((HERE/'b2.py').read_bytes()).hexdigest(),
             'protocol_sha256':sha256(protocol_bytes).hexdigest(),'input_sha256':sha256(input_bytes).hexdigest(),
             'runtime':{'python':sys.version,'arithmetic':'Fraction; exact equalities'},'checks':checks,'gauge_trials':gauge_records,
             'summary':{'response_commutators_span_dimension':dimension,'forward_cargo_response':str(records['forward_triangle']['response']),'reverse_cargo_response':str(records['reverse_triangle']['response']),'conditional_generation':True,'unique_transport_from_Core_alone':False,'local_covariance_without_reference':False,'local_covariance_with_reference':True},
             'generation_inputs':protocol['additional_choices'],'independent_audit':False,'Core_modified':False,'scope':protocol['scope']}
    for name,data in [('RESULTS.json',results),('EXACT_CERTIFICATE.json',packed(certificates))]:
        (out/name).write_bytes((json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    print(json.dumps({'status':results['status'],'checks':len(checks),'failed':[n for n,v in checks.items() if not v],'summary':results['summary'],'rejected':rejected},indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    run(parser.parse_args().out)
