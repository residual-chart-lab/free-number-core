# Note 15 — Spectator Placement Residuals

## the local quotient remembers where the omitted probes were folded

**Status:** exact finite-field classification at \(n=6,7\) over
\(\mathbb F_{1009}\) and \(\mathbb F_{1013}\)

**Depends on:** Notes 13 and 14

**Claim boundary:** this note refines each tetrahedral local quotient by its
six labelled edge images. It proves, over two prime fields, a complete
placement classification at \(n=6,7\) and isolates the exceptional
\(2\!-!1\!-!2\) residual as a canonical four-dimensional quotient. It does
not construct a general spectator transport, identify the displayed
quaternionic quotients with Note 14's \(K_4\), or interpret them as
curvature. Notes 16 and 17 subsequently give characteristic-zero decoders
for the exceptional \(n=7\) quotient and the central \(n=6\) quotient;
Note 18 gives the seed \(K_4\) its canonical quaternion coordinate.

---

## 0. Result in one line

The abstract \(SO(3)\)-module \(Y_{n,Q}\) is not the whole local object. The
six images of its edge-response summands retain placement data which the
total dimension and character can hide.

At \(n=6\), all five quotients have dimension \(48\) and the same spin type,
but the central-spectator support loses exactly one
\(\mathbb H\cong V_0\oplus V_1\) from its long-edge image.

At \(n=7\), a spectator in the central interval produces a hidden
\(\mathbb H\otimes V\) long-edge defect, whereas the unique spacing
\((2,1,2)\) produces a new quotient

\[
\boxed{
K_{212}\cong\mathbb H
}
\tag{0.1}
\]

seen by exactly the four cross edges of the ordered tetrahedron.

---

## 1. The decorated local quotient

Let

\[
Q=\{q_1<q_2<q_3<q_4\}\subset G_n
\tag{1.1}
\]

and let

\[
q_{n,Q}:
\bigoplus_{1\le a<b\le4}\mathcal R_{n-3}
\longrightarrow Y_{n,Q}
\tag{1.2}
\]

be the canonical quotient map of Note 13.  For each labelled local edge put

\[
\boxed{
E_{ab}^{(n,Q)}
:=
\operatorname{im}
\left(q_{n,Q}|_{\mathcal R_{n-3}^{(ab)}}\right)
\subseteq Y_{n,Q}.
}
\tag{1.3}
\]

The refined local object is therefore

\[
\boxed{
\mathscr Y_{n,Q}
:=
\left(Y_{n,Q};E_{12},E_{13},E_{14},E_{23},E_{24},E_{34}\right).
}
\tag{1.4}
\]

Every \(E_{ab}\) is \(SO(3)\)-stable. If \(P_j\) denotes the exact Casimir
projector onto spin \(j\), define the edge fingerprint

\[
\sigma(E):=
\left(\dim P_0E,\dim P_1E,\ldots\right).
\tag{1.5}
\]

Unlike a quotient basis, the dimensions in (1.5) are invariant under every
equivariant change of coordinates.  They allow two isomorphic total
quotients to be distinguished by the incidence of their labelled edge
images.

---

## 2. The \(n=5\) seed

Note 14 gives

\[
Y_{5,G_5}\cong\mathbb H\otimes\mathbb H
\tag{2.1}
\]

and the six edge-image dimensions

\[
\left(16,12,16,4,12,16\right).
\tag{2.2}
\]

Their Casimir fingerprints are

\[
\begin{array}{c|c}
ab&\sigma(E_{ab})\\ \hline
12,14,34&(2,9,5)\\
13,24&(1,6,5)\\
23&(1,3,0).
\end{array}
\tag{2.3}
\]

This is the placement-blind tensor seed against which the next two lengths
can be compared.

---

## 3. One spectator: a hidden quaternion at \(n=6\)

For every \(Q\in\binom{G_6}{4}\),

\[
\dim Y_{6,Q}=48,
\qquad
\sigma(Y_{6,Q})=(3,18,20,7).
\tag{3.1}
\]

Thus the total module always has the type expected from
\((\mathbb H\otimes\mathbb H)\otimes V\).

For four of the five supports, the edge fingerprints are

\[
\begin{array}{c|c|c}
ab&\dim E_{ab}&\sigma(E_{ab})\\ \hline
12,14,34&48&(3,18,20,7)\\
13,24&36&(2,12,15,7)\\
23&12&(1,6,5,0).
\end{array}
\tag{3.2}
\]

There is exactly one exception:

\[
Q=(1,2,4,5),
\qquad
G_6\setminus Q=\{3\}.
\tag{3.3}
\]

The spectator lies in the central interval \((q_2,q_3)=(2,4)\). Only the
long local edge \(14\), namely the actual edge \((1,5)\), changes:

\[
\dim E_{14}=44,
\qquad
\sigma(E_{14})=(2,15,20,7).
\tag{3.4}
\]

Subtracting (3.4) from the full profile in (3.1) gives

