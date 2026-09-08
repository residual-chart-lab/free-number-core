# Note 17 — Even-Length Capped Five-Edge Residual

## the central-spectator quaternion is the first odd-even-even-odd cap

**Status:** all-even-length complex and collapse identities over
\(\mathbb Q\); exact five-edge cokernel theorem over \(\mathbb Q\) at
\(n=6\)

**Depends on:** Notes 12–16

**Claim boundary:** this note gives a closed quaternion-valued operator on
every ordered four-support with parity pattern odd-even-even-odd. It proves
that the operator annihilates the five-edge matching map obtained by
discarding the outer odd-odd edge. At \(n=6\), a modular rank minor upgrades
the construction to an exact sequence over \(\mathbb Q\) and realizes the
central-spectator defect of Note 15 directly. It does not identify this
quaternion with Note 14's \(K_4\), nor prove five-edge exactness at every
even length.

---

## 0. Result in one line

For the first support of parity type

\[
\boxed{
Q=(1,2,4,5)
\quad\text{with pattern}\quad
\mathrm O\,\mathrm E\,\mathrm E\,\mathrm O,
}
\tag{0.1}
\]

discard the long local edge \(14=(1,5)\). On
\(\mathcal R_3\), define

\[
\boxed{
\begin{aligned}
\lambda_3^L(F)
&=
\sum_{a,b=1}^{3}e_bF(e_a,e_a,e_b),\\
\lambda_3^R(F)
&=
\sum_{a,b=1}^{3}F(e_b,e_a,e_a)e_b.
\end{aligned}
}
\tag{0.2}
\]

Then the remaining five edge responses carry the closed operator

\[
\boxed{
\begin{aligned}
\chi_6(
F_{12},F_{13},F_{23},F_{24},F_{34})
={}&
-\lambda_3^L(F_{12})
+\lambda_3^L(F_{13})\\
&-\lambda_3^R(F_{24})
+\lambda_3^R(F_{34}).
\end{aligned}
}
\tag{0.3}
\]

The central even-even edge \(23=(2,4)\) has coefficient zero. There is an
exact rational sequence

\[
\boxed{
\mathcal R_4^{\oplus4}
\xrightarrow{\ \partial_{\cap,6}\ }
\mathcal R_3^{\oplus5}
\xrightarrow{\ \chi_6\ }
\mathbb H
\longrightarrow0,
\qquad
\ker\chi_6=\operatorname{im}\partial_{\cap,6}.
}
\tag{0.4}
\]

Consequently,

\[
\boxed{
Y_{6,(1,2,4,5)}/E_{14}
\cong\mathbb H
\quad\text{over }\mathbb Q.
}
\tag{0.5}
\]

This upgrades the two-prime placement fingerprint of Note 15 to a direct
characteristic-zero quaternionic quotient.

---

## 1. Two odd-depth cap collapses

Let

\[
n=2r+4,
\qquad r\ge1,
\tag{1.1}
\]

so every pairwise common shadow has odd response depth \(2r+1\). Define

\[
\boxed{
\begin{aligned}
\lambda_{2r+1}^{L}(F)
&=
\sum_{\substack{a_1,\ldots,a_r\\b}}
e_b
F(
e_{a_1},e_{a_1},
\ldots,
e_{a_r},e_{a_r},
e_b),\\
\lambda_{2r+1}^{R}(F)
&=
\sum_{\substack{a_1,\ldots,a_r\\b}}
F(
e_b,
e_{a_1},e_{a_1},
\ldots,
e_{a_r},e_{a_r})
e_b.
\end{aligned}
}
\tag{1.2}
\]

Repeated indices in (1.2) run from \(1\) to \(3\). All paired arguments are
contracted with the Euclidean metric, and the remaining argument is capped
by the same quaternionic basis vector outside the response. Thus both maps
are independent of the chosen oriented orthonormal basis and are
\(SO(3)\)-equivariant.

Let \(J_{2r+1}\) be the right response encoder of Note 12 and put

\[
\theta(h)
:=
\sum_{b=1}^{3}e_bhe_b
=-(h+2\bar h).
\tag{1.3}
\]

The scalar and imaginary eigenspaces of \(\theta\) have eigenvalues
\(-3\) and \(1\), respectively, so \(\theta\) is invertible.

### Lemma 1.1 — cap decoder formulas

