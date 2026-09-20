#!/usr/bin/env python3
"""Note 29: exact 222 -> 232 continuation and minimal retained state.

Requires NumPy, SciPy, python-flint and the Note 26 g++ backend. New n=9
matching maps are reconstructed from literal quaternionic responses on
every run. Stored result JSONs and exploratory matrices are never inputs.
"""
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import json
import time
import hashlib
import argparse
import platform
import numpy as np
import scipy
from scipy import sparse
import flint
import n8_222_redetection_certificate as base
from n8_222_decoder_continuation_certificate import cap_primitive, direct_caps
from n8_222_minimal_refinement_certificate import exact_product

if not __debug__:
    raise RuntimeError('Assertions must be enabled.')

BASE_COMMIT = 'cb23eb4258396bb1d248972c2f86da084d200f67'


@lru_cache(None)
def decoder_numerator(depth):
    """Explicit recursive local decoder, denominator 2**depth.

    Coefficient order (h,v1,...,vm), evaluation order (x1,...,xm,h).
    Each recursion decodes the first probe using Note 28's local formula.
    """
    if depth == 0:
        return sparse.eye(4, dtype=np.int64, format='csr')
    old = decoder_numerator(depth-1).tocoo()
    count = 3**(depth-1)
    primitive = cap_primitive()
    rows, cols, data = [], [], []
    for a in range(3):
        for h in range(4):
            selected = old.col % 4 == h
            rr, cc, vv = old.row[selected], old.col[selected], old.data[selected]
            for e in np.flatnonzero(primitive[3*h+a]):
                rows.append((rr//count)*(3*count)+a*count+rr%count)
                cols.append((e//4)*(4*count)+(cc//4)*4+e%4)
                data.append(vv*primitive[3*h+a,e])
    return sparse.coo_matrix((np.concatenate(data),(np.concatenate(rows),np.concatenate(cols))),
                             shape=(12*count,12*count)).tocsr()


def restriction_exact(n, r, s):
    depth = n-3
    dec = decoder_numerator(depth)
    shadow = base.natural_shadow(n,r,s)
    result = dec @ sparse.csr_matrix(shadow)
    assert np.all(result.data % (2**depth) == 0)
    result.data //= 2**depth
    result.eliminate_zeros()
    assert np.array_equal((result.T @ base.encoder(depth).T).T, shadow)
    base.natural_shadow.cache_clear()
    return result


def matching_exact(n, support):
    blocks = []
    ed=4*3**(n-3)
    for r,s in combinations(support,2):
        row=[]
        for endpoint in support:
            if endpoint in (r,s):
                base.log('exact restriction',n,endpoint,s if endpoint==r else r)
                block=restriction_exact(n,endpoint,s if endpoint==r else r)
                row.append(block if endpoint==r else -block)
            else:
                row.append(sparse.csr_matrix((ed,3*ed),dtype=np.int64))
        blocks.append(row)
    return sparse.bmat(blocks,format='csr')


def mod_matrix(a,p):
    a=np.asarray(a,dtype=np.int64)%p
    return flint.nmod_mat(a.shape[0],a.shape[1],a.ravel().tolist(),p)


def left_kernel_mod(a,p):
    matrix=mod_matrix(a.T,p)
    null, count=matrix.nullspace()
    out=np.empty((count,a.shape[0]),dtype=np.int64)
    for i in range(count):
        for j in range(a.shape[0]):
            out[i,j]=int(null[j,i])
    return out


def quotient_exact(n,support):
    D=matching_exact(n,support)
    assert np.max(np.abs(D.data))==1
    cg=np.tile(base.grades(n-3),6)
    fg=np.tile(base.grades(n-2),4)
    pieces=[]
    for g in range(4):
        rows=np.flatnonzero(cg==g);cols=np.flatnonzero(fg==g)
        assert D[rows][:,fg!=g].nnz==0
        block=D[rows][:,cols].toarray()
        kernels=[]
        for p in base.PRIMES:
            base.log('left kernel',n,g,p,block.shape)
            ker=left_kernel_mod(block,p)
            base.log('nullity',len(ker))
            kernels.append(ker)
        den,ker=base.lift(*kernels)
        assert np.count_nonzero((D[rows].T @ ker.T).T)==0
        assert mod_matrix(ker,base.PRIMES[0]).rank()==len(ker)
        full=np.zeros((len(ker),D.shape[0]),dtype=np.int64)
        full[:,rows]=ker
        pieces.append(full)
    Q=np.concatenate(pieces)
    base.log('exact quotient',n,support,Q.shape)
    return Q,D


@lru_cache(None)
def suspension(depth,pos):
    """Literal right insertion F(...)*z*w, in right-decoded coordinates."""
    vec=base.words(depth)
    h=np.repeat(np.arange(4),len(vec));vs=np.tile(vec,(4,1))
    cs=[h]+[vs[:,i] for i in range(depth)]
    ps=[i for i in range(depth) if i!=pos]
    seq=[('c',0)]
    for i in reversed(range(depth-1)):
        seq += [('p',ps[i]),('c',i+1)]
    seq += [('p',pos),('c',depth)]
    evaluations=base.evaluate((cs,seq),vec)
    numerator=decoder_numerator(depth) @ sparse.csr_matrix(evaluations)
    denominator=2**depth
    div=int(np.gcd(denominator,np.gcd.reduce(np.abs(numerator.data))))
    numerator.data //= div
    denominator //= div
    assert np.array_equal((numerator.T @ base.encoder(depth).T).T,denominator*evaluations)
    return denominator,numerator


def retained_child():
    parent_q,_=base.exact_quotient(7,(1,3,4,6))
    child_q,_=base.exact_quotient(8,(1,3,5,7))
    q=np.kron(parent_q,np.eye(3,dtype=np.int64))
    blocks=[]
    for ei,edge in enumerate(combinations((1,3,5,7),2)):
        pos=[g for g in range(1,8) if g not in edge].index(4)
        den,cap=direct_caps(pos)
        blocks.append((den,exact_product(q[:,ei*972:(ei+1)*972],cap)))
    common=int(np.lcm.reduce([d for d,a in blocks]))
    readout=np.concatenate([(common//d)*a for d,a in blocks],axis=1)
    return np.concatenate([child_q,readout])


def forward_output(Q,new_gap=5):
    blocks=[]
    for ei,edge in enumerate(combinations((1,3,6,8),2)):
        pos=[g for g in range(1,9) if g not in edge].index(new_gap)
        den,sigma=suspension(6,pos)
        a=(sigma.T @ Q[:,ei*2916:(ei+1)*2916].T).T
        blocks.append((den,a))
    common=int(np.lcm.reduce([d for d,a in blocks]))
    return common,np.concatenate([(common//d)*a for d,a in blocks],axis=1)


def residual232():
    epsilon=np.zeros((36,2916),dtype=np.int64)
    for a in range(3):
        for b in range(3):
            for z in range(3):
                for w in range(3):
                    ix=0
                    for v in (a,a,z,w,b,b):
                        ix=3*ix+v
                    for h in range(4):
                        epsilon[4*(3*z+w)+h,4*ix+h]=1
    block=exact_product(epsilon,base.encoder(6))
    return np.concatenate([s*block for s in (0,1,-1,-1,1,0)],axis=1)


def rank_exact(a):
    """An exact left annihilator plus modular lower bounds proves rank."""
    kernels=[left_kernel_mod(a,p) for p in base.PRIMES]
    den,ker=base.lift(*kernels)
    assert np.count_nonzero(exact_product(ker,a))==0
    assert mod_matrix(ker,base.PRIMES[0]).rank()==len(ker)
    return a.shape[0]-len(ker)


def first_witness(h,f,global_columns):
    """Find an exact lost input with nonzero forward output."""
    rrefs=[]
    pivots=[]
    for p in base.PRIMES:
        rr,rank=mod_matrix(h,p).rref()
        a=np.array([[int(rr[i,j]) for j in range(h.shape[1])] for i in range(rank)],dtype=np.int64)
        piv=np.array([np.flatnonzero(row)[0] for row in a])
        rrefs.append(a);pivots.append(piv)
    assert np.array_equal(*pivots)
    piv=pivots[0]
    free=np.setdiff1d(np.arange(h.shape[1]),piv)
    for col in free:
        candidates=[]
        for rr,p in zip(rrefs,base.PRIMES):
            v=np.zeros((h.shape[1],1),dtype=np.int64)
            v[col,0]=1
            v[piv,0]=-rr[:,col]%p
            candidates.append(v)
        if not np.any((f @ candidates[0])%base.PRIMES[0]):
            continue
        try:
            den,v=base.lift(*candidates)
        except AssertionError:
            continue
        assert not np.any(exact_product(h,v))
        out=exact_product(f,v)
        assert np.any(out)
        ix=int(np.flatnonzero(out[:,0])[0])
        return {'input_coordinates':[[int(global_columns[i]),int(v[i,0])] for i in np.flatnonzero(v[:,0])],
                'output_local_row':ix,'output_numerator':int(out[ix,0]),
                'retained_zero':True,'output_nonzero':True}
    raise AssertionError('No reconstructible witness found')


def row_grades(matrix,grades):
    matrix=sparse.csr_matrix(matrix)
    out=np.full(matrix.shape[0],-1,dtype=np.int64)
    for i in range(matrix.shape[0]):
        start,end=matrix.indptr[i:i+2]
        values=np.unique(grades[matrix.indices[start:end]])
        assert len(values)<=1
        if len(values): out[i]=values[0]
    return out


def graded_rank(matrix,grades):
    rows=row_grades(matrix,grades)
    matrix=sparse.csr_matrix(matrix)
    return [rank_exact(matrix[rows==g][:,grades==g].toarray()) for g in range(4)]


def certificate(output=None):
    started=time.monotonic()
    base.primitive_checks()
    for depth in (1,4,5,6):
        dec=decoder_numerator(depth)
        identity=dec @ sparse.csr_matrix(base.encoder(depth))
        assert (identity-(2**depth)*sparse.eye(identity.shape[0],dtype=np.int64)).nnz==0
        base.log('recursive decoder verified',depth)
    Q,D=quotient_exact(9,(1,3,6,8))
    assert Q.shape==(1332,17496)
    assert D.shape==(17496,34992)
    K=residual232()
    assert not np.any(exact_product(K,D))
    assert rank_exact(K)==36
    target_grades=np.tile(base.grades(6),6)
    outer=np.concatenate([Q[:,:2916],Q[:,-2916:]],axis=1)
    outer_ranks=graded_rank(outer,np.tile(base.grades(6),2))
    assert outer_ranks==[324]*4
    assert not np.any(K[:,:2916]) and not np.any(K[:,-2916:])

    # Paired collapse commutes with the fixed new-gap-5 right insertion.
    bridge=np.kron(np.eye(3,dtype=np.int64),base.encoder(1))
    old_residual=base.residual(5)
    for ei,edge in enumerate(combinations((1,3,6,8),2)):
        pos=[g for g in range(1,9) if g not in edge].index(5)
        sd,sigma=suspension(6,pos)
        lhs=exact_product(K[:,ei*2916:(ei+1)*2916],sigma)
        rhs=sd*exact_product(bridge,np.kron(old_residual[:,ei*972:(ei+1)*972],np.eye(3,dtype=np.int64)))
        assert np.array_equal(lhs,rhs)
    assert rank_exact(bridge)==36
    base.log('new residual and exact continuation square verified')

    retained=retained_child()
    H=sparse.kron(sparse.csr_matrix(retained),sparse.eye(3,dtype=np.int64),format='csr')
    den,F=forward_output(Q)
    grades=np.repeat(np.tile(base.grades(5),6),3)^np.tile(np.arange(1,4),5832)
    hgrades=row_grades(H,grades);fgrades=row_grades(F,grades)
    totals=[]
    witness=None
    for g in range(4):
        cols=np.flatnonzero(grades==g)
        h=H[hgrades==g][:,cols].toarray()
        f=F[np.ix_(fgrades==g,cols)]
        base.log('joint rank',g,h.shape,f.shape)
        ranks=[rank_exact(h),rank_exact(f),rank_exact(np.concatenate([h,f]))]
        base.log('exact ranks retained/output/joint',g,ranks)
        totals.append(ranks)
        if witness is None and ranks[2]>ranks[0]:
            witness=first_witness(h,f,cols)
    assert totals==[[657,333,981]]*4
    ranks=np.sum(totals,axis=0).tolist()
    assert ranks==[2628,1332,3924]
    v=np.zeros((17496,1),dtype=np.int64)
    for index,value in witness['input_coordinates']:
        v[index,0]=value
    assert not np.any(exact_product(H,v))
    response=exact_product(F,v)
    outrow=int(np.flatnonzero(response[:,0])[0])
    assert np.any(response)
    assert all(index%3==0 for index,value in witness['input_coordinates'])
    del witness['output_local_row']
    witness.update({'fixed_new_vector':'i','output_row':outrow,
                    'output_numerator':int(response[outrow,0]),'output_denominator':den})
    sources=[Path(__file__).resolve(),Path(base.__file__).resolve(),
             base.HERE/'n8_222_decoder_continuation_certificate.py',
             base.HERE/'n8_222_minimal_refinement_certificate.py',
             base.HERE/'n8_222_exact_backend.cpp']
    result={
        'base_commit':BASE_COMMIT,
        'field':'Q and R, exact integer identities and certified rational ranks',
        'primes':list(base.PRIMES),
        'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'environment':{'python':platform.python_version(),'numpy':np.__version__,
                       'scipy':scipy.__version__,'python_flint':flint.__version__},
        'operation':{'parent_word':'222','child_word':'232','child_support':[1,3,6,8],
                     'inserted_actual_gap':5,'hand':'right','formula':'F(old probes) z w',
                     'raw_common_denominator':den},
        'raw_input_dimension':17496,
        'child_matching_rank':16164,
        'child_quotient_dimension':1332,
        'child_outer_core_dimension':1296,
        'child_residual_dimension':36,
        'residual_square_verified':True,
        'rank_profiles_retained_output_joint':totals,
        'old_refinement_dimension':876,
        'tensor_extended_retained_dimension':2628,
        'forward_descends_to_retained_state':False,
        'new_obstruction_rank':1296,
        'new_obstruction_equals_full_outer_core':True,
        'minimal_refinement_dimension':3924,
        'safe_relation_dimension_before':14868,
        'safe_relation_dimension_after':13572,
        'refined_update_kernel_dimension':2592,
        'fixed_vector_counterexample':witness,
        'elapsed_seconds':round(time.monotonic()-started,3),
        'scope':'Fixed new-gap-5 right insertion 222 -> 232 with full V input; minimal linear refinement preserving the Note 28 retained state and this prescribed full output.',
        'all_checks_passed':True,
    }
    rendered=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if output: Path(output).write_text(rendered)
    print(rendered,end='',flush=True)
    base.log('ALL CHECKS PASSED')
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output')
    args=parser.parse_args()
    certificate(args.output)
