---
title: "Ordered Quaternionic Response Quotients"
subtitle: "Flat Cores, Local Residuals, and a Three-Spectator Descent Obstruction"
author: "Residual Chart Lab"
date: "Depth-Generated Geometry - Research Snapshot 2026-09-07"
lang: en
---

## Abstract

We study finite cokernels formed from four ordered quaternion-valued face
responses and their six pairwise common shadows. The incidence of labelled
edge images distinguishes quotients with the same abstract dimension.
The one-spectator family admits two explicit coordinate charts with a
central cross-product transition. At two internal spectators, six reduced
spacing words carry a flat 144-dimensional stationary-edge core connection,
while the word 212 has an additional quaternionic residual invisible to its
incident hinges. We then construct the three-spectator quotient at 222. It
has dimension 444, an intrinsic 432-dimensional outer-edge subspace, and a
12-dimensional residual quotient. A specified central-slot right decoder
induces an isomorphism from the 212 residual tensored with the vector
representation onto this new residual quotient. The same suspension fails
to descend to the complete quotients: its obstruction image is exactly the
432-dimensional core. All finite rank claims are over the rationals and are
accompanied by exact arithmetic certificates. The comparison operator is
part of the theorem; no choice-independent full transport or nonzero core
curvature is asserted.

**Snapshot scope.** This research snapshot consolidates the results for
mathematical review. The immutable Free Numbers Core v1.0.0 artifact is
a cited foundation, not a version replaced by this snapshot. The manuscript
reorganizes established source notes and the Note 26 result; it does not
claim a complete three-spectator atlas or a physical interpretation.
This is revision research-2026-09-07-audit1; the companion audit report
records the corrections and the verification boundary.

## Overview

We first describe the finite atlas through two internal spectators, then
construct the residual comparison for the three-spectator word 222.

Four ordered face responses meet along six labelled edge responses.  At the
minimal tetrahedral level their compatibility quotient is

\[
\mathbb H\otimes\mathbb H
=
W_{12}\mathbin{\overset\perp\oplus}K_4,
\qquad
\dim W_{12}=12,
\qquad
K_4\cong\mathbb H.
\tag{0.1}
\]

Insert one spectator among the five ordered gap positions.  Each of the five
resulting local quotients still has the same abstract 48-dimensional type

\[
T_6=(\mathbb H\otimes\mathbb H)\otimes V,
\qquad V=\operatorname{Im}\mathbb H.
\tag{0.2}
\]

Nevertheless, no single direct seed coordinate covers all five placements.
Two chart families are necessary:

\[
U_L=\{1,2,3\},
\qquad
U_R=\{1,3,4,5\}.
\tag{0.3}
\]

Their exterior overlap is trivial, while their central overlap is not:

\[
G_1=I,
\qquad
G_3=\operatorname{id}_{\mathbb H}\otimes\theta.
\tag{0.4}
\]

For \(a,w\in V\),

\[
\boxed{
\begin{aligned}
\theta(1\otimes w)
&=1\otimes w+
\sum_{\rho=1}^{3}e_\rho\otimes(e_\rho\times w),\\
\theta(a\otimes w)&=-w\otimes a,
\end{aligned}}
\qquad
a\times w=\frac12(aw-wa).
\tag{0.5}
\]

Thus the abstract local module does not record the whole object.  The
incidence of its labelled edge images and the transition between valid local
coordinates retain where the spectator was inserted.

The shortest accurate summary is therefore

\[
\boxed{
\text{same local quotient type}
\;\not\Rightarrow\;
\text{same placement coordinate},
}
\tag{0.6}
\]

and the first nontrivial coordinate change is an explicit cross-product
shear.

---

## 1. Minimal setup

Let

\[
\mathbb H=\operatorname{span}_{\mathbb R}\{1,i,j,k\},
\qquad
V=\operatorname{Im}\mathbb H.
\tag{1.1}
\]

For response depth \(m\), put

\[
\mathcal R_m=\operatorname{Hom}(V^{\otimes m},\mathbb H).
\tag{1.2}
\]

Choose four ordered gaps

\[
Q=\{q_1<q_2<q_3<q_4\}.
\tag{1.3}
\]

They are treated as the four vertices of an ordered tetrahedron.  The six
local edges are labelled

\[
12,13,14,23,24,34.
\tag{1.4}
\]

Four face responses restrict to the six pairwise common shadows.  Their
signed disagreement defines the matching map

\[
\partial_{n,Q}:
\mathcal R_{n-2}^{\oplus4}
\longrightarrow
\mathcal R_{n-3}^{\oplus6},
\tag{1.5}
\]

\[
(\partial_{n,Q}F)_{ab}
=
\rho_{q_a}^{q_aq_b}F_a
-
\rho_{q_b}^{q_aq_b}F_b.
\tag{1.6}
\]

The local relation object is the cokernel

\[
Y_{n,Q}:=\operatorname{coker}\partial_{n,Q}.
\tag{1.7}
\]

For each labelled edge, retain its image in the quotient:

\[
E_{ab}^{(n,Q)}
:=
\operatorname{im}
\left(
\mathcal R_{n-3}^{(ab)}\longrightarrow Y_{n,Q}
\right).
\tag{1.8}
\]

