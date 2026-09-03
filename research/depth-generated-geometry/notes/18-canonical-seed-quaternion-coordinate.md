# Note 18 — Canonical Seed Quaternion Coordinate

## Frobenius factorization turns the hidden \(K_4\) into a measured quaternion

**Status:** theorem over \(\mathbb Q\), with an exact standard-library
certificate

**Depends on:** Notes 14, 16, and 17

**Claim boundary:** this note canonically identifies Note 14's central
four-dimensional channel with a concrete copy of \(\mathbb H\), proves that
the \(12+4\) split is orthogonal, and computes the central coordinate of all
six edge operators. It supplies a fixed target for the later cap and square
residuals. It does not yet construct a chain-level spectator transport from
the \(n=5\) seed to the \(n=6\) or \(n=7\) quotients.

---

## 0. Result in one line

Equip \(\mathbb H\) with its Euclidean inner product and define

\[
\boxed{
\iota:\mathbb H\longrightarrow\mathbb H\otimes\mathbb H,
\qquad
\iota(q)=\sum_{\alpha=0}^{3}e_\alpha\otimes q e_\alpha .
}
\tag{0.1}
\]

Then Note 14's central edge operator factors as

\[
\boxed{
\Lambda_{23}(h,u,v)
=
\iota\left(
-\frac14uv(\bar h+2h)
\right),
}
\tag{0.2}
\]

and its image is exactly

\[
\boxed{
K_4=\operatorname{im}\Lambda_{23}=\iota(\mathbb H).
}
\tag{0.3}
\]

Moreover, if

\[
\nu:=\frac14\iota^*:
\mathbb H\otimes\mathbb H\longrightarrow\mathbb H,
\tag{0.4}
\]

then

\[
\boxed{
\mathbb H\otimes\mathbb H
=
W_{12}\mathbin{\overset{\perp}{\oplus}}\iota(\mathbb H),
\qquad
W_{12}=\ker\nu
=\operatorname{im}\Lambda_{13}
=\operatorname{im}\Lambda_{24}.
}
\tag{0.5}
\]

Thus \(K_4\cong\mathbb H\) is no longer only an isomorphism type. The map
\(\nu\) is its normalized, basis-independent quaternion coordinate.

---

## 1. The Frobenius embedding and its adjoint

Use

\[
e_0=1,\qquad e_1=i,\qquad e_2=j,\qquad e_3=k
\tag{1.1}
\]

and the real inner product

\[
\langle x,y\rangle=\operatorname{Re}(x\bar y)
\tag{1.2}
\]

on \(\mathbb H\). Give \(\mathbb H\otimes\mathbb H\) the tensor-product
inner product.

Although (0.1) is written in an orthonormal basis, it is intrinsic for the
distinguished diagonal \(SO(3)\)-action. The tensor

\[
\Xi=\sum_{\alpha=0}^{3}e_\alpha\otimes e_\alpha
\tag{1.3}
\]

is invariant, and

\[
\iota(q)=(1\otimes L_q)\Xi.
\tag{1.4}
\]

For a pure tensor \(x\otimes y\), the adjoint has the closed formula

\[
\boxed{
\iota^*(x\otimes y)=y\bar x.
}
\tag{1.5}
\]

Indeed, for every \(q\in\mathbb H\),

\[
\begin{aligned}
\langle\iota(q),x\otimes y\rangle
&=
\sum_\alpha
\langle e_\alpha,x\rangle
\langle qe_\alpha,y\rangle\\
&=
\langle qx,y\rangle
=
\langle q,y\bar x\rangle.
\end{aligned}
\tag{1.6}
\]

It follows immediately that

\[
\boxed{
\iota^*\iota=4\,\operatorname{id}_{\mathbb H}.
}
\tag{1.7}
\]

Consequently \(\iota\) is injective, \(\nu\iota=\operatorname{id}\), and

\[
\boxed{
P_{K}:=\iota\nu=\frac14\iota\iota^*
}
\tag{1.8}
\]

is the orthogonal projector onto \(\iota(\mathbb H)\). Both \(\iota\) and
\(\nu\) are \(SO(3)\)-equivariant.

---

## 2. Exact factorization of the central seed

For every \(h\in\mathbb H\), the canonical-tensor identity

\[
\boxed{
(L_h\otimes1)\Xi=(1\otimes L_{\bar h})\Xi
}
\tag{2.1}
\]

