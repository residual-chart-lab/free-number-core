#!/usr/bin/env python3
"""Note 33: stationary-edge transport around a four-placement readout cell.

All twelve matching quotients and literal path/readout operators are rebuilt.
Requires the Note 32 dependencies; saved results are never proof inputs.
"""
from pathlib import Path
from itertools import combinations
import argparse
import hashlib
import json
import platform
import time
import numpy as np
import scipy
import flint
import n9_adjacent_core_transport_certificate as adjacent
from n8_222_minimal_refinement_certificate import exact_product, exact_row_factor

base, prev = adjacent.base, adjacent.prev
if not __debug__:
    raise RuntimeError('Assertions must remain enabled.')

BASE_COMMIT = '4c6aa068e9844be940a676eaa9da661af42397d7'
SUPPORTS = {
    '122': {7: (1,2,4,6), 8: (1,2,5,7), 9: (1,2,6,8)},
    '131': {7: (1,2,5,6), 8: (1,2,6,7), 9: (1,2,7,8)},
    '221': {7: (1,3,5,6), 8: (1,3,6,7), 9: (1,3,7,8)},
    '212': {7: (1,3,4,6), 8: (1,3,5,7), 9: (1,3,6,8)},
}
EDGES = [('122','131','left'), ('131','221','right'),
         ('122','212','right'), ('212','221','left')]


def rat(den, num):
    den = int(den)
    assert den > 0
    num = np.asarray(num, dtype=np.int64)
    divisor = int(np.gcd(den, np.gcd.reduce(np.abs(num).ravel())))
    return den//divisor, num//divisor


def compose(a, b):
    return rat(a[0]*b[0], exact_product(a[1], b[1]))