The restrictions in (1.6) have the following concrete construction. For
\(T=v_1\otimes\cdots\otimes v_n\) and a set of omitted gaps
\(S\subset\{1,\ldots,n-1\}\), set
\[
 A_{n,S}(T)(x)=v_n b_{n-1}v_{n-1}\cdots b_1v_1,
 \qquad
 b_g=\begin{cases}1,&g\in S,\\x_g,&g\notin S.\end{cases}
\]
Every terminal face \(A_{n,\{r\}}\) is onto. One can see this by replacing
\(v_{r+1}v_r\) by an arbitrary quaternion \(h\), then successively using
the invertible one-variable left and right encoders on the remaining probes.
The right encoder is
\[
 \Theta_R(h\otimes w)(z)=hzw,
 \qquad
 J_m(h;v_1,\ldots,v_m)(x_1,\ldots,x_m)
 =h x_m v_m\cdots x_1v_1.
\]
The left encoder is \(\Theta_L(w\otimes h)(z)=wzh\).
Their matrices in the quaternion basis are invertible. Thus the common-shadow
restriction, when factored through a face, is unique:
\[
 \rho_r^{rs}A_{n,\{r\}}=A_{n,\{r,s\}}.
\]
Its existence is the local decoder-collapse identity of Note 12. For all
finite supports reported here it is also checked entry by entry against the
literal product above. This fixes the matching map without choosing a basis
of its cokernel. It does not require the global all-length filling theorem.

We work over the rational quaternion algebra with \(i^2=j^2=k^2=ijk=-1\),
and extend scalars to \(\mathbb R\) for the usual diagonal \(SO(3)\)-action.
All reported rational ranks therefore also hold over \(\mathbb R\).
The word *atlas* refers here to a discrete family of quotient coordinates
and their labelled comparison maps; no ambient manifold is assumed.
Unless actual gap labels are explicitly stated, edge labels \(ab\) denote
the \(a\)-th and \(b\)-th support vertices. Local \(14\), for example, is
the long edge even when its actual gap labels are \((1,6)\).

The object relevant to placement is not only \(Y_{n,Q}\), but the decorated
quotient

\[
\mathscr Y_{n,Q}
=
\left(Y_{n,Q};E_{12},E_{13},E_{14},E_{23},E_{24},E_{34}\right).
\tag{1.9}
\]

This distinction is the starting point of the atlas.

---

## 2. The seed tetrahedron at \(n=5\)

At \(n=5\), there is one four-gap support.  Note 14 replaces an abstract
quotient basis by a closed, \(SO(3)\)-equivariant operator

\[
\omega_5:
\mathcal R_2^{\oplus6}
\longrightarrow
\mathbb H\otimes\mathbb H
\tag{2.1}
\]

satisfying

\[
\boxed{
\omega_5\partial_5=0,
\qquad
\operatorname{rank}\omega_5=16,
\qquad
\ker\omega_5=\operatorname{im}\partial_5.
}
\tag{2.2}
\]

Hence

\[
Y_{5,G_5}\cong\mathbb H\otimes\mathbb H.
\tag{2.3}
\]

Put \(e_0=1,e_1=i,e_2=j,e_3=k\). Define five maps

\[
P,A_0,B_0,C_0,D_0:
\mathbb H\otimes V\otimes V
\longrightarrow\mathbb H\otimes\mathbb H
\]

by

\[
\begin{aligned}
P(h,u,v)
&:=h\otimes uv,\\[1mm]
A_0(h,u,v)
&:=\sum_{a=0}^{3}he_a\otimes uv e_a,\\[1mm]
B_0(h,u,v)
&:=\sum_{a=0}^{3}he_a\otimes u e_a v,\\[1mm]
C_0(h,u,v)
&:=\sum_{a=0}^{3}e_a\otimes uvh e_a,\\[1mm]
D_0(h,u,v)
&:=\sum_{a=0}^{3}e_a h e_a v\otimes u.
\end{aligned}
\]

Associativity fixes all parentheses. Each map is \(SO(3)\)-equivariant:
quaternion multiplication is equivariant for conjugation, and every summed
pair of basis elements comes from the invariant tensor \(\sum_{a=0}^3e_a\otimes e_a\).

The six ordered blocks are
\[
\begin{aligned}
\Lambda_{12}&=P-\tfrac12B_0+\tfrac12C_0-D_0,\\
\Lambda_{13}&=P-\tfrac14A_0-\tfrac12B_0+\tfrac12C_0-D_0,\\
\Lambda_{14}&=-\tfrac14A_0-\tfrac12B_0,\\
\Lambda_{23}&=-\tfrac14A_0-\tfrac12C_0,\\
\Lambda_{24}&=P-\tfrac14A_0,\qquad \Lambda_{34}=P.
\end{aligned}
\]
Thus \(\omega_5(F)=\sum_{a<b}\Lambda_{ab}J_2^{-1}F_{ab}\).
Substitution gives four signed vertex identities
\[
\sum_{b>a}\Lambda_{ab}J_2^{-1}\rho_{q_a}^{q_aq_b}
=\sum_{b<a}\Lambda_{ba}J_2^{-1}\rho_{q_a}^{q_bq_a},
\]
which prove \(\omega_5\partial_5=0\). The block \(\Lambda_{34}=P\) is
onto, and the matching matrix has rank 200 in its 216-dimensional target.
These finite identities and ranks are verified over exact rational arithmetic
by the seed certificate. They prove (2.2).

Write \(\Lambda_{ab}\) for the six edge blocks of \(\omega_5\).  Their
ranks are

\[
\begin{array}{c|rrrrrr}
ab&12&13&14&23&24&34\\ \hline
\operatorname{rank}\Lambda_{ab}&16&12&16&4&12&16.
\end{array}
\tag{2.4}
\]

