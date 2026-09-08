# Note 19 — Central-Spectator Channel Transfer

## the first spectator kills the seed \(K_4\)-channel and exposes a quaternion from \(W_{12}\)

**Status:** theorem over \(\mathbb Q\) at the central \(n=6\) support, with
an exact integer certificate

**Depends on:** Notes 14, 15, 17, and 18

**Claim boundary:** this note constructs the unique outer-normalized
48-dimensional local quotient at \(Q=(1,2,4,5)\), factors the cap decoder
through it by one closed quaternionic contraction, and proves which seed
channel survives the long-edge quotient. It does not yet give a closed
all-placement spectator functor, identify the \(n=7\) square by the same
transport, or interpret the channel transfer as curvature.

---

## 0. Result in one line

Let

\[
T_6:=(\mathbb H\otimes\mathbb H)\otimes V
\tag{0.1}
\]

and let

\[
\Omega_6:
(\mathbb H\otimes V^{\otimes3})^{\oplus6}
\longrightarrow T_6
\tag{0.2}
\]

be the unique local quotient map on the ordered support

\[
Q=(1,2,4,5)
\tag{0.3}
\]

whose outer edge \(34=(4,5)\) is the direct spectator extension of
\(\Lambda_{34}=P\). Define

\[
\boxed{
\beta:T_6\longrightarrow\mathbb H,
\qquad
\beta((x\otimes y)\otimes w)=xw\bar y.
}
\tag{0.4}
\]

Then

\[
\boxed{
\beta\Omega_6
=
(-\lambda_3^L,\,+\lambda_3^L,\,0,\,0,\,
-\lambda_3^R,\,+\lambda_3^R)
}
\tag{0.5}
\]

in local edge order

\[
(12,13,14,23,24,34).
\tag{0.6}
\]

Moreover,

\[
\boxed{
\beta\bigl(\iota(\mathbb H)\otimes V\bigr)=0,
\qquad
\operatorname{im}(\Omega_6)_{14}=\ker\beta.
}
\tag{0.7}
\]

Consequently the central-spectator quaternion of Note 17 is not the direct
spectator extension \(K_4\otimes V\) of the seed quaternion. That entire
12-dimensional channel is absorbed by the long edge. The surviving
\(\mathbb H\) is a quotient of the orthogonal channel
\(W_{12}\otimes V\).

---

## 1. The outer-normalized local quotient

Write the four vertices of \(Q\) in their local order as \(1,2,3,4\).
After applying the right decoder \(J_3^{-1}\) on every edge response, the
six-edge space is

\[
\widehat C^1_{6,Q}
=
(\mathbb H\otimes V^{\otimes3})^{\oplus6},
\qquad
\dim\widehat C^1_{6,Q}=648.
\tag{1.1}
\]

Let

\[
\widehat\partial_{6,Q}:
\mathcal R_4^{\oplus4}
\longrightarrow
\widehat C^1_{6,Q}
\tag{1.2}
\]

be the actual four-face matching map in these decoder coordinates.

On the outer local edge \(34=(4,5)\), the remaining actual gaps are
\((1,2,3)\). Put

\[
\boxed{
(\Omega_6)_{34}
(h\otimes u\otimes v\otimes w)
=
(h\otimes uv)\otimes w.
}
\tag{1.3}
\]

This is

\[
\Lambda_{34}\otimes\operatorname{id}_V
=P\otimes\operatorname{id}_V
\tag{1.4}
\]

with the spectator in the third remaining position, and it is onto \(T_6\).

### Theorem 1.1 — normalized central-support exactness

There is a unique rational map \(\Omega_6\) satisfying (1.3) and

\[
\Omega_6\widehat\partial_{6,Q}=0.
\tag{1.5}
\]

It has entries in \(\frac14\mathbb Z\), is onto, and

\[
\boxed{
\ker\Omega_6=\operatorname{im}\widehat\partial_{6,Q}.
}
\tag{1.6}
\]

Equivalently,

\[
\boxed{
\mathcal R_4^{\oplus4}
\xrightarrow{\ \widehat\partial_{6,Q}\ }
\widehat C^1_{6,Q}
\xrightarrow{\ \Omega_6\ }
T_6
\longrightarrow0
}
\tag{1.7}
\]

