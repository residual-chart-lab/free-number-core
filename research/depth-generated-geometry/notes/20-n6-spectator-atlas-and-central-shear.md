# Note 20 — The \(n=6\) Spectator Atlas and Central Shear

## five placements require two seed charts, and their central transition is a closed cross-product twist

**Status:** theorem over \(\mathbb Q\), with exact integer identities and
exact rational rank certificates

**Depends on:** Notes 14, 15, 18, and 19

**Claim boundary:** this note classifies all direct full-seed
normalizations of the five one-spectator \(n=6\) local quotients, proves
that two such chart families cover all placements, and writes the unique
nontrivial overlap transition in closed form. It is the first exact
placement atlas in this program. It is not yet an all-\(n\) spectator
functor, a closed-loop holonomy, or a curvature theorem.

---

## 0. Result in one line

Let

\[
B_5=\{1,2,3,4,5\},
\qquad
Q_s=B_5\setminus\{s\}
\tag{0.1}
\]

be the four-gap support obtained by omitting the spectator \(s\). Every
local tetrahedral quotient \(Y_{6,Q_s}\) has dimension \(48\) and abstract
type

\[
T_6=(\mathbb H\otimes\mathbb H)\otimes V.
\tag{0.2}
\]

The three full-rank seed edges \(12,14,34\) do **not** provide a single
placement-blind coordinate. Their exact domains of definition are

\[
\begin{array}{c|c|ccc}
s&Q_s&12\text{-chart }L&14\text{-chart }M&34\text{-chart }R\\ \hline
1&(2,3,4,5)&\checkmark&\checkmark&\checkmark\\
2&(1,3,4,5)&\checkmark&\checkmark&-\\
3&(1,2,4,5)&\checkmark&-&\checkmark\\
4&(1,2,3,5)&-&-&\checkmark\\
5&(1,2,3,4)&-&-&\checkmark
\end{array}
\tag{0.3}
\]

Thus

\[
U_L=\{1,2,3\},
\qquad
U_R=\{1,3,4,5\},
\qquad
U_L\cup U_R=B_5,
\tag{0.4}
\]

and \(U_L\cap U_R=\{1,3\}\).

At the exterior overlap \(s=1\), the coordinate change is trivial:

\[
\Omega^L_1=\Omega^R_1.
\tag{0.5}
\]

At the central overlap \(s=3\), it is not:

\[
\boxed{
\Omega^L_3=G\Omega^R_3,
\qquad
G=\operatorname{id}_{\mathbb H}\otimes\theta.
}
\tag{0.6}
\]

The entire \(48\)-dimensional transition is controlled by the following
\(12\)-dimensional closed map. For \(a,w\in V=\operatorname{Im}\mathbb H\),
put

\[
a\times w=\frac12(aw-wa),
\qquad
\delta(w)=\sum_{\rho=1}^{3}
e_\rho\otimes(e_\rho\times w).
\tag{0.7}
\]

Then

\[
\boxed{
\begin{aligned}
\theta(1\otimes w)&=1\otimes w+\delta(w),\\
\theta(a\otimes w)&=-w\otimes a.
\end{aligned}}
\tag{0.8}
\]

The first spectator therefore does not merely permute tensor slots when it
lies between the two active pairs. It creates an unavoidable alternating
cross-product term.

---

## 1. Direct seed coordinates

Write the vertices of every \(Q_s\) in their local order as \(1,2,3,4\),
and order the local edges by

\[
(12,13,14,23,24,34).
\tag{1.1}
\]

After the right decoder \(J_3^{-1}\) is applied on each edge, the local
matching map is

\[
\widehat\partial_{6,Q_s}:
\mathcal R_4^{\oplus4}
\longrightarrow
(\mathbb H\otimes V^{\otimes3})^{\oplus6},
\tag{1.2}
\]

with matrix shape \(648\times1296\) and rank \(600\).

The seed operator of Note 14 has edge-block ranks

\[
\begin{array}{c|rrrrrr}
e&12&13&14&23&24&34\\ \hline
\operatorname{rank}\Lambda_e&16&12&16&4&12&16.
\end{array}
\tag{1.3}
\]

Only \(12,14,34\) can therefore normalize a \(48\)-dimensional spectator
extension.

For one of these full edges \(e\), let

\[
A^e_s:\mathbb H\otimes V^{\otimes3}\longrightarrow T_6
\tag{1.4}
\]