The two rank-12 images coincide, while the central rank-4 image supplies a
complement:

\[
W_{12}:=\operatorname{im}\Lambda_{13}
=\operatorname{im}\Lambda_{24},
\qquad
K_4:=\operatorname{im}\Lambda_{23},
\tag{2.5}
\]

\[
\mathbb H\otimes\mathbb H=W_{12}\oplus K_4.
\tag{2.6}
\]

Note 18 makes this split canonical.  Define

\[
\iota(q)=\sum_{\alpha=0}^{3}e_\alpha\otimes qe_\alpha,
\qquad
\nu=\frac14\iota^*,
\tag{2.7}
\]

where \(e_0=1,e_1=i,e_2=j,e_3=k\).  Then

\[
\boxed{
K_4=\iota(\mathbb H),
\qquad
W_{12}=\ker\nu=\iota(\mathbb H)^\perp.
}
\tag{2.8}
\]

Thus the seed contains a canonical orthogonal \(12+4\) channel split, not
merely a dimension decomposition.

The adjoint uses the Euclidean quaternion inner product and its tensor
product, with \(1,i,j,k\) orthonormal. Explicitly,
\(\iota^*(x\otimes y)=y\bar x\) and \(\iota^*\iota=4I\).

The quaternion coordinate of the six edge blocks has the exact incidence
pattern

\[
\begin{array}{c|rrrrrr}
ab&12&13&14&23&24&34\\ \hline
\operatorname{rank}(\nu\Lambda_{ab})&4&0&4&4&0&4\\
\text{outer sign}&+&0&-&\text{central}&0&+
\end{array}
\tag{2.9}
\]

This labelled pattern is the seed datum to be compared after a spectator is
inserted.

---

## 3. One spectator and five placements

Let

\[
B_5=\{1,2,3,4,5\},
\qquad
Q_s=B_5\setminus\{s\}.
\tag{3.1}
\]

The omitted gap \(s\) is the spectator position.  For every \(s\),

\[
\dim Y_{6,Q_s}=48,
\qquad
Y_{6,Q_s}\cong T_6
:=(\mathbb H\otimes\mathbb H)\otimes V.
\tag{3.2}
\]

The equality of abstract type does not produce one common seed coordinate.
Use the three full-rank seed edges as possible anchors:

\[
L=12,
\qquad
M=14,
\qquad
R=34.
\tag{3.3}
\]

Exact rational classification gives

\[
\begin{array}{c|c|ccc}
s&Q_s&L&M&R\\ \hline
1&(2,3,4,5)&\checkmark&\checkmark&\checkmark\\
2&(1,3,4,5)&\checkmark&\checkmark&-\\
3&(1,2,4,5)&\checkmark&-&\checkmark\\
4&(1,2,3,5)&-&-&\checkmark\\
5&(1,2,3,4)&-&-&\checkmark.
\end{array}
\tag{3.4}
\]

Every marked entry determines a unique surjective quotient coordinate

\[
\Omega_s^e:
(\mathbb H\otimes V^{\otimes3})^{\oplus6}
\longrightarrow T_6
\tag{3.5}
\]

whose kernel is exactly the image of the local matching map:

\[
\boxed{
\ker\Omega_s^e=\operatorname{im}\widehat\partial_{6,Q_s}.
}
\tag{3.6}
\]

The unmarked entries are impossible over \(\mathbb Q\), not merely absent
from one computation.

For precision, the direct normalization on the anchor edge \(e\) is
\[
 (\Omega_s^e)_e(h;v_1,v_2,v_3)
 =\Lambda_e(h;v_{a_1},v_{a_2})\otimes v_t.
\]
Here the three remaining probe slots are in increasing gap order;
\(a_1<a_2\) are the two slots belonging to the support and \(t\) is the
spectator slot. Compatibility uniquely completes each marked anchor.

The middle chart adds no new family.  The two essential domains are

\[
\boxed{
U_L=\{1,2,3\},
\qquad
U_R=\{1,3,4,5\},
\qquad
U_L\cup U_R=B_5.
}
\tag{3.7}
\]

This is the first exact placement atlas in the program.

---

## 4. The overlap transition

The two charts overlap at one exterior placement and one central placement:

\[
U_L\cap U_R=\{1,3\}.
\tag{4.1}
\]

At \(s=1\),

\[
\boxed{\Omega_1^L=\Omega_1^R.}
\tag{4.2}
\]

At \(s=3\),

\[
\boxed{
\Omega_3^L=G\Omega_3^R,
\qquad
G=\operatorname{id}_{\mathbb H}\otimes\theta.
}
\tag{4.3}
\]

Put

\[
\delta(w)=
\sum_{\rho=1}^{3}e_\rho\otimes(e_\rho\times w).
\tag{4.4}
\]

Then the transition is the closed map

\[
\boxed{
\begin{aligned}
\theta(1\otimes w)&=1\otimes w+\delta(w),\\
\theta(a\otimes w)&=-w\otimes a
\qquad(a,w\in V).
\end{aligned}}
\tag{4.5}
\]

The first line contains the essential alternating correction.  A spectator
outside the active region gives no correction; a spectator between the two
active pairs forces a cross-product term.

The internal decomposition

\[
\mathbb H\otimes V
=
(1\otimes V)\oplus\delta(V)\oplus\operatorname{Sym}^2V
\tag{4.6}
\]

puts \(\theta\) into the form

\[
\theta=R+N,
\qquad
R^2=I,
\qquad
N^2=0,
\qquad
\operatorname{rank}N=3.
\tag{4.7}
\]

