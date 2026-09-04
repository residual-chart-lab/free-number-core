# Note 25 — The \(n=7\) Spacing-Word Connection

## stationary-edge transport gives a flat 144-dimensional core and a quaternionic defect supported at \(212\)

**Status:** theorem over \(\mathbb Q\), with exact integer transition
identities, two-prime reconstruction, and a complete closed-loop check

**Depends on:** Notes 21, 23, and 24

**Claim boundary:** this note constructs transport between all adjacent
reduced two-spectator words at \(n=7\). It proves that the resulting core
connection is flat and that the exceptional quaternion is killed by both
incident hinge transports. It does not identify that quaternion with
curvature, construct transport for three internal spectators, or prove an
all-\(n\) word-atlas theorem.

---

## 0. Result in one line

The six reduced spacing words form a connected graph

\[
\Gamma_7:\qquad
\{113\!-\!122,\ 122\!-\!131,\ 122\!-\!212,
131\!-\!221,\ 212\!-\!221,\ 221\!-\!311\}.
\tag{0.1}
\]

At every vertex \(\lambda\), Notes 21 and 23 provide a
144-dimensional core coordinate

\[
C_\lambda:E_{Q_\lambda}\longrightarrow T_\lambda,
\qquad
T_\lambda\cong
(\mathbb H\otimes\mathbb H)\otimes V^{\otimes2}.
\tag{0.2}
\]

Each oriented edge \(\lambda\to\mu\) has a combinatorially distinguished
stationary outer edge \(h_{\lambda\mu}\) shared by the two supports. The two
core blocks on that edge have the same row space and full rank \(144\).
Therefore there is a unique integral \(SO(3)\)-equivariant isomorphism

\[
\boxed{
g_{\lambda\mu}:T_\lambda\xrightarrow{\sim}T_\mu,
\qquad
(C_\mu)_{h_{\lambda\mu}}
=g_{\lambda\mu}(C_\lambda)_{h_{\lambda\mu}}.
}
\tag{0.3}
\]

The graph has one independent cycle, and its holonomy is exactly trivial:

\[
\boxed{
g_{212,122}\,g_{221,212}\,g_{131,221}\,g_{122,131}
=I_{144}.
}
\tag{0.4}
\]

Thus the core coordinates form a flat local system on \(\Gamma_7\).
However, at the exceptional vertex,

\[
Y_{7,Q_{212}}\cong T_{212}\oplus\mathbb H,
\tag{0.5}
\]

and the intrinsic coordinate \(\kappa_{212}\) vanishes on both hinges
incident to \(212\). The distinguished defect-forgetting maps are therefore

\[
\boxed{
T_{212}\oplus\mathbb H
\xrightarrow{\ \pi_T\ }T_{212}
\xrightarrow{\ g\ }T_\mu,
\qquad
\ker(g\pi_T)=\mathbb H.
}
\tag{0.6}
\]

The complete reduced \(n=7\) atlas is consequently

\[
\boxed{
\text{flat 144-dimensional core}
\quad+\quad
\text{one quaternionic defect supported at }212.
}
\tag{0.7}
\]

---

## 1. The spacing-word graph

For a reduced support

\[
Q_\lambda=(q_1,q_2,q_3,q_4),\qquad q_1=1,\quad q_4=6,
\tag{1.1}
\]

write

\[
\lambda=(a,b,c)
=(q_2-q_1,q_3-q_2,q_4-q_3).
\tag{1.2}
\]

The positive solutions of \(a+b+c=5\) are

\[
113,\quad122,\quad131,\quad212,\quad221,\quad311.
\tag{1.3}
\]

There are two elementary rightward slides:

\[
\begin{aligned}
r_3(a,b,c)&=(a,b+1,c-1),&&c>1,\\
r_2(a,b,c)&=(a+1,b-1,c),&&b>1.
\end{aligned}
\tag{1.4}
\]

They move \(q_3\) or \(q_2\), respectively, by one gap. Their complete
adjacency list is