\[
(3,18,20,7)-(2,15,20,7)
=(1,3,0,0).
\tag{3.5}
\]

Hence the invariant defect quotient has type

\[
\boxed{
Y_{6,(1,2,4,5)}/E_{14}
\cong V_0\oplus V_1
\cong\mathbb H.
}
\tag{3.6}
\]

The total quotient in (3.1) does not reveal this defect.  It becomes visible
only after retaining the labelled edge images.

Note 17 subsequently realizes (3.6) directly over \(\mathbb Q\). It
constructs the five-edge operator

\[
\chi_6=(-\lambda_3^L,+\lambda_3^L,0,-\lambda_3^R,+\lambda_3^R)
\tag{3.7}
\]

after discarding the long edge \(14\), and proves

\[
\ker\chi_6=\operatorname{im}\partial_{\cap,6}.
\tag{3.8}
\]

Thus the characteristic-zero quotient in (3.6) is a theorem; the complete
edge-image profile (3.4) remains, at this stage, a two-prime exact check.

---

## 4. Two spectators: the complete \(n=7\) placement table

Fourteen supports have

\[
\dim Y_{7,Q}=144,
\qquad
\sigma(Y_{7,Q})=(6,39,55,35,9),
\tag{4.1}
\]

while

\[
Q_{212}:=(1,3,4,6)
\tag{4.2}
\]

has

\[
\dim Y_{7,Q_{212}}=148,
\qquad
\sigma(Y_{7,Q_{212}})=(7,42,55,35,9).
\tag{4.3}
\]

The difference between (4.3) and (4.1) is again

\[
(1,3,0,0)=V_0\oplus V_1\cong\mathbb H.
\tag{4.4}
\]

The edge data gives a complete finer classification.

### 4.1 Standard profile

For the nine ordinary supports, the six profiles are

\[
\begin{array}{c|c|c}
ab&\dim E_{ab}&\sigma(E_{ab})\\ \hline
12,14,34&144&(6,39,55,35,9)\\
13,24&108&(4,27,40,28,9)\\
23&36&(2,12,15,7,0).
\end{array}
\tag{4.5}
\]

### 4.2 A spectator in the central interval

Exactly five supports satisfy

\[
q_3-q_2>1.
\tag{4.6}
\]

They are

\[
\begin{aligned}
&(1,2,4,5),\quad(1,2,4,6),\quad(1,2,5,6),\\
&(1,3,5,6),\quad(2,3,5,6).
\end{aligned}
\tag{4.7}
\]

Their total quotient still has the generic profile (4.1), and five edge
profiles remain standard. The long edge \(14\) alone drops to

\[
\dim E_{14}=132,
\qquad
\sigma(E_{14})=(5,33,50,35,9).
\tag{4.8}
\]

The missing profile is

\[
(6,39,55,35,9)-(5,33,50,35,9)
=(1,6,5,0,0),
\tag{4.9}
\]

which is exactly

\[
\boxed{
V_0\oplus2V_1\oplus V_2
\cong\mathbb H\otimes V.
}
\tag{4.10}
\]

The same defect occurs whether one or both spectators lie in the central
interval.

### 4.3 The exceptional \(2\!-!1\!-!2\) support

The unique remaining nonstandard spacing has one spectator in each outer
interval:

\[
(q_2-q_1,q_3-q_2,q_4-q_3)=(2,1,2).
\tag{4.11}
\]

Its full edge table is

\[
\begin{array}{c|c|c|c}
ab&\dim E_{ab}&\sigma(E_{ab})&
\text{change from (4.5)}\\ \hline
12&144&(6,39,55,35,9)&0\\
13&112&(5,30,40,28,9)&+\mathbb H\\
14&148&(7,42,55,35,9)&+\mathbb H\\
23&40 &(3,15,15,7,0)&+\mathbb H\\
24&112&(5,30,40,28,9)&+\mathbb H\\
34&144&(6,39,55,35,9)&0.
\end{array}
\tag{4.12}
\]

Thus the extra quaternion is visible on precisely

\[
13,14,23,24,
\tag{4.13}
\]

the four edges crossing the ordered bipartition

\[
\{q_1,q_2\}\mid\{q_3,q_4\}.
\tag{4.14}
\]

It is absent from the two within-part edges \(12\) and \(34\).

---

## 5. A canonical cross-edge residual

Inside the exceptional quotient, exact row reduction gives

\[
\boxed{
E_{12}=E_{34}=:W_{\mathrm{out}},
\qquad
\dim W_{\mathrm{out}}=144.
}
\tag{5.1}
\]

This equality is tested internally: the two 144-dimensional images have
join rank \(144\), not \(148\). Define

\[
\boxed{
K_{212}
:=
Y_{7,Q_{212}}/W_{\mathrm{out}}.
}
\tag{5.2}
\]

Then

\[
\dim K_{212}=4,
\qquad
\sigma(K_{212})=(1,3,0,0),
\qquad
K_{212}\cong\mathbb H.
\tag{5.3}
\]