Its minimal polynomial is

\[
\boxed{m_\theta(t)=(t-1)^2(t+1).}
\tag{4.8}
\]

Therefore the transition is not a permutation of tensor slots.  It is an
involutive reflection together with a three-dimensional nilpotent shear.
Over characteristic zero it has infinite order.

In (4.7), \(R\) is the identity on \(1\otimes V\) and minus the tensor
flip on \(V\otimes V\); \(N(1\otimes w)=\delta(w)\) and
\(N(V\otimes V)=0\). In particular \(RN=NR\).

This is a statement about a coordinate transition.  No repeated power in
(4.8) is yet interpreted as a geometric loop.

---

## 5. What the placement remembers

At the central support

\[
Q_3=(1,2,4,5),
\tag{5.1}
\]

the long edge \(14=(1,5)\) has image dimension 44 rather than 48.  Its
four-dimensional quotient is detected by the cap residual of Note 17.

In the right chart define

\[
\beta_R((x\otimes y)\otimes w)=xw\bar y.
\tag{5.2}
\]

On actual responses define
\[
 \lambda_3^L(F)=\sum_{a,b=1}^3 e_bF(e_a,e_a,e_b),\qquad
 \lambda_3^R(F)=\sum_{a,b=1}^3 F(e_b,e_a,e_a)e_b.
\]
The chart in (3.5) uses decoded edge tensors, so write
\(\widehat\lambda_3^\bullet=\lambda_3^\bullet J_3\) and
\(\widehat\chi_6=\chi_6(\bigoplus_e J_3)\). This makes the domains in
the following identity explicit.

Then

\[
\boxed{
\beta_R\Omega_3^R
=
\widehat\chi_6
=
(-\widehat\lambda_3^L,+\widehat\lambda_3^L,0,0,
-\widehat\lambda_3^R,+\widehat\lambda_3^R).
}
\tag{5.3}
\]

Identify \(Y_{6,Q_3}\) with \(T_6\) by the induced right chart, so that
the edge images below are subspaces of \(T_6\). Then

\[
\boxed{
E_{14}=\ker\beta_R,
\qquad
T_6/E_{14}\cong\mathbb H.
}
\tag{5.4}
\]

Tensor the seed split (2.8) with \(V\):

\[
T_6
=
(W_{12}\otimes V)
\mathbin{\overset\perp\oplus}
(K_4\otimes V).
\tag{5.5}
\]

The direct extension of the seed quaternion does not survive the long-edge
quotient:

\[
\boxed{
\beta_R(K_4\otimes V)=0,
\qquad
K_4\otimes V\subset E_{14}.
}
\tag{5.6}
\]

The surviving quaternion is instead a quotient of
\(W_{12}\otimes V\).  Thus the spectator does not carry the seed channel
forward by a placement-blind tensor product.  It changes which channel
represents the residual.

The transition \(G\) explains this transfer.  It mixes the two summands in
(5.5), and in particular

\[
G(K_4\otimes V)\cap(K_4\otimes V)=0.
\tag{5.7}
\]

The seed quaternion has not been destroyed.  Its coordinate realization has
changed.

---

## 6. The residual is independent of the chart

Transporting \(\beta_R\) across the central transition gives

\[
\beta_L:=\beta_RG^{-1},
\tag{6.1}
\]

with the closed formula

\[
\beta_L((x\otimes y)\otimes w)=x(2y+\bar y)w.
\tag{6.2}
\]

The same observable is recovered from either chart:

\[
\boxed{
\widehat\chi_6
=
\beta_R\Omega_3^R
=
\beta_L\Omega_3^L.
}
\tag{6.3}
\]

This separates two roles:

- \(G\) records how the local coordinate changes with placement;
- \(\chi_6\) is the quaternionic residual unchanged by that coordinate
  change.

The coefficient \(2y+\bar y\) is not new bookkeeping.  The same
scalar-vector weighting already occurs in the canonical central coordinate
of the \(n=5\) seed.  The atlas transition forces it to reappear.

---

## 7. The exceptional two-spectator quotient at \(n=7\)

The \(n=6\) atlas is complete for one spectator. Notes 16 and 21 identify
and then fully coordinate the exceptional two-spectator continuation.

The first ordered support with parity separation

\[
\mathrm O\,\mathrm O\mid\mathrm E\,\mathrm E
\tag{7.1}
\]

is uniquely

\[
\boxed{(1,3\mid4,6),}
\tag{7.2}
\]

whose spacing is \((2,1,2)\).  On the four cross edges define

\[
\kappa_{212}
(F_{13},F_{14},F_{23},F_{24})
=
\varepsilon_4(F_{13})
-\varepsilon_4(F_{14})
-\varepsilon_4(F_{23})
+\varepsilon_4(F_{24}),
\tag{7.3}
\]

where

\[
\varepsilon_4(F)
=
\sum_{a,b=1}^{3}F(e_a,e_a,e_b,e_b).
\tag{7.4}
\]

Then, over \(\mathbb Q\),

\[
\boxed{
\mathcal R_5^{\oplus4}
\xrightarrow{\partial_\square}
\mathcal R_4^{\oplus4}
\xrightarrow{\kappa_{212}}
\mathbb H
\longrightarrow0,
\qquad
\ker\kappa_{212}=\operatorname{im}\partial_\square.
}
\tag{7.5}
\]

Thus the exceptional four-dimensional residual at \(n=7\) is the complete
cokernel of an alternating quaternionic cross square.  Its position is
forced by order and parity, not guessed from the dimension anomaly.