is exact at the last two terms.

### Proof

The certificate first factors every actual face-to-shadow map over
\(\mathbb Q\). A selected \(324\times324\) face minor has an inverse with
entries in \(\frac1{16}\mathbb Z\), and \(J_3^{-1}\) has entries in
\(\frac18\mathbb Z\). Hence

\[
128\,\widehat\partial_{6,Q}
\tag{1.8}
\]

is an explicit integer matrix of shape \(648\times1296\).

Independent nullspace elimination modulo \(1009\) and \(1013\), followed
by the outer normalization (1.3), reconstructs the same integer matrix

\[
4\Omega_6.
\tag{1.9}
\]

Its entries lie in

\[
\{-8,-4,-3,-1,0,1,3,4,9\}.
\tag{1.10}
\]

The final check is not modular:

\[
\boxed{
(4\Omega_6)(128\,\widehat\partial_{6,Q})=0
}
\tag{1.11}
\]

is verified entry by entry over \(\mathbb Z\), and the \(34\)-block is
exactly four times (1.3).

The outer block is onto, so \(\operatorname{rank}_{\mathbb Q}\Omega_6=48\)
and

\[
\dim\ker\Omega_6=648-48=600.
\tag{1.12}
\]

Both modular reductions of \(\widehat\partial_{6,Q}\) have rank \(600\).
Therefore its rational rank is at least \(600\), while (1.5) bounds it
above by \(600\). This proves (1.6).

Finally, any second map satisfying (1.3) and (1.5) factors through the
quotient (1.7). Its difference from \(\Omega_6\) vanishes on the surjective
\(34\)-block, hence vanishes everywhere. This proves uniqueness.
\(\square\)

The word “transport” in the title is deliberately restricted: \(\Omega_6\)
is the quotient coordinate forced by one transported outer block and all
matching identities. It is not yet an all-placement transport functor.

---

## 2. The closed bridge to the cap decoder

The contraction (0.4) is \(SO(3)\)-equivariant because conjugation commutes
with quaternion multiplication. It is onto: its values already contain
the real and all three imaginary basis directions.

On the normalized outer edge (1.3),

\[
\begin{aligned}
\beta(\Omega_6)_{34}(h,u,v,w)
&=
\beta((h\otimes uv)\otimes w)\\
&=
hw\overline{uv}\\
&=
hwvu.
\end{aligned}
\tag{2.1}
\]

Because \(u,v\in V\), the two conjugation signs cancel. Equation (2.1) is
exactly Note 17's right-cap decoder

\[
\lambda_3^R J_3(h,u,v,w)=hwvu.
\tag{2.2}
\]

The remaining five blocks obey the full identity

\[
\boxed{
\beta\Omega_6
=
(-\lambda_3^L,\,+\lambda_3^L,\,0,\,0,\,
-\lambda_3^R,\,+\lambda_3^R).
}
\tag{2.3}
\]

After deleting the long edge \(14\), (2.3) is precisely the five-edge
operator \(\chi_6\) of Note 17. Thus

\[
\boxed{
\chi_6=\beta\Omega_6
\quad\text{on the retained five edges}.
}
\tag{2.4}
\]

The certificate verifies (2.3) over \(\mathbb Z\) after multiplying
\(\Omega_6\) by four. No quotient-basis comparison remains in (2.4):
\(\beta\) is the single closed target contraction which reads the cap
residual from the normalized local quotient.

---

## 3. The seed channel is annihilated

Recall Note 18's Frobenius embedding

\[
\iota(q)=\sum_{\alpha=0}^{3}e_\alpha\otimes qe_\alpha,
\qquad
K_4=\iota(\mathbb H).
\tag{3.1}
\]

For every \(q\in\mathbb H\) and \(w\in V\),

\[
\begin{aligned}
\beta(\iota(q)\otimes w)
&=
\sum_{\alpha=0}^{3}
e_\alpha w\overline{qe_\alpha}\\
&=
\left(
\sum_{\alpha=0}^{3}
e_\alpha w\bar e_\alpha
\right)\bar q\\
&=0.
\end{aligned}
\tag{3.2}
\]

