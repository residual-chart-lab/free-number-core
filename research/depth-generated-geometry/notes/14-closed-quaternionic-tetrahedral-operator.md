# Note 14 — Closed Quaternionic Tetrahedral Operator

## the first response syzygy is an explicit ordered quaternion map

**Status:** theorem over \(\mathbb Q\) at \(n=5\), with an exact
standard-library certificate

**Depends on:** Notes 10, 12, and 13

**Claim boundary:** this note replaces the quotient-basis definition of the
minimal tetrahedral target by a closed \(SO(3)\)-equivariant quaternionic
operator. It proves the exact sequence at \(n=5\) and identifies a
distinguished four-dimensional quaternionic channel inside the target.
Note 18 subsequently gives that channel a canonical orthogonal quaternion
coordinate. Neither note proves a chain-level transport to the extra
\(\mathbb H\) found at the exceptional \(n=7\) placement.

---

## 0. Result in one line

Let

\[
\partial_5:\mathcal R_3^{\oplus4}\longrightarrow
\mathcal R_2^{\oplus6}
\tag{0.1}
\]

be the tetrahedral pair-matching map of Note 10. There is an explicit map

\[
\boxed{
\omega_5:\mathcal R_2^{\oplus6}
\longrightarrow \mathbb H\otimes\mathbb H
}
\tag{0.2}
\]

made only from quaternion multiplication, the right response decoder, and
one fixed \(SO(3)\)-invariant diagonal tensor, such that

\[
\boxed{
\omega_5\partial_5=0,
\qquad
\operatorname{rank}\omega_5=16,
\qquad
\ker\omega_5=\operatorname{im}\partial_5.
}
\tag{0.3}
\]

Consequently Note 13's abstract local quotient is now realized directly:

\[
\boxed{
0\longrightarrow\operatorname{im}\partial_5
\longrightarrow\mathcal R_2^{\oplus6}
\xrightarrow{\ \omega_5\ }
\mathbb H\otimes\mathbb H
\longrightarrow0.
}
\tag{0.4}
\]

No row-reduced quotient basis occurs in the definition of \(\omega_5\).

---

## 1. Right response coordinates

Use Note 12's right encoder

\[
J_2:\mathbb H\otimes V\otimes V\xrightarrow{\sim}\mathcal R_2,
\tag{1.1}
\]

\[
J_2(h\otimes u\otimes v)(x,y)=h y v x u.
\tag{1.2}
\]

Every formula below is defined on a pure decoder coordinate

\[
J_2^{-1}F=h\otimes u\otimes v
\tag{1.3}
\]

and extended linearly.

Fix

\[
e_0=1,
\qquad e_1=i,
\qquad e_2=j,
\qquad e_3=k,
\tag{1.4}
\]

and put

\[
\boxed{
\Xi:=\sum_{a=0}^{3}e_a\otimes e_a.
}
\tag{1.5}
\]

Although (1.5) is written in a basis, it is invariant under the distinguished
diagonal \(SO(3)\)-action. Indeed, conjugation fixes \(1\) and rotates
\((i,j,k)\) by an orthogonal matrix, so

\[
1\otimes1+i\otimes i+j\otimes j+k\otimes k
\tag{1.6}
\]

is unchanged. The formulas therefore use the same symmetry already present
in the spin and Casimir decompositions of the earlier notes.

---

## 2. Five primitive operators

Define five maps

\[
P,A,B,C,D:
\mathbb H\otimes V\otimes V
\longrightarrow\mathbb H\otimes\mathbb H
\tag{2.1}
\]

by

\[
\begin{aligned}
P(h,u,v)
&:=h\otimes uv,\\[1mm]
A(h,u,v)
&:=\sum_{a=0}^{3}he_a\otimes uv e_a,\\[1mm]
B(h,u,v)
&:=\sum_{a=0}^{3}he_a\otimes u e_a v,\\[1mm]
C(h,u,v)
&:=\sum_{a=0}^{3}e_a\otimes uvh e_a,\\[1mm]
D(h,u,v)
&:=\sum_{a=0}^{3}e_a h e_a v\otimes u.
\end{aligned}
\tag{2.2}
\]