Note 21 transports a full-rank edge anchor from the \(n=6\) atlas and proves
that it has a unique compatible completion

\[
C_{212}:E_{(1,3,4,6)}\longrightarrow
T_7:=(\mathbb H\otimes\mathbb H)\otimes V^{\otimes2}.
\tag{7.6}
\]

The core coordinate and the square residual exactly exhaust the quotient:

\[
\boxed{
Y_{7,(1,3,4,6)}
\cong T_7\oplus\mathbb H,
\qquad
\dim Y_{7,(1,3,4,6)}=144+4=148.
}
\tag{7.7}
\]

The six labelled edge ranks split as

\[
\begin{array}{c|rrrrrr}
&12&13&14&23&24&34\\ \hline
\text{core}&144&108&144&36&108&144\\
\text{full exceptional}&144&112&148&40&112&144.
\end{array}
\tag{7.8}
\]

Thus the extra quaternion is transverse to the transported 144-dimensional
spectator core and is seen exactly on the four cross edges.

---

## 8. The complete reduced two-spectator atlas

Exterior suspension strips off every spectator lying strictly outside the
support interval. At \(n=7\), the irreducible two-spectator problem therefore
consists of the six positive spacing words

\[
113,\quad122,\quad131,\quad212,\quad221,\quad311.
\tag{8.1}
\]

For each of the five generic words \(\lambda\ne212\), Note 23 transports one
full-rank \(n=6\) edge anchor and proves that local compatibility completes it
uniquely to an exact quotient coordinate

\[
C_\lambda:E_{Q_\lambda}\longrightarrow T_7,
\qquad
\ker C_\lambda=\operatorname{im}\widehat\partial_{7,Q_\lambda}.
\tag{8.2}
\]

Consequently the full characteristic-zero dimension row is

\[
\boxed{
\begin{array}{c|rrrrrr}
\lambda&113&122&131&212&221&311\\ \hline
\dim Y_{7,Q_\lambda}&144&144&144&148&144&144.
\end{array}}
\tag{8.3}
\]

The generic words fall into two edge-incidence classes. The exterior-type
words \(113,311\) have ranks

\[
(144,108,144,36,108,144),
\tag{8.4}
\]

whereas the three central words \(122,131,221\) have

\[
(144,108,132,36,108,144).
\tag{8.5}
\]

The latter lose precisely the \(\mathbb H\otimes V\) spin profile

\[
(1,6,5,0,0)
\tag{8.6}
\]

from the long-edge image. The exceptional word \(212\) instead restores the
144-dimensional standard core and adds the transverse cross-edge quaternion
of Section 7. Hence the reduced layer has three exact structural classes:

\[
\boxed{
\begin{array}{c|c}
113,311&\text{standard exterior-type profile}\\
122,131,221&\text{central long-edge defect}\\
212&\text{standard core plus cross-edge }\mathbb H.
\end{array}}
\tag{8.7}
\]

In (8.6), the entries are the dimensions of the spin-\(0,1,2,3,4\)
isotypic subspaces, not the numbers of irreducible copies. They sum to 12.

Together with exterior suspension, this closes all fifteen tetrahedral
supports at \(n=7\) over \(\mathbb Q\). Quotient existence and dimension
are no longer the finite problem. Note 24 takes the next step by comparing
all transported direct-anchor completions.

---

## 9. The transported-anchor transition groupoid

Write the two ordered spectator factors as \(V_a,V_b\), \(a<b\), and put

\[
T_7=\mathbb H_L\otimes\mathbb H_R\otimes V_a\otimes V_b.
\tag{9.1}
\]

If \(\phi_{\alpha,r}\) applies an operator
\(\phi:\mathbb H\otimes V\to\mathbb H\otimes V\) to the indicated
quaternion/vector pair, Note 24 proves that every transported direct-anchor
transition is generated by

\[
\boxed{
A=(\theta^{-1})_{R,a},
\qquad
B=(\theta^{-1})_{R,b},
\qquad
S=(-\theta)_{L,b}.
}
\tag{9.2}
\]

The generic history chains are

\[
\boxed{
122:S,A,
\qquad
131:B,S,A,
\qquad
221:B,S,
}
\tag{9.3}
\]

while all admissible histories collapse to one coordinate at \(113\) and
\(311\). Across all six reduced words, twenty histories yield fourteen
distinct core coordinates.

The factor supports determine the algebra:

\[
AS=SA,
\qquad
\operatorname{rank}[A,B]=64,
\qquad
\operatorname{rank}[S,B]=51.
\tag{9.4}
\]

The full internal composite has

\[
\boxed{
m_{ASB}(t)
=(t-1)^2(t+1)^3(t^2+1)(t^2-t+1).
}
\tag{9.5}
\]

Thus overlapping copies of the first cross-product shear create
\(\Phi_4\) and \(\Phi_6\) rotational factors. At the exceptional word the
full transition is instead sharply block diagonal:

\[
\boxed{
(C_1,\kappa_{212})
=
(S\oplus I_{\mathbb H})(C_0,\kappa_{212}).
}
\tag{9.6}
\]

The extra quaternion is fixed rather than converted into a core shear. This
rules out the simplest attempt to call the two-history comparison curvature.
Note 25 then constructs the required transport between distinct spacing
words and tests its only independent loop.

---

## 10. The spacing-word connection and localized defect

The six positive compositions of \(5\) form the reduced word graph

