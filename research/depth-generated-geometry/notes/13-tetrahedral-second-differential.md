# Note 13 — Tetrahedral Second Differential

## first response syzygies are generated on four-face supports in the first three cases

**Status:** canonical construction for every \(n\ge5\); theorem over
\(\mathbb Q\) at \(n=5\); exact finite-field checks at \(n=6,7\) over
\(\mathbb F_{1009}\) and \(\mathbb F_{1013}\)

**Depends on:** Notes 10–12

**Claim boundary:** this note constructs a genuine next map after the all-
\(n\) pairwise terminal descent and proves that its composition with the
first matching map is zero. Exactness at the middle term is proved at \(n=5\)
and checked over two prime fields at \(n=6,7\). It is not yet proved for every
\(n\). The placement-dependent residual first seen at \(n=7\) is an
algebraic response residual; it is not identified with curvature.

---

## 0. Result in one line

Note 12 ended with

\[
0\longrightarrow V_n
\longrightarrow V^{\otimes n}
\xrightarrow{\mathbf B_n}C_n^0
\xrightarrow{\partial_n}C_n^1
\longrightarrow\mathfrak S_n
\longrightarrow0,
\tag{0.1}
\]

where

\[
C_n^0=\mathcal R_{n-2}^{\oplus(n-1)},
\qquad
C_n^1=\mathcal R_{n-3}^{\oplus\binom{n-1}{2}}.
\tag{0.2}
\]

The new construction is

\[
\boxed{
C_n^0\xrightarrow{\partial_n}C_n^1
\xrightarrow{\partial_n^{(2)}}C_n^2,
\qquad
\partial_n^{(2)}\partial_n=0,
}
\tag{0.3}
\]

with one local target for every four-element subset of the response-simplex
vertices. In the first three nontrivial lengths,

\[
\boxed{
\ker\partial_n^{(2)}=\operatorname{im}\partial_n
\quad(n=5,6,7),
}
\tag{0.4}
\]

where \(n=5\) is exact over \(\mathbb Q\), while \(n=6,7\) are exact checks
over the two stated finite fields.

Thus the 16-, 176-, and 1200-dimensional first syzygy modules are not merely
abstract cokernels. In these cases they are exactly the images of a map
assembled from four-face local data.

---

## 1. Why the obvious triangle differential fails

Let

\[
G_n:=\{1,\ldots,n-1\}
\tag{1.1}
\]

be the vertex set indexing terminal faces. A first guess is Čech-like: an
edge response should restrict to a response on each triple, and alternating
edge restrictions should give the next differential.

That guess is false for the actual ordered quaternionic responses.

At \(n=5\), write a pair of missing gaps as an edge and a triple of missing
gaps as a triangle. Of the twelve pair-to-triple incidences, the following
four do not factor:

\[
\begin{aligned}
(1,3)&\subset(1,2,3),\\
(1,4)&\subset(1,2,4),\\
(1,4)&\subset(1,3,4),\\
(2,4)&\subset(2,3,4).
\end{aligned}
\tag{1.2}
\]

These are precisely the long-edge incidences in the ordered gap geometry.
So a raw triple-shadow map cannot be declared by forgetting one more probe:
the required factorization is absent.

There is a second obstruction to forcing a triangle target. Restrict the
\(n=5\) first matching operator to any three faces and their three mutual
edges. Every such local operator has full row rank

\[
108.
\tag{1.3}
\]

Hence no nonzero first syzygy is supported on three faces. The first possible
support is not a triangle but a tetrahedron.

This is not a cosmetic shift in indexing. It says that the first relation
among pairwise compatibility equations is genuinely four-body.

---

## 2. The four-face local quotient

Fix \(Q\in\binom{G_n}{4}\). Select from \(C_n^0\) the four face blocks indexed
by \(Q\), and from \(C_n^1\) the six edge blocks whose endpoints both lie in
\(Q\):

\[
C^0_{n,Q}
:=
\bigoplus_{r\in Q}\mathcal R_{n-2},
\qquad
C^1_{n,Q}
:=
\bigoplus_{\{r,s\}\in\binom Q2}\mathcal R_{n-3}.
\tag{2.1}
\]

Let

\[
\partial_{n,Q}:C^0_{n,Q}\longrightarrow C^1_{n,Q}
\tag{2.2}
\]

be the corresponding local suboperator of \(\partial_n\). Define its local
relation object by