\[
\begin{array}{c|c|c|c}
\lambda\to\mu&\text{moved vertex}&\text{shared face}&
h_{\lambda\mu}\\ \hline
113\to122&q_3&(1,2,6)&(1,2)\\
122\to131&q_3&(1,2,6)&(1,2)\\
122\to212&q_2&(1,4,6)&(4,6)\\
131\to221&q_2&(1,5,6)&(5,6)\\
212\to221&q_3&(1,3,6)&(1,3)\\
221\to311&q_2&(1,5,6)&(5,6).
\end{array}
\tag{1.5}
\]

If \(q_3\) moves, the stationary hinge is the left outer edge
\((q_1,q_2)\). If \(q_2\) moves, it is the right outer edge
\((q_3,q_4)\). This rule determines the last column of (1.5) without any
linear-algebraic choice.

The graph has six vertices and six edges and is connected. Its cycle rank
is therefore one. A representative cycle is

\[
122\longrightarrow131\longrightarrow221
\longrightarrow212\longrightarrow122.
\tag{1.6}
\]

---

## 2. Stationary-edge descent

For \(\lambda\ne212\), use the selected transported coordinate of Note 23.
At \(212\), use the first transported core coordinate of Notes 21 and 24.
Changing to another coordinate from Note 24 only applies an invertible
vertex gauge and does not change the conjugacy class of a loop holonomy.

For an actual edge \(h\subset Q_\lambda\), write

\[
(C_\lambda)_h:
\mathbb H\otimes V^{\otimes4}\longrightarrow T_\lambda
\tag{2.1}
\]

for the corresponding decoded block. For every row of (1.5), exact
calculation gives

\[
\operatorname{rank}(C_\lambda)_{h_{\lambda\mu}}
=\operatorname{rank}(C_\mu)_{h_{\lambda\mu}}
=144
\tag{2.2}
\]

and

\[
\boxed{
\operatorname{row}(C_\lambda)_{h_{\lambda\mu}}
=\operatorname{row}(C_\mu)_{h_{\lambda\mu}}.
}
\tag{2.3}
\]

Because either block is onto, (2.3) determines one and only one map
\(g_{\lambda\mu}\) satisfying (0.3). The reverse block construction gives

\[
g_{\mu\lambda}=g_{\lambda\mu}^{-1}.
\tag{2.4}
\]

Both matrices have entries in \(\{0,\pm1\}\), and the identities

\[
(C_\mu)_h=g_{\lambda\mu}(C_\lambda)_h,\qquad
g_{\mu\lambda}g_{\lambda\mu}=I
\tag{2.5}
\]

hold over \(\mathbb Z\). Since the edge blocks are \(SO(3)\)-equivariant
and onto, uniqueness forces

\[
\boxed{g_{\lambda\mu}\text{ is }SO(3)\text{-equivariant}.}
\tag{2.6}
\]

This is the first non-tautological transport between **different** reduced
spacing words. It is not obtained by declaring two abstract
144-dimensional quotients equal; it descends from one literal response
variable present in both local complexes.

---

## 3. The six exact slides

Put

\[
X:=g_{113,122},\qquad R:=g_{122,131}.
\tag{3.1}
\]

The six transitions reduce exactly to

\[
\boxed{
\begin{array}{c|c|c}
\lambda\to\mu&g_{\lambda\mu}&m_{g_{\lambda\mu}}(t)\\ \hline
113\to122&X&(t-1)^3(t+1)^2\\
122\to131&R&(t-1)(t+1)^2\\
122\to212&-I&t+1\\
131\to221&-I&t+1\\
212\to221&R&(t-1)(t+1)^2\\
221\to311&-I&t+1.
\end{array}}
\tag{3.2}
\]

In particular, the two horizontal transitions around the central cell are
the same integral operator \(R\), while the two vertical transitions are
both \(-I\):

\[
g_{122,131}=g_{212,221}=R,\qquad
g_{122,212}=g_{131,221}=-I.
\tag{3.3}
\]

The right tail also has \(g_{221,311}=-I\). The longer polynomial of \(X\)
occurs on a tree edge and therefore contributes no independent holonomy.

