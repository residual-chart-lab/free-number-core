# Note 16 — Parity-Square Quaternionic Residual

## paired metric collapse explains why the first cross-edge quaternion appears at \(n=7\)

**Status:** all-odd-length construction and complex identity over
\(\mathbb Q\); exact cross-square cokernel theorem over \(\mathbb Q\) at
\(n=7\)

**Depends on:** Notes 12–15

**Claim boundary:** this note gives a closed quaternion-valued operator on a
parity-separated four-support and proves that it annihilates the cross-edge
matching map for every odd length. At \(n=7\), a modular rank minor upgrades
the construction to an exact sequence over \(\mathbb Q\). It does not prove
that the entire tetrahedral quotient is controlled by parity squares, or
identify the resulting quaternion with Note 14's \(K_4\) by a spectator
transport map.

---

## 0. Result in one line

For the first parity-separated support

\[
Q=(1,3\mid4,6),
\tag{0.1}
\]

the four cross-edge responses carry the closed operator

\[
\boxed{
\kappa_{212}
(F_{13},F_{14},F_{23},F_{24})
=
\varepsilon_4(F_{13})
-\varepsilon_4(F_{14})
-\varepsilon_4(F_{23})
+\varepsilon_4(F_{24}),
}
\tag{0.2}
\]

where

\[
\boxed{
\varepsilon_4(F)
=
\sum_{a,b=1}^{3}F(e_a,e_a,e_b,e_b).
}
\tag{0.3}
\]

It gives the exact rational sequence

\[
\boxed{
\mathcal R_5^{\oplus4}
\xrightarrow{\ \partial_\square\ }
\mathcal R_4^{\oplus4}
\xrightarrow{\ \kappa_{212}\ }
\mathbb H
\longrightarrow0,
\qquad
\ker\kappa_{212}=\operatorname{im}\partial_\square.
}
\tag{0.4}
\]

Thus the exceptional four-dimensional residual is an explicit alternating
quaternionic square response, not only a Casimir multiplicity.

---

## 1. The paired collapse

Write

\[
e_1=i,
\qquad e_2=j,
\qquad e_3=k.
\tag{1.1}
\]

For every \(v\in V=\operatorname{Im}\mathbb H\),

\[
\boxed{
\sum_{a=1}^{3}e_av e_a=v.
}
\tag{1.2}
\]

For \(r\ge1\), define the adjacent-pair metric collapse

\[
\boxed{
\varepsilon_{2r}:\mathcal R_{2r}\longrightarrow\mathbb H,
\qquad
\varepsilon_{2r}(F)
=
\sum_{a_1,\ldots,a_r=1}^{3}
F(e_{a_1},e_{a_1},\ldots,e_{a_r},e_{a_r}).
}
\tag{1.3}
\]

Each repeated sum contracts two adjacent probe variables with the Euclidean
metric on \(V\). Hence (1.3) is independent of the chosen oriented
orthonormal basis and is \(SO(3)\)-equivariant.

Also define

\[
\mu_m:
\mathbb H\otimes V^{\otimes m}\longrightarrow\mathbb H,
\qquad
\mu_m(h\otimes v_1\otimes\cdots\otimes v_m)
=hv_m\cdots v_1.
\tag{1.4}
\]

### Lemma 1.1 — paired decoder collapse

For every \(r\ge1\),

\[
\boxed{
\varepsilon_{2r}J_{2r}=\mu_{2r}.
}
\tag{1.5}
\]

### Proof

Substitute Note 12's right response encoder:

\[
J_{2r}(h,v_1,\ldots,v_{2r})(x_1,\ldots,x_{2r})
=h x_{2r}v_{2r}\cdots x_1v_1.
\tag{1.6}
\]

In (1.3), the last equal probe pair surrounds \(v_{2r}\). Equation
(1.2) removes that pair and leaves \(v_{2r}\). The next pair surrounds
\(v_{2r-2}\), and so on. Repeating from right to left removes all probe
pairs without changing the order of the \(v_j\), giving

\[
h v_{2r}v_{2r-1}\cdots v_2v_1.
\tag{1.7}
\]

This is (1.5). \(\square\)

For \(r=2\), (1.5) reads

\[
\varepsilon_4
J_4(h\otimes v_1\otimes v_2\otimes v_3\otimes v_4)
=h v_4v_3v_2v_1.
\tag{1.8}
\]