\[
\Gamma_7
=
\{113\!-\!122,\ 122\!-\!131,\ 122\!-\!212,
131\!-\!221,\ 212\!-\!221,\ 221\!-\!311\}.
\tag{10.1}
\]

An elementary edge slides one internal support vertex by one gap. The two
support tetrahedra share a triangular face. Inside that face, the outer
edge on the stationary side is present as the same decoded response
variable in both local complexes.

For every adjacent pair \(\lambda,\mu\), the two selected 144-dimensional
core coordinates have full rank and the same row space on that stationary
hinge. Hence the equation

\[
\boxed{
(C_\mu)_{h_{\lambda\mu}}
=g_{\lambda\mu}(C_\lambda)_{h_{\lambda\mu}}
}
\tag{10.2}
\]

defines a unique integral \(SO(3)\)-equivariant isomorphism. These six
arrows are genuine inter-object transports, not coordinate changes on one
quotient.

The graph has one independent cycle. Its exact holonomy is

\[
\boxed{
g_{212,122}g_{221,212}g_{131,221}g_{122,131}
=I_{144}.
}
\tag{10.3}
\]

Thus the complete core connection is flat. This does not make the gluing
placement-blind. On the contrary, if all three common-face blocks are
concatenated, the two trace row spaces are maximally transverse:

\[
\dim(L_{\lambda,F}\cap L_{\mu,F})=0
\tag{10.4}
\]

on every graph edge. Generic face trace spaces project isomorphically
to their common 144-dimensional hinge row space. The full exceptional
trace instead has dimension 148 and a four-dimensional projection kernel.
Thus it is an extension over that hinge, not the graph of a function on it.
These distinct face traces prevent naive facewise identification.

At the exceptional word,

\[
Y_{7,Q_{212}}\cong T_{212}\oplus K_{212},
\qquad K_{212}\cong\mathbb H.
\tag{10.5}
\]

Both graph hinges incident to \(212\) are outer edges, and the closed square
coordinate vanishes on them:

\[
(\kappa_{212})_{13}=(\kappa_{212})_{46}=0.
\tag{10.6}
\]

Using the selected splitting, define the full maps to neighboring generic
fibers by \(\rho_{212,\mu}=g_{212,\mu}\pi_T\). These maps have kernel
\(K_{212}\). Their zero action on the residual is part of this definition:
the hinge equation alone allows every extension
\[
 \rho_B(t,k)=g_{212,\mu}t+B k,\qquad
 B\in\operatorname{Hom}(K_{212},T_\mu).
\]
Equivariance restricts \(B\) to equivariant maps; it does not force \(B=0\).
For example, in the displayed \(T_7\) model the nonzero injection
\(q\mapsto q\otimes1\otimes\sum_a e_a\otimes e_a\) is equivariant.
Thus the intrinsic assertion is invisibility on the hinges; forgetting is
the chosen extension. With that convention the complete finite answer is

\[
\boxed{
\text{flat transportable 144-core}
\quad+\quad
\text{\(212\)-supported quaternionic defect}.
}
\tag{10.7}
\]

The core loop is exactly flat and the defect does not enter the chosen
hinge transport. This separates chart shear, word holonomy, and placement
residual within the finite construction.

---

## 11. Three internal spectators: the 222 residual and descent obstruction

We now use actual gap labels. Let \(Q_{222}=(1,3,5,7)\), with
spectators \(2,4,6\). Removing these spectators one at a time gives parents
122, 212, and 221, respectively. The combinatorial deletion alone does not
define a map of quotients.

### 11.1 The intrinsic residual quotient

For a five-probe response define
\[
 \epsilon_5(F)(z)=\sum_{a,b=1}^3F(e_a,e_a,z,e_b,e_b),
\]
and put
\[
 \kappa_{222}(F)=\epsilon_5(F_{15})-\epsilon_5(F_{17})
                 -\epsilon_5(F_{35})+\epsilon_5(F_{37}).
\]
The blocks on 13 and 57 are zero. For \(v\in V\), the identity
\(\sum_a e_a v e_a=v\) removes the two paired probes. Each literal cross-edge
response reduces to the same response
\[
 v_8v_7v_6v_5\,z\,v_4v_3v_2v_1.
\]
Surjectivity of each terminal face therefore makes its two cross-edge
compositions agree. Their signed incidence contributions cancel, giving
\(\kappa_{222}\partial_{222}=0\). The three independent choices of the
open probe \(z\), each with four output components, show that the map is
onto \(\mathcal R_1\).

**Theorem 11.1 (the 222 object).** Over \(\mathbb Q\),
\[
 \operatorname{rank}\partial_{222}=5388,\qquad\dim Y_{222}=444.
\]
The dimensions of the labelled edge images are

| Actual edge | 13 | 15 | 17 | 35 | 37 | 57 |
|---|---:|---:|---:|---:|---:|---:|
| Image dimension | 432 | 336 | 408 | 120 | 336 | 432 |

The two outer-edge images coincide and give an intrinsic exact sequence
\[
 0\longrightarrow T_{222}\longrightarrow Y_{222}
 \xrightarrow{\bar\kappa_{222}}\mathcal R_1\longrightarrow0,
 \qquad \dim T_{222}=432.
\]
In particular,
\[
 T_{222}=E^Y_{13}=E^Y_{57}=\ker\bar\kappa_{222},\qquad
 D_{222}:=Y_{222}/T_{222}\cong\mathcal R_1.
\]
No complementary 12-dimensional subspace inside \(Y_{222}\) is chosen.

