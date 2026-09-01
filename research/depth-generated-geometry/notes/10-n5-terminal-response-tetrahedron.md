# Note 10 — \(n=5\) Terminal Response Tetrahedron

## pairwise gluing による intrinsic terminal boundary と最初の compatibility syzygy

**Status:** response-side restriction maps constructed; middle exactness, ranks, and the syzygy \(SO(3)\)-type certified by exact rational arithmetic

**Depends on:** Notes 02, 07, 09

**Claim boundary:** this note proves an intrinsic pairwise-gluing presentation at \(n=5\). It does not prove pairwise descent for every \(n\), construct a canonical next differential out of the 16-dimensional syzygy module, or identify that module with curvature.

---

## 0. Main result

Write

\[
\mathcal R_q
:=
\operatorname{Hom}_{\mathbb R}(V^{\otimes q},\mathbb H),
\qquad
\dim\mathcal R_q=4\cdot3^q.
\]

At length five there are four exact-depth-three terminal faces

\[
F_1,F_2,F_3,F_4\in\mathcal R_3.
\]

Every pair of faces has a canonical common exact-depth-two shadow. For
\(1\le r<s\le4\), there are response-side restriction maps

\[
\rho_r^{rs},\rho_s^{rs}:
\mathcal R_3\longrightarrow\mathcal R_2.
\]

Define the tetrahedral matching operator

\[
\boxed{
\partial_5:
\mathcal R_3^{\oplus4}
\longrightarrow
\mathcal R_2^{\oplus6}
}
\]

by

\[
\boxed{
(\partial_5F)_{rs}
=
\rho_r^{rs}F_r-\rho_s^{rs}F_s.
}
\tag{0.1}
\]

Then

\[
\operatorname{rank}\partial_5=200,
\qquad
\dim\ker\partial_5=232,
\qquad
\dim\operatorname{coker}\partial_5=16.
\tag{0.2}
\]

Let

\[
\mathbf B_5:
V^{\otimes5}\longrightarrow\mathcal R_3^{\oplus4}
\]

be the joint terminal-boundary map of Note 09. The central gluing theorem is

\[
\boxed{
\operatorname{im}\mathbf B_5
=
\ker\partial_5.
}
\tag{0.3}
\]

Thus the terminal boundary image no longer needs to be defined as an image:

\[
\boxed{
\mathcal P_{5,3}
:=
\ker\partial_5
\subset
\mathcal R_3^{\oplus4}.
}
\tag{0.4}
\]

If

\[
\mathfrak S_5:=\operatorname{coker}\partial_5,
\]

then there is an exact sequence

\[
\boxed{
0\longrightarrow S^5_0V
\longrightarrow V^{\otimes5}
\xrightarrow{\ \mathbf B_5\ }
\mathcal R_3^{\oplus4}
\xrightarrow{\ \partial_5\ }
\mathcal R_2^{\oplus6}
\longrightarrow\mathfrak S_5
\longrightarrow0.
}
\tag{0.5}
\]

The first compatibility-syzygy module has the canonical \(SO(3)\)-type

\[
\boxed{
\mathfrak S_5
\cong
2V_0\oplus3V_1\oplus V_2,
\qquad
\dim\mathfrak S_5=16.
}
\tag{0.6}
\]

At \(n=4\), the response triangle had no such cokernel. At \(n=5\),
pairwise matching is still sufficient for realizability, but the matching
equations themselves are no longer independent.

---

## 1. The four terminal faces

For a pure word

\[
T=a_1|a_2|a_3|a_4|a_5,
\]

let \(B_{5,r}\) probe every internal gap except \(r\). Thus

\[
B_{5,r}:V^{\otimes5}\longrightarrow\mathcal R_3,
\qquad 1\le r\le4.
\]

For example,

\[
B_{5,1}(T)(x_2,x_3,x_4)
=
a_5x_4a_4x_3a_3x_2(a_2a_1),
\]

while

\[
B_{5,2}(T)(x_1,x_3,x_4)
=
a_5x_4a_4x_3(a_3a_2)x_1a_1.
\]

Note 09 proves that every individual face is onto:

\[
\boxed{
\operatorname{rank}B_{5,r}
=
\dim\mathcal R_3
=108.
}
\tag{1.1}
\]

Hence an isolated terminal face is an arbitrary trilinear quaternion-valued
response. Global structure appears only when four such faces are required to
possess common lower-depth shadows.

The joint map is

