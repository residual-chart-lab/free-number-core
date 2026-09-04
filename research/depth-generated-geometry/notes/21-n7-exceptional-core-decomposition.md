# Note 21 — The Exceptional \(n=7\) Core–Residual Decomposition

## a transported 144-dimensional spectator core and the cross-square quaternion exactly exhaust the \(2\!-!1\!-!2\) quotient

**Status:** theorem over \(\mathbb Q\), with exact integer identities,
two-prime reconstruction, and a certified CRT lift

**Depends on:** Notes 15, 16, and 20

**Claim boundary:** this note gives the first exact full-coordinate theorem
for the exceptional two-spectator quotient. It proves that its generic
144-dimensional part is the unique completion of a transported \(n=6\)
chart anchor and that the remaining four dimensions are exactly
\(\kappa_{212}\). It does not itself prove arbitrary interior-spectator
transport, all-\(n\) tetrahedral generation, or a curvature interpretation.

Note 22 subsequently proves functorial transport for spectators outside the
support interval. Note 23 places the result inside the complete reduced
\(n=7\) six-word atlas.

---

## 0. Result in one line

Let

\[
Q=(1,3,4,6)\subset G_7,
\qquad
G_7\setminus Q=\{2,5\}.
\tag{0.1}
\]

After applying the right decoder on each of the six edge-response blocks,
write

\[
E_Q
:=
\bigoplus_{e\in\binom Q2}
\left(\mathbb H\otimes V^{\otimes4}\right)_e,
\qquad
\dim E_Q=6\cdot324=1944,
\tag{0.2}
\]

and let

\[
\widehat\partial_{7,Q}:
\mathcal R_5^{\oplus4}\longrightarrow E_Q
\tag{0.3}
\]

be the decoded local matching map. Put

\[
T_7
:=
(\mathbb H\otimes\mathbb H)\otimes V_2\otimes V_5,
\qquad
\dim T_7=144.
\tag{0.4}
\]

There is a transported \(n=6\) anchor on the maximal cross edge \((1,6)\),
and it has a unique compatible completion

\[
\boxed{
C_{212}:E_Q\longrightarrow T_7,
\qquad
C_{212}\widehat\partial_{7,Q}=0.
}
\tag{0.5}
\]

Together with Note 16's intrinsic square residual

\[
\kappa_{212}:E_Q\longrightarrow\mathbb H,
\tag{0.6}
\]

it gives an exact sequence over \(\mathbb Q\):

\[
\boxed{
\mathcal R_5^{\oplus4}
\xrightarrow{\ \widehat\partial_{7,Q}\ }
E_Q
\xrightarrow{\ (C_{212},\kappa_{212})\ }
T_7\oplus\mathbb H
\longrightarrow0.
}
\tag{0.7}
\]

Hence

\[
\boxed{
Y_{7,(1,3,4,6)}
\cong
\left((\mathbb H\otimes\mathbb H)\otimes V^{\otimes2}\right)
\oplus\mathbb H.
}
\tag{0.8}
\]

The first factor is canonical relative to the transported right-chart
anchor specified below. The second factor is the intrinsic cross-square
coordinate of Note 16.

---

## 1. The transported anchor

Delete the new spectator \(2\). The remaining ordered gaps are

\[
(1,3,4,5,6),
\tag{1.1}
\]

which become \((1,2,3,4,5)\) after order-preserving compression. The old
spectator \(5\) is then in position \(s=4\), while \(Q\) becomes the
\(n=6\) support

\[
(1,2,3,5).
\tag{1.2}
\]

By Note 20, this placement has the unique right chart

\[
\Omega_4^R:
(\mathbb H\otimes V^{\otimes3})^{\oplus6}
\longrightarrow
(\mathbb H\otimes\mathbb H)\otimes V_5.
\tag{1.3}
\]

Use its local edge \(14\), which becomes the actual edge \((1,6)\), and
carry the new \(V_2\)-variable without changing the old chart block. In the
integral normalization of Note 20 this gives

\[
\boxed{
A_{16}^{R;2,5}
:=
\operatorname{carry}_2\!\left((4\Omega_4^R)_{14}\right)
:
\mathbb H\otimes V^{\otimes4}\longrightarrow T_7.
}
\tag{1.4}
\]

The target spectator order is fixed as \(V_2\otimes V_5\). The anchor is
onto:

\[
\operatorname{rank}A_{16}^{R;2,5}=144.
\tag{1.5}
\]

Equation (1.4) prescribes one edge block, not a naive tensor extension of
all six blocks. Placement-blind extension of the whole chart is not
compatible with the \(n=7\) matching relations. The remaining five blocks
must be solved from local compatibility.

---

## 2. Unique compatible completion

Let

\[
L_Q
:=
\left\{
\ell\in E_Q^*:\ell\widehat\partial_{7,Q}=0
\right\}
\tag{2.1}
\]

be the left annihilator of the matching image. The exact rank theorem below
gives

\[
\dim L_Q=148.
\tag{2.2}
\]