be the direct extension of \(\Lambda_e\): the two nonspectator variables
feed the seed block in their induced order, while the omitted variable
\(s\) is carried as the final \(V\)-factor. An \(e\)-normalized chart is a
map

\[
\Omega^e_s:
(\mathbb H\otimes V^{\otimes3})^{\oplus6}
\longrightarrow T_6
\tag{1.5}
\]

such that

\[
\Omega^e_s\widehat\partial_{6,Q_s}=0,
\qquad
(\Omega^e_s)_e=A^e_s.
\tag{1.6}
\]

### Theorem 1.1 — exact direct-anchor classification

An \(e\)-normalized chart exists exactly for the entries marked in (0.3).
Whenever it exists, it is unique, onto, and

\[
\boxed{
\ker\Omega^e_s=\operatorname{im}\widehat\partial_{6,Q_s}.
}
\tag{1.7}
\]

Thus every marked entry gives an exact sequence

\[
\mathcal R_4^{\oplus4}
\xrightarrow{\ \widehat\partial_{6,Q_s}\ }
(\mathbb H\otimes V^{\otimes3})^{\oplus6}
\xrightarrow{\ \Omega^e_s\ }
T_6
\longrightarrow0.
\tag{1.8}
\]

### Exact proof

As in Note 19,

\[
128\widehat\partial_{6,Q_s}
\tag{1.9}
\]

is constructed over \(\mathbb Z\). For every marked entry in (0.3),
independent elimination modulo \(1009\) and \(1013\) reconstructs the same
small integer matrix

\[
4\Omega^e_s.
\tag{1.10}
\]

Every reconstructed matrix is then checked over the integers:

\[
\boxed{
(4\Omega^e_s)(128\widehat\partial_{6,Q_s})=0,
\qquad
(4\Omega^e_s)_e=4A^e_s.
}
\tag{1.11}
\]

The anchor is onto, so \(\Omega^e_s\) has rank \(48\). Since the matching
has rational rank \(600\), (1.7) follows by dimensions.

To prove the unmarked entries are genuinely impossible over \(\mathbb Q\),
choose any reconstructed reference coordinate and compare the row space of
its \(e\)-block \(B^e_s\) with the direct seed anchor. The exact ranks of
their vertical joins are

\[
\begin{array}{c|rrr}
s&\operatorname{rank}[B^{12}_s;A^{12}_s]
 &\operatorname{rank}[B^{14}_s;A^{14}_s]
 &\operatorname{rank}[B^{34}_s;A^{34}_s]\\ \hline
1&48&48&48\\
2&48&48&80\\
3&48&80&48\\
4&56&80&48\\
5&80&80&48.
\end{array}
\tag{1.12}
\]

The two row spaces agree exactly when the join rank is \(48\). This proves
both sides of (0.3) over \(\mathbb Q\), not merely over the two finite
fields.

Finally, two normalized quotient maps differ by an automorphism of \(T_6\).
Their common prescribed edge block is onto, so that automorphism fixes all
of \(T_6\) and must be the identity. This proves uniqueness.

The middle chart adds no new transition: wherever it exists,

\[
\Omega^M_s=\Omega^L_s
\qquad(s=1,2).
\tag{1.13}
\]

---

## 2. The central transition

The two essential chart families overlap twice. Direct integer comparison
gives

\[
\Omega^L_1=\Omega^R_1,
\qquad
\Omega^L_3=(\operatorname{id}_{\mathbb H}\otimes\theta)\Omega^R_3.
\tag{2.1}
\]

Because \(\Omega^R_3\) is onto, the second identity determines \(G\)
uniquely. In the basis

\[
(1,i,j,k)\otimes(i,j,k)
\tag{2.2}
\]

the entries of \(\theta\) all lie in \(\{-1,0,1\}\). For example,

\[
\begin{aligned}
\theta(1\otimes i)
 &=1\otimes i-j\otimes k+k\otimes j,\\
\theta(i\otimes j)&=-j\otimes i.
\end{aligned}
\tag{2.3}
\]

This is not a numerical fit to \(G\). The certificate constructs \(\theta\)
from (0.8) and verifies the full matrix identity (2.1) over \(\mathbb Z\).

The placement distinction is now exact:

- when the spectator is exterior at \(s=1\), left and right seed
  coordinates agree;
- when the spectator lies in the central gap at \(s=3\), the same two
  coordinates differ by the cross-product transition \(\theta\).

The abstract quotient type remains \(T_6\) in both cases. What changes is
the gluing of its distinguished edge-origin coordinates.