Associativity fixes all parentheses. Each map is \(SO(3)\)-equivariant:
quaternion multiplication is equivariant for conjugation, and every summed
pair of basis elements comes from the invariant tensor \(\Xi\).

The unsummed operator \(P\) is onto. Products \(uv\), with \(u,v\in V\),
span all of \(\mathbb H\): equal vectors produce the real direction and
orthogonal vectors produce all three imaginary directions. Hence

\[
\operatorname{rank}P=16.
\tag{2.3}
\]

---

## 3. The six ordered edge operators

Index the tetrahedral edges lexicographically by

\[
12,13,14,23,24,34.
\tag{3.1}
\]

Define

\[
\boxed{
\begin{aligned}
\Lambda_{12}&=P-\frac12B+\frac12C-D,\\
\Lambda_{13}&=P-\frac14A-\frac12B+\frac12C-D,\\
\Lambda_{14}&=-\frac14A-\frac12B,\\
\Lambda_{23}&=-\frac14A-\frac12C,\\
\Lambda_{24}&=P-\frac14A,\\
\Lambda_{34}&=P.
\end{aligned}
}
\tag{3.2}
\]

For an edge tuple

\[
(F_{12},F_{13},F_{14},F_{23},F_{24},F_{34})
\in\mathcal R_2^{\oplus6},
\tag{3.3}
\]

the closed tetrahedral operator is

\[
\boxed{
\omega_5(F)
=
\sum_{1\le i<j\le4}
\Lambda_{ij}\bigl(J_2^{-1}F_{ij}\bigr).
}
\tag{3.4}
\]

The fractions in (3.2) are not fitted numerical approximations. They are
exact rational coefficients forced by the four vertex-cancellation
identities below together with the outer normalization

\[
\Lambda_{34}=P.
\tag{3.5}
\]

The asymmetric appearance of (3.2) records the ordered gap geometry. This is
not the alternating differential of an unordered simplicial complex.

---

## 4. Exactness theorem

For an edge \(i<j\), let

\[
\rho_{ij}^{,i},\rho_{ij}^{,j}:\mathcal R_3\to\mathcal R_2
\tag{4.1}
\]

be the two intrinsic common-shadow restrictions used in Note 10. Thus

\[
(\partial_5G)_{ij}
=\rho_{ij}^{,i}G_i-\rho_{ij}^{,j}G_j.
\tag{4.2}
\]

### Theorem 4.1 — closed tetrahedral exactness at \(n=5\)

The map (3.4) is \(SO(3)\)-equivariant and the sequence (0.4) is exact.

### Proof

Substitution of (3.2) into the four vertex blocks gives the exact operator
identities

\[
\begin{aligned}
\Lambda_{12}J_2^{-1}\rho_{12}^{,1}
+\Lambda_{13}J_2^{-1}\rho_{13}^{,1}
+\Lambda_{14}J_2^{-1}\rho_{14}^{,1}&=0,\\
-\Lambda_{12}J_2^{-1}\rho_{12}^{,2}
+\Lambda_{23}J_2^{-1}\rho_{23}^{,2}
+\Lambda_{24}J_2^{-1}\rho_{24}^{,2}&=0,\\
-\Lambda_{13}J_2^{-1}\rho_{13}^{,3}
-\Lambda_{23}J_2^{-1}\rho_{23}^{,3}
+\Lambda_{34}J_2^{-1}\rho_{34}^{,3}&=0,\\
-\Lambda_{14}J_2^{-1}\rho_{14}^{,4}
-\Lambda_{24}J_2^{-1}\rho_{24}^{,4}
-\Lambda_{34}J_2^{-1}\rho_{34}^{,4}&=0.
\end{aligned}
\tag{4.3}
\]