Restriction of a relation to the edge \((1,6)\) is injective:

\[
\boxed{
\operatorname{rank}
\left(
L_Q\longrightarrow
(\mathbb H\otimes V^{\otimes4})_{16}^*
\right)
=148.
}
\tag{2.3}
\]

Every row of the anchor (1.4) lies in the image of this restriction. It
therefore has a unique lift to \(L_Q\). Lifting all 144 rows defines
\(C_{212}\), characterized by

\[
\boxed{
C_{212}\widehat\partial_{7,Q}=0,
\qquad
(C_{212})_{16}=A_{16}^{R;2,5}.
}
\tag{2.4}
\]

The second equation and (1.5) show that \(C_{212}\) is onto. If two maps
satisfied (2.4), every row of their difference would lie in \(L_Q\) and
restrict to zero on \((1,6)\). Injectivity in (2.3) forces the difference
to vanish. Thus the completion is unique.

Because the matching map and the anchor are \(SO(3)\)-equivariant,
uniqueness also gives

\[
\boxed{C_{212}\text{ is }SO(3)\text{-equivariant}.}
\tag{2.5}
\]

The certificate additionally verifies (2.5) entry by entry over
\(\mathbb Z\).

---

## 3. Exact quotient theorem

In tensor coordinates, Note 16's square map is

\[
\kappa_{212}
=
(0,+\varepsilon_4,-\varepsilon_4,-\varepsilon_4,
+\varepsilon_4,0),
\tag{3.1}
\]

in the edge order

\[
(13,14,16,34,36,46).
\tag{3.2}
\]

The signs in (3.1) belong to the four cross edges

\[
(1,4),(1,6),(3,4),(3,6)
\tag{3.3}
\]

as \(+,-,-,+\). Equivalently,

\[
\kappa_{212}
(F_{14},F_{16},F_{34},F_{36})
=
\varepsilon_4(F_{14})
-\varepsilon_4(F_{16})
-\varepsilon_4(F_{34})
+\varepsilon_4(F_{36}).
\tag{3.4}
\]

Both components kill the local matching image:

\[
C_{212}\widehat\partial_{7,Q}=0,
\qquad
\kappa_{212}\widehat\partial_{7,Q}=0.
\tag{3.5}
\]

The exact ranks are

\[
\operatorname{rank}\widehat\partial_{7,Q}=1796,
\qquad
\operatorname{rank}C_{212}=144,
\qquad
\operatorname{rank}\kappa_{212}=4,
\tag{3.6}
\]

and

\[
\boxed{
\operatorname{rank}
\begin{bmatrix}C_{212}\\ \kappa_{212}\end{bmatrix}
=148.
}
\tag{3.7}
\]

Therefore

\[
\dim\ker(C_{212},\kappa_{212})=1944-148=1796.
\tag{3.8}
\]

The inclusion from (3.5), together with the equal dimensions, proves

\[
\boxed{
\ker(C_{212},\kappa_{212})
=
\operatorname{im}\widehat\partial_{7,Q}.
}
\tag{3.9}
\]

This proves (0.7) and (0.8).

---

## 4. The six edge images split without remainder

The six exact block ranks of the transported core are

\[
\boxed{
\begin{array}{c|rrrrrr}
\text{local edge}&12&13&14&23&24&34\\ \hline
\operatorname{rank}(C_{212})_e
&144&108&144&36&108&144.
\end{array}}
\tag{4.1}
\]

After adjoining the square coordinate, the ranks become

\[
\boxed{
\begin{array}{c|rrrrrr}
\text{local edge}&12&13&14&23&24&34\\ \hline
\operatorname{rank}(C_{212},\kappa_{212})_e
&144&112&148&40&112&144.
\end{array}}
\tag{4.2}
\]

Thus \(\kappa_{212}\) changes exactly the four cross edges, by exactly four
dimensions each, and changes neither outer edge.

Since both outer core blocks are onto \(T_7\) and \(\kappa_{212}\) vanishes
on them,

\[
\boxed{
E_{12}=E_{34}=T_7\oplus0.
}
\tag{4.3}
\]

Consequently

\[
\boxed{
Y_{7,Q}/E_{12}
\cong
Y_{7,Q}/E_{34}
\cong
\mathbb H,
}
\tag{4.4}
\]

and the quotient coordinate is precisely \(\kappa_{212}\). The exceptional
placement is therefore

\[
\boxed{
\text{generic six-edge core}
\;\oplus\;
\text{one shared cross-edge }\mathbb H,
}
\tag{4.5}
\]

with no unaccounted dimension.

---

## 5. Characteristic-zero spin type

The core target has the generic type

\[
T_7
\cong
6V_0\oplus13V_1\oplus11V_2\oplus5V_3\oplus V_4.
\tag{5.1}
\]

The residual quaternion has

\[
\mathbb H\cong V_0\oplus V_1.
\tag{5.2}
\]

Since (0.7) is \(SO(3)\)-equivariant,