The last equality is the same quaternionic averaging identity used in
Note 18:

\[
\sum_{\alpha=0}^{3}e_\alpha w\bar e_\alpha=0
\qquad(w\in V).
\tag{3.3}
\]

Therefore

\[
\boxed{
K_4\otimes V\subseteq\ker\beta.
}
\tag{3.4}
\]

Using the orthogonal decomposition of Note 18,

\[
T_6
=
(W_{12}\otimes V)
\mathbin{\overset{\perp}{\oplus}}
(K_4\otimes V),
\tag{3.5}
\]

equation (3.4) says that \(\beta\) factors entirely through the first
36-dimensional channel:

\[
\boxed{
T_6
\xrightarrow{\ P_{W_{12}}\otimes1\ }
W_{12}\otimes V
\xrightarrow{\ \beta_W\ }
\mathbb H.
}
\tag{3.6}
\]

The restriction \(\beta_W\) is onto because \(\beta\) is onto and kills
the complementary summand.

---

## 4. The long edge is exactly the kernel

Let

\[
E_{14}:=\operatorname{im}(\Omega_6)_{14}\subset T_6
\tag{4.1}
\]

be the image of the long actual edge \((1,5)\). From the zero \(14\)-block
in (2.3),

\[
E_{14}\subseteq\ker\beta.
\tag{4.2}
\]

Exact row reduction gives

\[
\operatorname{rank}_{\mathbb Q}(\Omega_6)_{14}=44.
\tag{4.3}
\]

Since \(\beta:T_6\to\mathbb H\) is onto,

\[
\dim\ker\beta=48-4=44.
\tag{4.4}
\]

Thus the inclusion (4.2) is equality:

\[
\boxed{
E_{14}=\ker\beta.
}
\tag{4.5}
\]

Combining (3.4) and (4.5) gives the stronger statement

\[
\boxed{
K_4\otimes V\subset E_{14}.
}
\tag{4.6}
\]

The direct spectator extension of the seed quaternion is therefore wholly
long-edge-visible and disappears in the quotient by that edge.

On the other hand,

\[
\boxed{
\begin{aligned}
T_6/E_{14}
&\xrightarrow[\ \beta\ ]{\ \sim\ }\mathbb H,\\
T_6/E_{14}
&\cong
\frac{W_{12}\otimes V}
{E_{14}\cap(W_{12}\otimes V)}
\cong\mathbb H.
\end{aligned}
}
\tag{4.7}
\]

Equation (4.7) is the target-side form of Note 17's

\[
Y_{6,(1,2,4,5)}/E_{14}\cong\mathbb H.
\tag{4.8}
\]

It also identifies the exact origin of that residual: not \(K_4\otimes V\),
but a four-dimensional quotient of \(W_{12}\otimes V\).

---

## 5. The labelled channel fingerprint

The normalized quotient has the following exact rational ranks:

\[
\boxed{
\begin{array}{c|rrrrrr}
ij&12&13&14&23&24&34\\ \hline
\dim E_{ij}
&48&36&44&12&36&48\\
\dim P_{W\otimes V}E_{ij}
&36&36&32&12&36&36\\
\dim(\nu\otimes1)E_{ij}
&12&12&12&0&12&12\\
\operatorname{rank}\beta|_{E_{ij}}
&4&4&0&0&4&4.
\end{array}
}
\tag{5.1}
\]

Several effects which were compressed into the dimension defect of Note 15
are now separated:

1. the long edge \(14\) splits as \(32+12=44\), contains all of
   \(K_4\otimes V\), and equals \(\ker\beta\);
2. the four cap-visible edges are exactly \(12,13,24,34\);
3. the local central edge \(23\) has moved completely into
   \(W_{12}\otimes V\).

The third point is the sharpest obstruction to naive tensor transport. At
\(n=5\), Note 18 proved

\[
\operatorname{im}\Lambda_{23}=K_4.
\tag{5.2}
\]