\[
\mathbf B_5
=
\begin{pmatrix}
B_{5,1}\\B_{5,2}\\B_{5,3}\\B_{5,4}
\end{pmatrix}
:
V^{\otimes5}\longrightarrow\mathcal R_3^{\oplus4}.
\tag{1.2}
\]

By the all-length terminal theorem,

\[
\ker\mathbf B_5=S^5_0V\cong V_5,
\qquad
\dim S^5_0V=11,
\]

and therefore

\[
\boxed{
\operatorname{rank}\mathbf B_5
=243-11
=232.
}
\tag{1.3}
\]

---

## 2. Response-side common-shadow maps

Fix two omitted gaps \(r<s\). Probe the other two gaps. The resulting common
shadow of an actual state is

\[
D_{rs}:V^{\otimes5}\longrightarrow\mathcal R_2.
\tag{2.1}
\]

For adjacent omitted gaps, the two direct multiplications create one
length-three quaternion block. For example,

\[
D_{12}(T)(x_3,x_4)
=
a_5x_4a_4x_3(a_3a_2a_1).
\tag{2.2}
\]

For separated omitted gaps, two quaternion blocks remain. For example,

\[
D_{13}(T)(x_2,x_4)
=
a_5x_4(a_4a_3)x_2(a_2a_1).
\tag{2.3}
\]

The common shadow must now be extracted from a face without returning to a
tensor representative.

Recall the terminal-face encoder isomorphism of Note 09,

\[
\mathcal E_{5,r}:
W_{5,r}
\xrightarrow{\ \cong\ }
\mathcal R_3,
\]

where

\[
W_{5,r}
=
V^{\otimes(r-1)}
\otimes\mathbb H
\otimes V^{\otimes(4-r)}.
\]

Its inverse is a finite response-side algorithm obtained by iterating the
local decoders

\[
\Theta_R^{-1},\qquad\Theta_L^{-1}.
\]

After decoding \(F_r\in\mathcal R_3\) into \(W_{5,r}\), directly multiply
across the second omitted gap \(s\), and then insert probes into the two
remaining gaps. Denote this forward collapse-and-encode operation by

\[
\Gamma_{r;s}:W_{5,r}\longrightarrow\mathcal R_2.
\]

Define

\[
\boxed{
\rho_r^{rs}
:=
\Gamma_{r;s}\circ\mathcal E_{5,r}^{-1}
:
\mathcal R_3\longrightarrow\mathcal R_2.
}
\tag{2.4}
\]

This definition uses only the face response, the established local decoders,
and quaternion multiplication. It does not choose a state lift.

For every actual state,

\[
\boxed{
\rho_r^{rs}\circ B_{5,r}
=D_{rs}
=\rho_s^{rs}\circ B_{5,s}.
}
\tag{2.5}
\]

All twelve oriented restriction maps are onto:

\[
\boxed{
\operatorname{rank}\rho_r^{rs}
=
\dim\mathcal R_2
=36.
}
\tag{2.6}
\]

Because \(B_{5,r}\) is onto, a map

\[
\rho:\mathcal R_3\to\mathcal R_2
\]

satisfying \(\rho B_{5,r}=D_{rs}\) is unique. Thus (2.4) is independent of
the decoder presentation used to prove it.

The exact certificate constructs the same unique maps by factoring the
matrix of \(D_{rs}\) through the surjective matrix of \(B_{5,r}\), and checks
(2.5) entry by entry over \(\mathbb Q\).

---

## 3. Tetrahedral matching

Order the six pairs as

\[
12,13,14,23,24,34.
\]

For an arbitrary four-tuple

\[
F=(F_1,F_2,F_3,F_4)\in\mathcal R_3^{\oplus4},
\]

define

\[
\partial_5F
=
\begin{pmatrix}
\rho_1^{12}F_1-\rho_2^{12}F_2\\
\rho_1^{13}F_1-\rho_3^{13}F_3\\
\rho_1^{14}F_1-\rho_4^{14}F_4\\
\rho_2^{23}F_2-\rho_3^{23}F_3\\
\rho_2^{24}F_2-\rho_4^{24}F_4\\
\rho_3^{34}F_3-\rho_4^{34}F_4
\end{pmatrix}.
\tag{3.1}
\]

Equation (2.5) immediately gives

\[
\boxed{
\partial_5\circ\mathbf B_5=0.
}
\tag{3.2}
\]

Hence

\[
\operatorname{im}\mathbf B_5
\subseteq
\ker\partial_5.
\tag{3.3}
\]