\[
\boxed{
Y_{n,Q}:=\operatorname{coker}\partial_{n,Q},
}
\tag{2.3}
\]

and write

\[
q_{n,Q}:C^1_{n,Q}\longrightarrow Y_{n,Q}
\tag{2.4}
\]

for the quotient map.

The point is that (2.3) does not assume a nonexistent edge-to-triangle
restriction. It records exactly the relations among the six edge equations
which are forced by four face variables.

Now put

\[
\boxed{
C_n^2
:=
\bigoplus_{Q\in\binom{G_n}{4}}Y_{n,Q}.
}
\tag{2.5}
\]

If

\[
p_Q^1:C_n^1\longrightarrow C^1_{n,Q}
\tag{2.6}
\]

selects the six edge blocks supported on \(Q\), define

\[
\boxed{
(\partial_n^{(2)}x)_Q
:=
q_{n,Q}(p_Q^1x).
}
\tag{2.7}
\]

Although a matrix for \(q_{n,Q}\) requires a quotient basis, the map to the
abstract quotient \(Y_{n,Q}\) is canonical.

---

## 3. The complex identity holds for every \(n\ge5\)

For every four-subset \(Q\), restriction commutes with the first matching
map:

\[
p_Q^1\partial_n
=
\partial_{n,Q}p_Q^0,
\tag{3.1}
\]

where \(p_Q^0:C_n^0\to C^0_{n,Q}\) selects the four face blocks. Therefore

\[
q_{n,Q}p_Q^1\partial_n
=
q_{n,Q}\partial_{n,Q}p_Q^0
=0.
\tag{3.2}
\]

Taking the direct sum over all \(Q\) gives the all-length identity

\[
\boxed{
\partial_n^{(2)}\partial_n=0
\qquad(n\ge5).
}
\tag{3.3}
\]

Consequently,

\[
\operatorname{im}\partial_n
\subseteq
\ker\partial_n^{(2)}.
\tag{3.4}
\]

The nontrivial question is whether four-face supports generate every first
syzygy, namely whether equality holds in (3.4).

---

## 4. The exact tetrahedron at \(n=5\)

Here \(G_5=\{1,2,3,4\}\), so there is only one four-subset. Thus

\[
C_5^2=Y_{5,G_5}.
\tag{4.1}
\]

The exact rational computation gives

\[
\dim C_5^1=216,
\qquad
\operatorname{rank}\partial_5=200,
\qquad
\dim Y_{5,G_5}=16.
\tag{4.2}
\]

The quotient map has rank 16, hence

\[
\dim\ker\partial_5^{(2)}=216-16=200.
\tag{4.3}
\]

Together with (3.4), this proves

\[
\boxed{
\ker\partial_5^{(2)}=\operatorname{im}\partial_5
\quad\text{over }\mathbb Q.
}
\tag{4.4}
\]

The Casimir decomposition of the actual quotient is

\[
\boxed{
Y_{5,G_5}
\cong
2V_0\oplus3V_1\oplus V_2
\cong
\mathbb H\otimes\mathbb H.
}
\tag{4.5}
\]

Thus the first 16-dimensional compatibility syzygy from Note 10 is precisely
the image of the tetrahedral second differential.

---

## 5. Five tetrahedra at \(n=6\)

Now \(G_6\) has five vertices and therefore five four-subsets. Over each of
\(\mathbb F_{1009}\) and \(\mathbb F_{1013}\), every local quotient has
dimension 48 and actual Casimir type

\[
\boxed{
Y_{6,Q}
\cong
3V_0\oplus6V_1\oplus4V_2\oplus V_3
\cong
\mathbb H^{\otimes2}\otimes V.
}
\tag{5.1}
\]

Therefore

\[
\dim C_6^2=5\cdot48=240.
\tag{5.2}
\]

The assembled second map satisfies

\[
\operatorname{rank}\partial_6^{(2)}=176,
\qquad
\dim\ker\partial_6^{(2)}=1080-176=904.
\tag{5.3}
\]

Since \(\operatorname{rank}\partial_6=904\), (3.4) becomes equality in both
prime fields:

\[
\boxed{
\ker\partial_6^{(2)}=\operatorname{im}\partial_6.
}
\tag{5.4}
\]

There is already a next residual:

\[
\dim\operatorname{coker}\partial_6^{(2)}=240-176=64,
\tag{5.5}
\]