holds because \(L_h^*=L_{\bar h}\). Apply (2.1) to the primitive operators
of Note 14. One obtains

\[
\boxed{
\begin{aligned}
A(h,u,v)
&=
\sum_\alpha he_\alpha\otimes uv e_\alpha
=\iota(uv\bar h),\\
C(h,u,v)
&=
\sum_\alpha e_\alpha\otimes uvh e_\alpha
=\iota(uvh).
\end{aligned}
}
\tag{2.2}
\]

Since

\[
\Lambda_{23}=-\frac14A-\frac12C,
\tag{2.3}
\]

equation (0.2) follows.

Put

\[
\sigma_R(h):=2h+\bar h=3\operatorname{Re}(h)+\operatorname{Im}(h).
\tag{2.4}
\]

The map \(\sigma_R\) is invertible. Products \(uv\), for \(u,v\in V\),
span \(\mathbb H\); in fact one may already fix \(u=v\ne0\), when \(uv\)
is a nonzero real scalar. Hence the quaternion parameter in (0.2) is onto.
Therefore

\[
\operatorname{im}\Lambda_{23}
=\operatorname{im}A
=\operatorname{im}C
=\iota(\mathbb H),
\tag{2.5}
\]

which proves (0.3).

---

## 3. The \(12+4\) split is canonical and orthogonal

Note 14 proved

\[
\operatorname{im}\Lambda_{13}
=\operatorname{im}\Lambda_{24}
=:W_{12},
\qquad
\dim W_{12}=12.
\tag{3.1}
\]

Direct substitution into (1.5) gives

\[
\boxed{
\iota^*\Lambda_{13}=0,
\qquad
\iota^*\Lambda_{24}=0.
}
\tag{3.2}
\]

Thus \(W_{12}\subseteq\ker\nu\). Since \(\nu\) is onto,
\(\dim\ker\nu=16-4=12\), so equality holds:

\[
W_{12}=\ker\nu.
\tag{3.3}
\]

But

\[
\ker\nu=\ker\iota^*=\iota(\mathbb H)^\perp.
\tag{3.4}
\]

Equations (2.5), (3.3), and (3.4) prove (0.5). In particular, the two
canonical projectors are

\[
\boxed{
P_K=\frac14\iota\iota^*,
\qquad
P_W=1-\frac14\iota\iota^*.
}
\tag{3.5}
\]

The decomposition found by row reduction in Note 14 is therefore not an
accidental complement:

\[
\boxed{
\mathbb H\otimes\mathbb H
\cong
(\mathbb H\otimes V)\mathbin{\overset{\perp}{\oplus}}\mathbb H
}
\tag{3.6}
\]

with both summands and both projections specified by the response
operator itself.

---

## 4. The central coordinate of every edge

Formula (1.5) first gives the five primitive coordinates

\[
\boxed{
\begin{array}{c|ccccc}
X&P&A&B&C&D\\ \hline
\nu X(h,u,v)
&
\frac14uv\bar h&
uv\bar h&
0&
uvh&
\frac12uvh.
\end{array}
}
\tag{4.1}
\]

For \(B\) and \(D\), this uses the standard quaternion identities

\[
\sum_{\alpha=0}^{3}e_\alpha v\bar e_\alpha=0
\quad(v\in V),
\qquad
\sum_{\alpha=0}^{3}\bar e_\alpha\bar h\bar e_\alpha=-2h.
\tag{4.2}
\]

Substitution into the six combinations of Note 14 yields

\[
\boxed{
\begin{array}{c|c|c}
ij&\nu\Lambda_{ij}(h,u,v)&
\operatorname{rank}(\nu\Lambda_{ij})\\ \hline
12&\frac14uv\bar h&4\\
13&0&0\\
14&-\frac14uv\bar h&4\\
23&-\frac14uv(\bar h+2h)&4\\
24&0&0\\
34&\frac14uv\bar h&4.
\end{array}
}
\tag{4.3}
\]

This table sharpens the edge-image ranks \(16,12,16,4,12,16\):

- the rank-12 edges \(13\) and \(24\) are exactly central-free;
- the rank-4 edge \(23\) is entirely central;
- the full-rank edges \(12,14,34\) carry both channels, with central signs
  \(+,-,+\).

The seed tetrahedron therefore has a labelled quaternionic incidence
pattern before any spectator is inserted.

