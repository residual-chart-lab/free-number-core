"""Independent finite audit evidence; quantified proofs are in REPORT_JA.md.
Run: python -I -B independent_checks.py --study FIXED_STUDY --out NEW_JSON
Standard library only. Fraction except explicitly labeled Hermitian-spin floats.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse,importlib.util,json,math,platform,sys

def mat(a):return [[F(x) for x in r] for r in a]
def eye(n):return mat([[int(i==j) for j in range(n)] for i in range(n)])
def transpose(a):return [list(r) for r in zip(*a)]
def mm(a,b):return [[sum(x*y for x,y in zip(r,c)) for c in zip(*b)] for r in a]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(x,a):return [[x*y for y in r] for r in a]
def sub(a,b):return add(a,scale(-1,b))
def comm(a,b):return sub(mm(a,b),mm(b,a))
def trace(a):return sum(a[i][i] for i in range(len(a)))
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def norm2(a):return sum(x*x for r in a for x in r)
def conj(g,a):return mm(mm(g,a),transpose(g))
def diag(v):return mat([[x if i==j else 0 for j in range(len(v))] for i,x in enumerate(v)])
def rot(n,i,j,c=F(3,5),s=F(4,5)):
    a=eye(n);a[i][i]=a[j][j]=c;a[i][j]=-s;a[j][i]=s;return a
def pack(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {k:pack(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [pack(v) for v in x]
    return x
# Quaternion multiplication through an independent Cayley table.
TABLE=[[(1,0),(1,1),(1,2),(1,3)],[(1,1),(-1,0),(1,3),(-1,2)],[(1,2),(-1,3),(-1,0),(1,1)],[(1,3),(1,2),(-1,1),(-1,0)]]
def qm(a,b):
    out=[F(0)]*4
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            s,k=TABLE[i][j];out[k]+=s*x*y
    return out
QB=[tuple(F(i==j) for i in range(4)) for j in range(4)]
def basis_response(word,probes):
    sign=1;index=word[0]
    for a,c in zip(word[1:],probes):
        s,k=TABLE[a][c];ss,index=TABLE[k][index];sign*=s*ss
    return index,sign
def evaluate(tensor,probes):
    result=[F(0)]*4
    for word,coeff in tensor.items():
        a=list(QB[word[0]])
        for k in range(1,len(word)):a=qm(qm(QB[word[k]],probes[k-1]),a)
        result=[x+coeff*y for x,y in zip(result,a)]
    return result

def run(study):
    spec=importlib.util.spec_from_file_location('subject',study/'checker.py');subject=importlib.util.module_from_spec(spec);spec.loader.exec_module(subject)
    checks={};evidence={}
    def ck(name,v):
        checks[name]=bool(v)
        if not v:raise AssertionError(name)
    # T03 length 5: all 1024 inverse coefficients, 256 quaternion assay entries.
    m=5;words=list(product(range(4),repeat=m));probes=list(product(range(4),repeat=m-1))
    tensor={w:F((i%13)-6,(i%5)+1) for i,w in enumerate(words) if i%71==0 or i%103==7}
    output=[]
    for p in probes:
        value=[F(0)]*4
        for w,c in tensor.items():k,s=basis_response(w,p);value[k]+=s*c
        output.append(value)
    inverse=[]
    for w in words:
        total=F(0)
        for p,value in zip(probes,output):k,s=basis_response(w,p);total+=s*value[k]
        inverse.append(total/F(4**(m-1)))
    ck('T03_length5_all_inverse_coefficients',inverse==[tensor.get(w,F(0)) for w in words])
    lhs=sum(dot(v,v) for v in output);rhs=4**(m-1)*sum(x*x for x in tensor.values())
    ck('T03_length5_exact_norm_identity',lhs==rhs)
    concatenations=[]
    for t in range(6):
        x={(0,1):F(2+t,7),(3,2):F(-3,5),(1,0):F(1,3)}
        y={(2,0,3):F(1+t,9),(1,3,1):F(4,11)}
        xy={wx+wy:a*b for wx,a in x.items() for wy,b in y.items()}
        cs=[[F(t+i+j+1,2*j+3) for j in range(4)] for i in range(4)]
        direct=evaluate(xy,cs);composed=qm(qm(evaluate(y,cs[2:]),cs[1]),evaluate(x,cs[:1]))
        concatenations.append(direct==composed)
    ck('T03_all_gap_concatenation_with_nonbasis_probes',all(concatenations))
    evidence['T03']={'length':5,'all_inverse_coefficients':len(inverse),'quaternion_evaluations':len(probes),'nonzero_input_coefficients':sum(bool(x) for x in tensor.values()),'inner_product_factor':256,'norm_factor':16,'response_norm_squared':lhs,'concatenation_trials':6}
    # T07 arbitrary D, including non-scalar variations inside degenerate blocks.
    cases=[]
    spectra=[[1,-1],[0,0],[2,1,1],[0,0,0],[3,1,-1,-3],[2,2,-1,-1],[3,1,1,-2,-3],[2,2,2,-1,-1,-4]]
    for ix,values in enumerate(spectra):
        n=len(values);s=diag(values);d=mat([[F((i+j+ix)%7-3,i+j+2) for j in range(n)] for i in range(n)])
        expected=[[d[i][j]/(values[j]-values[i]) if values[i]!=values[j] else F(0) for j in range(n)] for i in range(n)]
        E=[[d[i][j] if values[i]==values[j] else F(0) for j in range(n)] for i in range(n)]
        g=mm(rot(n,0,1),rot(n,n-2,n-1,F(5,13),F(12,13)))
        actual,_=subject.canonical_generator(conj(g,s),conj(g,d))
        ck('T07_full_symmetric_D_case_'+str(ix),actual==conj(g,expected) and add(comm(expected,s),E)==d and comm(E,s)==scale(0,s))
        if len(set(values))>1:
            delta=min(abs(x-y) for x in values for y in values if x!=y)
            ck('T12_gap_bound_case_'+str(ix),norm2(expected)*delta**2<=norm2(sub(d,E))<=norm2(d))
        cases.append({'spectrum':values,'arbitrary_D':d,'commuting_part':E,'Omega':expected})
    evidence['T07']=cases
    # Rational S whose spectral values are irrational: no diagonalization in oracle.
    s=mat([[0,1,0],[1,1,0],[0,0,3]]);k=mat([[0,-2,3],[2,0,-5],[-3,5,0]])
    E=add(mm(s,s),scale(F(2,3),eye(3)));d=add(comm(k,s),E)
    actual,_=subject.canonical_generator(s,d)
    ck('T07_rational_solve_with_irrational_eigenvalues',actual==k and comm(E,s)==scale(0,s))
    # Concrete textual error: applying a residual-only amplitude formula without centering.
    S=diag([2,1,1]);raw=3*trace(mm(mm(S,S),S))/trace(mm(S,S));S0=sub(S,scale(trace(S)/3,eye(3)))
    centered=3*trace(mm(mm(S0,S0),S0))/trace(mm(S0,S0))
    ck('T08_uncentered_amplitude_counterexample',raw==5 and centered==1)
    evidence['T08_formula_correction']={'S':S,'actual_simple_minus_double_gap':1,'uncentered_formula':raw,'centered_formula':centered,'S_centered':S0}
    # T08 extra term at a splitting jet; this tests orbit decomposition, not nonexistent smooth branches.
    p=diag([1,0,0]);q=sub(eye(3),p);D=mat([[0,1,0],[1,0,1],[0,1,0]])
    z=mm(mm(q,comm(D,mm(mm(D,p),D))),q);omega,_=subject.canonical_generator(S,D)
    ck('T08_splitting_term_preserves_only_instantaneous_orbit_component',z!=scale(0,z) and comm(z,S)==scale(0,S) and comm(add(omega,z),S)==comm(omega,S))
    # T13 independent orthonormal, Hermitian ladder representation (floating only here).
    basis=[diag([1,0,-1]),diag([0,1,-1]),mat([[0,1,0],[1,0,0],[0,0,0]]),mat([[0,0,1],[0,0,0],[1,0,0]]),mat([[0,0,0],[0,0,1],[0,1,0]])]
    spinrows=[]
    for twice_j in [0,1,2,3,4,5,6,7,9,14,31]:
        j=F(twice_j,2);dim=twice_j+1
        plus=[[0j]*dim for _ in range(dim)]
        for col in range(1,dim):
            magnetic=j-col;plus[col-1][col]=math.sqrt(float((j-magnetic)*(j+magnetic+1)))
        minus=transpose(plus);jx=scale(0.5,add(plus,minus));jy=scale(-0.5j,sub(plus,minus));jz=[[complex(float(j-i)) if i==k else 0j for k in range(dim)] for i in range(dim)]
        generators=[jx,jy,jz];ops=[]
        products=[[mm(a,b) for b in generators] for a in generators]
        for b in basis:
            op=[[0j]*dim for _ in range(dim)]
            for a in range(3):
                for c in range(3):op=add(op,scale(float(b[a][c]),products[a][c]))
            ops.append(op)
        coefficient=(2*j+1)*j*(j+1)*(4*j*(j+1)-3)/30
        worst=0.0
        for a,op in enumerate(ops):
            for b,other in enumerate(ops):
                # trace(op*other) without a second dense matrix product.
                val=sum(op[i][k]*other[k][i] for i in range(dim) for k in range(dim))
                target=float(coefficient*trace(mm(basis[a],basis[b])))
                worst=max(worst,abs(val-target)/max(1.0,abs(target),float(coefficient)))
        weights=[j-k for k in range(dim)];qdiag=[m*m-j*(j+1)/3 for m in weights]
        exact_coeff=F(3,2)*sum(x*x for x in qdiag)
        ck('T13_Hermitian_Gram_and_exact_weight_sum_2j_'+str(twice_j),worst<1e-12 and exact_coeff==coefficient)
        spinrows.append({'j':j,'dimension':dim,'exact_coefficient':coefficient,'max_scaled_Hermitian_Gram_error':worst})
    evidence['T13']={'floating_tolerance':1e-12,'weight_sum_arithmetic':'Fraction','offdiagonal_Gram_arithmetic':'Python complex, orthonormal Hermitian ladder matrices','cases':spinrows}
    # T16 independent Hamiltonian reduction on a genuinely position-dependent metric.
    hamilton=[]
    for x,y,p,kappa,phi_sign in [(F(1,3),F(2,5),F(-2,7),F(3,5),1),(F(1,2),F(-1,5),F(0),F(2,3),1),(F(2,3),F(1,5),F(3,7),F(0),1),(F(1,4),F(3,5),F(2,7),F(4,5),-1)]:
        g=[-(1+x)**2,(1+2*x)**2];gx=[-2*(1+x),4*(1+2*x)];ginv=[1/a for a in g];ginvx=[-a/(b*b) for a,b in zip(gx,g)]
        phi=phi_sign*(2+x);phix=F(phi_sign);A=[y,x*x+y];dA=[[F(0),F(1)],[2*x,F(1)]]
        v=[F(2,5),F(-3,7)];pi=[g[i]*v[i]+kappa*p*A[i] for i in range(2)];P=[pi[i]-kappa*p*A[i] for i in range(2)]
        dpi=[-F(1,2)*sum(ginvx[i]*P[i]**2 for i in range(2))+kappa*p*sum(v[i]*dA[i][0] for i in range(2))+p*p*phix/phi**3,kappa*p*sum(v[i]*dA[i][1] for i in range(2))]
        dpkin=[dpi[i]-kappa*p*sum(dA[i][j]*v[j] for j in range(2)) for i in range(2)]
        accel=[ginvx[i]*v[0]*P[i]+ginv[i]*dpkin[i] for i in range(2)]
        connection=[F(1,2)*ginv[0]*(gx[0]*v[0]**2-gx[1]*v[1]**2),ginv[1]*gx[1]*v[0]*v[1]]
        field=2*x-1
        target=[-connection[0]+kappa*p*ginv[0]*field*v[1]+p*p*ginv[0]*phix/phi**3,-connection[1]-kappa*p*ginv[1]*field*v[0]]
        ck('T16_independent_Hamilton_equations_case_'+str(len(hamilton)),accel==target)
        hamilton.append({'position':[x,y],'p':p,'kappa':kappa,'phi':phi,'Hamilton_acceleration':accel,'reduced_field_acceleration':target})
    evidence['T16']=hamilton
    return {'status':'PASS','count':len(checks),'checks':checks,'evidence':pack(evidence),'environment':{'python':sys.version,'platform':platform.platform()},'limits':['Finite verification does not prove universal claims','Hermitian-spin off-diagonal Gram comparison is floating point; exact weight sums are separately checked','No new trajectory integration or field-equation solution']}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--study',type=Path,required=True);parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args();r=run(a.study.resolve())
    with a.out.open('x',encoding='utf-8') as f:json.dump(r,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps({'status':r['status'],'checks':r['count'],'T08_counterexample':r['evidence']['T08_formula_correction'],'worst_spin_scaled_error':max(x['max_scaled_Hermitian_Gram_error'] for x in r['evidence']['T13']['cases'])},ensure_ascii=False))
