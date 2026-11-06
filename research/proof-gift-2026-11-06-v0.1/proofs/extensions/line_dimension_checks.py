"""Exact invariant-subspace checks for the all-dimensional line corollary."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact import *
from hashlib import sha256
import argparse,json

def invariant_nullity(n,group):
    p=diag([1]+[0]*(n-1));d=zero(n);d[0][1]=d[1][0]=1
    generators=[]
    h=eye(n);h[0][0]=h[1][1]=-1;generators.append(h)
    for i in range(2,n):
        for j in range(i+1,n):
            h=eye(n);h[i][i]=h[j][j]=-1;generators.append(h)
    if group=='O' and n>2:
        h=eye(n);h[2][2]=-1;generators.append(h)
    basis=[k for k in basis_skew(n) if comm(k,p)==zero(n)]
    if not basis:return 0
    rows=[]
    for g in generators:
        assert conj(g,p)==p and conj(g,d)==d
        cols=[flat(sub(conj(g,k),k)) for k in basis];rows.extend(tp(cols))
    _,null,_=rref(rows,[0]*len(rows),len(basis));return len(null)

def run(out):
    cases=[]
    for n in range(2,8):
        so=invariant_nullity(n,'SO');oo=invariant_nullity(n,'O')
        assert so==(1 if n==4 else 0) and oo==0
        cases.append({'underlying_dimension':n,'SO_free_twists':so,'O_free_twists':oo})
    result={'status':'PASS','source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'cases':cases,
            'scope':'Finite invariant-subspace verification in dimensions 2..7; all-dimensional proof is in 05_LINE_DIMENSION_CLASSIFICATION_EN.md.'}
    out.write_bytes((json.dumps(result,indent=2)+'\n').encode('utf-8'));print(json.dumps(result,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(a.out.resolve())