These matrices depend on the selected vertex coordinates, as every
connection matrix must. Their stationary-edge definition, invertibility,
equivariance, and the identity or nonidentity of closed holonomy are
coordinate-independent.

---

## 4. Exact flatness of the core

Using (3.3), the holonomy of (1.6), based at \(122\), is

\[
\begin{aligned}
\operatorname{Hol}_{122}
&=g_{212,122}\,g_{221,212}\,
  g_{131,221}\,g_{122,131}\\
&=(-I)\,R^{-1}\,(-I)\,R\\
&=I_{144}.
\end{aligned}
\tag{4.1}
\]

This is an exact integer matrix identity. Since (1.6) generates the cycle
space of \(\Gamma_7\), every closed path has trivial holonomy:

\[
\boxed{\operatorname{Hol}_\gamma=I_{144}\quad
\text{for every closed path }\gamma\subset\Gamma_7.}
\tag{4.2}
\]

Equivalently, after choosing one base vertex and parallel-transporting its
basis along the graph, every core edge map can be gauged to the identity.
The reduced \(n=7\) core system is globally trivializable.

This result separates two phenomena which had to remain distinct:

1. Notes 20 and 24 exhibit genuine nontrivial, partly noncommuting chart
   transitions generated by the cross-product wall operator \(\theta\);
2. the new connection between distinct spacing words nevertheless has zero
   core holonomy on its first closed cell.

Thus a nontrivial shear is present, but this \(n=7\) word loop does not yet
carry nonzero curvature.

---

## 5. Why the whole common face is not the transport

Adjacent supports share three vertices and hence three edge-response
variables. Let \(F_{\lambda\mu}\) be that triangular face, and let

\[
\operatorname{Tr}_{F_{\lambda\mu}}C_\lambda
\tag{5.1}
\]

denote the horizontal concatenation of the three corresponding blocks. At
\(212\), use the full coordinate \((C_{212},\kappa_{212})\). Define

\[
L_{\lambda,F}
:=
\operatorname{row}\!\left(
\operatorname{Tr}_{F}C_\lambda
\right),
\tag{5.2}
\]

with the same full-coordinate convention at \(212\).

The exact ranks are maximal:

\[
\boxed{
\begin{array}{c|c|c|c|c}
\lambda-\mu&\dim L_{\lambda,F}&\dim L_{\mu,F}&
\dim(L_{\lambda,F}+L_{\mu,F})&\dim(L_{\lambda,F}\cap L_{\mu,F})\\ \hline
\text{generic--generic}&144&144&288&0\\
122-212&144&148&292&0\\
212-221&148&144&292&0.
\end{array}}
\tag{5.3}
\]

Here the generic--generic row covers the other four graph edges. The
concatenated rank reaches the sum of the two row counts in every case, so
the zero intersections in the last column hold over \(\mathbb Q\).

There is no contradiction between (2.3) and (5.3). Projection to the hinge
has the same 144-dimensional row space, but the other two blocks make the
two face traces different graphs over that common projection. In geometric
language, the tetrahedra share a hinge but do not lie in one common flat
face chart. Algebraically, this is exactly why the transport must be solved
from the hinge rather than imposed as equality of the whole face.

Equation (5.3) is an algebraic fold signature. Calling it curvature would
require an additional invariant comparison law; no such identification is
made here.

---

## 6. The exceptional quaternion is a vertex defect

For the exceptional support

\[
Q_{212}=(1,3,4,6),
\tag{6.1}
\]

Note 21 proves

\[
\boxed{
Y_{7,Q_{212}}\cong T_{212}\oplus K_{212},\qquad
K_{212}\cong\mathbb H,
}
\tag{6.2}
\]

where \(K_{212}\) is detected by \(\kappa_{212}\). The two graph edges
incident to \(212\) use the actual hinges

\[
(1,3)\qquad\text{and}\qquad(4,6).
\tag{6.3}
\]

These are precisely the two local outer edges of the exceptional
tetrahedron. Note 21's closed formula gives