Thus the apparently tensorial definition (0.3) is exactly ordinary
quaternion multiplication after the intrinsic decoder.

---

## 2. Odd-before-even common shadows become indistinguishable

Let

\[
n=2r+3
\tag{2.1}
\]

and let

\[
D_{n;pq}:V^{\otimes n}\longrightarrow\mathcal R_{2r}
\tag{2.2}
\]

be the actual common-shadow response which probes every internal gap except
\(p<q\). Define the unprobed total product

\[
\Pi_n(a_1\otimes\cdots\otimes a_n)
:=a_n\cdots a_1.
\tag{2.3}
\]

### Lemma 2.1 — odd-even shadow collapse

If \(p\) is odd and \(q\) is even, then

\[
\boxed{
\varepsilon_{2r}D_{n;pq}=\Pi_n.
}
\tag{2.4}
\]

In particular, the left side is independent of which odd-before-even pair
\((p,q)\) was omitted.

### Proof

Write \(p=2a-1\) and \(q=2b\). After removing \(p\) and \(q\), the remaining
gap labels pair as

\[
\begin{aligned}
&(1,2),(3,4),\ldots,(p-2,p-1),\\
&(p+1,p+2),(p+3,p+4),\ldots,(q-2,q-1),\\
&(q+1,q+2),(q+3,q+4),\ldots,(2r+1,2r+2).
\end{aligned}
\tag{2.5}
\]

Empty ranges are allowed. Every listed pair consists of consecutive gaps.
When the two corresponding probes are assigned the same \(e_a\), they
surround exactly one state factor. Summing that pair applies (1.2) and
removes both probes without changing the factor. Repeating through all
pairs leaves exactly

\[
a_n\cdots a_1=\Pi_n(a_1,\ldots,a_n).
\tag{2.6}
\]

\(\square\)

This statement concerns the actual two-gap shadow \(D_{n;pq}\), not a
uniform coordinate model for all face restrictions.

For the intrinsic restrictions of Note 12,

\[
\rho_p^{pq}B_{n,p}=D_{n;pq}
=\rho_q^{pq}B_{n,q}.
\tag{2.7}
\]

Every \(B_{n,p}\) is onto. Hence Lemma 2.1 implies, whenever all displayed
odd gaps lie before all displayed even gaps,