---

## 3. Reflection plus nilpotent shear

The closed formula immediately exposes the internal structure of
\(\theta\). There is an \(SO(3)\)-equivariant direct sum

\[
\boxed{
\mathbb H\otimes V
=
(1\otimes V)
\oplus\delta(V)
\oplus\operatorname{Sym}^2V.
}
\tag{3.1}
\]

Here \(\delta(V)=\Lambda^2V\), so the first two summands are two copies of
\(V_1\), while

\[
\operatorname{Sym}^2V\cong V_0\oplus V_2.
\tag{3.2}
\]

On these three pieces,

\[
\boxed{
\begin{aligned}
\theta(1\otimes w)&=1\otimes w+\delta(w),\\
\theta(\delta(w))&=\delta(w),\\
\theta(S)&=-S
\qquad(S\in\operatorname{Sym}^2V).
\end{aligned}}
\tag{3.3}
\]

Consequently

\[
\chi_\theta(t)=(t-1)^6(t+1)^6,
\qquad
\boxed{m_\theta(t)=(t-1)^2(t+1).}
\tag{3.4}
\]

The repeated factor is essential: on the two \(V_1\) copies, \(\theta\)
is one nontrivial \(2\times2\) unipotent block tensored with
\(\operatorname{id}_{V_1}\). Exact ranks are

\[
\operatorname{rank}(\theta-I)=9,
\quad
\operatorname{rank}(\theta-I)^2=6,
\quad
\operatorname{rank}(\theta+I)=6.
\tag{3.5}
\]

Put \(D=\theta-I\) and define

\[
P_-:=\frac14D^2,
\qquad
N:=D+\frac12D^2,
\qquad
R:=I-\frac12D^2.
\tag{3.6}
\]

Then

\[
\boxed{
\theta=R+N,
\qquad
R^2=I,
\qquad
N^2=0,
\qquad
RN=NR=N,
\qquad
\operatorname{rank}N=3.
}
\tag{3.7}
\]

Thus the central change of coordinates is an involutive reflection plus a
three-dimensional nilpotent shear. In particular,

\[
\theta^m=R^m+mN
\qquad(m\ge1),
\tag{3.8}
\]

so \(\theta\), and hence \(G\), has infinite order over characteristic zero.
This is an algebraic statement about the coordinate transition; repeated
powers are not yet being interpreted as a geometric loop.

The full transition inherits

\[
\chi_G(t)=(t-1)^{24}(t+1)^{24},
\qquad
m_G(t)=(t-1)^2(t+1),
\tag{3.9}
\]

and

\[
\operatorname{rank}(G-I)=36,
\qquad
\operatorname{rank}(G-I)^2=24.
\tag{3.10}
\]

Because cross product and the scalar-vector splitting of \(\mathbb H\) are
\(SO(3)\)-natural, \(\theta\) and \(G\) are \(SO(3)\)-equivariant. The
certificate also checks all three infinitesimal intertwining identities
over \(\mathbb Z\).

---

## 4. Exact mixing of the seed channels

Recall the seed decomposition from Note 18:

\[
\mathbb H\otimes\mathbb H
=W_{12}\mathbin{\overset\perp\oplus}K_4,
\qquad
K_4=\iota(\mathbb H).
\tag{4.1}
\]

Tensoring with \(V\) decomposes \(T_6\) into dimensions \(36+12\). Let
\(P_W,P_K\) denote the two projectors. The four exact transition-block
ranks are

\[
\begin{array}{c|cc}
&K_4\otimes V\text{ input}&W_{12}\otimes V\text{ input}\\ \hline
P_KG&12&12\\
P_WG&12&24.
\end{array}
\tag{4.2}
\]

In particular,

\[
\boxed{
G(K_4\otimes V)\cap(K_4\otimes V)=0,
\qquad
K_4\otimes V\subset G(W_{12}\otimes V).
}
\tag{4.3}
\]

So the transition does not preserve the seed \(12+4\) split tensored with
the spectator. It sends a full \(12\)-dimensional part of the old
\(W_{12}\otimes V\) channel onto the new \(K_4\otimes V\) channel, while
the old \(K_4\otimes V\) becomes a transverse graph across both pieces.

This is the coordinate mechanism behind Note 19's apparently paradoxical
channel transfer. The seed quaternion was not destroyed. The central
placement changes which subspace represents it.

---

## 5. The cap residual is chart-independent

In the right chart, Note 19 used

