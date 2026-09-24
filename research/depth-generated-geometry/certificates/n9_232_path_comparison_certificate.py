#!/usr/bin/env python3
"""Note 30: two ordered internal insertions and local interchange.

Exact integer identities plus modular lower bounds and reconstructed rational
annihilators. Requires the Note 29 dependencies. No result JSON is an input.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import argparse
import hashlib
import json
import time
import platform
import numpy as np
import scipy
from scipy import sparse
import flint
import n8_222_redetection_certificate as base
import n9_232_continuation_certificate as prev
from n8_222_minimal_refinement_certificate import exact_product

if not __debug__:
    raise RuntimeError('Assertions must remain enabled.')

BASE_COMMIT='be89eec9b5cc6a2ed3c558d5b0ccd62565127f4a'


def primitive_paths():
    vec=base.words(2)
    h=np.repeat(np.arange(4),len(vec));vs=np.tile(vec,(4,1))
    cs=[h,vs[:,0],vs[:,1]]
    ab=base.evaluate((cs,[('c',0),('p',0),('c',1),('p',1),('c',2)]),vec)
    ba=base.evaluate((cs,[('c',0),('p',1),('c',2),('p',0),('c',1)]),vec)
    den,inv=base.lift(*(base.inverse(ab,p) for p in base.PRIMES))
    assert np.array_equal(exact_product(inv,ab),den*np.eye(36,dtype=np.int64))
    numerator=exact_product(ba,inv)
    div=int(np.gcd(den,np.gcd.reduce(np.abs(numerator).ravel())))
    den//=div;numerator//=div
    assert np.array_equal(exact_product(numerator,ab),den*ba)
    assert base.certified_rank(ab)==base.certified_rank(ba)==36
    assert base.certified_rank(ba-ab)==24
    return den,numerator,ab,ba


@lru_cache(None)
def path(pos_a,pos_b,order):
    """Source order is (old h,v1,...,v4,a,b), with final probe labels fixed."""
    vec=base.words(6);h=np.repeat(np.arange(4),len(vec));vs=np.tile(vec,(4,1))
    cs=[h]+[vs[:,i] for i in range(6)]
    old=[i for i in range(6) if i not in (pos_a,pos_b)]
    seq=[('c',0)]
    for i in reversed(range(4)):
        seq += [('p',old[i]),('c',i+1)]
    slots={'a':(pos_a,5),'b':(pos_b,6)}
    for letter in order:
        pos,coef=slots[letter]
        seq += [('p',pos),('c',coef)]
    ev=base.evaluate((cs,seq),vec)
    matrix=prev.decoder_numerator(6) @ sparse.csr_matrix(ev)
    den=64
    div=int(np.gcd(den,np.gcd.reduce(np.abs(matrix.data))))
    matrix.data//=div;den//=div
    assert np.array_equal((matrix.T @ base.encoder(6).T).T,den*ev)
    return den,matrix


@lru_cache(None)
def interchange(pos_a,pos_b):
    """Apply the fixed 36-dimensional local comparison to two probe slots.

    Constructed from local probe evaluations, independently of the quotient.
    """
    den,primitive,_,_=primitive_paths()
    encoder=base.encoder(6)
    out=np.zeros_like(encoder)
    oldslots=[i for i in range(6) if i not in (pos_a,pos_b)]
    for args in base.words(4):
        rows=[]
        for a,b in base.words(2):
            full=[0]*6
            for slot,value in zip(oldslots,args): full[slot]=int(value)
            full[pos_a]=int(a);full[pos_b]=int(b)
            ix=0
            for value in full: ix=3*ix+value-1
            rows.extend(range(4*ix,4*ix+4))
        out[rows]=exact_product(primitive,encoder[rows])
    matrix=prev.decoder_numerator(6) @ sparse.csr_matrix(out)
    den*=64
    div=int(np.gcd(den,np.gcd.reduce(np.abs(matrix.data))))
    matrix.data//=div;den//=div
    assert np.array_equal((matrix.T @ encoder.T).T*primitive_paths()[0],den*out)
    return den,matrix


@lru_cache(None)
def cap(depth,pos):
    """Read all three coefficients of a selected probe by the local formula."""
    primitive=prev.cap_primitive()
    parent_dim=4*3**(depth-1)
    child_dim=3*parent_dim
    evaluations=[np.zeros((parent_dim,child_dim),dtype=np.int64) for _ in range(3)]
    encoder=base.encoder(depth)
    for ix,args in enumerate(base.words(depth-1)):
        rows=[]
        for z in (1,2,3):
            full=list(args);full.insert(pos,z)
            col=0
            for value in full: col=3*col+int(value)-1
            rows.extend(range(4*col,4*col+4))
        values=exact_product(primitive,encoder[rows])
        for a in range(3): evaluations[a][4*ix:4*ix+4]=values[a::3]
    out=np.zeros((child_dim,child_dim),dtype=np.int64)
    for a in range(3): out[a::3]=prev.decoder_numerator(depth-1) @ evaluations[a]
    den=2**depth
    div=int(np.gcd(den,np.gcd.reduce(np.abs(out).ravel())))
    out//=div;den//=div
    sd,sigma=prev.suspension(depth,pos)
    assert np.array_equal(exact_product(out,sigma),den*sd*np.eye(child_dim,dtype=np.int64))
    return den,sparse.csr_matrix(out)


def graded_profile(matrices,grades):
    rowgrades=[prev.row_grades(m,grades) for m in matrices]
    profiles=[]
    for g in range(4):
        cols=np.flatnonzero(grades==g)
        blocks=[sparse.csr_matrix(m)[r==g][:,cols].toarray() for m,r in zip(matrices,rowgrades)]
        profiles.append(prev.rank_exact(np.concatenate(blocks)))
    return profiles


def certificate(output=None):
    started=time.monotonic()
    primitive_den,primitive,ab0,ba0=primitive_paths()
    assert np.any(np.count_nonzero(primitive,axis=1)>1)
    base.log('local comparison fixed; local difference rank 24')
    Q,D=prev.quotient_exact(9,(1,3,6,8))
    assert Q.shape==(1332,17496)
    q7,d7=base.exact_quotient(7,(1,3,4,6))
    q8,d8=base.exact_quotient(8,(1,3,5,7))
    K=prev.residual232();k7=base.residual(4)
    source=sparse.kron(sparse.csr_matrix(q7),sparse.eye(9,dtype=np.int64),format='csr')
    first_blocks=[];forward_a=[];forward_b=[];comparison=[]
    readout_a=[];readout_b=[]
    raw_ab=[];raw_ba=[];raw_c=[]
    swap=np.arange(2916).reshape(324,3,3).transpose(0,2,1).ravel()
    for ei,(edge,oldedge) in enumerate(zip(combinations((1,3,6,8),2),combinations((1,3,5,7),2))):
        probes=[g for g in range(1,9) if g not in edge]
        pa,pb=probes.index(4),probes.index(5)
        da,a=path(pa,pb,'ab');db,b=path(pa,pb,'ba');dc,c=interchange(pa,pb)
        assert not (db*(c@a)-dc*da*b).nnz
        kr=K[:,ei*2916:(ei+1)*2916]
        ks=np.kron(k7[:,ei*324:(ei+1)*324],np.eye(9,dtype=np.int64))
        assert np.array_equal(exact_product(kr,a),da*exact_product(ab0,ks))
        assert np.array_equal(exact_product(kr,b),db*exact_product(ba0,ks))
        assert np.array_equal(primitive_den*exact_product(kr,c),dc*exact_product(primitive,kr))
        # Verify literal paths against compositions of the existing insertions.
        oldpos=[g for g in range(1,8) if g not in oldedge].index(4)
        d1,j1=prev.suspension(5,oldpos)
        d2,j2=prev.suspension(6,pb)
        d3,j3=prev.suspension(6,pa)
        first=sparse.kron(j1,sparse.eye(3,dtype=np.int64),format='csr')
        assert not (da*(j2@first)-d1*d2*a).nnz
        assert not (db*(j3@first)[:,swap]-d1*d3*b).nnz
        block=q8[:,ei*972:(ei+1)*972]
        first_blocks.append((d1,sparse.kron(sparse.csr_matrix((j1.T@block.T).T),sparse.eye(3,dtype=np.int64),format='csr')))
        block=Q[:,ei*2916:(ei+1)*2916]
        forward_a.append((da,(a.T@block.T).T))
        forward_b.append((db,(b.T@block.T).T))
        comparison.append((dc,(c.T@block.T).T))
        dr,cr=cap(6,pb)
        parent_block=sparse.kron(sparse.csr_matrix(q8[:,ei*972:(ei+1)*972]),sparse.eye(3,dtype=np.int64),format='csr')
        r=parent_block @ cr
        readout_a.append((dr*da,r@a));readout_b.append((dr*db,r@b))
        raw_ab.append((da,a));raw_ba.append((db,b));raw_c.append((dc,c))
    def join(blocks):
        den=int(np.lcm.reduce([d for d,a in blocks]))
        return den,sparse.hstack([(den//d)*sparse.csr_matrix(a) for d,a in blocks],format='csr')
    dm,middle_a=join(first_blocks)
    global_swap=np.arange(17496).reshape(1944,3,3).transpose(0,2,1).ravel()
    middle_b=middle_a[:,global_swap]
    da,fa=join(forward_a);db,fb=join(forward_b);dc,qc=join(comparison)
    dra,ra=join(readout_a);drb,rb=join(readout_b)
    assert not (dm*ra-dra*middle_a).nnz
    delta=db*fa-da*fb
    readout_delta=drb*ra-dra*rb
    grades=np.repeat(np.tile(base.grades(4),6),9)^np.tile(base.grades(2)[:9],1944)
    target_grades=np.tile(base.grades(6),6)
    families={
        'endpoint_ab':[fa], 'endpoint_ba':[fb], 'endpoint_difference':[delta],
        'both_endpoints':[fa,fb],
        'retained_ab':[source,middle_a,fa],
        'retained_ba':[source,middle_b,fb],
        'retained_ab_and_other_endpoint':[source,middle_a,fa,fb],
        'both_retained_paths':[source,middle_a,middle_b,fa,fb],
        'same_gap5_readout_difference':[readout_delta],
        'endpoint_and_readout_difference':[delta,readout_delta],
        'both_paths_with_same_gap5_readout':[source,middle_a,middle_b,fa,fb,rb],
    }
    ranks={}
    for name,matrices in families.items():
        base.log('rank family',name)
        profile=graded_profile(matrices,grades)
        ranks[name]={'total':sum(profile),'grades':profile}
        base.log(name,ranks[name])
    ranks['quotient_and_local_comparison']={}
    profile=graded_profile([Q,qc],target_grades)
    ranks['quotient_and_local_comparison']={'total':sum(profile),'grades':profile}
    base.log('comparison quotient rank',ranks['quotient_and_local_comparison'])
    assert ranks['endpoint_ab']['total']==ranks['endpoint_ba']['total']==1332
    assert ranks['endpoint_difference']['total']==1320
    assert ranks['retained_ab']['total']==ranks['retained_ba']['total']==3924
    witnesses={}
    for name,observation,continuation,gs in [
        ('comparison_descent',sparse.csr_matrix(Q),qc,target_grades),
        ('equal_endpoints_different_readouts',delta,readout_delta,grades),
    ]:
        if name=='comparison_descent' and ranks['quotient_and_local_comparison']['total']==1332:
            witnesses[name]=None
            continue
        if name=='equal_endpoints_different_readouts' and ranks['endpoint_and_readout_difference']['total']==ranks['endpoint_difference']['total']:
            witnesses[name]=None
            continue
        cols=np.flatnonzero(gs==0)
        og=prev.row_grades(observation,gs);cg=prev.row_grades(continuation,gs)
        h=observation[og==0][:,cols].toarray()
        f=continuation[cg==0][:,cols].toarray()
        base.log('finding witness',name)
        witnesses[name]=prev.first_witness(h,f,cols)
        v=np.zeros((17496,1),dtype=np.int64)
        for index,value in witnesses[name]['input_coordinates']:v[index,0]=value
        assert not np.any(exact_product(observation,v))
        response=exact_product(continuation,v)
        row=int(np.flatnonzero(response[:,0])[0])
        del witnesses[name]['output_local_row']
        witnesses[name].update({'output_row':row,'output_numerator':int(response[row,0]),
                               'output_denominator':dc if name=='comparison_descent' else dra*drb})
        if name=='equal_endpoints_different_readouts':
            va=exact_product(fa,v);vb=exact_product(fb,v)
            assert np.array_equal(db*va,da*vb)
            witnesses[name]['common_endpoint_nonzero']=bool(np.any(va))
            witnesses[name]['readout_coefficient_channel']='ijk'[row%3]
        base.log('witness',name,witnesses[name])
    difference_coo=delta.tocoo()
    row,col,value=map(int,(difference_coo.row[0],difference_coo.col[0],difference_coo.data[0]))
    witnesses['direct_path_difference']={'input_basis_column':col,'output_row':row,
                                         'difference_numerator':value,'difference_denominator':da*db}
    sources=[Path(__file__).resolve(),Path(prev.__file__).resolve(),Path(base.__file__).resolve(),
             base.HERE/'n8_222_decoder_continuation_certificate.py',
             base.HERE/'n8_222_minimal_refinement_certificate.py',base.HERE/'n8_222_exact_backend.cpp']
    result={'base_commit':BASE_COMMIT,
            'field':'Q and R: exact integer identities and certified rational ranks',
            'primes':list(base.PRIMES),
            'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
            'environment':{'python':platform.python_version(),'numpy':np.__version__,
                           'scipy':scipy.__version__,'python_flint':flint.__version__},
            'source_word':'212','target_word':'232','final_support':[1,3,6,8],
            'fixed_probe_labels':{'a':4,'b':5},'source_tensor_order':'E212, Va, Vb',
            'path_ab':'first a at gap 4, then b at gap 5; F za a zb b',
            'path_ba':'first b at gap 4, then a at gap 4, shifting b to 5; F zb b za a',
            'ranks':ranks,
            'witnesses':witnesses,
            'denominators':{'primitive':primitive_den,'middle':dm,'ab':da,'ba':db,'comparison':dc,'readout_ab':dra,'readout_ba':drb},
            'local_interchange_built_before_quotient':True,
            'local_interchange_mixes_response_coordinates':True,
            'residual_path_difference_rank':24,
            'comparison_descent_obstruction_rank':ranks['quotient_and_local_comparison']['total']-1332,
            'hidden_path_readout_rank':ranks['endpoint_and_readout_difference']['total']-ranks['endpoint_difference']['total'],
            'extra_for_other_endpoint':ranks['retained_ab_and_other_endpoint']['total']-3924,
            'extra_for_both_retained_paths':ranks['both_retained_paths']['total']-3924,
            'extra_for_same_gap5_readout':ranks['both_paths_with_same_gap5_readout']['total']-ranks['both_retained_paths']['total'],
            'raw_adjusted_defect_zero':True,
            'scope':'Fixed two right-insertion paths with final labels and input tensor order held fixed; raw equality after adding the local comparison is distinguished from uncorrected path equality and quotient descent.',
            'elapsed_seconds':round(time.monotonic()-started,3),'all_checks_passed':True}
    rendered=json.dumps(result,indent=2)+'\n'
    if output: Path(output).write_text(rendered)
    print(rendered,end='',flush=True)
    base.log('ALL CHECKS PASSED')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output')
    args=parser.parse_args()
    certificate(args.output)
