# Note 31 — Symmetric endpoint law and recovered core

**Base:** Notes 21, 25–30; commit `65fa8fa94bd82747ce5fa4041dc1f113771dafce`.

**Question.** Note 30 leaves a 144-dimensional quotient of the later readout
core determined by the five recorded observations. What is this quotient,
and which observations determine it?

**Result.** The quotient is identified with the original core \(T_{212}\)
by an explicit, representative-independent, \(SO(3)\)-equivariant
isomorphism. It already depends only on the common source observation and
the **sum** of the two endpoints. On the source core, the two new vector
inputs enter through their ordinary inner product.

Writing \(N=R_bP_{ba}\), the resulting core law is

\[
\boxed{\Psi^{-1}([Nx])
=\langle a,b\rangle c+
\Lambda_{\mathrm{sym}}\bigl((F_{ab}+F_{ba})x\bigr)}
\tag{0.1}
\]

whenever \(Sx=c\otimes a\otimes b\), with \(c\in T_{212}\).
Here \(\Lambda_{\mathrm{sym}}:T_{232}\twoheadrightarrow T_{212}\) is a
specified rank-144 map. All maps use Note 30's fixed input order, final
labels, paths, and later readout.

## 1. Fix the spaces and observations

Use Note 30's source

\[
\Omega=E_{212}\otimes V_a\otimes V_b,\qquad \dim\Omega=17496.
\]

Its five observations are

\[
H_5=(S,M_a,M_b,F_{ab},F_{ba}).
\]

The later gap-5 readout on the second path is

\[
N=R_bP_{ba}:\Omega\longrightarrow
B:=Y_{222}\otimes V_b,\qquad \dim B=1332.
\]

Let

\[
\beta_R:B\twoheadrightarrow D_R=\mathcal R_1\otimes V_b,
\qquad T_R=\ker\beta_R=T_{222}\otimes V_b.
\]

Thus \(\dim D_R=36\) and \(\dim T_R=1296\). Note 30 proves

\[
W_5=N(\ker H_5)\subseteq T_R,\qquad \dim W_5=1152.
\tag{1.1}
\]

The determined core is the quotient \(T_R/W_5\). Keeping the quotient,
rather than choosing a complement to \(W_5\), makes its meaning independent
of coordinates.

## 2. Source plus symmetric endpoint suffices

Set

\[
T_+=F_{ab}+F_{ba},\qquad H_+=(S,T_+).
\]

The exact certificate establishes

\[
\operatorname{rank}H_+=2628,\qquad
\operatorname{rank}N=1332,\qquad
\operatorname{rank}(H_+,N)=3780.
\tag{2.1}
\]

Consequently

\[
\dim N(\ker H_+)=3780-2628=1152.
\]

Since \(\ker H_5\subseteq\ker H_+\), equation (1.1) gives the equality

\[
\boxed{W:=N(\ker H_+)=N(\ker H_5).}
\tag{2.2}
\]

In particular, both observations leave exactly the same ambiguity in this
specified readout. Their retained information differs:

| Information retained | Its dimension | Dimension with the full readout \(N\) added |
|---|---:|---:|
| \(H_+=(S,F_{ab}+F_{ba})\) | 2628 | 3780 |
| \(H_5=(S,M_a,M_b,F_{ab},F_{ba})\) | 6516 | 7668 |

The second row continues to be the minimum for preserving all five
observations. Equation (2.2) specifies what can be discarded when asking
only for the determined quotient of \(N\).

Put

\[
\mathcal D=B/W,\qquad \mathcal C=T_R/W.
\]

There is an intrinsic exact sequence

\[
0\longrightarrow\mathcal C\longrightarrow\mathcal D
\xrightarrow{\bar\beta_R}D_R\longrightarrow0,
\qquad(\dim\mathcal C,\dim\mathcal D,\dim D_R)=(144,180,36).
\tag{2.3}
\]

### A concrete factorization

The certificate constructs an onto matrix \(K:B\to\mathbb Q^{180}\)
with \(\ker K=W\). It constructs \(A\) and \(B_+\) such that, in these
coordinates for \(\mathcal D\),

\[
\boxed{KN=A S+B_+T_+.}
\tag{2.4}
\]

The factorization has

\[
\operatorname{rank}A=180,\qquad
\operatorname{im}B_+=K(T_R),\qquad
\operatorname{rank}(B_+|_{T_{232}})=144.
\tag{2.5}
\]

The implemented integer matrices satisfy

\[
K N_{\mathrm{num}}=A_{\mathrm{num}}S+
B_{\mathrm{num}}T_{\mathrm{num}},
\]

with \(N=N_{\mathrm{num}}/8\), \(T_+=T_{\mathrm{num}}/4\).
Thus \(A=A_{\mathrm{num}}/8\) and \(B_+=B_{\mathrm{num}}/2\).
This records the actual maps, including their scales.

## 3. Compatible pairs and the canonical core identification

Let \(D_0=\mathbb H\otimes V_a\otimes V_b\), and let
\(\alpha=\beta_{212}\otimes\mathrm{id}\) be the residual of the source
observation. Note 30 gives

\[
\beta_{232}T_+=(\Theta_{ab}+\Theta_{ba})\alpha S.
\tag{3.1}
\]

The 36-dimensional operator \(\Theta_{ab}+\Theta_{ba}\) is invertible;
the certificate checks its exact rank. The compatible-pair space in (3.1)
has dimension \(1332+1332-36=2628\). Equation (2.1) attains this bound, so
**every compatible pair is realized by an input in \(\Omega\)**.

Equip \(V=\operatorname{Im}\mathbb H\) with its standard Euclidean inner
product and define its normalized scalar coevaluation

\[
\eta=\frac13\sum_{r=1}^{3}e_r\otimes e_r\in V_a\otimes V_b.
\tag{3.2}
\]

