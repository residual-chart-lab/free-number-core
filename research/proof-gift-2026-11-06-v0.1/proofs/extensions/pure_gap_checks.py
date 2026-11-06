"""Exact finite support for T03's pure-imaginary-gap corollary."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact import *
from itertools import product
from hashlib import sha256
import json,argparse

def basis_response(word,probes):
    ans=QB[word[0]]
    for k in range(1,len(word)):ans=qm(qm(QB[word[k]],QB[probes[k-1]]),ans)
    return ans

def reconstruct(m,data):
    if m==1:
        value=data[()];assert value[0]==0
        return {(i,):value[i] for i in range(1,4)}
    pieces=[{} for _ in range(3)]
    for rest in product(range(1,4),repeat=m-2):
        fs=[data[(i,*rest)] for i in range(1,4)]
        b=(F(0),)*4
        for r,f in enumerate(fs,1):b=qadd(b,qm(f,QB[r]))
        for i in range(1,4):pieces[i-1][rest]=qscale(F(-1,2),qadd(fs[i-1],qm(b,QB[i])))
    answer={}
    for i,piece in enumerate(pieces,1):
        for tail,value in reconstruct(m-1,piece).items():answer[(i,*tail)]=value
    return answer

def run(root,out):
    records=[]
    for m in range(1,5):
        words=list(product(range(1,4),repeat=m));probes=list(product(range(1,4),repeat=m-1))
        columns=[flat([list(basis_response(w,p)) for p in probes]) for w in words]
        _,_,rank=rref(tp(columns),[0]*(4*len(probes)),len(words))
        coeffs={w:F(k%11-5,k%4+1) for k,w in enumerate(words)}
        data={p:tuple(sum(coeffs[w]*basis_response(w,p)[r] for w in words) for r in range(4)) for p in probes}
        got=reconstruct(m,data);n2=sum(c*c for c in coeffs.values());r2=sum(dot(v,v) for v in data.values())
        assert got==coeffs and rank==3**m and n2<=r2<=4**(m-1)*n2
        records.append({'length':m,'rank':rank,'tensor_dimension':3**m,'quaternion_evaluations':3**(m-1),
                        'tensor_norm_squared':n2,'restricted_response_norm_squared':r2,'recursive_inverse_exact':True})
    result={'status':'PASS','source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'cases':records,
            'scope':'Finite checks at lengths 1..4; all-length proof is the induction in 04_IMAGINARY_GAPS_EN.md.'}
    out.write_bytes((json.dumps(pack(result),indent=2)+'\n').encode('utf-8'));print(json.dumps({'status':'PASS','lengths':[1,2,3,4],'largest_rank':records[-1]['rank']}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(Path(__file__).resolve().parent,a.out.resolve())