These are identities between fixed finite-dimensional quaternionic maps;
the certificate verifies every matrix entry over
\(\operatorname{Fraction}\). Equation (4.3) is exactly

\[
\omega_5\partial_5=0.
\tag{4.4}
\]

Equivariance follows from Section 2 and is also checked on all three
infinitesimal \(SO(3)\) generators.

By (3.5) and (2.3), \(\omega_5\) is onto, so

\[
\dim\ker\omega_5=6\cdot36-16=200.
\tag{4.5}
\]

Note 10 proved

\[
\operatorname{rank}\partial_5=200.
\tag{4.6}
\]

The inclusion from (4.4) and equality of dimensions now give

\[
\ker\omega_5=\operatorname{im}\partial_5.
\tag{4.7}
\]

This proves (0.4). \(\square\)

### Normalized uniqueness

The edge-\(34\) block already maps onto the quotient. Therefore any linear
map

\[
\widetilde\omega:\mathcal R_2^{\oplus6}\to
\mathbb H\otimes\mathbb H
\tag{4.8}
\]

which kills \(\operatorname{im}\partial_5\) and has
\(\widetilde\Lambda_{34}=P\) must equal \(\omega_5\). Thus (3.2) is not one
arbitrary quotient coordinate choice: it is the unique representative after
the ordered right-coordinate normalization (3.5).

---

## 5. A hidden \(12+4\) channel decomposition

The six blocks of \(\omega_5\) have exact ranks

\[
\boxed{
\begin{array}{c|cccccc}
ij&12&13&14&23&24&34\\ \hline
\operatorname{rank}\Lambda_{ij}&16&12&16&4&12&16.
\end{array}
}
\tag{5.1}
\]

Exact Casimir projection refines these ranks:

\[
\begin{array}{c|c|c}
\text{edges}&\text{spin dimensions }(V_0,V_1,V_2)&
\text{image type}\\ \hline
12,14,34&(2,9,5)&2V_0\oplus3V_1\oplus V_2
\cong\mathbb H\otimes\mathbb H\\
13,24&(1,6,5)&V_0\oplus2V_1\oplus V_2
\cong\mathbb H\otimes V\\
23&(1,3,0)&V_0\oplus V_1
\cong\mathbb H.
\end{array}
\tag{5.2}
\]

There is more than a rank coincidence. Put

\[
W_{12}:=\operatorname{im}\Lambda_{13},
\qquad
K_4:=\operatorname{im}\Lambda_{23}.
\tag{5.3}
\]

Then exact row reduction gives

\[
\boxed{
\operatorname{im}\Lambda_{13}
=\operatorname{im}\Lambda_{24}=W_{12},
\qquad
\mathbb H\otimes\mathbb H=W_{12}\oplus K_4,
}
\tag{5.4}
\]

with

\[
W_{12}\cong\mathbb H\otimes V,
\qquad
K_4\cong\mathbb H.
\tag{5.5}
\]

Thus the minimal tetrahedral quotient already contains a distinguished
quaternionic channel. It is visible through the central edge \(23\), while
the two rank-12 edges \(13\) and \(24\) land in the same complementary
channel.

Note 18 strengthens (5.4) canonically. With

\[
\iota(q)=\sum_{\alpha=0}^{3}e_\alpha\otimes qe_\alpha,
\qquad
\nu=\frac14\iota^*,
\tag{5.6}
\]

one has

\[
\boxed{
K_4=\iota(\mathbb H),
\qquad
W_{12}=\ker\nu=\iota(\mathbb H)^\perp,
\qquad
\mathbb H\otimes\mathbb H
=W_{12}\mathbin{\overset{\perp}{\oplus}}K_4.
}
\tag{5.7}
\]

In particular, the four-dimensional channel now has an explicit normalized
coordinate rather than only a dimension and spin type.

