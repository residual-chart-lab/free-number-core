# Standalone Synthesis — Ordered Tetrahedral Spectator Atlas

## Notes 14–20 reorganized around placement memory and chart transition

**Status:** synthesis and reorganization; no new theorem is claimed here

**Source:** Notes 14–20 and their exact certificates

**Purpose:** isolate the finite algebraic mechanism that can be understood
without first following the full probe-depth filtration program.  The central
object is the first exact spectator atlas at \(n=6\).  The odd-length square at
\(n=7\) is recorded separately as the first two-spectator continuation.

**Claim boundary:** the results below prove an order-sensitive local quotient,
a two-chart cover, a nontrivial quaternionic transition, and a chart-independent
residual.  They do not yet prove a closed-loop holonomy, a curvature theorem,
an all-\(n\) spectator functor, or a physical interpretation.

---

## 0. Executive statement

The seven notes establish the following finite phenomenon.

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

Then

\[
\boxed{
\beta_R\Omega_3^R
=
\chi_6
=
(-\lambda_3^L,+\lambda_3^L,0,0,-\lambda_3^R,+\lambda_3^R).
}
\tag{5.3}
\]

Moreover,

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
\chi_6
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

## 7. The first two-spectator continuation at \(n=7\)

The \(n=6\) atlas is complete for one spectator.  Note 16 records a related
but not yet atlas-connected phenomenon for two spectators.

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

What is not yet proved is the chain-level transport taking the one-spectator
transition \(G\) to this two-spectator square.  Equation (7.5) is therefore
the next compatible endpoint, not yet a face of the completed \(n=6\)
atlas.

---

## 8. The independent theorem package

Stripped of the surrounding depth-filtration narrative, Notes 14–20 give
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

The central implication is

\[
\boxed{
\text{ordered placement}
\longrightarrow
\text{choice of valid local chart}
\longrightarrow
\text{nontrivial transition}
\longrightarrow
\text{chart-independent residual}.
}
\tag{8.1}
\]

This is already a finite algebraic atlas.  Calling its transition
``curvature'' would still be premature: curvature requires a closed
comparison of multiple transport paths.  The next mathematical problem is
to construct the second-spectator transport and then ask whether a genuine
closed-path obstruction survives.

---

## 9. Source map

| Note | Role in this synthesis |
|---:|---|
| [14](../notes/14-closed-quaternionic-tetrahedral-operator.md) | closed seed operator \(\omega_5\) and the first \(12+4\) split |
| [15](../notes/15-spectator-placement-residuals.md) | decorated edge images and placement classification |
| [16](../notes/16-parity-square-quaternionic-residual.md) | all-odd parity square and exact \(n=7\) cross residual |
| [17](../notes/17-even-length-capped-five-edge-residual.md) | all-even cap complex and exact \(n=6\) residual |
| [18](../notes/18-canonical-seed-quaternion-coordinate.md) | Frobenius coordinate and orthogonal seed channels |
| [19](../notes/19-central-spectator-channel-transfer.md) | normalized \(n=6\) quotient, contraction \(\beta\), and channel transfer |
| [20](../notes/20-n6-spectator-atlas-and-central-shear.md) | complete one-spectator atlas and central transition |

The exact computations are supplied by

```text
certificates/n5_quaternionic_second_differential_certificate.py
certificates/n5_central_channel_factorization_certificate.py
certificates/spectator_placement_residual_certificate.py
certificates/n7_exceptional_square_operator_certificate.py
certificates/n6_capped_five_edge_operator_certificate.py
certificates/n6_seed_cap_bridge_certificate.py
certificates/n6_spectator_chart_transition_certificate.py
```
