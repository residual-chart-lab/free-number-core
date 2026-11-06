"""Independent finite evidence for T03/T08 supplements; stdlib only.
Run beside independent_checks.py: python -I -B supplement_independent_checks.py --out NEW_JSON
No target checker imports. All arithmetic is Fraction/integer.
"""
from pathlib import Path
import argparse,importlib.util,json,platform,sys
from fractions import Fraction as F
from itertools import product,combinations
spec=importlib.util.spec_from_file_location('audit_base',Path(__file__).with_name('independent_checks.py'))
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

def qadd(x,y):return [u+v for u,v in zip(x,y)]
def qscale(c,x):return [c*u for u in x]
def one_inverse(fs):
    b=[F(0)]*4
    for i,f in enumerate(fs,1):b=qadd(b,a.qm(f,a.QB[i]))
    return [qscale(F(-1,2),qadd(f,a.qm(b,a.QB[i]))) for i,f in enumerate(fs,1)]
def reconstruct(m,data):
    if m==1:
        assert data[()][0]==0
        return {(i,):data[()][i] for i in range(1,4)}
    pieces=[{} for _ in range(3)]
    for tail in product(range(1,4),repeat=m-2):
        values=one_inverse([data[(i,)+tail] for i in range(1,4)])
        for i in range(3):pieces[i][tail]=values[i]
    return {(i,)+w:c for i in range(1,4) for w,c in reconstruct(m-1,pieces[i-1]).items()}
def response(tensor):
    m=len(next(iter(tensor)));data={}
    for p in product(range(1,4),repeat=m-1):
        val=[F(0)]*4
        for w,c in tensor.items():k,s=a.basis_response(w,p);val[k]+=s*c
        data[p]=val
    return data
def star(k):
    out=a.scale(0,k)
    for i,j in combinations(range(4),2):
        r,s=[x for x in range(4) if x not in (i,j)]
        seq=[i,j,r,s];sign=(-1)**sum(seq[x]>seq[y] for x in range(4) for y in range(x+1,4))
        out[i][j]=sign*k[r][s];out[j][i]=-out[i][j]
    return out
def run():
    checks={};evidence={}
    def ck(name,v):
        checks[name]=bool(v)
        if not v:raise AssertionError(name)
    # Full 12x12 operator identity: arbitrary three quaternion coefficients.
    columns=[];inverses=[]
    for j in range(12):
        coeff=[[F(i*4+k==j) for k in range(4)] for i in range(3)]
        fs=[]
        for r in range(1,4):
            val=[F(0)]*4
            for i in range(1,4):val=qadd(val,a.qm(a.qm(coeff[i-1],a.QB[r]),a.QB[i]))
            fs.append(val)
        columns.append([x for f in fs for x in f]);inverses.append([x for c in one_inverse(fs) for x in c])
    ck('T03_one_gap_inverse_matrix_identity',a.transpose(inverses)==a.eye(12))
    L=a.transpose(columns);C=[]
    for j in range(12):
        val=[F(0)]*4
        for i in range(3):val=qadd(val,a.qm([F(i*4+k==j) for k in range(4)],a.QB[i+1]))
        C.append(val)
    C=a.transpose(C)
    ck('T03_one_gap_Gram_exact',a.mm(a.transpose(L),L)==a.sub(a.scale(4,a.eye(12)),a.mm(a.transpose(C),C)))
    ck('T03_C_Cadjoint_equals_3I',a.mm(C,a.transpose(C))==a.scale(3,a.eye(4)))
    words=list(product(range(1,4),repeat=5));tensor={w:F(i%17-8,i%7+1) for i,w in enumerate(words)}
    data=response(tensor);n2=sum(x*x for x in tensor.values());r2=sum(a.dot(v,v) for v in data.values())
    ck('T03_pure_length5_recursive_inverse',reconstruct(5,data)==tensor)
    ck('T03_pure_length5_norm_bounds',n2<=r2<=256*n2)
    left={(1,1):F(1),(2,2):F(1)};right={(1,1):F(1),(2,2):F(-1)}
    norms=[sum(a.dot(v,v) for v in response(t).values()) for t in [left,right]]
    ck('T03_pure_not_scaled_isometry_equal_input_norm',norms==[4,8])
    evidence['T03']={'length':5,'coefficient_count':243,'quaternion_evaluations':81,'tensor_norm_squared':n2,'response_norm_squared':r2,'equal_input_norm_squared':2,'unequal_response_norm_squared':norms,'one_gap_real_matrix':L}
    # Exhaust all diagonal sign stabilizers, rather than the subject rref routine.
    dimensions=[]
    for n in range(2,11):
        pairs=list(combinations(range(1,n),2))
        stabilizers={g:[] for g in ['SO','O','SO_zero','O_zero']}
        for signs in product([-1,1],repeat=n):
            det=1
            for x in signs:det*=x
            if signs[0]==signs[1]:
                stabilizers['O'].append(signs)
                if det==1:stabilizers['SO'].append(signs)
            stabilizers['O_zero'].append(signs)
            if det==1:stabilizers['SO_zero'].append(signs)
        surviving={g:[ij for ij in pairs if all(s[ij[0]]*s[ij[1]]==1 for s in ss)] for g,ss in stabilizers.items()}
        ck('T08_sign_stabilizer_dimension_'+str(n),len(surviving['SO'])==(1 if n==4 else 0) and all(not surviving[g] for g in ['O','SO_zero','O_zero']))
        dimensions.append({'n':n,'surviving_coefficient_pairs':surviving})
    P=a.diag([1,0,0,0]);D=a.mat([[0,2,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]])
    O=a.comm(D,P);K=star(O)
    ck('T08_SO4_nonzero_extra_tracks',a.norm2(K)>0 and a.comm(K,P)==a.scale(0,P) and a.comm(a.add(O,K),P)==D)
    rotations=[a.rot(4,i,j) for i,j in combinations(range(4),2)]
    ck('T08_SO4_Hodge_covariance',all(star(a.conj(g,O))==a.conj(g,K) for g in rotations))
    H=a.diag([1,1,-1,1])
    ck('T08_O4_reflection_kills_exception',a.conj(H,P)==P and a.conj(H,D)==D and a.conj(H,K)==a.scale(-1,K))
    evidence['T08']={'dimensions':dimensions,'SO4_Omega0':O,'SO4_extra':K,'proper_rotation_trials':6,'zero_tangent_tested':True,'note':'Sign stabilizers give upper bounds. The nonzero Hodge construction supplies the lower bound in n=4; arbitrary dimension is proved in the written audit.'}
    return {'status':'PASS','check_count':len(checks),'checks':checks,'evidence':evidence,'python':sys.version,'platform':platform.platform(),'arithmetic':'exact integers and Fraction','limits':'Finite checks do not establish arbitrary-length or arbitrary-dimension quantifiers; see REPORT_JA.md.'}
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);args=p.parse_args();result=run();args.out.write_text(json.dumps(a.pack(result),indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':result['status'],'check_count':result['check_count']}))
