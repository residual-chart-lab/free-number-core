#!/usr/bin/env python3
"""Exact certificate for the three-internal-spectator word 222.

All arithmetic is integer or prime-field arithmetic. A tiny compiled backend
accelerates Gaussian elimination. Natural face coordinates avoid building
or inverting length-eight state response matrices.
"""
from pathlib import Path
from itertools import product, combinations
from functools import lru_cache
import ctypes
import subprocess
import time
import os
import json
import tempfile
import math
import hashlib
import numpy as np
from scipy import sparse

if not __debug__:
    raise RuntimeError('Certificate checks require assertions: do not run Python with -O or -OO.')

HERE = Path(__file__).resolve().parent
CACHE_ROOT = Path(os.environ.get('FREE_NUMBER_222_CACHE', str(Path(tempfile.gettempdir())/'free-number-222-certificate-v2')))
# Cache provenance changes with either implementation. Cached matrices are
# still verified below; the hash is not a substitute for a rank proof.
SOURCE_HASH = hashlib.sha256(Path(__file__).read_bytes() + (HERE/'n8_222_exact_backend.cpp').read_bytes()).hexdigest()
CACHE = CACHE_ROOT/SOURCE_HASH[:20]
CACHE.mkdir(parents=True,exist_ok=True)
SO = CACHE/'exact_backend.so'
if not SO.exists() or SO.stat().st_mtime < (HERE/'n8_222_exact_backend.cpp').stat().st_mtime:
    subprocess.run(['g++','-O3','-shared','-fPIC',str(HERE/'n8_222_exact_backend.cpp'),'-o',str(SO)],check=True)
LIB = ctypes.CDLL(str(SO))
LIB.rref.argtypes=[np.ctypeslib.ndpointer(np.int64,flags='C_CONTIGUOUS'),ctypes.c_int,ctypes.c_int,ctypes.c_int,np.ctypeslib.ndpointer(np.int32,flags='C_CONTIGUOUS')]
SIGNS=np.array([[1,1,1,1],[1,-1,1,-1],[1,-1,-1,1],[1,1,-1,-1]],dtype=np.int64)

def log(*x): print(time.strftime('%H:%M:%S'),*x,flush=True)

def rref(a,p):
    validate_prime(p)
    a=np.ascontiguousarray(a,dtype=np.int64)%p
    piv=np.empty(min(a.shape),dtype=np.int32)
    rank=LIB.rref(a,*a.shape,p,piv)
    return a[:rank],piv[:rank]

@lru_cache(None)
def validate_prime(p):
    if not 2 <= p <= 65521 or any(p % d == 0 for d in range(2,math.isqrt(p)+1)):
        raise ValueError('Use a prime between 2 and 65521.')

def kernel(a,p):
    rr,piv=rref(a,p)
    free=np.setdiff1d(np.arange(a.shape[1]),piv)
    out=np.zeros((a.shape[1],len(free)),dtype=np.int64)
    out[free,np.arange(len(free))]=1
    out[piv]=-rr[:,free]%p
    return out

def inverse(a,p):
    n=a.shape[0]
    rr,piv=rref(np.concatenate([a,np.eye(n,dtype=np.int64)],axis=1),p)
    assert np.array_equal(piv,np.arange(n))
    inv=rr[:,n:]
    assert np.array_equal(a@inv%p,np.eye(n,dtype=np.int64))
    return inv

@lru_cache(None)
def words(depth): return np.array(list(product(range(1,4),repeat=depth)),dtype=np.int64).reshape(-1,depth) if depth else np.empty((1,0),dtype=np.int64)

def grades(depth):
    return (np.arange(4)[:,None]^np.bitwise_xor.reduce(words(depth),axis=1)[None,:]).ravel()

def eval_grades(depth):
    return (np.bitwise_xor.reduce(words(depth),axis=1)[:,None]^np.arange(4)[None,:]).ravel()

def evaluate(letters,probes):
    """letters/probes are quaternion basis indices, in product order."""
    nr,nc=len(probes),len(letters[0][0])
    val=np.zeros((nr,nc),dtype=np.int64); sign=np.ones((nr,nc),dtype=np.int64)
    for typ,index in letters[1]:
        b=letters[0][index][None,:] if typ=='c' else probes[:,index,None]
        sign*=SIGNS[val,b]; val^=b
    out=np.zeros((4*nr,nc),dtype=np.int64)
    out[(4*np.arange(nr))[:,None]+val,np.arange(nc)[None,:]]=sign
    return out