\[
\boxed{
\begin{aligned}
\lambda_{2r+1}^{L}
J_{2r+1}(h\otimes v_1\otimes\cdots\otimes v_{2r+1})
&=
\theta(h)v_{2r+1}\cdots v_1,\\
\lambda_{2r+1}^{R}
J_{2r+1}(h\otimes v_1\otimes\cdots\otimes v_{2r+1})
&=
hv_{2r+1}\cdots v_1.
\end{aligned}
}
\tag{1.4}
\]

### Proof

For the left formula, each equal adjacent probe pair is removed by

\[
\sum_{a=1}^{3}e_ave_a=v
\qquad(v\in V).
\tag{1.5}
\]

The final probe \(e_b\) occurs immediately to the right of the coefficient
\(h\), while the external cap occurs to its left. Their sum replaces \(h\)
by \(\sum_be_bhe_b=\theta(h)\). This gives the first line of (1.4).

For the right formula, the first probe \(e_b\) occurs immediately to the
left of \(v_1\), and the external cap occurs on the far right. Equation
(1.5) replaces \(e_bv_1e_b\) by \(v_1\); the adjacent probe pairs remove
the remaining insertions. The full reverse product remains.
\(\square\)

Both maps in (1.2) are therefore onto \(\mathbb H\).

---

## 2. The two cap-shadow laws

Let

\[
D_{n;pq}:V^{\otimes n}\longrightarrow\mathcal R_{2r+1}
\tag{2.1}
\]

be the actual common-shadow response which probes every internal gap except
\(p<q\), and retain Note 16's total product

\[
\Pi_n(a_1\otimes\cdots\otimes a_n)=a_n\cdots a_1.
\tag{2.2}
\]

### Lemma 2.1 — left cap

If \(p\) is odd and \(q\) is even, then

\[
\boxed{
\lambda_{2r+1}^{L}D_{n;pq}=\Pi_n.
}
\tag{2.3}
\]

### Lemma 2.2 — right cap

If \(p\) is even and \(q\) is odd, then

\[
\boxed{
\lambda_{2r+1}^{R}D_{n;pq}=\Pi_n.
}
\tag{2.4}
\]

### Proof

For (2.3), leave the last gap \(n-1\) as the left-capped probe. After
removing the odd-even pair \(p,q\), all other gap labels through \(n-2\)
split into consecutive pairs:

\[
\begin{aligned}
&(1,2),\ldots,(p-2,p-1),\\
&(p+1,p+2),\ldots,(q-2,q-1),\\
&(q+1,q+2),\ldots,(n-3,n-2).
\end{aligned}
\tag{2.5}
\]

Empty ranges are allowed. The adjacent pairs collapse by (1.5). The
external left cap and the probe in gap \(n-1\) surround the endpoint state
factor \(a_n\), so their sum also collapses by (1.5). What remains is
\(\Pi_n\).

For (2.4), leave gap \(1\) as the right-capped probe. After removing the
even-odd pair \(p,q\), the remaining labels from \(2\) through \(n-1\)
again split into consecutive pairs:

\[
\begin{aligned}
&(2,3),\ldots,(p-2,p-1),\\
&(p+1,p+2),\ldots,(q-2,q-1),\\
&(q+1,q+2),\ldots,(n-2,n-1).
\end{aligned}
\tag{2.6}
\]

The paired probes collapse as before. The probe in gap \(1\) and the
external right cap surround \(a_1\), completing the reverse product.
\(\square\)

These are identities for the actual common-shadow maps, not for a
placement-blind deletion model.

---

## 3. The all-even-length cap complex

Choose any ordered four-support

\[
Q=\{q_1<q_2<q_3<q_4\}\subset G_n
\tag{3.1}
\]

with parity pattern

\[
\boxed{
q_1,q_4\text{ odd},
\qquad
q_2,q_3\text{ even}.
}
\tag{3.2}
\]

Discard the outer odd-odd edge \(14\), retain the five local edges

\[
12,\quad13,\quad23,\quad24,\quad34,
\tag{3.3}
\]

and let

\[
\partial_{n,Q}^{\cap}:
\mathcal R_{2r+2}^{\oplus4}
\longrightarrow
\mathcal R_{2r+1}^{\oplus5}
\tag{3.4}
\]

be the corresponding projection of the local tetrahedral matching map.
Define

\[
\boxed{
\begin{aligned}
\chi_{n,Q}(F_{12},F_{13},F_{23},F_{24},F_{34})
={}&
-\lambda_{2r+1}^{L}(F_{12})
+\lambda_{2r+1}^{L}(F_{13})\\
&-\lambda_{2r+1}^{R}(F_{24})
+\lambda_{2r+1}^{R}(F_{34}).
\end{aligned}
}
\tag{3.5}
\]