\[
\boxed{
(\kappa_{212})_{13}=0,\qquad
(\kappa_{212})_{46}=0.
}
\tag{6.4}
\]

Consequently the direct-sum coordinate supplies two distinguished
defect-forgetting maps

\[
\begin{aligned}
\rho_{212,122}
&=g_{212,122}\circ\pi_T,
\\
\rho_{212,221}
&=g_{212,221}\circ\pi_T,
\end{aligned}
\qquad
\pi_T:T_{212}\oplus K_{212}\to T_{212},
\tag{6.5}
\]

and both satisfy

\[
\boxed{
\ker\rho_{212,\mu}=K_{212}\cong\mathbb H.
}
\tag{6.6}
\]

The core transports are reversible. The defect-forgetting maps incident to
\(212\) are not: the shared hinge contains no information from which to
reconstruct \(\kappa_{212}\). The hinge equation alone also cannot prescribe
any nonzero image for that invisible summand; such an extension would be
additional data. Thus the full 148-dimensional atlas is not a local system
of constant rank. Its canonically available part is the flat core system
together with a four-dimensional component supported only at one
vertex—equivalently, a quaternionic vertex defect over the spacing graph.

This gives a precise sense in which the interlaced word remembers something
which every neighboring generic placement forgets.

---

## 7. What is and is not curvature here

Three exact conclusions can now be stated without metaphor:

\[
\boxed{
\begin{aligned}
&\text{chart shear: nontrivial and noncommutative},\\
&\text{core word holonomy: trivial},\\
&\text{exceptional residual: nonzero but transport-invisible}.
\end{aligned}}
\tag{7.1}
\]

Therefore

\[
\kappa_{212}\ne\text{core curvature at }n=7.
\tag{7.2}
\]

What has been proved is already structural: the first complete finite word
atlas splits into a flat transportable sector and a localized sector which
cannot be propagated through the available boundary hinges. A future
curvature theorem would need one of the following genuinely new effects:

- a nonidentity closed holonomy with three or more internal spectators;
- a canonical extension law which couples a placement residual back into
  the transported core;
- a higher cell relation whose failure lands canonically in a residual
  summand.

Note 24 proves that the residual-to-core shear is zero inside the two
available \(212\) chart histories, and the present note proves that the
first word loop is core-flat. These are constraints on any later curvature
definition, not negative evidence against the program.

---

## 8. What this closes

Notes 21–25 now give, over \(\mathbb Q\):

1. every reduced \(n=7\) two-spectator quotient;
2. the exact \(144+4\) exceptional decomposition;
3. every transported direct-anchor coordinate at every word;
4. every same-word transition among those coordinates;
5. every adjacent-word stationary-edge transport;
6. the only independent closed-path holonomy;
7. the exact location of the quaternionic defect relative to that
   transport.

Together with the all-length exterior suspension of Note 22, this closes
the complete \(n=7\) two-spectator atlas, including both its objects and its
arrows.

The next genuinely new problem is no longer another \(n=7\) basis census.
It is the first three-internal-spectator atlas, where the word complex has
enough two-dimensional cells for residual transport and higher holonomy to
interact.

---

## 9. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/n7_spacing_word_transport_certificate.py
~~~

The certificate verifies:

- reconstruction of all six selected core coordinates independently over
  \(\mathbb F_{1009}\) and \(\mathbb F_{1013}\);
- full rank and row-space equality on all six stationary hinges;
- integral forward and reverse slides with entry alphabet
  \(\{0,\pm1\}\);
- exact stationary-edge, inverse, and \(SO(3)\)-equivariance identities;
- the six minimal polynomials in (3.2);
- the exact equalities in (3.3);
- identity holonomy around the unique central cycle;
- maximal transversality of every pair of common-face traces;
- exact vanishing of \(\kappa_{212}\) on both incident hinges;
- factorization of both full exceptional transports through the core, with
  four-dimensional residual kernel.

Expected final line:

~~~text
ALL CHECKS PASSED
~~~
