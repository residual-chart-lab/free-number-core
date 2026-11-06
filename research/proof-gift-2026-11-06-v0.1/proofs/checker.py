"""Exact finite regression checks for the accompanying general written proofs.

The finite corpus is not advertised as a proof of the quantified theorems.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from exact import *
from itertools import product
from hashlib import sha256
import argparse,json,platform

def stf(t):return sub(sc(F(1,2),add(t,tp(t))),sc(tr(t)/len(t),eye(len(t))))
def hat(w):x,y,z=w;return mat([[0,-z,y],[z,0,-x],[-y,x,0]])
def compression(t):
    q=(F(0),)*4
    for a in range(3):
        for b in range(3):q=qadd(q,qscale(t[a][b],qm(QB[b+1],QB[a+1])))
    return q
def insertion(t,c):
    q=(F(0),)*4
    for a in range(3):
        for b in range(3):q=qadd(q,qscale(t[a][b],qm(qm(QB[b+1],c),QB[a+1])))
    return q
def canonical_generator(s,d):
    a,da=sc(-2,s),sc(-2,d);js=basis_skew(len(s));b=axial(comm(da,a))
    cols=[axial(comm(comm(j,a),a)) for j in js];m=tp(cols)
    _,null,rank=rref(m,b,len(js))
    x,free,_=rref(m+null,b+[F(0)]*len(null),len(js));assert not free
    return lin(x,js),{'rank':rank,'kernel_dimension':len(null),'coefficients':x}
def star4(k):
    def eps(v):
        if len(set(v))<4:return 0
        return (-1)**sum(v[i]>v[j] for i in range(4) for j in range(i+1,4))
    return [[sum(F(eps((i,j,a,b)),2)*k[a][b] for a in range(4) for b in range(4)) for j in range(4)] for i in range(4)]
def spin(j):
    n=int(2*j);e=zero(n+1);f=zero(n+1)
    for k in range(n+1):
        if k:e[k-1][k]=k
        if k<n:f[k+1][k]=n-k
    return [sc(F(1,2),add(e,f)),sc(C(0,F(-1,2)),sub(e,f)),diag([j-k for k in range(n+1)])]
def quadratic(s,js):
    out=zero(len(js[0]))
    for a in range(3):
        for b in range(3):out=add(out,sc(s[a][b]/2,add(mm(js[a],js[b]),mm(js[b],js[a]))))
    return out
def real(x):return C.of(x).r

def run(root,out):
    checks={};cert={}
    def ck(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    # T01/T02: tensor basis, full quaternion probes and scalar-observation rank.
    tensors=[mat([[int(i==a and j==b) for j in range(3)] for i in range(3)]) for a in range(3) for b in range(3)]
    all_eq=True
    for t in tensors:
        q=compression(t);s=stf(t);lift=add(sc(-q[0]/3,eye(3)),sc(F(1,2),hat(q[1:])))
        all_eq &= add(lift,s)==t
        for c in QB:
            tt,v=c[0],c[1:];vec=[-q[0]*v[i]/3-2*dot(s[i],v) for i in range(3)]
            expected=qadd(qscale(tt,q),(dot(q[1:],v),*vec))
            all_eq &= insertion(t,c)==expected
    ck('T01_full_insertion_on_tensor_and_quaternion_bases',all_eq)
    sb=[diag([1,0,-1]),diag([0,1,-1]),add(tensors[1],tensors[3]),add(tensors[2],tensors[6]),add(tensors[5],tensors[7])]
    samples=[(0,0),(1,1),(0,1),(0,2),(1,2)]
    obs=[[-2*s[i][j] for s in sb] for i,j in samples]
    _,_,rk=rref(obs,[0]*5,5);ck('T02_five_probe_rank',rk==5)
    # T03: complete response Gram matrices and inverse at lengths 1..4.
    tomography=[]
    for m in range(1,5):
        words=list(product(range(4),repeat=m));probes=list(product(range(4),repeat=m-1));columns=[]
        for w in words:
            col=[]
            for p in probes:
                a=QB[w[0]]
                for k in range(1,m):a=qm(qm(QB[w[k]],QB[p[k-1]]),a)
                ix=next(i for i,x in enumerate(a) if x);col.append((ix,a[ix]))
            columns.append(col)
        factor=4**(m-1);ok=True
        for i,col in enumerate(columns):
            for j in range(i+1):
                value=sum(s*t for (a,s),(b,t) in zip(col,columns[j]) if a==b)
                if value!=(factor if i==j else 0):ok=False
        cs=[F(k%9-4,k%5+1) for k in range(len(words))];response=[F(0)]*(4*len(probes))
        for c,col in zip(cs,columns):
            for p,(a,s) in enumerate(col):response[4*p+a]+=c*s
        inverse_cs=[sum(s*response[4*p+a] for p,(a,s) in enumerate(col))/factor for col in columns]
        ck('T03_Gram_and_inverse_length_'+str(m),ok and inverse_cs==cs and dot(response,response)==factor*dot(cs,cs))
        tomography.append({'length':m,'tensor_dimension':4**m,'pure_imaginary_dimension':3**m,'quaternion_evaluations':len(probes),'Gram_factor':factor,'Gram_diagonal_and_inverse_exact':ok})
    cert['tomography']=tomography
    # T05/T07: generic dimensions, multiplicities, eigenvalue drifts and rotations.
    spectra=[[1,-1],[0,0],[1,0,-1],[2,-1,-1],[0,0,0],[3,1,-1,-3],[1,1,-1,-1],[3,-1,-1,-1],[2,2,-1,-1,-2]]
    spectral=[];spectral_ok=True;cov_ok=True;minimum_ok=True
    for vals in spectra:
        n=len(vals);js=basis_skew(n);d=diag(vals);g=mm(rotation(n,0,1),rotation(n,n-2,n-1,F(5,13),F(12,13)))
        k=lin([F(i+1,i+3) for i in range(len(js))],js)
        drift=diag([F(v+2,7) for v in vals]);deriv=add(comm(k,d),drift)
        expected=mat([[k[i][j] if vals[i]!=vals[j] else 0 for j in range(n)] for i in range(n)])
        omega,rec=canonical_generator(d,deriv);s,dd=conj(g,d),conj(g,deriv);om2,_=canonical_generator(s,dd)
        spectral_ok &= omega==expected and sub(deriv,comm(omega,d))==drift and comm(d,drift)==zero(n)
        cov_ok &= om2==conj(g,omega)
        ker=[j for j in js if comm(j,d)==zero(n)]
        for z in ker:minimum_ok &= norm2(add(omega,z))==norm2(omega)+norm2(z)
        spectral.append({'eigenvalues':vals,'dimension':n,**rec,'Omega':omega,'rotated_Omega':om2})
        # Independent Lie-span check with a simple-spectrum diagonal.
        simple=diag([F(2*i-(n-1)) for i in range(n)]);columns=[]
        for j in js:
            sym=mat([[abs(x) for x in r] for r in j]);columns.append(axial(comm(simple,sym)))
        _,_,rank=rref(tp(columns),[0]*len(js),len(js));ck('T05_Lie_span_dimension_'+str(n)+'_case_'+str(len(spectral)),rank==len(js))
    ck('T07_spectral_split_and_response_pseudoinverse',spectral_ok)
    ck('T07_common_frame_covariance',cov_ok);ck('T07_minimum_norm_decomposition',minimum_ok);cert['spectral_cases']=spectral
    # T08: exceptional extra data and dimension four are real counterexamples.
    p=diag([1,0,0]);q=sub(eye(3),p);exy=sb[2];eyz=sb[4];bad=add(exy,eyz)
    z=mm(mm(q,comm(bad,mm(mm(bad,p),bad))),q)
    ck('T08_multiplicity_splitting_jet_has_extra_covariant_twist',z!=zero(3) and comm(z,p)==zero(3) and mm(mm(q,bad),q)!=zero(3))
    p4=diag([1,0,0,0]);d4=zero(4);d4[0][1]=d4[1][0]=1;om4=comm(d4,p4);extra=star4(om4)
    g4=mm(rotation(4,0,2),rotation(4,1,3,F(5,13),F(12,13)))
    ck('T08_dimension4_Hodge_counterexample',extra!=zero(4) and comm(extra,p4)==zero(4) and comm(add(om4,extra),p4)==d4 and star4(conj(g4,om4))==conj(g4,extra))
    cert['uniqueness_boundaries']={'splitting_jet':bad,'extra_twist':z,'dimension4_Omega':om4,'dimension4_extra':extra}
    # T12: realizable jets converge to zero while their unique generators diverge.
    collisions=[]
    for r in [F(1),F(1,2),F(1,5),F(1,11)]:
        s=diag([r*r,-r*r,0]);d=sc(r,exy);om,_=canonical_generator(s,d)
        assert om==sc(1/(2*r),basis_skew(3)[0])
        collisions.append({'r':r,'input_norm_squared':norm2(s)+norm2(d),'generator_norm_squared':norm2(om)})
    ck('T12_collision_divergence_family',all(a['input_norm_squared']>b['input_norm_squared'] and a['generator_norm_squared']<b['generator_norm_squared'] for a,b in zip(collisions,collisions[1:])))
    cert['collision_family']=collisions
    # T13/T14: exact spin representation, rank and trace normalization for six spins.
    spins=[];all_spin=True;noether=True
    for j in [F(0),F(1,2),F(1),F(3,2),F(2),F(3)]:
        js=spin(j);dim=int(2*j+1);unit=eye(dim);cas=sum_matrix([mm(x,x) for x in js])
        all_spin &= cas==sc(j*(j+1),unit) and comm(js[0],js[1])==sc(C(0,1),js[2])
        ops=[quadratic(s,js) for s in sb];vecs=[]
        for op in ops:vecs.append([v for x in flat(op) for v in [C.of(x).r,C.of(x).i]])
        _,_,rank=rref(tp(vecs),[0]*(2*dim*dim),5)
        c=(2*j+1)*j*(j+1)*(4*j*(j+1)-3)/30
        for s,t,qs,qt in [(s,t,qs,qt) for s,qs in zip(sb,ops) for t,qt in zip(sb,ops)]:
            all_spin &= tr(mm(qs,qt))==c*tr(mm(s,t))
        all_spin &= rank==(0 if j<F(1) else 5)
        v=add(ops[0],sc(F(2,7),ops[2]));field=[F(1,3),F(-2,5),F(4,7)];zfield=lin([-b for b in field],js)
        h=add(v,zfield);dtheta=sc(C(0,1),comm(v,js[2]))
        noether &= add(sc(-1,dtheta),sc(C(0,1),comm(h,js[2])))==sc(C(0,1),comm(zfield,js[2]))
        noether &= sc(C(0,1),comm(zfield,js[2]))==sub(sc(field[1],js[0]),sc(field[0],js[1]))
        spins.append({'j':j,'dimension':dim,'residual_rank':rank,'trace_coefficient':c})
    ck('T13_all_six_spins_rank_and_bilinear_trace_identity',all_spin);ck('T14_Noether_operator_identity_all_spins',noether);cert['spin_cases']=spins
    # Norm and work cancellation use a genuinely Hermitian matrix in an orthonormal basis.
    psi=[C(F(2,3)),C(0,F(2,3)),C(F(1,3))];h=add(diag([1,-2,3]),sc(F(1,5),exy));ht=sc(F(2,3),sb[0]);hth=sc(F(5,7),sb[3])
    hp=mv(h,psi);psidot=[C(0,-1)*x for x in hp];expect=lambda a:sum(C.of(x).conjugate()*y for x,y in zip(psi,mv(a,psi)))
    inertia,momentum=F(3,2),F(5,7);theta_dot=momentum/inertia;ldot=-expect(hth)
    normdot=2*sum(C.of(x).conjugate()*y for x,y in zip(psi,psidot)).r
    state_term=2*sum(C.of(x).conjugate()*y for x,y in zip(psidot,hp)).r
    energy_dot=theta_dot*ldot+state_term+theta_dot*expect(hth)+expect(ht)
    ck('T14_exact_norm_and_energy_work_cancellation',normdot==0 and energy_dot==expect(ht))
    # T15 rescaling algebra with arbitrary positive rational scales.
    si=True
    for hbar,e0,ii in [(F(2,3),F(5,7),F(11,13)),(F(7,5),F(3,11),F(19,2))]:
        t0=hbar/e0;idim=ii*e0/hbar**2;ell=F(4,9)
        si &= t0*hbar*ell/ii==ell/idim and t0*e0/hbar==1
    ck('T15_arbitrary_positive_scale_conversion',si)
    # T04/T06 general proofs are checked against explicit nontrivial path fixtures below.
    path_checks,paths=check_paths();ck('T04_same_value_distinct_internal_response',path_checks[0]);ck('T06_path_composition_and_independent_vertex_frames',path_checks[1]);cert['paths']=paths
    # Exact second-order automatic differentiation: arbitrary curved KK backgrounds.
    from kk_jets import check_kk
    kk=check_kk();ck('T16_Routh_full_geodesic_projection_and_converse_at_all_jets',kk['projection_and_lift']);ck('T16_arbitrary_quadratic_gauge_coordinate_change',kk['gauge']);cert['KK_jets']=kk
    out.mkdir(parents=True,exist_ok=False)
    dump=lambda n,x:(out/n).write_bytes((json.dumps(pack(x),ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
    dump('EXACT_CERTIFICATES.json',cert)
    bind={p.name:sha256(p.read_bytes()).hexdigest() for p in sorted(root.glob('*.py'))}
    result={'id':'FN-GENERAL-PROOFS-001-v0.1','status':'PASS','checks':checks,'passed_checks':len(checks),
        'source_sha256':sha256((root/'checker.py').read_bytes()).hexdigest(),'module_sha256':bind,
        'protocol_sha256':sha256((root/'PROOF_PLAN.json').read_bytes()).hexdigest(),
        'scope':'Exact finite regression checks; universally quantified statements are proved in the accompanying documents.',
        'python':sys.version,'platform':platform.platform(),'formal_proof_assistant':False}
    dump('RESULTS.json',result);print(json.dumps({k:v for k,v in result.items() if k not in ['checks','module_sha256']},indent=2))

def sum_matrix(xs):
    r=zero(len(xs[0]))
    for x in xs:r=add(r,x)
    return r
def mv(a,v):return [dot(r,v) for r in a]
def check_paths():
    i,j,k=QB[1:];u=F(3,5);v=F(4,5);c=(u,v,0,0)
    t1=zero(3);t2=zero(3);t1[0][0]=t2[1][1]=1
    first=compression(t1)==compression(t2) and insertion(t1,c)!=insertion(t2,c)
    unit_quats=[(F(3,5),F(4,5),0,0),(F(5,13),0,F(12,13),0),(F(8,17),0,0,F(15,17))]
    links=[unit_quats[n%3] for n in range(13)];frames=[unit_quats[(n+1)%3] for n in range(14)]
    total=(1,0,0,0);transformed=(1,0,0,0);split=(1,0,0,0)
    for n,u in enumerate(links):
        total=qm(u,total);up=qm(qm(frames[n+1],u),qc(frames[n]));transformed=qm(up,transformed)
    left=(1,0,0,0);right=(1,0,0,0)
    for u in links[:6]:left=qm(u,left)
    for u in links[6:]:right=qm(u,right)
    g=adj(total);cargo=stf(mat([[1,2,3],[4,-1,2],[1,0,0]]))
    second=total==qm(right,left) and transformed==qm(qm(frames[-1],total),qc(frames[0]))
    second &= compression(conj(g,cargo))==(0,0,0,0) and sc(-2,conj(g,cargo))==conj(g,sc(-2,cargo))
    return (first,second),{'length':len(links),'holonomy':total,'transformed':transformed}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(Path(__file__).resolve().parent,a.out.resolve())