### Theorem 3.1 — capped five-edge complex

For every even \(n\ge6\) and every support satisfying (3.2),

\[
\boxed{
\chi_{n,Q}\partial_{n,Q}^{\cap}=0.
}
\tag{3.6}
\]

The map \(\chi_{n,Q}\) is \(SO(3)\)-equivariant and onto. Consequently,

\[
\boxed{
\operatorname{coker}\partial_{n,Q}^{\cap}
\twoheadrightarrow\mathbb H
}
\tag{3.7}
\]

canonically.

### Proof

Write \(F_a\) for the face response at \(q_a\). Expanding (3.5) after the
matching map and grouping by face gives

\[
\begin{aligned}
\chi_{n,Q}\partial_{n,Q}^{\cap}(F_1,F_2,F_3,F_4)
={}&
\lambda^L
\left(-\rho_{q_1}^{q_1q_2}
+\rho_{q_1}^{q_1q_3}\right)F_1\\
&+
\left(
\lambda^L\rho_{q_2}^{q_1q_2}
-\lambda^R\rho_{q_2}^{q_2q_4}
\right)F_2\\
&+
\left(
-\lambda^L\rho_{q_3}^{q_1q_3}
+\lambda^R\rho_{q_3}^{q_3q_4}
\right)F_3\\
&+
\lambda^R
\left(
\rho_{q_4}^{q_2q_4}
-\rho_{q_4}^{q_3q_4}
\right)F_4,
\end{aligned}
\tag{3.8}
\]

where the depth subscripts on \(\lambda^L,\lambda^R\) are suppressed.
Precompose each parenthesis with its onto face map \(B_{n,q_a}\). Every
resulting composition is one of (2.3) or (2.4), hence equals \(\Pi_n\).
All four lines therefore vanish. Since the face maps are onto, (3.8)
vanishes intrinsically on response space.

Equivariance follows from (1.2), and surjectivity follows from either
\(\lambda^L\) or \(\lambda^R\). \(\square\)

---

## 4. Why the first support is \(n=6\)

At \(n=4\), there are only three internal gaps, so no four-support exists.
At \(n=5\), the four gaps have parity pattern

\[
\mathrm O\,\mathrm E\,\mathrm O\,\mathrm E,
\tag{4.1}
\]

not (3.2). At \(n=6\), there are exactly two even labels between an ordered
pair of odd endpoints:

\[
\boxed{
(q_1,q_2,q_3,q_4)=(1,2,4,5).
}
\tag{4.2}
\]

It is therefore the unique first support for Theorem 3.1. Its unselected
gap is \(3\), precisely the central spectator isolated computationally in
Note 15.

This gives a structural explanation for the first \(n=6\) defect:

\[
\boxed{
\text{central spectator placement}
=
\text{first admissible }\mathrm O\,\mathrm E\,\mathrm E\,\mathrm O
\text{ cap}.
}
\tag{4.3}
\]

---

## 5. Exactness at \(n=6\)

For (4.2), discard actual edge \((1,5)\) and keep

\[
(1,2),\quad(1,4),\quad(2,4),\quad(2,5),\quad(4,5).
\tag{5.1}
\]

The projected matching map has dimensions

\[
\partial_{\cap,6}:
\mathcal R_4^{\oplus4}
\longrightarrow
\mathcal R_3^{\oplus5},
\qquad
1296\longrightarrow540.
\tag{5.2}
\]

Theorem 3.1 and the surjectivity of \(\chi_6\) give

\[
\operatorname{rank}_{\mathbb Q}\partial_{\cap,6}
\le540-4=536.
\tag{5.3}
\]

Exact elimination independently gives

\[
\operatorname{rank}_{\mathbb F_{1009}}\partial_{\cap,6}
=
\operatorname{rank}_{\mathbb F_{1013}}\partial_{\cap,6}
=536.
\tag{5.4}
\]

Either computation exhibits a nonzero \(536\)-minor of the rational
matching map. Hence its rational rank is at least \(536\), and (5.3)
forces equality:

\[
\boxed{
\operatorname{rank}_{\mathbb Q}\partial_{\cap,6}=536,
\qquad
\ker\chi_6=\operatorname{im}\partial_{\cap,6}.
}
\tag{5.5}
\]

The five labelled edge blocks of \(\chi_6\) have ranks

\[
\boxed{
(4,4,0,4,4).
}
\tag{5.6}
\]