The issue is whether pairwise matching is sufficient, or whether a four-face
family can satisfy all six common-shadow equations without coming from one
global length-five state.

---

## 4. \(n=5\) pairwise-gluing theorem

Exact rational row reduction gives

\[
\boxed{
\operatorname{rank}\partial_5=200.
}
\tag{4.1}
\]

Since

\[
\dim\mathcal R_3^{\oplus4}
=4\cdot108
=432,
\]

we obtain

\[
\dim\ker\partial_5
=432-200
=232.
\tag{4.2}
\]

But (1.3) gives

\[
\dim\operatorname{im}\mathbf B_5=232.
\]

Together with (3.3), this proves:

### Theorem 4.1 — terminal response tetrahedron gluing

A four-tuple

\[
(F_1,F_2,F_3,F_4)\in\mathcal R_3^{\oplus4}
\]

is the terminal boundary of a length-five state if and only if all six
pairwise common shadows match:

\[
\boxed{
\rho_r^{rs}F_r
=
\rho_s^{rs}F_s
\qquad
(1\le r<s\le4).
}
\tag{4.3}
\]

Equivalently,

\[
\boxed{
\mathcal P_{5,3}
=
\ker\partial_5.
}
\tag{4.4}
\]

The definition on the right is intrinsic to the response tetrahedron. The
ambient tensor space is used in the proof of completeness, not in the final
presentation of the boundary object.

---

## 5. The first compatibility syzygy

The equation target has dimension

\[
\dim\mathcal R_2^{\oplus6}
=6\cdot36
=216.
\]

Since \(\partial_5\) has rank 200,

\[
\boxed{
\dim\operatorname{coker}\partial_5
=216-200
=16.
}
\tag{5.1}
\]

Thus the 216 scalar coordinates in the six pairwise matching defects contain
only 200 independent directions. Equivalently, after choosing invariant inner
products, the row-syzygy space

\[
\ker\partial_5^*
\]

is 16-dimensional and is canonically dual to

\[
\mathfrak S_5=\operatorname{coker}\partial_5.
\]

This is the first place in the terminal response family where relations among
the matching equations themselves survive.

For comparison, at \(n=4\),

\[
\partial_4:\mathcal R_2^{\oplus3}\to\mathcal R_1^{\oplus3}
\]

has rank 36 and is onto. Hence

\[
\operatorname{coker}\partial_4=0.
\]

The response triangle has exact matching with no next syzygy. The response
tetrahedron still has exact pairwise descent, but its six edge equations obey
a nonzero higher relation.

---

## 6. \(SO(3)\)-type of the 16-dimensional module

Under diagonal quaternionic conjugation,

\[
\mathbb H\cong V_0\oplus V_1.
\]

Clebsch-Gordan decomposition gives

\[
\mathcal R_2
\cong
2V_0\oplus4V_1\oplus3V_2\oplus V_3,
\tag{6.1}
\]

and

\[
\mathcal R_3
\cong
4V_0\oplus9V_1\oplus8V_2\oplus4V_3\oplus V_4.
\tag{6.2}
\]

Also,

\[
V^{\otimes5}
\cong
6V_0\oplus15V_1\oplus15V_2
\oplus10V_3\oplus4V_4\oplus V_5.
\tag{6.3}
\]

Since the terminal boundary removes precisely the unique \(V_5\),

\[
\mathcal P_{5,3}
\cong
6V_0\oplus15V_1\oplus15V_2
\oplus10V_3\oplus4V_4.
\tag{6.4}
\]

The exact sequence gives, in the representation ring,

\[
[\mathfrak S_5]
=
6[\mathcal R_2]
-4[\mathcal R_3]
+[\mathcal P_{5,3}].
\tag{6.5}
\]

Substitution of (6.1)--(6.4) yields

\[
\boxed{
\mathfrak S_5
\cong
2V_0\oplus3V_1\oplus V_2.
}
\tag{6.6}
\]

Its dimension is

\[
2\cdot1+3\cdot3+1\cdot5=16.
\]

All spins \(V_3,V_4,V_5\) cancel. The first higher compatibility module is a
purely lower-spin object; it is not another copy of the terminal highest-spin
interior.

---

## 7. What has become intrinsic

Note 09 defined

\[
\mathcal P_{n,n-2}=\operatorname{im}\mathbf B_n
\]

and proved its kernel, dimension, and canonical filling for every \(n\).

At \(n=5\), this note replaces the image definition by the direct response
presentation