This is the first exact algebraic object against which the exceptional
four-dimensional summand at \(n=7\) can be compared. Note 15 isolates that
summand intrinsically as a cross-edge quotient \(K_{212}\cong\mathbb H\),
and Note 16 gives that quotient a closed rational square decoder. Note 17
similarly gives the \(n=6\) central-spectator quotient a closed rational cap
decoder. However, no transport map from \(K_4\) to either later quaternion
has yet been proved. The equality of dimension and spin type is therefore a
sharply testable statement rather than an identification.

---

## 6. What changed relative to Note 13

Note 13 knew that

\[
\operatorname{coker}\partial_5
\cong2V_0\oplus3V_1\oplus V_2
\cong\mathbb H\otimes\mathbb H.
\tag{6.1}
\]

That conclusion used a computed quotient basis and a Casimir decomposition.
The present note adds three stronger facts:

1. the quotient has a direct operational decoder \(\omega_5\);
2. the decoder is forced by four local cancellations and one outer
   normalization;
3. its edge blocks expose the intrinsic split
   \(\mathbb H\otimes\mathbb H\cong(\mathbb H\otimes V)\oplus\mathbb H\).

The tetrahedral target is therefore no longer only the place where sixteen
row relations happen to live. It is a concrete ordered quaternionic
relation object.

---

## 7. Certificate

Run from `research/depth-generated-geometry`:

```bash
python3 certificates/n5_quaternionic_second_differential_certificate.py
```

The script uses only Python's standard library and exact rational
arithmetic. It verifies:

- equivariance of \(P,A,B,C,D\) on the three infinitesimal rotation
  generators;
- all entries of \(\omega_5\partial_5=0\);
- \(\operatorname{rank}\omega_5=16\) and
  \(\operatorname{rank}\partial_5=200\);
- the six block ranks in (5.1);
- the spin dimensions in (5.2);
- the common 12-dimensional image and its complementary central
  \(\mathbb H\).

Expected final line:

```text
ALL CHECKS PASSED
```

---

### Companion central-channel certificate

Run

~~~bash
python3 certificates/n5_central_channel_factorization_certificate.py
~~~

to verify the Frobenius factorization, orthogonal projectors, and all six
normalized central edge coordinates stated in Note 18.

---

## 8. What is not proved

This note does **not** prove:

- an all-\(n\) closed formula for every local quotient \(Y_{n,Q}\);
- that naive spectator tensoring works for every placement;
- that \(K_4\) is the exceptional \(n=7\) summand;
- that the exceptional summand is curvature, holonomy, a gauge field, or a
  physical force;
- a third response differential.

The proved statement is narrower: the first nonzero tetrahedral syzygy has
an exact, closed, ordered quaternionic formula and contains a distinguished
\(\mathbb H\)-channel.

---

## 9. Next target

For a four-support \(Q\subset G_n\), the generic dimension law suggests a
transported operator

\[
\omega_{n,Q}^{\mathrm{tr}}:
\bigoplus_{\{i,j\}\subset Q}\mathcal R_{n-3}
\longrightarrow
(\mathbb H\otimes\mathbb H)\otimes V^{\otimes(n-5)}.
\tag{9.1}
\]

Note 15 proves that a placement-blind version of (9.1) cannot preserve all
six edge images. The next calculation is now rigid:

1. add the order-sensitive slide/correction required by a spectator in the
   central interval, now constrained by Note 17's explicit cap decoder and
   Note 18's canonical seed coordinate;
2. recover not only the total \(n=6,7\) quotients but all six labelled
   edge-image profiles of Note 15;
3. compare both the \(n=6\) cap quotient of Note 17 and the exceptional
   \(n=7\) cross-edge quotient \(K_{212}\) of Note 16 directly with the
   transported central channel \(K_4\cong\mathbb H\).

If the last comparison is positive, the extra \(\mathbb H\) will no longer
be merely a same-type residual. It will have an explicit local origin in the
minimal tetrahedral operator.
