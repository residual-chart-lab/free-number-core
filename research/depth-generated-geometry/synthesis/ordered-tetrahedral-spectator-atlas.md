# Standalone Synthesis — Ordered Tetrahedral Spectator Atlas

## Notes 14–24 reorganized around placement memory and chart transition

**Status:** synthesis and reorganization; no new theorem is claimed here

**Source:** Notes 14–24 and their exact certificates

**Purpose:** isolate the finite algebraic mechanism that can be understood
without first following the full probe-depth filtration program. The central
object is the first exact spectator atlas at \(n=6\). The odd-length square
at \(n=7\) is the exceptional two-spectator continuation, the full reduced
six-word layer is exact over \(\mathbb Q\), exterior suspension propagates
these finite objects to exact all-length towers, and the resulting
transported-anchor groupoid has three closed pair-local generators.

**Claim boundary:** the results below prove an order-sensitive local quotient,
a two-chart cover, a nontrivial quaternionic transition, a chart-independent
residual, the complete exact two-spectator reduced atlas, an all-\(n\)
exterior spectator functor, and every same-word transported-anchor
transition at \(n=7\). They do not yet construct transports between
different internal words, a closed-loop holonomy, a curvature theorem, or a
physical interpretation.

---

## 0. Executive statement

The eleven notes establish the following finite phenomenon and its exterior
propagation.

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
rules out the simplest attempt to call the two-history comparison curvature
and makes the next target a transport between distinct spacing words.

---

## 10. The independent theorem package

Stripped of the surrounding depth-filtration narrative, Notes 14–24 give
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

8. **Exceptional core–residual decomposition.**  A transported spectator
   core and the cross square give the exact split \(144+4\).

9. **Exterior functoriality.**  Left and right exterior spectators tensorize
   every quotient and labelled edge image, and the two suspensions commute.

10. **Complete reduced two-spectator layer.**  All six internal words have
    exact rational coordinates and certified edge-incidence profiles.

11. **Three-generator transition groupoid.**  All transported-anchor
    histories are generated by pair-local \(A,B,S\), and the exceptional
    residual is fixed by its full transition.

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
\tag{10.1}
\]

This is a complete finite algebraic atlas through two spectators, together
with its exterior towers and same-word transition groupoid. Calling a
transition curvature would still be premature: curvature requires
independently defined transports between distinct word objects and a closed
path comparison. Constructing those word-level arrows is the next
mathematical problem.

---

## 11. Source map

| Note | Role in this synthesis |
|---:|---|
| [14](../notes/14-closed-quaternionic-tetrahedral-operator.md) | closed seed operator \(\omega_5\) and the first \(12+4\) split |
| [15](../notes/15-spectator-placement-residuals.md) | decorated edge images and placement classification |
| [16](../notes/16-parity-square-quaternionic-residual.md) | all-odd parity square and exact \(n=7\) cross residual |
| [17](../notes/17-even-length-capped-five-edge-residual.md) | all-even cap complex and exact \(n=6\) residual |
| [18](../notes/18-canonical-seed-quaternion-coordinate.md) | Frobenius coordinate and orthogonal seed channels |
| [19](../notes/19-central-spectator-channel-transfer.md) | normalized \(n=6\) quotient, contraction \(\beta\), and channel transfer |
| [20](../notes/20-n6-spectator-atlas-and-central-shear.md) | complete one-spectator atlas and central transition |
| [21](../notes/21-n7-exceptional-core-decomposition.md) | exact exceptional \(144+4\) core–residual coordinate |
| [22](../notes/22-exterior-spectator-suspension.md) | all-length exterior suspension and strict left/right flatness |
| [23](../notes/23-n7-reduced-internal-word-atlas.md) | complete rational atlas of the six reduced \(n=7\) words |
| [24](../notes/24-n7-transported-anchor-transition-groupoid.md) | exhaustive anchor histories, three transition generators, and exceptional residual invariance |

The exact computations are supplied by

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
```