If a central spectator merely tensor-extended every seed block, the
corresponding \(n=6\) edge would lie in \(K_4\otimes V\). Instead (5.1)
gives

\[
\boxed{
(\nu\otimes1)E_{23}=0,
\qquad
E_{23}\subset W_{12}\otimes V,
\qquad
\dim E_{23}=12.
}
\tag{5.3}
\]

The ordered matching equations have transferred the entire central-edge
image to the orthogonal channel while leaving the outer \(34\)-block fixed.
This is an exact channel change, not a relabelling of two isomorphic
four-dimensional modules.

---

## 6. What changed

Note 18 reduced the open comparison to three fixed quaternion decoders:

\[
\nu\omega_5,\qquad\chi_6,\qquad\kappa_{212}.
\tag{6.1}
\]

The first arrow of that comparison is now resolved, but negatively for the
most obvious hypothesis:

\[
\boxed{
\text{the \(n=6\) residual is not transported \(K_4\);
it is extracted from transported \(W_{12}\).}
}
\tag{6.2}
\]

At the same time, it is resolved positively at the level of the full
normalized quotient:

\[
\boxed{
\chi_6=\beta\Omega_6,
\qquad
\beta(x\otimes y\otimes w)=xw\bar y.
}
\tag{6.3}
\]

Thus the missing order-sensitive operation is not an arbitrary correction.
It inserts the spectator **between** the two quaternion factors and
conjugates the second. That operation automatically kills the Frobenius
diagonal \(K_4\otimes V\) and reads a quotient of its orthogonal complement.

This gives a precise algebraic version of “the fold remembers where it was
made”: moving the spectator into the central interval changes which
orthogonal channel carries the surviving quaternion.

---

## 7. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/n6_seed_cap_bridge_certificate.py
~~~

The script verifies:

- exact rational factorization of every actual face-to-shadow map;
- reconstruction of the same \(4\Omega_6\) modulo \(1009\) and \(1013\);
- the integer identity
  \((4\Omega_6)(128\widehat\partial_{6,Q})=0\);
- outer-edge normalization and exactness of (1.7);
- \(\beta\Omega_6=\chi_6\) over \(\mathbb Q\);
- \(\beta(\iota(\mathbb H)\otimes V)=0\) over \(\mathbb Z\);
- all rational ranks in (5.1);
- \(E_{14}=\ker\beta\) and
  \(K_4\otimes V\subset E_{14}\).

Expected final line:

~~~text
ALL CHECKS PASSED
~~~

---

## 8. What is not proved

This note does **not** prove:

- a short primitive-operator formula for all six blocks of \(\Omega_6\);
- a common spectator insertion law for the other four \(n=6\) supports;
- an all-\(n\) recurrence for the normalized local quotients;
- that the \(n=7\) parity square is obtained by a second application of
  \(\beta\) or of a conjugate operation;
- transport nonconfluence, curvature, or a physical interpretation.

The finite matrix defining \(\Omega_6\) is exact and canonically normalized,
but discovering its short all-placement formula remains a separate problem.

**Subsequent resolution:** Note 20 classifies every direct full-seed
normalization at all five spectator placements and constructs a two-chart
cover. Its central overlap transition is the closed map
\(\operatorname{id}_{\mathbb H}\otimes\theta\); the all-block primitive
formula and multi-spectator iteration remain open.

---

## 9. Next target

The coefficient alphabet (1.10) is small enough that the six blocks of
\(\Omega_6\) should admit a short expression in quaternion multiplication,
Frobenius insertions, and order-sensitive slides. The next steps are:

1. compress \(4\Omega_6\) into such a primitive formula;
2. repeat the same outer normalization for the four noncentral spectator
   placements and identify the insertion word controlling each block;
3. determine whether the second spectator sends the
   \(W_{12}\)-born cap residual to Note 16's parity-square residual;
4. only then compare two insertion paths and isolate a genuine
   nonconfluence operator.

The immediate object is no longer an unspecified transport correction. It
is the explicit map

\[
\beta(x\otimes y\otimes w)=xw\bar y
\tag{9.1}
\]

and the exact question is how that “insert-between-and-conjugate” operation
iterates with ordered spectators.