\[
\beta_R((x\otimes y)\otimes w)=xw\bar y
\tag{5.1}
\]

and proved

\[
\beta_R\Omega^R_3=\chi_6.
\tag{5.2}
\]

The transition polynomial gives

\[
G^{-1}=-G^2+G+I.
\tag{5.3}
\]

Transporting the decoder to the left chart produces another closed
contraction:

\[
\boxed{
\begin{aligned}
\beta_L
&:=\beta_RG^{-1},\\
\beta_L((x\otimes y)\otimes w)
&=x(2y+\bar y)w.
\end{aligned}}
\tag{5.4}
\]

Hence

\[
\boxed{
\chi_6
=\beta_R\Omega^R_3
=\beta_L\Omega^L_3.
}
\tag{5.5}
\]

The observable residual is unchanged; only its coordinate decoder changes.
The factor \(2y+\bar y\) is the same scalar-vector weight that already
appeared in Note 18's seed central coordinate

\[
\nu\Lambda_{23}(h,u,v)
=-\frac14uv(\bar h+2h).
\tag{5.6}
\]

Thus the coefficient that seemed local to the \(n=5\) seed returns as the
left decoder forced by the \(n=6\) chart transition.

---

## 6. What has been gained

Before this calculation, “placement-aware transport” meant that the six
edge-image profiles remembered the spectator location. It did not yet
supply transition maps.

Now the first full finite atlas exists:

\[
\boxed{
\text{five spectator placements}
=U_L\cup U_R,
\qquad
G_1=I,
\qquad
G_3=\operatorname{id}_{\mathbb H}\otimes\theta.
}
\tag{6.1}
\]

Three facts are simultaneous:

1. the local quotient has the same abstract \(SO(3)\)-type at all five
   placements;
2. no single direct seed coordinate covers all five;
3. the unique central overlap map contains a nonzero cross-product shear.

This is stronger than a placement-dependent rank fingerprint. It is a
closed, invertible, symmetry-preserving gluing law between two locally
valid reconstructions.

It also isolates exactly where the one-dimensional order becomes
insufficient. The exterior overlap is flat in the literal algebraic sense
\(G_1=I\); the overlap whose spectator separates the two active pairs is
the one that produces \(\delta(V)=\Lambda^2V\).

The word “twist” is justified here by the explicit alternating term in
(0.8). The word “curvature” is still withheld. A curvature statement needs
a closed comparison of multiple transport paths, not one nontrivial change
of chart.

---

## 7. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/n6_spectator_chart_transition_certificate.py
~~~

The script verifies:

- the exact seed edge ranks \(16,12,16,4,12,16\);
- the full direct-anchor coverage table (0.3);
- the incompatibility ranks (1.12) over exact rational arithmetic;
- reconstruction of every compatible \(4\Omega^e_s\) from both prime
  fields and its matching cancellation over \(\mathbb Z\);
- equality of the redundant \(14\)- and \(12\)-charts;
- \(G_1=I\) and \(G_3=\operatorname{id}_{\mathbb H}\otimes\theta\) over
  \(\mathbb Z\);
- the decomposition (3.1), action (3.3), minimal polynomial, and
  reflection-shear splitting;
- exact \(K/W\) block ranks and both incidences in (4.3);
- \(SO(3)\)-equivariance and the chart-independent cap identity (5.5).

Expected final line:

~~~text
ALL CHECKS PASSED
~~~

---

## 8. Remaining boundary

This note completes the one-spectator \(n=6\) atlas, but it does not yet
prove:

- a single closed formula for all six blocks of every \(\Omega^e_s\);
- functorial insertion of arbitrarily many spectators;
- that two successive copies or conjugates of \(\theta\) produce the
  \(n=7\) exceptional parity square;
- a cocycle around a genuine closed path;
- curvature, holonomy, topology, or a physical gauge field.

The next finite question is now rigid. At \(n=7\), transport two ordered
spectators through the seed coordinates, compare the available paths, and
test whether their nonconfluence factors through Note 16's canonical
\(\mathbb H\)-valued square residual. Only that comparison can promote the
present cross-product shear from a chart transition to a curvature
candidate.

**Subsequent status.** Note 22 proves functorial exterior insertion for
arbitrarily many spectators. Notes 21 and 23 construct exact anchored
coordinates for all six reduced two-spectator words, including the
exceptional \(144+4\) split. What remains is precisely the comparison step:
enumerating the several admissible anchors, computing their transitions,
and composing them around genuine closed paths.