and its measured Casimir type is

\[
\boxed{
5V_0\oplus9V_1\oplus5V_2\oplus V_3
\cong
\mathbb H^{\otimes3}.
}
\tag{5.6}
\]

So at \(n=6\), the first local quotient is
\(\mathbb H^{\otimes2}\otimes V\), while the part not consumed by gluing
the five tetrahedra is \(\mathbb H^{\otimes3}\).

---

## 6. The first placement-sensitive residual at \(n=7\)

The \(n=7\) computation is the first test not used in finding the \(n=5,6\)
pattern. The first matching map has

\[
\partial_7:C_7^0\longrightarrow C_7^1,
\qquad
\dim C_7^0=5832,
\qquad
\dim C_7^1=4860,
\tag{6.1}
\]

and, in both prime fields,

\[
\operatorname{rank}\partial_7=3660.
\tag{6.2}
\]

There are fifteen four-subsets \(Q\subset G_7\). Fourteen have

\[
\dim Y_{7,Q}=144
\tag{6.3}
\]

and Casimir type

\[
\boxed{
6V_0\oplus13V_1\oplus11V_2\oplus5V_3\oplus V_4
\cong
\mathbb H^{\otimes2}\otimes V^{\otimes2}.
}
\tag{6.4}
\]

Exactly one support is different:

\[
\boxed{
Q_{212}=(1,3,4,6).
}
\tag{6.5}
\]

Its consecutive spacing vector is

\[
(3-1,4-3,6-4)=(2,1,2).
\tag{6.5a}
\]

This support will therefore be called the **exceptional \(2\!-!1\!-!2\)
placement**. The earlier label “interlaced” was provisional: the intervals
\([1,3]\) and \([4,6]\) are disjoint in the standard order-theoretic sense,
so that word should not carry mathematical weight here. For this placement,

\[
\dim Y_{7,Q_{212}}=148
\tag{6.6}
\]

and

\[
\boxed{
Y_{7,Q_{212}}
\cong
7V_0\oplus14V_1\oplus11V_2\oplus5V_3\oplus V_4.
}
\tag{6.7}
\]

Comparing (6.4) and (6.7), the difference is exactly

\[
V_0\oplus V_1\cong\mathbb H.
\tag{6.8}
\]

Note 15 refines this total-module comparison by retaining the six labelled
edge images. Over both tested prime fields, the two exceptional outer images
coincide in a 144-dimensional subspace

\[
E_{12}=E_{34}=:W_{\mathrm{out}},
\tag{6.8a}
\]

and the residual is the canonical quotient

\[
K_{212}:=Y_{7,Q_{212}}/W_{\mathrm{out}}\cong\mathbb H.
\tag{6.8b}
\]

Exactly the four cross edges \(13,14,23,24\) surject onto (6.8b) in both
fields. Thus the four-dimensional difference is a single shared
edge-incidence channel, not only a multiplicity increase in the total
character.

Note 16 then realizes the quotient by the two outer images directly over
\(\mathbb Q\), through the closed square operator

\[
\kappa_{212}(F_{13},F_{14},F_{23},F_{24})
=
\varepsilon_4(F_{13})-\varepsilon_4(F_{14})
-\varepsilon_4(F_{23})+\varepsilon_4(F_{24}).
\tag{6.8c}
\]

Thus the naive spectator law

\[
Y_{n,Q}\stackrel{?}{\cong}
\mathbb H^{\otimes2}\otimes V^{\otimes(n-5)}
\tag{6.9}
\]

is false without a placement correction. The first counterterm is a local
quaternionic residual carried by the exceptional \(2\!-!1\!-!2\)
four-support.

Summing all fifteen targets gives

\[
\dim C_7^2
=14\cdot144+148
=2164.
\tag{6.10}
\]

The assembled map has

\[
\operatorname{rank}\partial_7^{(2)}=1200,
\qquad
\dim\ker\partial_7^{(2)}=4860-1200=3660.
\tag{6.11}
\]

Hence the two-prime checks again give

\[
\boxed{
\ker\partial_7^{(2)}=\operatorname{im}\partial_7.
}
\tag{6.12}
\]

By Note 12, this 1200-dimensional image has the universal first-syzygy type

\[
45V_0\oplus100V_1\oplus90V_2\oplus45V_3\oplus10V_4.
\tag{6.13}
\]

