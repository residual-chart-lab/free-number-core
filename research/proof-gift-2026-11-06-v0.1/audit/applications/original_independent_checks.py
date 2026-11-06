"""Astra audit: independent exact oracles and small boundary examples.

Run: python -I -B independent_checks.py --source SOURCE_ROOT --out NEW_JSON
SOURCE_ROOT is a checkout root containing the two fixed Ronnie submissions.
Only Python standard library is used; subject sources are imported unchanged.
"""
import argparse
import importlib.util
import json
import platform
import sys
from fractions import Fraction as F
from pathlib import Path

def mat(x): return [[F(v) for v in r] for r in x]
I=mat([[1,0,0],[0,1,0],[0,0,1]])
def tr(a): return sum(a[i][i] for i in range(3))
def tp(a): return [list(r) for r in zip(*a)]
def mm(a,b): return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def add(a,b): return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def sc(k,a): return [[k*x for x in r] for r in a]
def sub(a,b): return add(a,sc(-1,b))
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def outer(a,b): return [[x*y for y in b] for x in a]
def mv(a,v): return [dot(r,v) for r in a]
def conj(r,a): return mm(mm(r,a),tp(r))
def comm(a,b): return sub(mm(a,b),mm(b,a))
def norm2(a): return sum(x*x for r in a for x in r)
def cross(a,b): return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def skew(w):
    x,y,z=w
    return mat([[0,-z,y],[z,0,-x],[-y,x,0]])
def stf(a): return sub(sc(F(1,2),add(a,tp(a))),sc(tr(a)/3,I))
def res(n,a=F(1)): return sc(a,sub(outer(n,n),sc(F(1,3),I)))
def unit(u,v):
    u,v=F(u),F(v); d=1+u*u+v*v
    return [(1-u*u-v*v)/d,2*u/d,2*v/d]
def reflect(v): return sub(I,sc(2/dot(v,v),outer(v,v)))
def minimal_by_reflections(n,m):
    # Product of two plane reflections: maps n to sign-aligned m,
    # fixes the orthogonal complement of span(n,m). No response commutator.
    if dot(n,m)<0: m=[-x for x in m]
    return mm(reflect([x+y for x,y in zip(n,m)]),reflect(n))
def qm(a,b):
    # Explicit Hamilton multiplication, separate from both subject engines.
    w,x,y,z=a; W,X,Y,Z=b
    return (w*W-x*X-y*Y-z*Z,w*X+x*W+y*Z-z*Y,
            w*Y-x*Z+y*W+z*X,w*Z+x*Y-y*X+z*W)
def qc(q): return (q[0],-q[1],-q[2],-q[3])
E=[tuple(F(i==j+1) for i in range(4)) for j in range(3)]
def insert(t,c):
    ans=[F(0)]*4
    for i in range(3):
        for j in range(3):
            v=qm(qm(E[j],c),E[i])
            ans=[x+t[i][j]*y for x,y in zip(ans,v)]
    return tuple(ans)
def adj(q,v): return qm(qm(q,(F(0),*v)),qc(q))[1:]
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
def pack(v):
    if isinstance(v,F): return str(v)
    if isinstance(v,dict): return {k:pack(x) for k,x in v.items()}
    if isinstance(v,(list,tuple)): return [pack(x) for x in v]
    return v

