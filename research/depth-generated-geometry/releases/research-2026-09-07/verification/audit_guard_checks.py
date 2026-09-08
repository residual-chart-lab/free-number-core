#!/usr/bin/env python3
"""Regression checks for the audit's cache-completeness and execution fixes."""
from pathlib import Path
import argparse
import json
import subprocess
import sys
import numpy as np
from scipy import sparse

if not __debug__:
    raise RuntimeError('Run this audit without -O or -OO.')
HERE=Path(__file__).resolve().parent
CERT=next(p for p in (HERE.parent/'certificates',HERE.parents[2]/'certificates') if p.is_dir())
sys.path.insert(0,str(CERT))
import n8_222_redetection_certificate as c

def run(output):
    support=(1,3,4,6)
    original=c.quotient
    l1,d1=original(7,support,1009)
    l2,d2=original(7,support,1013)
    _,L=c.lift(l1[1:],l2[1:]);_,D=c.lift(d1,d2)
    # A missing annihilator row passes the former checks, but represents
    # a quotient of the true cokernel, not the full cokernel.
    assert c.iszero(sparse.csr_matrix(L)@sparse.csr_matrix(D))
    assert len(c.rref(L,1009)[1])==147
    def incomplete(n,s,p):
        l,d=original(n,s,p)
        return l[1:],d
    c.quotient=incomplete
    try:
        c.exact_quotient(7,support)
    except AssertionError as exc:
        assert 'not the full quotient' in str(exc)
    else:
        raise AssertionError('incomplete cached quotient was accepted')
    finally:
        c.quotient=original
    print('[PASS] incomplete cached annihilator rejected',flush=True)
    p=subprocess.run([sys.executable,'-O',str(CERT/'n8_222_redetection_certificate.py'),'--certificate'],
                     capture_output=True,text=True)
    assert p.returncode!=0 and 'require assertions' in p.stderr
    print('[PASS] optimized Python cannot silently disable certification',flush=True)
    for prime in (1,9,1000,65522):
        try:c.rref(np.eye(2,dtype=np.int64),prime)
        except ValueError:pass
        else:raise AssertionError('invalid prime accepted')
    print('[PASS] invalid prime inputs rejected',flush=True)
    result={'status':'passed','certificate_source_sha256':c.SOURCE_HASH,
            'incomplete_cached_annihilator_rejected':True,
            'optimized_execution_rejected':True,'invalid_prime_inputs_rejected':True}
    Path(output).write_text(json.dumps(result,indent=2)+'\n')
    print('ALL CHECKS PASSED',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default='audit-guard-result.json')
    run(p.parse_args().output)