Thus the residual is shared by the four odd-even edges, while the central
even-even edge is invisible to it.

---

## 6. Passage back to the tetrahedral quotient

Let \(C^1_{6,Q}\) be the full six-edge target and let
\(\mathcal R_3^{(14)}\) be the discarded long-edge block. Quotient
associativity gives

\[
\begin{aligned}
Y_{6,Q}/E_{14}
&\cong
C^1_{6,Q}/
\left(
\operatorname{im}\partial_{6,Q}
+\mathcal R_3^{(14)}
\right)\\
&\cong
\operatorname{coker}\partial_{\cap,6}.
\end{aligned}
\tag{6.1}
\]

Combining (6.1) with (5.5) proves (0.5). No quotient basis, Casimir
complement, or finite-field identification is needed to define the map:
\(\chi_6\) itself is the characteristic-zero decoder.

Note 15 showed only that the quotient has spin fingerprint
\(V_0\oplus V_1\) over two prime fields. The present formula explains its
edge placement and realizes its standard quaternionic action directly.

---

## 7. Relation to the odd-length square

Notes 16 and 17 expose complementary parity mechanisms:

\[
\begin{array}{c|c|c}
&\text{support parity}&\text{quaternionic operator}\\ \hline
\text{odd }n&
\mathrm O\,\mathrm O\,\mathrm E\,\mathrm E&
+,-,-,+\text{ paired square}\\
\text{even }n&
\mathrm O\,\mathrm E\,\mathrm E\,\mathrm O&
-\lambda^L,+\lambda^L,0,-\lambda^R,+\lambda^R
\text{ capped five-edge map}.
\end{array}
\tag{7.1}
\]

In both cases, the support is not guessed from a dimension anomaly. Its
position is forced by the order in which actual common shadows can be
collapsed to the same total product \(\Pi_n\).

The two mechanisms are not yet a single transport law. In particular,
Note 14's \(n=5\) central channel lies on the interleaved pattern
\(\mathrm O\,\mathrm E\,\mathrm O\,\mathrm E\), which neither theorem
directly covers. The missing operation is now localized: it must transport
between the paired square, the left/right caps, and that interleaved seed
without erasing their labelled edge incidence.

---

## 8. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/n6_capped_five_edge_operator_certificate.py
~~~

The script verifies:

- both decoder identities in (1.4) at depth three exactly over
  \(\mathbb Q\);
- \(SO(3)\)-equivariance and surjectivity of \(\lambda_3^L,\lambda_3^R\);
- all four actual cap-shadow collapses to \(\Pi_6\) over \(\mathbb Z\);
- factorization of every actual face-to-shadow map over both prime fields;
- \(\chi_6\partial_{\cap,6}=0\) and rank \(536\) independently over
  \(\mathbb F_{1009}\) and \(\mathbb F_{1013}\);
- the labelled residual ranks \(4,4,0,4,4\).

Expected final line:

~~~text
ALL CHECKS PASSED
~~~

---

## 9. Next target

The two first placement anomalies now have closed rational decoders:

\[
\begin{aligned}
n=6:&\quad
Y_{6,(1,2,4,5)}/E_{14}
\xrightarrow{\ \chi_6\ }\mathbb H,\\
n=7:&\quad
Y_{7,(1,3,4,6)}/(E_{12}+E_{34})
\xrightarrow{\ \kappa_{212}\ }\mathbb H.
\end{aligned}
\tag{9.1}
\]

The next problem is no longer to find either quaternion. It is to construct
the order-sensitive transport which compares these two explicit decoders
with the central \(K_4\subset\mathbb H\otimes\mathbb H\) of Note 14.
Note 18 fixes the latter as \(K_4=\iota(\mathbb H)\) with normalized
coordinate \(\nu=\frac14\iota^*\), so this comparison now has no
target-coordinate ambiguity. Note 19 carries out the \(n=6\) comparison:
there is a unique outer-normalized local quotient \(\Omega_6\) and

\[
\chi_6=\beta\Omega_6,
\qquad
\beta((x\otimes y)\otimes w)=xw\bar y,
\tag{9.2}
\]

but \(\beta(K_4\otimes V)=0\). The cap quaternion is therefore a quotient
of \(W_{12}\otimes V\), not a direct tensor transport of \(K_4\).

The next comparison is the second spectator: whether this
\(W_{12}\)-born quaternion reaches the \(n=7\) square by a common
order-sensitive insertion law. Only after that step should overlapping cap
and square operators be assembled into a third differential or interpreted
as transport nonconfluence.