@lru_cache(None)
def encoder(depth):
    vec=words(depth); h=np.repeat(np.arange(4),len(vec)); vs=np.tile(vec,(4,1))
    cs=[h]+[vs[:,i] for i in range(depth)]
    seq=[('c',0)]
    for i in reversed(range(depth)): seq += [('p',i),('c',i+1)]
    return evaluate((cs,seq),vec)

@lru_cache(None)
def natural_shadow(n,r,s):
    """Evaluate the r-face natural encoder after omitting also gap s.

    Replace the adjacent pair v_(r+1)v_r by h. Remaining n-2
    vector coefficients and h freely parametrize the onto r-face response.
    The s-deletion is performed in this literal product string.
    """
    depth=n-2; vec=words(depth)
    h=np.repeat(np.arange(4),len(vec)); vs=np.tile(vec,(4,1))
    positions=[i for i in range(1,n+1) if i not in (r,r+1)]
    cs=[h]+[vs[:,j] for j in range(depth)]
    ci={i:j+1 for j,i in enumerate(positions)}
    probed=[g for g in range(1,n) if g not in (r,s)]
    pi={g:j for j,g in enumerate(probed)}
    seq=[]
    for i in range(n,0,-1):
        if i==r: continue
        seq.append(('c',0 if i==r+1 else ci[i]))
        gap=r-1 if i==r+1 else i-1
        if gap in pi: seq.append(('p',pi[gap]))
    return evaluate((cs,seq),words(n-3))

@lru_cache(None)
def decoder(depth,p):
    j=encoder(depth); cg=grades(depth); eg=eval_grades(depth)
    inv=np.zeros_like(j)
    for g in range(4):
        cols=np.flatnonzero(cg==g); rows=np.flatnonzero(eg==g)
        inv[np.ix_(cols,rows)]=inverse(j[np.ix_(rows,cols)],p)
    return inv

def restriction(n,r,s,p):
    path=CACHE/f'restriction-{n}-{r}-{s}-{p}.npy'
    if path.exists(): return np.load(path)
    depth=n-3; jinv=decoder(depth,p); shadow=natural_shadow(n,r,s)
    cg=grades(depth); fg=grades(depth+1); eg=eval_grades(depth)
    out=np.zeros((len(cg),len(fg)),dtype=np.int64)
    for g in range(4):
        a=np.flatnonzero(cg==g); b=np.flatnonzero(eg==g); c=np.flatnonzero(fg==g)
        out[np.ix_(a,c)]=jinv[np.ix_(a,b)]@shadow[np.ix_(b,c)]%p
    np.save(path,out)
    return out

def matching(n,support,p):
    ed=4*3**(n-3); fd=3*ed
    out=np.zeros((6*ed,4*fd),dtype=np.int64)
    for i,(r,s) in enumerate(combinations(support,2)):
        for endpoint,sign in [(r,1),(s,-1)]:
            log('restriction',n,endpoint,s if endpoint==r else r,p)
            a=restriction(n,endpoint,s if endpoint==r else r,p)
            j=support.index(endpoint)
            out[i*ed:(i+1)*ed,j*fd:(j+1)*fd]=sign*a%p
    return out

def quotient(n,support,p):
    key=''.join(map(str,support)); path=CACHE/f'quotient-{n}-{key}-{p}.npz'
    if path.exists():
        z=np.load(path); return z['L'],z['D']
    d=matching(n,support,p)
    cg=np.tile(grades(n-3),6); fg=np.tile(grades(n-2),4)
    parts=[]
    for g in range(4):
        cols=np.flatnonzero(cg==g); rows=np.flatnonzero(fg==g)
        log('nullspace',n,g,len(rows),len(cols),p)
        l=kernel(d[np.ix_(cols,rows)].T,p).T
        full=np.zeros((len(l),d.shape[0]),dtype=np.int64); full[:,cols]=l
        parts.append(full); log('dimension',g,len(l))
    L=np.concatenate(parts)
    np.savez_compressed(path,L=L,D=d)
    log('quotient dimension',n,support,len(L))
    return L,d

PRIMES=(1009,1013)

