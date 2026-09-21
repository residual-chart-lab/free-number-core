#!/usr/bin/env python3
"""Note 32: adjacent core transport and naturality of the fixed readout law.

Rebuilds all six quotients and all literal operators. No saved matrices or
result JSONs are proof inputs. Requires the Note 29 dependencies.
"""
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import json
import platform
import time
import numpy as np
from scipy import sparse
import scipy
import flint
import n8_222_redetection_certificate as base
import n9_232_continuation_certificate as prev
import n9_232_path_comparison_certificate as paths
from n8_222_minimal_refinement_certificate import exact_product, exact_row_factor

if not __debug__:
    raise RuntimeError('Assertions must remain enabled.')

BASE_COMMIT = '08d7ea8306c33a171ec52ca53fb8594a85f6a952'
SUPPORTS = {
    'source': {7: (1,3,4,6), 8: (1,3,5,7), 9: (1,3,6,8)},
    'neighbor': {7: (1,2,4,6), 8: (1,2,5,7), 9: (1,2,6,8)},
}
EXPECTED = {'source': {7: 148, 8: 444, 9: 1332},
            'neighbor': {7: 144, 8: 432, 9: 1296}}


def quotient_exact(n, support):
    """A modular lower bound and exactly lifted nullspace give a Q-rank proof.

    A second prime is needed only if the small-denominator lift fails.
    Every lifted row is checked on the full integer matching map.
    """
    D = prev.matching_exact(n, support)
    cg = np.tile(base.grades(n-3), 6)
    fg = np.tile(base.grades(n-2), 4)
    pieces, records = [], []
    for g in range(4):
        rows = np.flatnonzero(cg == g)
        cols = np.flatnonzero(fg == g)
        assert not D[rows][:, fg != g].nnz
        block = D[rows][:, cols].toarray()
        base.log('matching kernel', n, support, g, block.shape)
        modular = prev.left_kernel_mod(block, 1009)
        used_primes = [1009]
        for scale in (1, 2, 4, 8, 16, 32, 64, 128, 256):
            ker = scale*modular % 1009
            ker[ker > 504] -= 1009
            if not np.any((D[rows].T @ ker.T).T):
                break
        else:
            scale, ker = base.lift(modular, prev.left_kernel_mod(block, 1013))
            assert not np.any((D[rows].T @ ker.T).T)
            used_primes.append(1013)
        assert int(prev.mod_matrix(ker, 1009).rank()) == len(ker)
        full = np.zeros((len(ker), D.shape[0]), dtype=np.int64)
        full[:, rows] = ker
        pieces.append(full)
        records.append({'grade': g, 'quotient_dimension': len(ker),
                        'matching_rank': len(rows)-len(ker),
                        'lift_scale': int(scale), 'primes': used_primes})
    Q = np.concatenate(pieces)
    base.log('exact quotient', n, support, Q.shape)
    return Q, records