The exceptional four dimensions do not increase the rank of
\(\partial_7^{(2)}\). They survive wholly into its cokernel:

\[
\dim\operatorname{coker}\partial_7^{(2)}
=2164-1200
=964.
\tag{6.14}
\]

Its measured type is

\[
\boxed{
46V_0\oplus96V_1\oplus75V_2\oplus30V_3\oplus5V_4.
}
\tag{6.15}
\]

If all fifteen local targets had the generic type (6.4), the corresponding
virtual result would instead be

\[
45V_0\oplus95V_1\oplus75V_2\oplus30V_3\oplus5V_4.
\tag{6.16}
\]

The difference between (6.15) and (6.16) is again exactly \(\mathbb H\).

This is the first explicit response residual which depends not only on the
number of selected blocks but on their ordered placement.

---

## 7. What is now conjectured

The finite evidence supports the following statement.

### Conjecture 7.1 — tetrahedral generation

For every \(n\ge5\), all first row syzygies of the pairwise terminal matching
map are generated on four-face supports:

\[
\boxed{
\ker\partial_n^{(2)}=\operatorname{im}\partial_n.
}
\tag{7.1}
\]

Equivalently,

\[
\boxed{
\operatorname{im}\partial_n^{(2)}
\cong
\operatorname{coker}\partial_n
=\mathfrak S_n.
}
\tag{7.2}
\]

The stronger uniformity conjecture that every \(Y_{n,Q}\) is merely a fixed
tetrahedral quotient tensored with spectators is already false by (6.5)–
(6.8). Any all-\(n\) theorem must remember ordered placement, not only
cardinality.

This separates two statements which should not be conflated:

1. **generation conjecture:** four-face supports generate all first
   syzygies;
2. **local classification problem:** determine the placement-dependent
   decorated quotient
   \((Y_{n,Q};E_{12},E_{13},E_{14},E_{23},E_{24},E_{34})\).

The \(n=7\) result strengthens the first while disproving the simplest answer
to the second.

---

## 8. Why this is the next structural rung

Before this note, the universal object

\[
\mathfrak S_n=\operatorname{coker}\partial_n
\tag{8.1}
\]

was known by exactness and character, but only as a global quotient of all
pairwise equations. The map \(\partial_n^{(2)}\) gives it a local candidate
presentation:

\[
\boxed{
\text{four terminal faces}
\longrightarrow
\text{six pair equations}
\longrightarrow
\text{one tetrahedral relation object}.
}
\tag{8.2}
\]

At \(n=5,6,7\), overlapping copies of (8.2) generate the whole first syzygy
module. Therefore the response-simplex program has advanced from

\[
\text{faces}+\text{pairwise matching}
\tag{8.3}
\]

to the beginning of an actual higher complex.

The important surprise is that ordered quaternion multiplication does not
produce an ordinary simplicial or Čech complex. Triangle descent fails, four-
face descent succeeds in the checked range, and the \(2\!-!1\!-!2\)
placement changes the local quotient at \(n=7\). The higher object is
therefore sensitive to the residual order which ordinary set-theoretic
incidence forgets.

---

## 9. What is not proved by this note

This note does **not** prove:

- exactness of (0.3) at \(C_n^1\) for arbitrary \(n\);
- a closed local quaternion formula for \(q_{n,Q}\);
- a general all-\(n\) classification of the decorated local quotients by
  spectator placement;
- a third differential out of \(C_n^2\);
- characteristic-zero versions of the full \(n=6,7\) quotient decompositions;
- that the exceptional \(2\!-!1\!-!2\) \(\mathbb H\) is curvature, gauge
  field, holonomy, or a physical force.

What has been isolated is more conservative and more useful: a precise
placement-sensitive algebraic residual which survives one additional descent
step.

**Subsequent status.** Notes 20–23 construct the full \(n=6\) spectator
atlas, the exact exceptional \(n=7\) core–residual coordinate, exterior
suspension, and exact rational coordinates for all six reduced \(n=7\)
words. Thus the finite characteristic-zero item above is now resolved.
All-\(n\) middle exactness, general internal-word transport, a third
differential, and any curvature interpretation remain open.

---

## 10. Certificate

Run from `research/depth-generated-geometry`:

```bash
python3 certificates/second_response_simplex_differential_certificate.py
python3 certificates/n7_tetrahedral_syzygy_modular_stress.py
python3 certificates/spectator_placement_residual_certificate.py
python3 certificates/n7_exceptional_square_operator_certificate.py
python3 certificates/n6_capped_five_edge_operator_certificate.py
```