def run(root):
    base=root/'10_ARTIFACTS/magnetic-needle/submissions/ronnie'
    A=load('subject_a',base/'2026-11-05-kk-fn-v0.1/study/model.py')
    B=load('subject_b',base/'2026-11-05-generated-connection-v0.1/study/model.py')
    b=sys.modules['b2']; checks={}; evidence={}
    def ck(name,value):
        checks[name]=bool(value)
        if not value: raise AssertionError(name)
    # All nine tensor basis elements, four quaternion probe basis elements.
    basis=[mat([[int(i==r and j==c) for j in range(3)] for i in range(3)]) for r in range(3) for c in range(3)]
    qbasis=[(F(1),F(0),F(0),F(0)),*E]
    core=[]
    for t in basis:
        value=insert(t,qbasis[0]);s=stf(t)
        core += [A.compression(t)==b.compression(t)==value,
                 A.add(A.value_lift(value),A.residual(t))==t,
                 A.residual(t)==b.residual(t)==s]
        for c in qbasis: core.append(A.insertion(t,c)==insert(t,c))
        for j,c in enumerate(E): core.append(insert(s,c)==(F(0),*[-2*s[i][j] for i in range(3)]))
    ck('core_all_9_basis_compression_splitting_36_insertions_and_response',all(core))
    d=mat([[1,0,0],[0,-1,0],[0,0,0]]); e=mat([[0,1,0],[1,0,0],[0,0,0]])
    k=comm(sc(-2,e),sc(-2,d))
    ck('commutator_sign_and_antisymmetric_compression',k==sc(8,skew([0,0,1])) and b.compression(sc(F(1,2),k))==(0,0,0,8))
    # Independent finite-step oracle; varying signs/amplitudes and non-flat references.
    rows=[]
    for j in range(1,25):
        n=unit(F(j,31),F(j-7,29));m=unit(F(2-j,23),F(j+3,37))
        s,t=res(n,F((-1)**j*(j+1),7)),res(m,F((-1)**(j+1)*(j+2),11))
        r,_=B.generated_link(s,t);expected=minimal_by_reflections(n,m)
        ck('B_reflection_oracle_'+str(j),r==expected)
        g=minimal_by_reflections(unit(0,0),unit(F(j,19),F(1,3)))
        h=minimal_by_reflections(unit(0,0),unit(F(1,5),F(j,17)))
        ref=minimal_by_reflections(unit(0,0),unit(F(2,7),F(j,41)))
        rr,_=B.generated_link(s,t,ref)
        ref_expected=mm(minimal_by_reflections(mv(ref,n),m),ref)
        newref=mm(mm(h,ref),tp(g))
        transformed,_=B.generated_link(conj(g,s),conj(h,t),newref)
        ck('B_nontrivial_reference_and_independent_frames_'+str(j),rr==ref_expected and transformed==mm(mm(h,rr),tp(g)))
        # Variable amplitude derivative must cancel. Independent angular vector oracle.
        raw=[F(2*j,13),F(1-j,17),F(3,7)]
        v=[x-dot(raw,n)*y for x,y in zip(raw,n)]
        p=outer(n,n);dp=add(outer(v,n),outer(n,v));a=F(j+2,5);adot=F(3-j,11)
        ds=add(sc(adot,sub(p,sc(F(1,3),I))),sc(a,dp))
        omega=sc(1/(a*a),comm(ds,res(n,a)));w=skew(cross(n,v));z=skew(n)
        ck('B_continuous_generator_and_norm_'+str(j),omega==w and comm(omega,p)==dp and
           all(comm(add(omega,sc(lam,z)),p)==dp and norm2(add(omega,sc(lam,z)))==norm2(omega)+lam*lam*norm2(z) for lam in [F(-7,3),F(0),F(5,2)]))
        rows.append({'trial':j,'R':r,'Omega':omega})
    evidence['exact_corpus']=rows
    # Independent quaternion path and readout from stored graph, not graph generator.
    graph=json.loads((base/'2026-11-05-kk-fn-v0.1/study/run/CONNECTION.json').read_text())
    links={(x['from'],x['to']):tuple(map(F,x['U'])) for x in graph['directed_links']}
    def hol(path):
        acc=(F(1),F(0),F(0),F(0))
        for x,y in zip(path,path[1:]): acc=qm(links[x,y],acc)
        return acc
    hx,hy=hol(graph['loops']['x']),hol(graph['loops']['y']); c=(F(3,5),F(4,5),F(0),F(0))
    ux,uy=qm(qm(hx,c),hx),qm(qm(hy,c),hy)
    ck('A_independent_graph_holonomy_midpoint_and_suffix',qm(hx,hx)==qm(hy,hy)==(-1,0,0,0) and
       adj(ux,[0,1,0])[2]==F(24,25) and adj(uy,[0,1,0])[2]==F(-24,25) and qm(c,qm(hx,hx))==qm(c,qm(hy,hy)))
    # New A pair: i|i versus k|k, a different common probe and readout.
    c2=(F(5,13),F(12,13),F(0),F(0)); tx,tz=basis[0],basis[8]
    vals=[adj(insert(t,c2),[0,1,0])[2] for t in [tx,tz]]
    ck('A_new_pair_same_value_different_intervention',A.compression(tx)==A.compression(tz) and vals==[F(120,169),F(-120,169)])
    evidence['A_new_pair']={'probe':c2,'readouts':vals}
    # New indistinguishability example: tensors have different S but a commuting probe cannot detect it.
    cz=(F(3,5),F(0),F(0),F(4,5))
    ck('A_one_probe_is_not_complete',insert(basis[0],cz)==insert(basis[4],cz) and stf(basis[0])!=stf(basis[4]))
    # Arithmetic domain counterexample: entirely rational, valid uniaxial endpoint matrices.
    p=mat([[1,0,0],[0,0,0],[0,0,0]]); q=mat([[F(1,2),F(1,2),0],[F(1,2),F(1,2),0],[0,0,0]])
    s=sub(p,sc(F(1,3),I));t=sub(q,sc(F(1,3),I))
    try: B.generated_link(s,t); err=None
    except Exception as exc: err={'type':type(exc).__name__,'message':str(exc)}
    ck('B_valid_uniaxial_nonorthogonal_pair_hits_arithmetic_limit',B.line_projector(s)[1]==B.line_projector(t)[1]==1 and tr(mm(q,p))==F(1,2) and err is not None and err['type']=='ArithmeticError')
    evidence['B_rational_domain_counterexample']={'P':p,'Q':q,'overlap_squared':F(1,2),'observed_error':err,'geometry':'Unique 45 degree minimal rotation exists over the reals; this is not geometrical underdetermination.'}
    # Closed noncontractible RP2 loop: line returns while a continuous oriented lift changes sign.
    axes=[[F(1),F(0),F(0)],[F(3,5),F(4,5),F(0)],[F(-3,5),F(4,5),F(0)],[F(-1),F(0),F(0)]]
    total=I
    for n,m in zip(axes,axes[1:]):
        step,_=B.generated_link(res(n),res(m));total=mm(step,total)
    ck('B_closed_line_loop_need_not_fix_oriented_axis',res(axes[0])==res(axes[-1]) and total==mat([[-1,0,0],[0,-1,0],[0,0,1]]))
    evidence['B_noncontractible_line_loop']={'axes_for_audit_only':axes,'holonomy':total,'meaning':'Returning projector allows R n=-n, not just rotations around oriented n; this does not contradict the submitted contractible triangle.'}
    # Stronger endpoint stabilizer example: even a simple spectrum has nontrivial stabilizers.
    s=d;h=mat([[-1,0,0],[0,-1,0],[0,0,1]])
    f=minimal_by_reflections(unit(0,0),unit(F(2,5),F(1,3)))
    ck('local_endpoint_obstruction_also_for_simple_spectrum',conj(h,s)==s and mm(h,f)!=f)
    evidence['simple_spectrum_stabilizer']={'S':s,'H':h,'invertible_F':f,'HF':mm(h,f)}
    # Readout distinction: rotate cargo alone versus the entire experimental arrangement.
    cargo=e;probe=[F(0),F(1),F(0)];analyzer=[F(1),F(0),F(0)]
    r=mat([[0,0,1],[0,1,0],[-1,0,0]])
    original=dot(analyzer,mv(sc(-2,cargo),probe))
    active=dot(analyzer,mv(sc(-2,conj(r,cargo)),probe))
    passive=dot(mv(r,analyzer),mv(sc(-2,conj(r,cargo)),mv(r,probe)))
    ck('B_active_difference_passive_invariance',original==passive and active!=original)
    evidence['active_vs_passive']={'original':original,'cargo_only_rotated':active,'whole_arrangement_transformed':passive}
    return {'status':'PASS','checks':checks,'count':len(checks),'evidence':pack(evidence),
            'environment':{'python':sys.version,'platform':platform.platform(),'arithmetic':'fractions.Fraction; exact equality'},
            'scope':'Finite independent checks and explicit boundary certificates; not exhaustive formal verification.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,required=True);parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); result=run(args.source.resolve())
    with args.out.open('x',encoding='utf-8') as out: json.dump(result,out,ensure_ascii=False,indent=2);out.write('\n')
    print(json.dumps({'status':result['status'],'checks':result['count'],'boundary_example':result['evidence']['B_rational_domain_counterexample']},ensure_ascii=False))