*Proof.* The companion certificate constructs the rational matching in
natural face coordinates and right-decoded edge coordinates. Its target
dimension is 5832. A reconstructed 444-row annihilator is checked against the
matching over the integers and has full row rank. Matching ranks 5388 over
both prime fields give the opposite bound over \(\mathbb Q\). The six
edge ranks and the 432-dimensional joint outer-edge image are verified using
exact rational row identities. Since \(\kappa_{222}\) is onto and vanishes
on the outer edges, each 432-dimensional outer image equals its kernel in
\(Y_{222}\). This proves the sequence and the equalities. Full construction
and all finite matrices are reproducible from Note 26's certificate.

On the generic parent sides, Note 22's exterior edge suspension gives
\[
 Y_{122}\otimes V\xrightarrow{\sim}T_{222},\qquad
 Y_{221}\otimes V\xrightarrow{\sim}T_{222}.
\]
The first uses actual child edge 13 and the second uses 57 (with the standard
tensor flip for the left suspension). In each case the carried parent block
and the child block have the same kernel and rank 432. This proves the
unique descended isomorphism onto the core; it does not define a projection
from the complete child quotient onto that core.

### 11.2 A specified central-slot decoder comparison

For the central parent, put \(D_{212}=Y_{212}/T_{212}\), where
\(T_{212}=\ker\bar\kappa_{212}\) is the common 144-dimensional outer-edge
image. Thus \(D_{212}\cong\mathbb H\). The anchored summand \(K_{212}\)
of Section 7 maps isomorphically onto this intrinsic quotient.

Choose the **central-slot right decoder suspension**. On every edge, insert
an argument \(z\) at actual gap 4, but multiply its value on the right:
\[
 (\Sigma_4^R(F\otimes w))(\ldots,z,\ldots)
       =F(\ldots,\widehat z,\ldots)\,z\,w.
\]
This is an explicitly chosen response operator. It is not identified with
inserting a vector into a literal state word, and no full chain-map property
is assumed. Invertibility of the local encoder makes it an isomorphism
\(E_{212}\otimes V\to E_{222}\).

On the cross edges, the open argument is the middle one, so the paired sums
give the exact residual square
\[
 \boxed{\kappa_{222}\Sigma_4^R
 =\Theta_R(\kappa_{212}\otimes\operatorname{id}_V),
 \qquad \Theta_R(k\otimes w)(z)=kzw.}
\]
This identity is checked edge by edge in the certificate as well.

**Theorem 11.2 (residual comparison and full descent obstruction).** The
chosen suspension induces an isomorphism
\[
 \beta_R:D_{212}\otimes V\xrightarrow{\sim}D_{222},
 \qquad\operatorname{rank}\beta_R=12,\quad\ker\beta_R=0.
\]
For a fixed unit \(w\in V\), the corresponding map on the parent residual
has rank four and zero kernel, with readout
\[
 f_k(z)=kzw,\qquad k=-f_k(w).
\]
However, the full suspension does not descend to
\(Y_{212}\otimes V\to Y_{222}\). Its obstruction
\[
 \mathcal O=\pi_{222}\Sigma_4^R
            (\partial_{212}\otimes\operatorname{id}_V)
\]
satisfies
\[
 \boxed{\operatorname{im}\mathcal O=T_{222},
        \qquad\operatorname{rank}\mathcal O=432.}
\]
Hence \(D_{222}\) is exactly the largest quotient of \(Y_{222}\) on which
this suspension descends from \(Y_{212}\otimes V\).

*Proof.* The residual square sends old matching relations into
\(\ker\bar\kappa_{222}=T_{222}\). Passing to that quotient gives
\(\Theta_R(\bar\kappa_{212}\otimes\operatorname{id}_V)\); its kernel is
\(T_{212}\otimes V\) and its induced residual map is an isomorphism.
For fixed unit \(w\), \(w^2=-1\) gives the displayed inverse readout.
The same residual square bounds the obstruction rank by 432. The certificate
exhibits rank 432 modulo each prime, using operators whose exact rational
identities have been verified. The upper and lower bounds agree. Every
quotient admitting full descent must kill this entire image; quotienting by
it is also sufficient. This proves the final universal property.

### 11.3 What has and has not been transported

The earlier projection-defined maps forget \(K_{212}\). The operation in this
section is a different, specified comparison into a new residual quotient;
its successful readout does not reverse those information-losing hinges.
The right decoder choice is part of Theorem 11.2. A choice-independent full
transport, or a local rule that turns the representative ambiguity into a
new core state, is not provided.

The finite obstruction supplies a concrete next question: which additional
local condition, if any, determines a representative or a correction? It
is not a time-update law and is not nonzero core holonomy.

---

## 12. Results and scope

Stripped of the surrounding depth-filtration narrative, Notes 14--26 give
the following self-contained package.

1. **Closed tetrahedral quotient.**  The minimal six-edge relation object is
   explicitly \(\mathbb H\otimes\mathbb H\), with a canonical
   \(12+4\) orthogonal channel split.

2. **Placement-sensitive decoration.**  Isomorphic total quotients can be
   distinguished by the incidence of their six labelled edge images.

3. **Two-chart spectator atlas.**  The five one-spectator placements require
   two direct seed charts, and the existence and nonexistence of every chart
   anchor are exact over \(\mathbb Q\).

4. **Central cross-product transition.**  The exterior overlap is the
   identity, while the central overlap is the explicit reflection-plus-shear
   map \(G\).