\[
\begin{aligned}
\varepsilon_{2r}\rho_p^{pq}
&=\varepsilon_{2r}\rho_p^{pq'}
&&\text{for fixed odd }p,\\
\varepsilon_{2r}\rho_q^{pq}
&=\varepsilon_{2r}\rho_q^{p'q}
&&\text{for fixed even }q.
\end{aligned}
\tag{2.8}
\]

These are equalities of intrinsic response-side maps.

---

## 3. The all-odd-length parity square

Let

\[
n=2r+3
\tag{3.1}
\]

be odd, so a terminal face has response depth \(2r+1\) and a pairwise
shadow has depth \(2r\). Choose an ordered four-support

\[
Q=\{q_1<q_2<q_3<q_4\}\subset G_n
\tag{3.2}
\]

with parity pattern

\[
\boxed{
q_1,q_2\text{ odd},
\qquad
q_3,q_4\text{ even}.
}
\tag{3.3}
\]

Partition the vertices as

\[
\{q_1,q_2\}\mid\{q_3,q_4\}
\tag{3.4}
\]

and retain the four cross edges \(13,14,23,24\). Let

\[
\partial_{n,Q}^{\square}:
\mathcal R_{2r+1}^{\oplus4}
\longrightarrow
\mathcal R_{2r}^{\oplus4}
\tag{3.5}
\]

be the projection of the local tetrahedral matching map onto those four
edge blocks.

Define

\[
\boxed{
\kappa_{n,Q}
(F_{13},F_{14},F_{23},F_{24})
=
\varepsilon_{2r}(F_{13})
-\varepsilon_{2r}(F_{14})
-\varepsilon_{2r}(F_{23})
+\varepsilon_{2r}(F_{24}).
}
\tag{3.6}
\]

### Theorem 3.1 — parity-square complex

For every odd \(n\ge7\) and every support satisfying (3.3),

\[
\boxed{
\kappa_{n,Q}\partial_{n,Q}^{\square}=0.
}
\tag{3.7}
\]

The map \(\kappa_{n,Q}\) is \(SO(3)\)-equivariant and onto. Consequently it
induces a canonical surjection

\[
\boxed{
\operatorname{coker}\partial_{n,Q}^{\square}
\twoheadrightarrow\mathbb H.
}
\tag{3.8}
\]

### Proof

Write \(F_a\in\mathcal R_{2r+1}\) for the face response at \(q_a\).
By (0.2) of Note 12, expansion of the left side of (3.7) groups its
terms by face:

\[
\begin{aligned}
\kappa_{n,Q}\partial_{n,Q}^{\square}(F_1,F_2,F_3,F_4)
={}&
\varepsilon_{2r}
\left(\rho_{q_1}^{q_1q_3}-\rho_{q_1}^{q_1q_4}\right)F_1\\
&+
\varepsilon_{2r}
\left(-\rho_{q_2}^{q_2q_3}+\rho_{q_2}^{q_2q_4}\right)F_2\\
&+
\varepsilon_{2r}
\left(-\rho_{q_3}^{q_1q_3}+\rho_{q_3}^{q_2q_3}\right)F_3\\
&+
\varepsilon_{2r}
\left(\rho_{q_4}^{q_1q_4}-\rho_{q_4}^{q_2q_4}\right)F_4.
\end{aligned}
\tag{3.9}
\]

The first two lines vanish by the fixed-odd equalities in (2.8), and the
last two vanish by the fixed-even equalities. This proves (3.7) using only
the intrinsic common-shadow maps.

Equivariance follows from the metric contractions in (1.3). Surjectivity
follows already from any one edge block: by (1.5),
\(\varepsilon_{2r}J_{2r}=\mu_{2r}\), and \(\mu_{2r}\) is onto
\(\mathbb H\). \(\square\)

---

## 4. Why the first case is \(n=7\)

At \(n=5\), the ordered gap set is

\[
G_5=\{1,2,3,4\}.
\tag{4.1}
\]

There is no increasing four-support whose first two entries are odd and
last two are even: the only two odd labels are \(1,3\), while the even label
\(2\) lies between them.

One can repartition \(G_5\) abstractly as
\(\{1,3\}\mid\{2,4\}\), but its two parts interleave in the ambient order.
The odd-before-even hypothesis of Lemma 2.1 then fails, and the naive
\(+,-,-,+\) collapse does not annihilate the \(n=5\) matching map. Thus the
central \(K_4\) of Note 14 is not a disguised instance of Theorem 3.1; an
order-sensitive transport is genuinely still required.

At \(n=7\),

\[
G_7=\{1,2,3,4,5,6\},
\tag{4.2}
\]

and the first possible parity-separated support is uniquely

\[
\boxed{
(q_1,q_2\mid q_3,q_4)=(1,3\mid4,6).
}
\tag{4.3}
\]

Its spacing vector is

\[
(2,1,2).
\tag{4.4}
\]

Thus the position of the first residual is forced simultaneously by order
and parity. The exceptional support found computationally in Note 13 is
exactly the first support on which Theorem 3.1 can exist.

---

## 5. Exactness of the first square over \(\mathbb Q\)

For (4.3), the four actual cross edges are

\[
(1,4),\quad(1,6),\quad(3,4),\quad(3,6).
\tag{5.1}
\]

The two within-part edges are the distinguished pairs

\[
(1,3),\qquad(4,6).
\tag{5.2}
\]

The cross matching map has dimensions

\[
\partial_\square:
\mathcal R_5^{\oplus4}
\longrightarrow
\mathcal R_4^{\oplus4},
\qquad
3888\longrightarrow1296.
\tag{5.3}
\]

Theorem 3.1 gives

\[
\operatorname{rank}_{\mathbb Q}\partial_\square
\le1296-4=1292.
\tag{5.4}
\]

In right coefficient coordinates the matrix of (5.3) has integer entries.
Exact elimination gives

\[
\operatorname{rank}_{\mathbb F_{1009}}\partial_\square
=
\operatorname{rank}_{\mathbb F_{1013}}\partial_\square
=1292.
\tag{5.5}
\]

Either modular rank exhibits a nonzero 1292-minor over \(\mathbb Z\), hence

\[
\operatorname{rank}_{\mathbb Q}\partial_\square\ge1292.
\tag{5.6}
\]

Combining (5.4) and (5.6) proves

\[
\boxed{
\operatorname{rank}_{\mathbb Q}\partial_\square=1292,
\qquad
\ker\kappa_{212}=\operatorname{im}\partial_\square.
}
\tag{5.7}
\]

This proves the exact sequence (0.4) over \(\mathbb Q\).

---

## 6. Relation to the full tetrahedral quotient

Let the six-edge target of the exceptional local matching map split as

\[
C^1_{7,Q}
=
O\oplus X,
\tag{6.1}
\]

where

\[
O=\mathcal R_4^{(12)}\oplus\mathcal R_4^{(34)}
\tag{6.2}
\]

contains the two within-part edges and

\[
X=\mathcal R_4^{(13)}\oplus\mathcal R_4^{(14)}
\oplus\mathcal R_4^{(23)}\oplus\mathcal R_4^{(24)}
\tag{6.3}
\]

contains the cross square. Quotient associativity gives

\[
\boxed{
Y_{7,Q}/(E_{12}+E_{34})
\cong
X/\operatorname{im}\partial_\square
\cong\mathbb H.
}
\tag{6.4}
\]

Thus the canonical cross-edge quotient detected over two prime fields in
Note 15 now has a direct characteristic-zero realization. Note 15 also
finds

\[
E_{12}=E_{34}
\tag{6.5}
\]

over both tested fields; equality (6.5) itself has not yet been separately
lifted to a rational closed identity. Equation (6.4) needs only their sum
and is already exact over \(\mathbb Q\).

---

## 7. What the operator measures

Formula (0.2) is the mixed alternating difference on the complete bipartite
cross graph \(K_{2,2}\), but with the scalar evaluation replaced by the
quaternionic collapse (0.3):

\[
\begin{array}{c|cc}
&q_3&q_4\\ \hline
q_1&+&-\\
q_2&-&+.
\end{array}
\tag{7.1}
\]

The two within-part edges (5.2) are discarded, and the operator compares
the four ways of connecting their endpoints. This is the exact algebraic
content of the residual.

It is tempting to call (7.1) a discrete curvature or holonomy. That is still
premature: no path transport, gauge covariance law, or flatness theorem has
been supplied. The proved statement is both narrower and harder: a
quaternion-valued alternating square functional is forced by the ordered
response calculus, first becomes combinatorially possible at \(n=7\), and
is the complete rational cokernel of that first cross square.

---

## 8. Certificate

Run from `research/depth-generated-geometry`:

```bash
python3 certificates/n7_exceptional_square_operator_certificate.py
```

The script verifies:

- \(\varepsilon_4J_4=\mu_4\) exactly over \(\mathbb Q\);
- equality, over \(\mathbb Z\), of all four actual odd-before-even
  common-shadow collapses appearing in the exceptional square;
- factorization of the actual face-to-shadow maps and
  \(\kappa_{212}\partial_\square=0\) independently over both prime fields;
- \(SO(3)\)-equivariance and surjectivity of \(\varepsilon_4\);
- rank \(1292\) of \(\partial_\square\) independently over
  \(\mathbb F_{1009}\) and \(\mathbb F_{1013}\).

Expected final line:

```text
ALL CHECKS PASSED
```

---

## 9. Next target

Note 17 subsequently resolves the \(n=6\) item which was open when this
square was first isolated: an odd-depth left/right cap calculus gives an
exact quaternionic decoder for the central-spectator defect. The remaining
questions are now:

1. determine the full cokernel of every parity square in Theorem 3.1 and
   decide when the canonical surjection (3.8) is an isomorphism;
2. unify this even-depth paired collapse with Note 17's odd-depth left/right
   caps;
3. determine the correction required for genuinely interleaved placements,
   where neither parity theorem directly applies;
4. identify whether Note 14's \(K_4\) transports to the exact quotient
   (6.4) and to Note 17's exact \(n=6\) quotient. Note 18 removes the
   target-coordinate ambiguity by fixing \(K_4=\iota(\mathbb H)\) and
   \(\nu=\frac14\iota^*\);
5. assemble overlapping cap and square residuals into the next differential only
   after their incidence relations are known.

The central reversal has become concrete: the parity and order of omitted
probes do not merely label a pre-existing local space. They determine
whether a quaternion-valued two-directional residual can be formed at all.