No complement of \(W_{\mathrm{out}}\) is chosen in (5.2). The residual is
therefore canonical relative to the ordered quotient and its labelled edge
maps.

Note 16 subsequently constructs this residual directly over \(\mathbb Q\).
Without using the finite-field equality \(E_{12}=E_{34}\), it proves

\[
Y_{7,Q_{212}}/(E_{12}+E_{34})
\cong\mathbb H
\tag{5.3a}
\]

by an explicit quaternionic square operator. Thus the characteristic-zero
quotient by the two outer images is a theorem; their stronger equality in
(5.1) remains, at this stage, a two-prime exact check.

Moreover,

\[
W_{\mathrm{out}}+E_{ab}=Y_{7,Q_{212}}
\qquad
\text{for }ab\in\{13,14,23,24\},
\tag{5.4}
\]

whereas

\[
E_{12},E_{34}\subseteq W_{\mathrm{out}}.
\tag{5.5}
\]

Equivalently, all four cross edges surject onto \(K_{212}\), and both outer
edges vanish in it. The exceptional summand is therefore a single shared
cross-edge channel, not four unrelated dimension increments.

---

## 6. What is rigorously remembered

At \(n=6\), all five \(Y_{6,Q}\) are isomorphic as \(SO(3)\)-modules, but
their decorated objects (1.4) are not all isomorphic with the edge labels
preserved: one has a 44-dimensional \(E_{14}\), while the other four have a
48-dimensional \(E_{14}\).

Thus

\[
\boxed{
\text{total quotient type}
\quad\text{forgets data retained by}\quad
\text{labelled edge-image incidence}.
}
\tag{6.1}
\]

This is a precise algebraic sense in which the local object remembers where
the spectator was inserted, or where the ordered response was folded.  No
ontological or physical meaning is required for (6.1): it is already a
strict invariant statement about the response presentation.

It also rules out any placement-blind transport which carries all six seed
edge images by the same tensor prescription.  A valid transport law must
include an order-sensitive slide or correction term.

---

## 7. Relation to the minimal quaternionic channel

Three quaternionic fingerprints are now exposed:

\[
\begin{array}{c|c}
\text{location}&\text{four-dimensional object}\\ \hline
n=5&K_4=\operatorname{im}\Lambda_{23}\subset Y_5\\
n=6&Y_{6,(1,2,4,5)}/E_{14}\\
n=7&K_{212}=Y_{7,(1,3,4,6)}/W_{\mathrm{out}}.
\end{array}
\tag{7.1}
\]

All three have the exact spin profile

\[
(1,3)=V_0\oplus V_1\cong\mathbb H.
\tag{7.2}
\]

This is stronger than a bare dimension match but weaker than a
chain-level identification. Note 16 supplies a closed
characteristic-zero decoder for the third object, Note 17 supplies one for
the second, and Note 18 identifies the first as
\(K_4=\iota(\mathbb H)\) with normalized coordinate
\(\nu=\frac14\iota^*\). A placement-aware transport comparing all three
fixed decoders has not yet been constructed in general. Note 19 resolves
the central \(n=6\) case: the full normalized quotient factors to the cap
decoder, but the surviving quaternion comes from
\(W_{12}\otimes V\), not from the direct extension
\(K_4\otimes V\).

---

## 8. Certificate

Run from `research/depth-generated-geometry`:

```bash
python3 certificates/spectator_placement_residual_certificate.py
```

The script uses exact finite-field arithmetic and checks both
\(\mathbb F_{1009}\) and \(\mathbb F_{1013}\). It verifies:

- every local quotient and every labelled edge-image Casimir profile at
  \(n=6,7\);
- the unique \(n=6\) central-spectator \(\mathbb H\) defect;
- the five \(n=7\) central-interval \(\mathbb H\otimes V\) defects;
- the unique \(2\!-!1\!-!2\) extra \(\mathbb H\);
- equality of the two outer edge images in (5.1);
- surjectivity of exactly the four cross edges in (5.4).

Expected final line:

```text
ALL CHECKS PASSED
```

---

## 9. What remains open

The next step is no longer to ask whether placement matters.  It does.  The
open tasks are:

1. construct a closed placement-aware transport of Note 14's five primitive
   quaternionic operators and compare it with Note 16's paired collapse and
   Note 17's left/right cap collapses in Note 18's normalized seed
   coordinate;
2. prove over \(\mathbb Q\), and then uniformly in \(n\), the edge-image
   fingerprints detected here;
3. extend Note 19's \(n=6\) channel-transfer theorem to the \(n=7\)
   quotient \(K_{212}\);
4. classify the decorated quotients \(\mathscr Y_{n,Q}\) by general spectator
   words;
5. only after such transport exists, test path nonconfluence and curvature
   interpretations.

The safe conclusion is exact and already nontrivial: the response quotient
retains order-placement memory in its internal incidence structure, and the
first surviving two-spectator residual is a canonical quaternionic
cross-edge quotient.
