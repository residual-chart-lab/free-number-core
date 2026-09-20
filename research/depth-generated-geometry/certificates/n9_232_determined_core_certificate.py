#!/usr/bin/env python3
"""Note 31: symmetric endpoint law and the recovered 144-dimensional core.

Reconstructs literal operators and quotients; stored result files are not
inputs. Uses the Note 29 dependencies and exact characteristic-zero checks.
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

BASE_COMMIT = '65fa8fa94bd82747ce5fa4041dc1f113771dafce'


def assemble():
    Q, _ = prev.quotient_exact(9, (1, 3, 6, 8))
    q7, _ = base.exact_quotient(7, (1, 3, 4, 6))
    q8, _ = base.exact_quotient(8, (1, 3, 5, 7))
    S = sparse.kron(q7, sparse.eye(9, dtype=np.int64), format='csr')
    forward_ab, forward_ba, readout = [], [], []
    for ei, edge in enumerate(combinations((1, 3, 6, 8), 2)):
        probes = [g for g in range(1, 9) if g not in edge]
        pa, pb = probes.index(4), probes.index(5)
        da, a = paths.path(pa, pb, 'ab')
        db, b = paths.path(pa, pb, 'ba')
        child = sparse.csr_matrix(Q[:, ei*2916:(ei+1)*2916])
        forward_ab.append((da, child @ a))
        forward_ba.append((db, child @ b))
        dr, cr = paths.cap(6, pb)
        parent = sparse.kron(q8[:, ei*972:(ei+1)*972],
                             sparse.eye(3, dtype=np.int64), format='csr')
        readout.append((dr*db, parent @ cr @ b))

    def join(blocks):
        den = int(np.lcm.reduce([d for d, _ in blocks]))
        return den, sparse.hstack([(den//d)*sparse.csr_matrix(a)
                                   for d, a in blocks], format='csr')

    da, a = join(forward_ab)
    db, b = join(forward_ba)
    dn, N = join(readout)
    dt = int(np.lcm(da, db))
    T = (dt//da)*a + (dt//db)*b
    H = sparse.vstack([S, T], format='csr')
    grades = np.repeat(np.tile(base.grades(4), 6), 9) ^ np.tile(base.grades(2)[:9], 1944)
    return H, N, grades, q7, q8, dt, dn


def quotient_factor(H, N, grades):
    """Construct K and L with K*N_num=L*(S,T_num) and certify completeness."""
    hg, ng = prev.row_grades(H, grades), prev.row_grades(N, grades)
    Ks, Ls, profiles = [], [], []
    for g in range(4):
        hi, ni = np.flatnonzero(hg == g), np.flatnonzero(ng == g)
        cols = np.flatnonzero(grades == g)
        h, n = H[hi][:, cols].toarray(), N[ni][:, cols].toarray()
        joint = np.concatenate([h, n])
        base.log('determined quotient grade', g)
        _, annihilator = base.lift(*(prev.left_kernel_mod(joint, p) for p in base.PRIMES))
        assert annihilator.shape == (54, 999)
        assert not np.any(exact_product(annihilator, joint))
        assert int(prev.mod_matrix(annihilator, 1009).rank()) == 54
        projected = annihilator[:, len(hi):]
        _, pivots = base.rref(projected.T, 1009)
        assert len(pivots) == 45
        k = np.zeros((45, 1332), dtype=np.int64)
        l = np.zeros((45, 2664), dtype=np.int64)
        k[:, ni] = projected[pivots]
        l[:, hi] = -annihilator[pivots, :len(hi)]
        Ks.append(k)
        Ls.append(l)
        profile = [prev.rank_exact(h), prev.rank_exact(n), joint.shape[0]-len(annihilator)]
        assert profile == [657, 333, 945]
        profiles.append(profile)
    K, L = np.concatenate(Ks), np.concatenate(Ls)
    assert np.array_equal(exact_product(K, N), exact_product(L, H))
    assert prev.rank_exact(K) == 180
    return K, L, profiles


def generators(depth):
    vectors = [np.array(a, dtype=np.int64) for a in (
        [[0, 0, 0], [0, 0, -1], [0, 1, 0]],
        [[0, 0, 1], [0, 0, 0], [-1, 0, 0]],
        [[0, -1, 0], [1, 0, 0], [0, 0, 0]])]
    for v in vectors:
        h = np.zeros((4, 4), dtype=np.int64)
        h[1:, 1:] = v
        out = sparse.csr_matrix(h)
        for _ in range(depth):
            out = (sparse.kron(out, sparse.eye(3, dtype=np.int64))
                   + sparse.kron(sparse.eye(out.shape[0], dtype=np.int64), v))
        yield v, out.tocsr()


def rotation_profile(q8, K):
    matrices, denominators = [], []
    for v, raw in generators(5):
        response = (sparse.csr_matrix(q8) @ sparse.kron(sparse.eye(6, dtype=np.int64), raw)).toarray()
        d, y = exact_row_factor(response, q8)
        b = np.kron(y, np.eye(3, dtype=np.int64)) + d*np.kron(np.eye(444, dtype=np.int64), v)
        e, c = exact_row_factor(exact_product(K, b), K)
        matrices.append(c)
        denominators.append(d*e)
    den = int(np.lcm.reduce(denominators))
    matrices = [c*(den//d) for c, d in zip(matrices, denominators)]
    for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        assert np.array_equal(exact_product(matrices[a], matrices[b])
                              - exact_product(matrices[b], matrices[a]), den*matrices[c])
    casimir = -sum(exact_product(c, c) for c in matrices)
    profile = [180-prev.rank_exact(casimir-den**2*j*(j+1)*np.eye(180, dtype=np.int64))
               for j in range(5)]
    assert profile == [8, 51, 70, 42, 9]
    assert sum(profile) == 180
    return profile


def certificate(output=None):
    started = time.monotonic()
    H, N, grades, q7, q8, dt, dn = assemble()
    K, L, profiles = quotient_factor(H, N, grades)
    A, B = L[:, :1332], L[:, 1332:]
    assert prev.rank_exact(A) == 180
    assert prev.rank_exact(B) == 144
    # The actual law is K*N = (A/dn)*S + (dt*B/dn)*(F_ab+F_ba).
    beta_den, beta8 = exact_row_factor(base.residual(5), q8)
    beta = np.kron(beta8, np.eye(3, dtype=np.int64))
    residual_den, residual = exact_row_factor(beta, K)
    assert prev.rank_exact(beta) == prev.rank_exact(residual) == 36
    assert not np.any(exact_product(residual, B))
    # The scalar coevaluation is invariant under SO(3), with no anchor choice.
    coevaluation = np.kron(np.eye(148, dtype=np.int64), np.eye(3, dtype=np.int64).ravel()[:, None])
    core = q7[:, :324]  # The full outer-edge core, as established in Note 26.
    assert prev.rank_exact(core) == 144
    beta7_den, beta7 = exact_row_factor(base.residual(4), q7)
    assert prev.rank_exact(beta7) == 4
    assert not np.any(exact_product(beta7, core))
    embedding = exact_product(A, coevaluation)
    core_embedding = exact_product(embedding, core)
    assert prev.rank_exact(embedding) == 148
    assert prev.rank_exact(core_embedding) == 144
    assert not np.any(exact_product(residual, core_embedding))
    # On the source core the two new vector slots enter only through their
    # Euclidean inner product. Use eta=(sum e_i tensor e_i)/3 in the note.
    core_inputs = np.kron(core, np.eye(9, dtype=np.int64))
    dot = np.eye(3, dtype=np.int64).ravel()[None, :]
    assert np.array_equal(3*exact_product(A, core_inputs), np.kron(core_embedding, dot))
    # Raw inputs on the first outer edge have zero residual; their endpoint
    # sums lie in T232. They already make the endpoint coefficient onto C.
    assert prev.rank_exact(exact_product(B, H[1332:, :2916])) == 144
    spin_profile = rotation_profile(q8, K)
    core_profile = [a-b for a, b in zip(spin_profile, [2, 12, 15, 7, 0])]
    assert core_profile == [6, 39, 55, 35, 9]
    _, _, ab, ba = paths.primitive_paths()
    assert base.certified_rank(ab+ba) == 36
    sources = [Path(__file__), Path(paths.__file__), Path(prev.__file__), Path(base.__file__),
               base.HERE/'n8_222_minimal_refinement_certificate.py',
               base.HERE/'n8_222_decoder_continuation_certificate.py', base.HERE/'n8_222_exact_backend.cpp']
    result = {
        'base_commit': BASE_COMMIT,
        'field': 'Q and R; exact integer identities, reconstructed annihilators and modular lower bounds',
        'sources_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                        'scipy': scipy.__version__, 'python_flint': flint.__version__},
        'primes': list(base.PRIMES),
        'observation': 'H_plus=(S,F_ab+F_ba); same final labels and source tensor order as Note 30',
        'graded_ranks_Hplus_N_joint': profiles,
        'ranks': {'H_plus': 2628, 'N': 1332, 'joint': 3780, 'ambiguity': 1152,
                  'determined_quotient': 180, 'residual': 36, 'determined_core': 144,
                  'source_law_coefficient': 180, 'endpoint_sum_law_coefficient': 144,
                  'scalar_coevaluation_core_embedding': 144},
        'matrix_denominators': {'endpoint_sum': dt, 'readout': dn,
                                'beta8': beta_den, 'residual_factor': residual_den,
                                'beta7': beta7_den},
        'factor_identity': 'K @ N_num = A @ S + B @ T_num; T=F_ab+F_ba',
        'factor_shapes': {'K': list(K.shape), 'A': list(A.shape), 'B': list(B.shape)},
        'K_row_nonzero_counts': {str(i): int(np.sum(np.count_nonzero(K, axis=1) == i))
                                for i in np.unique(np.count_nonzero(K, axis=1))},
        'quotient_casimir_eigenspace_dimensions_spin_0_to_4': spin_profile,
        'core_casimir_eigenspace_dimensions_spin_0_to_4': core_profile,
        'core_spin_multiplicities': [core_profile[j]//(2*j+1) for j in range(5)],
        'symmetric_residual_bridge_rank': 36,
        'core_identification': 'c maps to [N x] for S x=c tensor (sum(e_i tensor e_i)/3), (F_ab+F_ba)x=0',
        'source_core_law': 'A_actual(c tensor a tensor b)=dot(a,b)*Psi(c)',
        'endpoint_core_law_rank': 144,
        'note30_dependency': 'Its proved rank 1152 for N(ker H5), together with ker H5 subset ker Hplus, identifies the two ambiguity spaces.',
        'scope': 'Fixed two insertion paths and fixed later readout; identifies the determined core with T212. Compatibility with an enlarged transport family remains to be checked.',
        'elapsed_seconds': round(time.monotonic()-started, 3),
        'all_checks_passed': True,
    }
    rendered = json.dumps(result, indent=2)+'\n'
    if output:
        Path(output).write_text(rendered)
    print(rendered, end='', flush=True)
    base.log('ALL CHECKS PASSED')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output')
    args = parser.parse_args()
    certificate(args.output)