---

## 5. The precise bridge to the parity collapses

Define the conjugate companion of (2.4):

\[
\sigma_L(h):=h+2\bar h
=3\operatorname{Re}(h)-\operatorname{Im}(h).
\tag{5.1}
\]

Then

\[
\overline{\sigma_R(h)}=\sigma_L(h).
\tag{5.2}
\]

The seed central coordinate is

\[
\boxed{
\nu\Lambda_{23}(h,u,v)
=-\frac14uv\,\sigma_R(h).
}
\tag{5.3}
\]

Note 17's left cap decoder contains the mirror involution:

\[
\boxed{
\lambda_{2r+1}^{L}
J_{2r+1}(h,v_1,\ldots,v_{2r+1})
=-\sigma_L(h)v_{2r+1}\cdots v_1.
}
\tag{5.4}
\]

Its right cap is

\[
\lambda_{2r+1}^{R}J_{2r+1}
=hv_{2r+1}\cdots v_1,
\tag{5.5}
\]

while Note 16's paired collapse is the even-depth reverse product

\[
\varepsilon_{2r}J_{2r}
=hv_{2r}\cdots v_1.
\tag{5.6}
\]

Thus the three closed constructions now live in the same fixed quaternion
coordinate and differ by visible, invertible operations: reverse ordered
products and the conjugate pair \(\sigma_R,\sigma_L\). This is an exact
algebraic bridge. It is not yet a proof that inserting spectators defines a
chain map between the three complexes.

---

## 6. What changed

Before this note, the three relevant residuals were known only as separate
copies of the same \(SO(3)\)-module:

\[
K_4\cong\mathbb H,
\qquad
Y_{6,(1,2,4,5)}/E_{14}\cong\mathbb H,
\qquad
K_{212}\cong\mathbb H.
\tag{6.1}
\]

The first of these now has a canonical target coordinate

\[
K_4\xrightarrow{\ \nu\ }\mathbb H,
\tag{6.2}
\]

and the other two already have the explicit decoders \(\chi_6\) and
\(\kappa_{212}\). Hence a proposed transport can no longer hide behind an
unspecified module isomorphism. It must make explicit quaternion-valued
diagrams commute and reproduce the labelled zero pattern in (4.3).

This reduces the open problem from

\[
\text{compare three abstract four-dimensional modules}
\tag{6.3}
\]

to

\[
\boxed{
\text{find the order-sensitive chain map relating three fixed decoders}.
}
\tag{6.4}
\]

---

## 7. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/n5_central_channel_factorization_certificate.py
~~~

The script uses only Python's standard library and exact rational
arithmetic. It verifies:

- \(\iota^*\iota=4\,\operatorname{id}_{\mathbb H}\);
- equivariance and injectivity of \(\iota\);
- the factorizations of \(A,C,\Lambda_{23}\);
- surjectivity of the central quaternion parameter;
- idempotence and self-adjointness of \(P_K\);
- the primitive formulas (4.1);
- all six edge formulas and ranks in (4.3);
- \(W_{12}=\ker\nu=\iota(\mathbb H)^\perp\).

Expected final line:

~~~text
ALL CHECKS PASSED
~~~

---

## 8. What is not proved

This note does **not** prove:

- a spectator insertion map from \(\omega_5\) to \(\chi_6\);
- a two-spectator insertion map from \(\omega_5\) to
  \(\kappa_{212}\);
- that either later quotient is literally a subspace of the \(n=5\)
  target;
- all-length exactness of every cap or parity-square cokernel;
- curvature, holonomy, or a physical gauge interpretation.

What is proved is the target-side normalization needed to ask those
questions without coordinate ambiguity.

---

## 9. Next target

Construct order-sensitive maps on the **source complexes**, not merely
isomorphisms of their four-dimensional cokernels, so that the induced
quaternion coordinates satisfy

\[
\nu\circ\omega_5
\quad\rightsquigarrow\quad
\chi_6
\quad\rightsquigarrow\quad
\kappa_{212}.
\tag{9.1}
\]

The first local test is rigid: a one-spectator transport must recover the
five-edge sign pattern of Note 17, preserve the central-free nature of the
appropriate edge images, and convert the seed factor
\(\sigma_R\) into its cap-side mirror \(\sigma_L\). Any failure is a
measurable correction term rather than an ambiguity of quotient
coordinates.