\[
\boxed{
Y_{7,(1,3,4,6)}
\cong
7V_0\oplus14V_1\oplus11V_2\oplus5V_3\oplus V_4.
}
\tag{5.3}
\]

Thus the total Casimir type first observed over two prime fields is forced
by an explicit rational quotient map.

---

## 6. How the rational lift is certified

The decoded matching matrix is reconstructed independently over

\[
\mathbb F_{1009}
\qquad\text{and}\qquad
\mathbb F_{1013}.
\tag{6.1}
\]

In both fields, multiplying it by \(16\) and taking centered representatives
produces the same integer matrix

\[
M_{16}=16\widehat\partial_{7,Q},
\tag{6.2}
\]

with alphabet

\[
\{-2,-1,0,1,2\}.
\tag{6.3}
\]

Let \(J_4\) be the integral right encoder, \(B_r\) a face matrix, and
\(S_{rs}\) its actual common shadow. Every entry of

\[
J_4(M_{16})_{rs}B_r-16S_{rs}
\tag{6.4}
\]

is bounded in absolute value by

\[
324\cdot972\cdot2+16=629872.
\tag{6.5}
\]

The expression vanishes modulo both primes, while

\[
629872<1009\cdot1013=1022117.
\tag{6.6}
\]

It must therefore vanish over \(\mathbb Z\). Since every face map is onto,
\(M_{16}/16\) is the unique rational face-to-shadow matching map.

The two fields also reconstruct the same integral \(C_{212}\), with entry
alphabet

\[
\{-4,-3,-1,0,1,3,4,8,9\}.
\tag{6.7}
\]

Ordinary integer multiplication gives

\[
C_{212}M_{16}=0,
\qquad
\kappa_{212}M_{16}=0.
\tag{6.8}
\]

A rank-1796 modular minor supplies the rational lower bound for the matching
rank. The 148 independent rows in (3.7) supply the opposite upper bound.
This proves every rank in Section 3 over \(\mathbb Q\).

---

## 7. What this resolves

Before this note, three facts were known separately:

1. the generic two-spectator quotient has dimension \(144\);
2. the exceptional \(2\!-!1\!-!2\) support has dimension \(148\);
3. the four-dimensional quotient is detected by \(\kappa_{212}\).

The new gluing statement is

\[
\boxed{
\text{transported }n=6\text{ chart anchor}
\xrightarrow{\text{unique compatibility completion}}
144\text{-core},
}
\tag{7.1}
\]

followed by

\[
\boxed{
144\text{-core}+\kappa_{212}(\mathbb H)
=148\text{-dimensional full quotient}.
}
\tag{7.2}
\]

The exceptional placement is not a deformation of all 144 generic
directions. The generic core survives with its complete six-edge rank
profile, and one quaternionic channel is added transversely on the four
cross edges.

Note 23 subsequently proves that every other reduced two-spectator word has
exactly the 144-dimensional core and no extra quotient direction. Thus the
first unresolved layer begins with transition laws between those exact
coordinates and with three internal spectators.

---

## 8. What is still open

This note does **not** prove:

- that every \(Y_{n,Q}\) is a direct sum of a transported generic core and
  square/cap residuals;
- independence of the anchor construction from every admissible transport
  path;
- that \(\kappa_{212}\) is path nonconfluence or holonomy;
- all-\(n\) exactness of the tetrahedral second complex;
- a third differential or curvature theorem.

The all-length target remains

\[
\boxed{
Y_{n,Q}
=
\text{transported generic core}
\oplus
\text{placement residual complex},
}
\tag{8.1}
\]

first as a classification problem and then as the local generator theorem
needed for

\[
\ker\partial_n^{(2)}=\operatorname{im}\partial_n.
\tag{8.2}
\]

Equation (8.1) is a program suggested by the exact decomposition, not yet an
all-\(n\) theorem.

**Subsequent resolution at \(n=7\).** Notes 23 and 24 complete every reduced
word and every transported anchor history. Note 25 then proves that the two
spacing-word hinges incident to \(212\) are exactly the outer edges on
which \(\kappa_{212}\) vanishes. Hence the \(144\)-core transports flatly
through the reduced word graph, while the remaining \(\mathbb H\) is
supported at the exceptional vertex and is not core holonomy.

---

## 9. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/n7_exceptional_core_decomposition_certificate.py
~~~

The certificate verifies:

- reconstruction of the transported \(n=6\) long-cross anchor;
- independent construction of the \(n=7\) local matching map over
  \(\mathbb F_{1009}\) and \(\mathbb F_{1013}\);
- equality of the two centered lifts of
  \(16\widehat\partial_{7,Q}\);
- the CRT bound promoting the modular factorization to \(\mathbb Q\);
- unique completion to the same integral \(C_{212}\) in both fields;
- exact integer cancellation by \(C_{212}\) and \(\kappa_{212}\);
- exact \(SO(3)\)-equivariance of both output components;
- ranks \(1796,144,4,148\);
- the generic and exceptional six-edge rank profiles (4.1) and (4.2).

Expected final line:

~~~text
ALL CHECKS PASSED
~~~