def lift(a,b,scales=(1,2,4,8,16,32,64,128,256)):
    for scale in scales:
        x=scale*a%1009; x[x>504]-=1009
        y=scale*b%1013; y[y>506]-=1013
        if np.array_equal(x,y): return scale,x
    # Some auxiliary pivot choices introduce odd denominators. Reconstruct
    # each distinct coefficient modulo the product, then verify the actual
    # matrix identity at the caller; modular agreement alone is not a proof.
    modulus=1009*1013;bound=math.isqrt(modulus//2)
    values,indices=np.unique(a+1009*b,return_inverse=True)
    fractions=[]
    for value in values:
        aa=int(value)%1009;bb=int(value)//1009
        residue=aa+1009*((bb-aa)*pow(1009,-1,1013)%1013)
        if residue==0:fractions.append((0,1));continue
        r0,r1=modulus,residue;t0,t1=0,1
        while abs(r1)>bound:
            q=r0//r1;r0,r1=r1,r0-q*r1;t0,t1=t1,t0-q*t1
        num,den=r1,t1
        if den<0:num,den=-num,-den
        assert 0<den<=bound and math.gcd(num,den)==1 and (num-den*residue)%modulus==0
        fractions.append((num,den))
    scale=math.lcm(*(d for n,d in fractions))
    integers=[n*(scale//d) for n,d in fractions]
    assert max(map(abs,integers),default=0)<2**40
    return scale,np.array(integers,dtype=np.int64)[indices].reshape(a.shape)

def iszero(a):
    return a.count_nonzero()==0 if sparse.issparse(a) else not np.count_nonzero(a)

def certified_rank(a):
    """A modular minor plus an exact rational RREF reconstruction."""
    r1,p1=rref(a,1009); r2,p2=rref(a,1013)
    assert np.array_equal(p1,p2)
    if not len(p1):
        assert iszero(a); return 0
    scale,rr=lift(r1,r2)
    assert int(np.abs(a[:,p1]).sum(axis=1).max())*int(np.abs(rr).max())<2**63
    assert scale*int(np.abs(a).max())<2**63
    # Pivot columns are identity: every original row is its pivot entries
    # times the reconstructed row basis. This proves the upper rank bound.
    assert iszero(sparse.csr_matrix(a[:,p1])@sparse.csr_matrix(rr)-scale*sparse.csr_matrix(a))
    return len(p1)

def exact_quotient(n,support):
    l1,d1=quotient(n,support,1009);l2,d2=quotient(n,support,1013)
    ls,L=lift(l1,l2);ds,D=lift(d1,d2)
    assert ds==1
    assert int(np.abs(L).max())<=100 and int(np.abs(D).max())<=1
    assert iszero(sparse.csr_matrix(L)@sparse.csr_matrix(D))
    # The exact matching maps factor literal quaternionic response maps.
    ed=4*3**(n-3);fd=3*ed;j=encoder(n-3)
    for i,(r,s) in enumerate(combinations(support,2)):
        for ix,endpoint in enumerate(support):
            if endpoint not in (r,s):
                assert iszero(D[i*ed:(i+1)*ed,ix*fd:(ix+1)*fd])
        for endpoint,sign in [(r,1),(s,-1)]:
            ix=support.index(endpoint)
            block=D[i*ed:(i+1)*ed,ix*fd:(ix+1)*fd]
            actual=(sparse.csr_matrix(block).T@j.T).T
            assert np.array_equal(actual,sign*natural_shadow(n,endpoint,s if endpoint==r else r))
    # Recompute the lower rank bound even when L and D came from a cache.
    # L*D=0 and full row rank of L alone do not prove L is complete.
    cg=np.tile(grades(n-3),6);fg=np.tile(grades(n-2),4)
    block_indices=[]
    for g in range(4):
        rows=np.flatnonzero(cg==g);cols=np.flatnonzero(fg==g)
        assert iszero(D[np.ix_(rows,np.flatnonzero(fg!=g))])
        block_indices.append((rows,cols))
    for p in PRIMES:
        rank=sum(len(rref(D[np.ix_(rows,cols)],p)[1]) for rows,cols in block_indices)
        assert rank==D.shape[0]-len(L), 'cached annihilator is not the full quotient'
    assert len(rref(L,1009)[1])==len(L)
    log('exact quotient certified',n,support,len(L),'matching rank',D.shape[0]-len(L),'L scale',ls)
    return L,D

def epsilon(depth):
    assert depth in (4,5)
    out=np.zeros((4 if depth==4 else 12,4*3**depth),dtype=np.int64)
    for a,b,h in product(range(3),range(3),range(4)):
        for z in (range(3) if depth==5 else [None]):
            seq=(a,a,b,b) if z is None else (a,a,z,b,b)
            ix=0
            for v in seq:ix=3*ix+v
            row=h if z is None else 4*z+h
            out[row,4*ix+h]=1
    return out

def residual(depth):
    b=epsilon(depth)@encoder(depth)
    return np.concatenate([s*b for s in (0,1,-1,-1,1,0)],axis=1)

@lru_cache(None)
def suspension_eval(pos,hand='right'):
    """Insert the central argument, using F*z*w (right) or w*z*F (left).

    Source order is (old coefficient, new vector). This is a chosen local
    decoder operation. It is NOT asserted to be a chain map on full
    tetrahedral complexes when the inserted argument is internal.
    """
    vec=words(5);h=np.repeat(np.arange(4),len(vec));vs=np.tile(vec,(4,1))
    cs=[h]+[vs[:,i] for i in range(5)]
    ps=[i for i in range(5) if i!=pos];seq=[('c',0)]
    for i in reversed(range(4)):seq += [('p',ps[i]),('c',i+1)]
    seq=seq+[('p',pos),('c',5)] if hand=='right' else [('c',5),('p',pos)]+seq
    return evaluate((cs,seq),words(5))

@lru_cache(None)
def exact_suspension(pos,hand='right'):
    ev=suspension_eval(pos,hand)
    a=decoder(5,1009)@ev%1009;b=decoder(5,1013)@ev%1013
    scale,I=lift(a,b)
    assert scale<=100 and int(np.abs(I).max())<=100
    assert np.array_equal((sparse.csr_matrix(I).T@encoder(5).T).T,scale*ev)
    return scale,I

def primitive_checks():
    # Multiplication conventions and the paired-probe identity driving both
    # residuals: sum_a e_a*v*e_a=v, for v in Im(H).
    assert SIGNS[1,2]==1 and SIGNS[2,1]==-1
    for v in (1,2,3):
        out=np.zeros(4,dtype=np.int64)
        for a in (1,2,3):
            out[a^v^a]+=SIGNS[a,v]*SIGNS[a^v,a]
        want=np.eye(4,dtype=np.int64)[:,v]
        assert np.array_equal(out,want)
    assert certified_rank(encoder(1))==12

def certificate(output=None):
    primitive_checks()
    parent=(1,3,4,6);child=(1,3,5,7)
    l,d=exact_quotient(7,parent);L,D=exact_quotient(8,child)
    assert len(l)==148 and len(L)==444
    k=residual(4);K=residual(5)
    assert iszero(sparse.csr_matrix(k)@sparse.csr_matrix(d))
    assert iszero(sparse.csr_matrix(K)@sparse.csr_matrix(D))
    assert certified_rank(k)==4 and certified_rank(K)==12
    ed=972
    edge_ranks=[]
    for i,e in enumerate(combinations(child,2)):
        rank=certified_rank(L[:,i*ed:(i+1)*ed]);edge_ranks.append(rank)
        log('certified edge rank',e,rank)
    assert edge_ranks==[432,336,408,120,336,432]
    outer=np.concatenate([L[:,:ed],L[:,5*ed:]],axis=1)
    assert certified_rank(outer)==432
    assert certified_rank(np.concatenate([l[:,:324],l[:,5*324:]],axis=1))==144
    # Outer edge images equal ker(kappa) in each quotient, by dimensions.
    # Check both generic parents reach that exact same 432-dimensional core.
    parent_records=[]
    for word,support,new,ei,hand in [
        ('122',(1,2,4,6),2,0,'right'),
        ('221',(1,3,5,6),6,5,'left'),
    ]:
        lp,dp=exact_quotient(7,support)
        assert len(lp)==144
        edge=tuple(combinations(child,2))[ei]
        pos=[g for g in range(1,8) if g not in edge].index(new)
        scale,I=exact_suspension(pos,hand)
        A=(sparse.csr_matrix(L[:,ei*ed:(ei+1)*ed])@sparse.csr_matrix(I)).toarray()
        B=np.kron(lp[:,ei*324:(ei+1)*324],np.eye(3,dtype=np.int64))
        assert certified_rank(A)==432 and certified_rank(B)==432
        assert certified_rank(np.concatenate([A,B]))==432
        # Same kernel gives a unique descended isomorphism to the child
        # outer-edge image. No choice of a complementary core projection.
        parent_records.append({'word':word,'new_spectator':new,'edge':list(edge),'rank':432,'kernel_dimension':0})
        log('generic parent core transport certified',word)
    # Full central-slot right suspension and its exact residual square.
    theta=encoder(1)  # H tensor V -> Hom(V,H), k tensor w |-> (z |-> k z w).
    Ablocks=[];scales=[];suspensions=[]
    for ei,edge in enumerate(combinations(child,2)):
        pos=[g for g in range(1,8) if g not in edge].index(4)
        scale,I=exact_suspension(pos,'right');scales.append(scale);suspensions.append(I)
        lhs=sparse.csr_matrix(K[:,ei*ed:(ei+1)*ed])@sparse.csr_matrix(I)
        rhs=scale*theta@np.kron(k[:,ei*324:(ei+1)*324],np.eye(3,dtype=np.int64))
        assert np.array_equal(lhs.toarray(),rhs)
    common=int(np.lcm.reduce(scales))
    for ei,(scale,I) in enumerate(zip(scales,suspensions)):
        Ablocks.append((sparse.csr_matrix(L[:,ei*ed:(ei+1)*ed])@sparse.csr_matrix((common//scale)*I)).toarray())
    A=np.concatenate(Ablocks,axis=1)
    obstruction=(sparse.csr_matrix(A)@sparse.kron(sparse.csr_matrix(d),sparse.eye(3,dtype=np.int64))).toarray()
    # The exact residual square forces the image into ker(K)=T_222,
    # so its rank is at most 432. A modular 432-minor proves equality.
    for p in PRIMES: assert len(rref(obstruction,p)[1])==432
    log('full-suspension obstruction rank certified',432)
    # Fixed unit w gives an injective H -> Hom(V,H): f(w)=-k.
    for w in range(3):
        fixed=theta[:,[3*h+w for h in range(4)]]
        assert certified_rank(fixed)==4
        assert np.array_equal(fixed[4*w:4*w+4],-np.eye(4,dtype=np.int64))
    witness=np.argwhere(obstruction!=0)[0]
    result={
        'base_commit':'09b77f329d0c825c794443a0cd98cde89d8f1d73',
        'field':'Q (exact integer identities plus modular nonzero minors)',
        'primes':list(PRIMES),'child_word':'222','child_support':list(child),
        'certificate_source_sha256':SOURCE_HASH,
        'matching_lower_bound_recomputed':True,
        'source_edge_dimension':5832,'matching_rank':5388,'quotient_dimension':444,
        'edge_order':[list(e) for e in combinations(child,2)],'edge_ranks':edge_ranks,
        'common_outer_core_dimension':432,'residual_dimension':12,
        'residual_operator_rank':12,'residual_operator_kernel_in_E_dimension':5820,
        'residual_operator_kernel_in_Y_dimension':432,
        'generic_parent_core_transports':parent_records,
        'residual_bridge_domain_dimension':12,'residual_bridge_rank':12,'residual_bridge_kernel_dimension':0,
        'fixed_unit_vector_bridge_rank':4,'fixed_unit_vector_bridge_kernel_dimension':0,
        'full_central_suspension_descends':False,'full_suspension_obstruction_rank':432,
        'full_suspension_common_denominator':common,
        'integer_obstruction_witness':{'row':int(witness[0]),'column':int(witness[1]),'value':int(obstruction[tuple(witness)])},
        'claim_boundary':'An explicitly chosen central-slot right decoder induces an isomorphism of residual quotients. Its full quotient descent fails; no time update, curvature, or choice-independent full residual-to-core transport is proved.',
    }
    if output: Path(output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2),flush=True)
    log('ALL CHECKS PASSED')
    return result

def main():
    import argparse
    a=argparse.ArgumentParser(); a.add_argument('--prime',type=int,default=1009); a.add_argument('--n',type=int,default=8)
    a.add_argument('--certificate',action='store_true');a.add_argument('--output')
    args=a.parse_args()
    if args.certificate:
        certificate(args.output);return
    support=(1,3,5,7) if args.n==8 else (1,3,4,6)
    l,d=quotient(args.n,support,args.prime)
    log('DONE',args.n,l.shape,d.shape)

if __name__=='__main__': main()