5. **Channel transfer.**  The central placement changes which orthogonal
   seed channel carries the surviving quaternion.

6. **Invariant residual.**  The coordinate decoder changes across the
   overlap, but the quaternion-valued cap residual does not.

7. **Parity continuation.**  The first admissible two-spectator cross square
   produces an exact quaternionic residual at \(n=7\).

8. **Exceptional core--residual decomposition.**  A transported spectator
   core and the cross square give the exact split \(144+4\).

9. **Exterior functoriality.**  Left and right exterior spectators tensorize
   every quotient and labelled edge image, and the two suspensions commute.

10. **Complete reduced two-spectator layer.**  All six internal words have
    exact rational coordinates and certified edge-incidence profiles.

11. **Three-generator transition groupoid.**  All transported-anchor
    histories are generated by pair-local \(A,B,S\), and the exceptional
    residual is fixed by its full transition.

12. **Stationary-edge word connection.**  Every adjacent reduced word pair
    has a unique integral equivariant core transport descending from its
    shared outer hinge, and the unique independent loop is exactly flat.

13. **Localized quaternionic defect.**  Full common-face traces are
    transverse, while the exceptional quaternion vanishes on both incident
    hinges and is supported only at \(212\).

14. **Three-spectator residual comparison.** The word 222 has an intrinsic
    432-dimensional outer core and a 12-dimensional residual quotient.
    A specified right decoder induces an isomorphism from \(D_{212}\otimes V\)
    onto that quotient, while its full descent obstruction fills the core.

Ordered placement determines which local charts exist. Their transitions
define the stationary-edge core connection, while the exceptional residual
is invisible on the two incident hinges.

This is a complete finite algebraic atlas through two spectators, together
with its exterior towers, same-word transition groupoid, adjacent-word
connection, and closed-loop test. Calling the quaternion curvature would
still be premature: the first independently defined loop is flat, and the
quaternion lies in the kernel of both selected projection-defined maps.
Section 11 settles one three-internal-spectator object and a specified
residual comparison. The remaining three-spectator word complex and any
residual-coupled holonomy remain open.

---

\newpage

## 13. Sources and reproducibility

| Note | Role in this synthesis |
|---:|---|
| [14](../notes/14-closed-quaternionic-tetrahedral-operator.md) | closed seed operator \(\omega_5\) and the first \(12+4\) split |
| [15](../notes/15-spectator-placement-residuals.md) | decorated edge images and placement classification |
| [16](../notes/16-parity-square-quaternionic-residual.md) | all-odd parity square and exact \(n=7\) cross residual |
| [17](../notes/17-even-length-capped-five-edge-residual.md) | all-even cap complex and exact \(n=6\) residual |
| [18](../notes/18-canonical-seed-quaternion-coordinate.md) | Frobenius coordinate and orthogonal seed channels |
| [19](../notes/19-central-spectator-channel-transfer.md) | normalized \(n=6\) quotient, contraction \(\beta\), and channel transfer |
| [20](../notes/20-n6-spectator-atlas-and-central-shear.md) | complete one-spectator atlas and central transition |
| [21](../notes/21-n7-exceptional-core-decomposition.md) | exact exceptional \(144+4\) core--residual coordinate |
| [22](../notes/22-exterior-spectator-suspension.md) | all-length exterior suspension and strict left/right flatness |
| [23](../notes/23-n7-reduced-internal-word-atlas.md) | complete rational atlas of the six reduced \(n=7\) words |
| [24](../notes/24-n7-transported-anchor-transition-groupoid.md) | exhaustive anchor histories, three transition generators, and exceptional residual invariance |
| [25](../notes/25-n7-spacing-word-flat-core-and-quaternionic-defect.md) | stationary-edge word transport, core flatness, face transversality, and localized quaternionic defect |
| [26](../notes/26-n8-222-residual-redetection.md) | 444-dimensional 222 quotient, residual comparison, and full descent obstruction |

The companion archive supplies the original notes and the following certificates.
Earlier certificates retain their original claim boundaries; the release
verification record identifies which were executed for this snapshot.

```text
certificates/n8_222_redetection_certificate.py
```

The earlier exact computations are supplied by

```text
certificates/n5_quaternionic_second_differential_certificate.py
certificates/n5_central_channel_factorization_certificate.py
certificates/spectator_placement_residual_certificate.py
certificates/n7_exceptional_square_operator_certificate.py
certificates/n6_capped_five_edge_operator_certificate.py
certificates/n6_seed_cap_bridge_certificate.py
certificates/n6_spectator_chart_transition_certificate.py
certificates/n7_exceptional_core_decomposition_certificate.py
certificates/exterior_spectator_suspension_certificate.py
certificates/n7_internal_word_atlas_certificate.py
certificates/n7_anchor_transition_groupoid_certificate.py
certificates/n7_spacing_word_transport_certificate.py
```


## 14. Provenance and mathematical dependencies

Section 1 gives the local definitions. Complete derivations and computational
proof components are retained in the companion notes and certificates.

Foundation: Residual Chart Lab, *Free Numbers Core v1.0.0* (2026),
DOI [10.5281/zenodo.21328471](https://doi.org/10.5281/zenodo.21328471).

[Source repository](https://github.com/residual-chart-lab/free-number-core):
baseline `09b77f329d0c825c794443a0cd98cde89d8f1d73`; Note 26 commit `881ff66`.
The claim ledger, verification records, manifest and checksums fix the scope
and reproducibility of this MIT-licensed snapshot. No literature-wide novelty
or physical interpretation is claimed.