The first certificate checks:

- the four failures of the naive pair-to-triple restriction at \(n=5\);
- surjectivity of every three-face local subsystem;
- the exact rational \(n=5\) quotient and middle exactness;
- the \(n=5\) Casimir type;
- both-prime \(n=6\) local dimensions, middle exactness, local types, and
  second cokernel.

The second certificate checks, independently over both prime fields:

- the \(4860\times5832\) first matching matrix and rank 3660;
- all fifteen four-support quotients;
- the unique \(Q=(1,3,4,6)\) anomaly;
- the \(2164\times4860\) second map and rank 1200;
- exactness at \(C_7^1\);
- the 964-dimensional second cokernel and its actual Casimir type.

The third certificate checks every labelled edge-image rank and Casimir
profile at \(n=6,7\), including the central-interval defects, equality of
the two exceptional outer images, and surjectivity of exactly the four cross
edges onto \(K_{212}\).

The fourth certificate proves the paired-collapse identities and square
cancellation exactly, then uses two modular minors to lift the
\(n=7\) cross-square exactness to \(\mathbb Q\).

The fifth certificate proves the left/right cap identities exactly, then
uses two modular minors to lift the \(n=6\) central-spectator five-edge
exactness to \(\mathbb Q\).

All five scripts use exact rational or finite-field arithmetic only. NumPy is a
storage and integer row-operation backend; floating-point arithmetic is not
used.

---

## 11. Next target — updated by Notes 14–25

Note 14 has now replaced the quotient-basis construction at \(n=5\) by the
direct quaternionic operator

\[
\boxed{
\omega_5:
\mathcal R_2^{\oplus6}
\longrightarrow
\mathbb H\otimes\mathbb H,
\qquad
\ker\omega_5=\operatorname{im}\partial_5.
}
\tag{11.1}
\]

with a closed formula built from five explicit quaternionic operations. It
also isolates a central four-dimensional image \(K_4\cong\mathbb H\) inside
\(\mathbb H\otimes\mathbb H\).

Note 15 shows that a placement-blind tensor transport cannot preserve the
six edge images. Notes 16–19 identify the square and cap residuals, fix the
canonical seed coordinate, and prove that the central \(n=6\) cap quaternion
is born from \(W_{12}\otimes V\), not from the direct extension
\(K_4\otimes V\). Note 20 then constructs the full two-chart \(n=6\) atlas
and its central transition \(\operatorname{id}_{\mathbb H}\otimes\theta\).

Notes 21–23 complete the next finite layer. The exceptional word \(212\)
has the exact core–residual coordinate \(T_7\oplus\mathbb H\); exterior
spectators tensorize the entire decorated quotient functorially; and the
five generic reduced words possess exact rational coordinates in the common
144-dimensional target. Hence the reduced dimension row

\[
144,144,144,148,144,144
\tag{11.2}
\]

and all fifteen \(n=7\) supports are now closed over \(\mathbb Q\).

Note 24 exhausts every transported direct-anchor history on this reduced
layer. Their same-word transition groupoid is generated by three pair-local
copies

\[
A=(\theta^{-1})_{R,a},
\qquad
B=(\theta^{-1})_{R,b},
\qquad
S=(-\theta)_{L,b},
\tag{11.3}
\]

and the exceptional full transition is
\(S\oplus I_{\mathbb H}\). Thus \(\kappa_{212}\) is fixed by the first
two-history comparison rather than produced as its defect.

Note 25 constructs all adjacent-word transports from stationary shared
outer edges. The unique independent loop in the reduced spacing graph has
exact identity core holonomy. Meanwhile \(\kappa_{212}\) vanishes on both
hinges incident to \(212\), so the complete layer is a flat
144-dimensional core together with a quaternionic defect supported at the
exceptional vertex.

The remaining program is therefore:

1. extend the internal-word construction to three spectators and prove a
   uniform word theorem;
2. compose its genuinely higher word-level paths and determine whether any
   nonconfluence factors through a placement residual;
3. prove all-\(n\) middle exactness and only then seek a third differential.

The immediate mathematical target is therefore not curvature. It is the
first three-internal-spectator word complex. Note 25 supplies the flat
two-spectator base case against which any later nontrivial holonomy must be
measured.
