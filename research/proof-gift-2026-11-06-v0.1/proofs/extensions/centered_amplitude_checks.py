"""Regression for audit F01: amplitude recovery requires trace centering."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from exact import *
from hashlib import sha256
import argparse,json

def centered_amplitude(s):
    s0=sub(s,sc(tr(s)/3,eye(3)));t2=tr(mm(s0,s0))
    if not t2:return None
    return 3*tr(mm(mm(s0,s0),s0))/t2

def run(out):
    gs=[eye(3),rotation(3,0,1),mm(rotation(3,0,2),rotation(3,1,2,F(5,13),F(12,13)))];cases=[]
    for shift in [F(-3),F(0),F(1),F(5,7)]:
        for a in [F(-2),F(1),F(3,5)]:
            s=diag([shift+a,shift,shift])
            for g in gs:
                ss=conj(g,s);got=centered_amplitude(ss);assert got==a
                cases.append({'shift':shift,'a':a,'trace':tr(ss),'recovered':got})
    s=diag([2,1,1]);old=3*tr(mm(mm(s,s),s))/tr(mm(s,s));new=centered_amplitude(s)
    assert old==5 and new==1
    for shift in [F(-3),F(0),F(1),F(5,7)]:assert centered_amplitude(sc(shift,eye(3))) is None
    result={'status':'PASS','finding':'Astra F01','source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'counterexample':{'S':s,'old_uncentered_formula':old,'corrected_centered_formula':new},
            'nonisotropic_cases':cases,'isotropic_separate_branch_cases':4,
            'scope':'Finite regression; general correction follows from S0=a(P-I/3), tr(S0^2)=2a^2/3 and tr(S0^3)=2a^3/9.'}
    out.write_bytes((json.dumps(pack(result),indent=2)+'\n').encode('utf-8'));print(json.dumps({'status':'PASS','nonisotropic_cases':len(cases),'old':str(old),'corrected':str(new)}))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();run(a.out.resolve())