\[
\boxed{
\mathcal P_{5,3}
=
\left\{
(F_1,F_2,F_3,F_4)\in\mathcal R_3^4
\;\middle|\;
\rho_r^{rs}F_r=\rho_s^{rs}F_s
\text{ for all }r<s
\right\}.
}
\tag{7.1}
\]

The logical order is now

\[
\boxed{
\text{four local responses}
+\text{six pairwise matches}
\Longrightarrow
\text{intrinsic terminal boundary}
\Longrightarrow
\text{canonical filler}+V_5.
}
\tag{7.2}
\]

This is the tetrahedral successor of the \(n=4\) response triangle.

---

## 8. Curvature status

The 16-dimensional module is a genuine higher compatibility phenomenon, but
it is not yet curvature.

What is proved is:

- the pairwise defect operator is not onto;
- its equation module has a canonical 16-dimensional quotient;
- the quotient has type \(2V_0\oplus3V_1\oplus V_2\).

A curvature statement would still require:

- transport maps between response charts;
- at least two composable paths with common endpoints;
- a path-comparison residual;
- coordinate or gauge covariance of that residual;
- a theorem relating the residual to the compatibility complex.

The present module is therefore a candidate location for a future Bianchi-type
identity, not a curvature sector by itself.

---

## 9. General response-simplex problem

For general \(n\ge4\), define

\[
C_n^0
:=
\mathcal R_{n-2}^{\oplus(n-1)},
\]

one terminal face for every omitted gap, and

\[
C_n^1
:=
\mathcal R_{n-3}^{\oplus\binom{n-1}{2}},
\]

one common shadow for every pair of omitted gaps.

The same decoder-collapse construction defines

\[
\partial_n:C_n^0\longrightarrow C_n^1.
\]

The next all-length question is

\[
\boxed{
\ker\partial_n
\stackrel{?}{=}
\mathcal P_{n,n-2}
\qquad(n\ge4).
}
\tag{9.1}
\]

It holds for \(n=4\) by Note 07 and for \(n=5\) by Theorem 4.1.

The first new test is \(n=6\). Pairwise descent predicts

\[
\begin{aligned}
\dim C_6^0&=5\cdot324=1620,\\
\dim\mathcal P_{6,4}&=3^6-13=716,\\
\operatorname{rank}\partial_6&=904,\\
\dim\operatorname{coker}\partial_6&=176.
\end{aligned}
\tag{9.2}
\]

If middle exactness holds, representation bookkeeping predicts

\[
\operatorname{coker}\partial_6
\cong
10V_0\oplus21V_1\oplus15V_2\oplus4V_3.
\tag{9.3}
\]

If (9.1) fails, the excess

\[
\ker\partial_n/\mathcal P_{n,n-2}
\]

will be the first genuine higher gluing obstruction. Either outcome gives a
precise next theorem.

---

## 10. Exact certificate

Run

```bash
python3 certificates/n5_response_tetrahedron_certificate.py
```

from `research/depth-generated-geometry/`.

The certificate uses only Python's standard library and exact
`fractions.Fraction` arithmetic. It verifies:

- the generic common-shadow construction recovers the established \(n=4\)
  response triangle;
- all twelve oriented \(n=5\) face-to-shadow restrictions factor exactly and
  are onto;
- \(\partial_5\mathbf B_5=0\);
- \(\operatorname{rank}\mathbf B_5=232\);
- \(\operatorname{rank}\partial_5=200\);
- \(\ker\partial_5=\operatorname{im}\mathbf B_5\) by exact inclusion and
  dimension equality;
- \(\dim\operatorname{coker}\partial_5=16\);
- the exact character calculation
  \(\mathfrak S_5\cong2V_0\oplus3V_1\oplus V_2\).

Expected final line:

```text
ALL CHECKS PASSED
```

---

## 11. Claim boundary

This note closes the intrinsic terminal-boundary presentation at \(n=5\).
It does not yet prove:

- pairwise terminal descent for every \(n\);
- an intrinsic generators-and-relations presentation of
  \(\operatorname{coker}\partial_5\) beyond its quotient definition;
- a canonical higher differential after \(\partial_5\);
- the intermediate-depth multiplicity filtration;
- transport, holonomy, or curvature.

The new hard fact is narrower:

\[
\boxed{
\text{response triangle at }n=4
\quad\longrightarrow\quad
\text{response tetrahedron at }n=5,
}
\]

with pairwise descent still exact and a first 16-dimensional compatibility
syzygy appearing one level later.