def difference(a, b):
    den = int(np.lcm(a[0], b[0]))
    return rat(den, (den//a[0])*a[1] - (den//b[0])*b[1])


def solve_injective(a, b):
    """Solve a x=b; transpose row factor also verifies the entire identity."""
    den, num = exact_row_factor(b[1].T, a[1].T)
    return rat(b[0]*den, a[0]*num.T)


def core_coordinates(q, n):
    """Fix a core basis by row coordinates on the right outer edge."""
    width = 4*3**(n-3)
    edge = q[:,5*width:]
    _, rows = base.rref(edge.T, 1009)
    dim = 144*3**(n-7)
    assert len(rows) == dim
    # The selected rows are a full-rank quotient of the shared response
    # block; an exact factor proves that they span its full row space.
    den, embedding = exact_row_factor(edge, edge[rows])
    assert np.array_equal(embedding[rows], den*np.eye(dim, dtype=np.int64))
    # Independently check the left edge has this very same core image.
    left = q[:,:width]
    assert prev.rank_exact(left[rows]) == dim
    assert np.array_equal(exact_product(embedding, left[rows]), den*left)
    return rows, rat(den, embedding)


def certificate(output=None, checkpoint_dir=None):
    started = time.monotonic()
    qs, cores, qrecords = {}, {}, {}
    for tag, supports in SUPPORTS.items():
        qs[tag], cores[tag], qrecords[tag] = {}, {}, {}
        for n, support in supports.items():
            q, record = adjacent.quotient_exact(n, support)
            expected = (148 if tag == '212' else 144)*3**(n-7)
            assert len(q) == expected
            rows, emb = core_coordinates(q, n)
            qs[tag][n], cores[tag][n] = q, (rows, emb)
            qrecords[tag][n] = {'dimension':len(q), 'core_dimension':len(rows),
                               'embedding_denominator':emb[0], 'grades':record}
            if checkpoint_dir:
                np.savez_compressed(Path(checkpoint_dir)/f'q-{tag}-{n}.npz', q=q,
                                    rows=rows, embedding=emb[1], denominator=emb[0])
            base.log('both core anchors verified', tag, n, len(rows))

    maps, trecords = {}, {}
    for src, dst, side in EDGES:
        key = src+'->'+dst
        maps[key], trecords[key] = {}, {}
        for n in (7,8,9):
            width = 4*3**(n-3)
            idx = 0 if side == 'left' else 5
            common = list(combinations(SUPPORTS[src][n],2))[idx]
            assert common == list(combinations(SUPPORTS[dst][n],2))[idx]
            sr, _ = cores[src][n]; dr, _ = cores[dst][n]
            a = qs[src][n][sr,idx*width:(idx+1)*width]
            b = qs[dst][n][dr,idx*width:(idx+1)*width]
            g = rat(*exact_row_factor(b,a))
            assert prev.rank_exact(g[1]) == len(sr)
            maps[key][n] = g
            trecords[key][n] = {'common_edge':common, 'rank':len(sr),
                                 'denominator':g[0], 'anchor_identity_exact':True}
            base.log('independent transport',key,n,g[0])

    cells = {}
    for n in (7,8,9):
        upper = compose(maps['131->221'][n], maps['122->131'][n])
        lower = compose(maps['212->221'][n], maps['122->212'][n])
        defect = difference(upper, lower)
        rank = prev.rank_exact(defect[1]) if np.any(defect[1]) else 0
        cells[n] = {'dimension':len(upper[1]), 'two_route_defect_rank':rank,
                     'upper_denominator':upper[0], 'lower_denominator':lower[0]}
        base.log('CELL DEFECT',n,rank)

    laws, lrecords = {}, {}
    for tag, q in qs.items():
        H, N, dt, dn = adjacent.assemble(q[7],q[8],q[9],SUPPORTS[tag][9])
        K, L, profile = adjacent.factor(H,N,tag)
        srcdim = 9*len(q[7])
        A, B = L[:,:srcdim], int(dt)*L[:,srcdim:]
        eta = np.kron(np.eye(len(q[7]),dtype=np.int64),
                     np.eye(3,dtype=np.int64).ravel()[:,None])
        E = exact_product(A,eta)
        _, c7 = cores[tag][7]; _, c8 = cores[tag][8]; _, c9 = cores[tag][9]
        psi = compose((3*int(dn),E),c7)
        assert prev.rank_exact(psi[1]) == 144
        # Independently certify the source's scalar-contraction law.
        assert np.array_equal(3*exact_product(A,np.kron(c7[1],np.eye(9,dtype=np.int64))),
                              np.kron(exact_product(E,c7[1]),np.eye(3,dtype=np.int64).ravel()[None,:]))
        core_readout = compose((1,K),(c8[0],np.kron(c8[1],np.eye(3,dtype=np.int64))))
        endpoint = compose((int(dn),B),c9)
        D = solve_injective(psi,core_readout)
        Lam = solve_injective(psi,endpoint)
        assert prev.rank_exact(D[1]) == prev.rank_exact(Lam[1]) == 144
        ambiguity = sum(r[2]-r[0] for r in profile)
        assert ambiguity == 1152
        laws[tag] = {'D':D,'Lambda':Lam,'Psi':psi}
        lrecords[tag] = {'graded_Hplus_N_joint_ranks':profile,
                          'Hplus_rank':sum(r[0] for r in profile),
                          'N_rank':sum(r[1] for r in profile),
                          'joint_rank':sum(r[2] for r in profile),
                          'ambiguity_dimension':ambiguity,
                          'determined_quotient_dimension':len(K),
                          'determined_core_dimension':144,
                          'source_scalar_identity_exact':True,
                          'endpoint_coefficient_rank':144,
                          'D_denominator':D[0],'Lambda_denominator':Lam[0],
                          'Psi_denominator':psi[0]}
        if checkpoint_dir:
            np.savez_compressed(Path(checkpoint_dir)/f'law-{tag}.npz',
                                D=D[1],Dd=D[0],Lambda=Lam[1],Ld=Lam[0])
        base.log('core law reconstructed',tag,lrecords[tag])

    comparisons = {}
    for src,dst,side in EDGES:
        key = src+'->'+dst
        g7,g8,g9 = (maps[key][n] for n in (7,8,9))
        gr = (g8[0],np.kron(g8[1],np.eye(3,dtype=np.int64)))
        rd = difference(compose(laws[dst]['D'],gr),compose(g7,laws[src]['D']))
        ed = difference(compose(laws[dst]['Lambda'],g9),compose(g7,laws[src]['Lambda']))
        ranks = [prev.rank_exact(d[1]) if np.any(d[1]) else 0 for d in (rd,ed)]
        comparisons[key] = {'readout_defect_rank':ranks[0], 'endpoint_defect_rank':ranks[1]}
        base.log('NATURALITY DEFECTS',key,ranks)

    sources = [Path(__file__),Path(adjacent.__file__),Path(adjacent.paths.__file__),
               Path(prev.__file__),Path(base.__file__),
               base.HERE/'n8_222_minimal_refinement_certificate.py',
               base.HERE/'n8_222_decoder_continuation_certificate.py',
               base.HERE/'n8_222_exact_backend.cpp']
    result = {'base_commit':BASE_COMMIT, 'field':'Q and R',
              'sources_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
              'environment':{'python':platform.python_version(),'numpy':np.__version__,
                             'scipy':scipy.__version__,'python_flint':flint.__version__},
              'supports':SUPPORTS,'quotients':qrecords,'transports':trecords,
              'cells':cells,'readout_laws':lrecords,'adjacent_comparisons':comparisons,
              'execution_mode':'All twelve matching quotients and literal path/readout operators rebuilt; no saved matrix or result is an input.',
              'elapsed_seconds':round(time.monotonic()-started,3),'all_checks_passed':True}
    rendered = json.dumps(result,indent=2)+'\n'
    if output: Path(output).write_text(rendered)
    print(rendered,end='',flush=True)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output')
    parser.add_argument('--checkpoint-dir',help='Optional output-only intermediate matrices.')
    args = parser.parse_args()
    certificate(args.output,args.checkpoint_dir)