def assemble(q7,q8,Q,support):
    S=sparse.kron(q7,sparse.eye(9,dtype=np.int64),format='csr')
    aa=[];bb=[];nn=[]
    for ei,edge in enumerate(combinations(support,2)):
        probes=[g for g in range(1,9) if g not in edge];pa,pb=probes.index(4),probes.index(5)
        da,a=paths.path(pa,pb,'ab');db,b=paths.path(pa,pb,'ba')
        child=sparse.csr_matrix(Q[:,ei*2916:(ei+1)*2916])
        aa.append((da,child@a));bb.append((db,child@b))
        dr,cap=paths.cap(6,pb)
        parent=sparse.kron(q8[:,ei*972:(ei+1)*972],sparse.eye(3,dtype=np.int64),format='csr')
        nn.append((dr*db,parent@cap@b))
    def join(bs):
        d=int(np.lcm.reduce([d for d,_ in bs]));return d,sparse.hstack([(d//di)*m for di,m in bs],format='csr')
    da,a=join(aa);db,b=join(bb);dn,N=join(nn)
    dt=int(np.lcm(da,db));T=(dt//da)*a+(dt//db)*b
    return sparse.vstack([S,T],format='csr'),N,dt,dn

def factor(H,N,tag):
    grades=np.repeat(np.tile(base.grades(4),6),9)^np.tile(base.grades(2)[:9],1944)
    hg=prev.row_grades(H,grades);ng=prev.row_grades(N,grades)
    Ks=[];Ls=[];profiles=[]
    for g in range(4):
        hi=np.flatnonzero(hg==g);ni=np.flatnonzero(ng==g);cs=np.flatnonzero(grades==g)
        h=H[hi][:,cs].toarray();n=N[ni][:,cs].toarray();joint=np.concatenate([h,n])
        base.log('factor grade',tag,g,joint.shape)
        _,ann=base.lift(*(prev.left_kernel_mod(joint,p) for p in base.PRIMES))
        assert not np.any(exact_product(ann,joint))
        assert int(prev.mod_matrix(ann,1009).rank())==len(ann)
        projected=ann[:,len(hi):];_,piv=base.rref(projected.T,1009)
        k=np.zeros((len(piv),N.shape[0]),dtype=np.int64);k[:,ni]=projected[piv]
        l=np.zeros((len(piv),H.shape[0]),dtype=np.int64);l[:,hi]=-ann[piv,:len(hi)]
        Ks.append(k);Ls.append(l)
        profiles.append([prev.rank_exact(h),prev.rank_exact(n),len(joint)-len(ann)])
    K=np.concatenate(Ks);L=np.concatenate(Ls)
    assert np.array_equal(exact_product(K,N),exact_product(L,H))
    base.log('factor result',tag,K.shape,profiles)
    return K,L,profiles


def certificate(output=None):
    started=time.monotonic()
    quotients={};quotient_records={}
    for tag in ('source','neighbor'):
        quotients[tag]={};quotient_records[tag]={}
        for n in (7,8,9):
            q,records=quotient_exact(n,SUPPORTS[tag][n])
            assert len(q)==EXPECTED[tag][n]
            quotients[tag][n]=q;quotient_records[tag][str(n)]=records
    source,target=quotients['source'],quotients['neighbor']
    transports={};transport_records={}
    for n in (7,8,9):
        width=4*3**(n-3)
        a,b=source[n][:,5*width:],target[n][:,5*width:]
        dimension=EXPECTED['neighbor'][n]
        assert prev.rank_exact(a)==prev.rank_exact(b)==dimension
        d,v=exact_row_factor(a,b)
        # Both supports have the same final (right outer) edge. Its image
        # in the source has zero residual and the full known core dimension.
        residual=base.residual(n-3) if n<9 else prev.residual232()
        assert not np.any(residual[:,5*width:])
        transports[n]=(d,v)
        transport_records[str(n)]={'common_edge':list(SUPPORTS['source'][n][-2:]),
                                   'dimension':dimension,'denominator':int(d),
                                   'anchor_identity_exact':True}
        base.log('common-edge transport verified',n,dimension)
    factors={};factor_records={}
    for tag,qs in quotients.items():
        H,N,dt,dn=assemble(qs[7],qs[8],qs[9],SUPPORTS[tag][9])
        K,L,profile=factor(H,N,tag)
        expected=[657,333,945] if tag=='source' else [648,324,936]
        assert profile==[expected]*4
        expected_k=180 if tag=='source' else 144
        assert prev.rank_exact(K)==expected_k
        srcdim=9*len(qs[7]);A=L[:,:srcdim];B=int(dt)*L[:,srcdim:]
        assert prev.rank_exact(A)==expected_k
        assert prev.rank_exact(B)==144
        eta=np.kron(np.eye(len(qs[7]),dtype=np.int64),np.eye(3,dtype=np.int64).ravel()[:,None])
        E=exact_product(A,eta)
        core=qs[7][:,5*324:]
        assert prev.rank_exact(core)==144
        core_embedding=exact_product(E,core)
        assert prev.rank_exact(core_embedding)==144
        assert np.array_equal(3*exact_product(A,np.kron(core,np.eye(9,dtype=np.int64))),
                              np.kron(core_embedding,np.eye(3,dtype=np.int64).ravel()[None,:]))
        # The scalar coevaluation is normalized by 1/3.
        factors[tag]=(K,A,B,E,3*int(dn),int(dn))
        factor_records[tag]={'graded_Hplus_N_joint_ranks':profile,
                             'Hplus_rank':4*expected[0],'N_rank':4*expected[1],
                             'joint_rank':4*expected[2],
                             'ambiguity_dimension':4*(expected[2]-expected[0]),
                             'determined_quotient_dimension':expected_k,
                             'core_identification_rank':144,
                             'source_scalar_identity_exact':True,
                             'endpoint_coefficient_rank':144,
                             'endpoint_sum_denominator':int(dt),'readout_denominator':int(dn)}
        assert factor_records[tag]['ambiguity_dimension']==1152
    Ks,As,Bs,Es,des,dns=factors['source']
    Kt,At,Bt,Et,det,dnt=factors['neighbor']
    assert Et.shape==(144,144) and prev.rank_exact(Et)==144
    d0,v0=transports[7];d1,v1=transports[8];d2,v2=transports[9]
    # F=Psi_source J0 Psi_neighbor^{-1}, in determined-quotient coordinates.
    df,Fn=exact_row_factor(det*exact_product(Es,v0),Et)
    Fd=des*d0*df
    assert prev.rank_exact(Fn)==144
    left=exact_product(Ks,np.kron(v1,np.eye(3,dtype=np.int64)))
    readout_defect=Fd*left-d1*exact_product(Fn,Kt)
    endpoint_defect=Fd*dnt*exact_product(Bs,v2)-dns*d2*exact_product(Fn,Bt)
    assert not np.any(readout_defect)
    assert not np.any(endpoint_defect)
    assert prev.rank_exact(left)==144
    assert prev.rank_exact(np.concatenate([Kt,left]))==144
    # Verify that the induced image is the original determined core.
    _,beta8=exact_row_factor(base.residual(5),source[8])
    beta=np.kron(beta8,np.eye(3,dtype=np.int64))
    _,beta_determined=exact_row_factor(beta,Ks)
    assert prev.rank_exact(beta_determined)==36
    assert not np.any(exact_product(beta_determined,Fn))
    base.log('readout and endpoint squares are exactly zero')
    sources=[Path(__file__),Path(paths.__file__),Path(prev.__file__),Path(base.__file__),
             base.HERE/'n8_222_minimal_refinement_certificate.py',
             base.HERE/'n8_222_decoder_continuation_certificate.py',base.HERE/'n8_222_exact_backend.cpp']
    result={'base_commit':BASE_COMMIT,
            'field':'Q and R; exact integer identities and certified characteristic-zero ranks',
            'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
            'environment':{'python':platform.python_version(),'numpy':np.__version__,
                           'scipy':scipy.__version__,'python_flint':flint.__version__},
            'supports':SUPPORTS,'quotient_dimensions':EXPECTED,
            'quotient_rank_certificates':quotient_records,
            'transport_direction':'neighbor core to source core, uniquely fixed by the shared right outer edge',
            'transports':transport_records,'readout_quotients':factor_records,
            'comparison':{'readout_defect_rank':0,'endpoint_defect_rank':0,
                          'pulled_readout_kernel_joint_rank':144,
                          'induced_core_transport_rank':144,
                          'ambiguity_transport_equality':True,
                          'core_identification_square_exact':True,
                          'endpoint_readout_square_exact':True},
            'interpretation':'J1 tensor I maps the neighbor ambiguity onto the source ambiguity; the induced quotient transport intertwines Psi, and J0 Lambda_neighbor=Lambda_source J2.',
            'scope':'The fixed right-edge ladder 122/132/142 to 212/222/232, with right insertions at final gaps 4 and 5 and the same later gap-5 readout. Source residuals of dimensions 4,12,36 remain outside these core transports.',
            'execution_mode':'Full reconstruction of all six matching quotients and all literal path/readout operators; no saved matrices or result records used as inputs.',
            'elapsed_seconds':round(time.monotonic()-started,3),'all_checks_passed':True}
    rendered=json.dumps(result,indent=2)+'\n'
    if output:Path(output).write_text(rendered)
    print(rendered,end='',flush=True)
    base.log('ALL CHECKS PASSED')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output')
    args=parser.parse_args()
    certificate(args.output)