This tensor is independent of the orthonormal basis and has contraction 1.
For \(c\in T_{212}=\ker\beta_{212}\), choose any \(x\in\Omega\) satisfying

\[
Sx=c\otimes\eta,\qquad T_+x=0.
\tag{3.3}
\]

Such an input exists by compatible-pair surjectivity. Define

\[
\boxed{\Psi(c)=[Nx]\in\mathcal C.}
\tag{3.4}
\]

The residual of \(Nx\) vanishes, because the residual of \(Sx\) does.
Two choices in (3.3) differ by \(\ker H_+\), whose image under \(N\) is
exactly \(W\). Hence (3.4) is well-defined, linear, and independent of a
representative. All the defining operations and \(\eta\) are
\(SO(3)\)-equivariant.

In the certificate, the first outer-edge block of \(q_{212}\) has image
\(T_{212}\), with exact rank144. The restriction of

\[
\frac{1}{24}A_{\mathrm{num}}
\left(I_{Y_{212}}\otimes\sum_r e_r\otimes e_r\right)
\tag{3.5}
\]

to that image has exact rank144 and is annihilated by the residual of
\(\mathcal D\). It is precisely (3.4) in \(K\)-coordinates. Therefore

\[
\boxed{\Psi:T_{212}\xrightarrow{\sim}\mathcal C=T_R/W.}
\tag{3.6}
\]

This supplies the isomorphism from the prescribed operation data and the
standard quaternionic inner product. The 144-dimensional object is the
original core recovered as a determined quotient of the later readout.

## 4. The source term is an inner-product contraction

The certificate verifies the stronger identity on the whole source core:

\[
A(c\otimes a\otimes b)=\Psi(\langle a,b\rangle c),
\qquad c\in T_{212}.
\tag{4.1}
\]

It tests equality of the full integer operators. Thus the antisymmetric
and symmetric traceless parts of \(V_a\otimes V_b\) vanish in this source
contribution. The scalar part carries the recovered core.

The endpoint contribution also has a representative-independent
description. For \(t\in T_{232}\), choose an input with
\(Sx=0\), \(T_+x=t\), and set

\[
\Lambda_{\mathrm{sym}}(t)=\Psi^{-1}([Nx]).
\tag{4.2}
\]

Existence and independence follow as in (3.3)–(3.4). The certificate
checks that its image has dimension144, already using endpoint sums
arising from the first outer edge. The literal paths preserve each edge
summand, so these endpoint sums have zero residual. Therefore

\[
\Lambda_{\mathrm{sym}}:T_{232}\twoheadrightarrow T_{212},
\qquad \dim\ker\Lambda_{\mathrm{sym}}=1152.
\tag{4.3}
\]

Combining (4.1) and (4.2) proves (0.1). For a general zero-residual source
observation, replace \(\langle a,b\rangle c\) by its linear contraction
in the two new vector slots.

The two 1152-dimensional spaces have specified domains:
\(W\subset T_R\) is the remaining readout ambiguity, while
\(\ker\Lambda_{\mathrm{sym}}\subset T_{232}\) is the endpoint-core
information killed by (4.2). Equation (4.3) alone supplies no transport
between those kernels.

## 5. Rotation structure

As an independent check, the certificate descends the three infinitesimal
rotation generators through \(q_{222}\) and \(K\), verifies their Lie
brackets, and computes the exact Casimir eigenspaces. If \(V_\ell\)
denotes spin \(\ell\), of dimension \(2\ell+1\), then

\[
\mathcal C\cong
6V_0\oplus13V_1\oplus11V_2\oplus5V_3\oplus V_4.
\tag{5.1}
\]

| Spin \(\ell\) | 0 | 1 | 2 | 3 | 4 | Total |
|---|---:|---:|---:|---:|---:|---:|
| \(\mathcal D\): eigenspace dimensions | 8 | 51 | 70 | 42 | 9 | 180 |
| \(D_R\): eigenspace dimensions | 2 | 12 | 15 | 7 | 0 | 36 |
| \(\mathcal C\): eigenspace dimensions | 6 | 39 | 55 | 35 | 9 | 144 |

These are the components of Note 21's
\(T_{212}\cong\mathbb H\otimes\mathbb H\otimes V\otimes V\).
The explicit map (3.4) establishes the identification, and the rotation
calculation checks the full representation profile.

## 6. Verification and scope

Run from the repository root:

```bash
python research/depth-generated-geometry/certificates/n9_232_determined_core_certificate.py \
  --output research/depth-generated-geometry/certificates/n9_232_determined_core_result.json
```

The certificate rebuilds the matching quotients and literal two-path
operators, constructs the determined quotient from exact left
annihilators, verifies the factorization, residual, scalar source law,
core isomorphism and rotation profile. Ranks are certified over
characteristic zero by integer identities and modular lower bounds.
The output records source hashes and environment versions.

The recorded run resumed after a workspace reset: recovered quotient
coordinates were checked again for full row rank and annihilation of
freshly reconstructed literal matching maps. Their completeness uses the
dimensions already proved in Notes 26 and 29. All literal path/readout
operators and all new checks were then rerun. The result record identifies
this mode and the scope of its timing; the command above performs the full
quotient reconstruction as well.

The direct new rank statement is for \(H_+\). Equality with Note 30's
ambiguity uses that note's proved 1152-dimensional \(N(\ker H_5)\) and
the kernel inclusion in Section 2. Stored result files are not proof inputs.

This closes the identification of the determined144 quotient for the
specified paths and readout. Compatibility of \(\Psi\) and
\(\Lambda_{\mathrm{sym}}\) with a larger spectator/transport network is
a subsequent question. The present identification provides a concrete
map against which that compatibility can be tested.
