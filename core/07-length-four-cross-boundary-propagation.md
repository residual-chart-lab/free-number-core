# Length-Four Cross-Boundary Propagation

**Status:** proved concrete-model theorem with exact certificate  
**Branch:** `core-reconstruction`  
**Depends on:** `core/04-length-two-exact-splitting.md`, `core/05-length-three-propagation.md`, `core/06-reconstruction-handoff.md`, `notes/11-spin-depth-filtration.md`  
**Certificate:** `certificates/core07_cross_boundary_certificate.py`  
**Model:** quaternionic boundary words at structural length four

## 0. Purpose

This note closes the final small-product test listed in the Core Capability Ledger:

\[
B_2\times B_2\longrightarrow B_4.
\]

Let

\[
\Phi_2(x)=(q,S),
\qquad
\Phi_2(y)=(p,T),
\]

where

\[
q=m_2(x),
\qquad
p=m_2(y),
\qquad
S,T\in S^2_0V.
\]

The objectives are:

1. prove exact factorisation formulas for every internal probe profile through depth three;
2. identify the first direct residual-residual interaction;
3. give a finite complete signature for \(B_4\);
4. explain the length-four multiplicity-depth splitting from the factor sectors;
5. determine whether any additional cross-boundary input datum is needed once both length-two factors are retained exactly.

The answer is:

\[
\boxed{
(q,S,p,T)
\text{ determine a complete finite length-four signature.}
}
\]

No additional input datum is required for this product.

However, the output does not close back into one fixed pair of the form

\[
\mathbb H\oplus S^2_0V.
\]

The grade-four response hierarchy contains genuinely new multiplicity and depth structure.

---

## 1. Exact factorised coordinates at grade four

Recall the exact length-two splitting

\[
B_2=W_2\oplus U_2,
\]

where

\[
W_2:=\mathbb Rg\oplus\Lambda^2V
\cong\mathbb H,
\qquad
U_2:=S^2_0V.
\]

The subspace \(W_2\) is the canonical value-lift sector, while \(U_2\) is the length-two residual sector.

Since

\[
B_4
=
B_2\otimes B_2,
\]

there is an exact four-sector decomposition

\[
\boxed{
B_4
=
(W_2\otimes W_2)
\oplus
(W_2\otimes U_2)
\oplus
(U_2\otimes W_2)
\oplus
(U_2\otimes U_2).
}
\]

For brevity write

\[
VV:=W_2\otimes W_2,
\qquad
VR:=W_2\otimes U_2,
\qquad
RV:=U_2\otimes W_2,
\qquad
RR:=U_2\otimes U_2.
\]

The labels refer to value-lift and residual sectors of the left and right length-two factors. They do not assert that the final Free Numbers object is a two-letter decoration.

The dimensions are

\[
\dim VV=16,
\qquad
\dim VR=20,
\qquad
\dim RV=20,
\qquad
\dim RR=25,
\]

and hence

\[
81=16+20+20+25.
\]

Equivalently, the length-two coordinate isomorphism induces

\[
\boxed{
B_4
\cong
(\mathbb H\oplus S^2_0V)
\otimes
(\mathbb H\oplus S^2_0V).
}
\]

This is an exact factorised coordinate space. It is not yet a minimal intrinsic grade-four response coordinate.

### 1.1 Rotation-module content

As \(SO(3)\)-modules,

\[
W_2\cong V_0\oplus V_1,
\qquad
U_2\cong V_2.
\]

Therefore the four sectors decompose as

\[
VV
\cong
2V_0\oplus3V_1\oplus V_2,
\]

\[
VR
\cong
V_1\oplus2V_2\oplus V_3,
\]

\[
RV
\cong
V_1\oplus2V_2\oplus V_3,
\]

and

\[
RR
\cong
V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4.
\]

Summing gives

\[
B_4
\cong
3V_0\oplus6V_1\oplus6V_2\oplus3V_3\oplus V_4,
\]

as required.

This already shows why representation type alone cannot determine probe depth: the same spin occurs through several factor sectors and multiplicity channels.

---

## 2. Response notation

Let

\[
\Phi_2(x)=(q,S),
\qquad
\Phi_2(y)=(p,T).
\]

Write

\[
q=a+w,
\qquad
p=b+z,
\]

with

\[
a,b\in\mathbb R,
\qquad
w,z\in V.
\]

For a length-two coordinate \((q,S)\), recall the exact internal response

\[
L_{q,S}(d)
=
\langle\operatorname{Im}q,d\rangle
-
\frac{\operatorname{Re}q}{3}d
-
2S(d).
\]

Set

\[
L_x:=L_{q,S},
\qquad
L_y:=L_{p,T}.
\]

Thus

\[
L_x=\mathcal R_2(x),
\qquad
L_y=\mathcal R_2(y).
\]

For a pure composite

\[
x|y=r|s|t|u,
\]

there are three original internal gaps.

The depth-one responses are

\[
\mathcal R_4^{(1)},
\qquad
\mathcal R_4^{(2)},
\qquad
\mathcal R_4^{(3)}.
\]

For depth two, define the three distinct-gap components by

\[
D_{12}(r|s|t|u)(d_1,d_2)
:=
m_6(r|d_1|s|d_2|t|u),
\]

\[
D_{13}(r|s|t|u)(d_1,d_2)
:=
m_6(r|d_1|s|t|d_2|u),
\]

and

\[
D_{23}(r|s|t|u)(d_1,d_2)
:=
m_6(r|s|d_1|t|d_2|u).
\]

For depth three, define the canonical all-gap component

\[
A_4(r|s|t|u)(d_1,d_2,d_3)
:=
m_7(r|d_1|s|d_2|t|d_3|u).
\]

All maps are extended linearly to \(B_4\).

---

## 3. Exact cross-boundary factorisation theorem

### Theorem 3.1

Let

\[
\Phi_2(x)=(q,S),
\qquad
\Phi_2(y)=(p,T).
\]

Then for all probe vectors \(d,d_1,d_2,d_3\in V\),

\[
\boxed{
m_4(x|y)=pq.
}
\]

The depth-one responses are

\[
\boxed{
\mathcal R_4^{(1)}(x|y)(d)
=
pL_x(d),
}
\]

\[
\boxed{
\mathcal R_4^{(2)}(x|y)(d)
=
pdq,
}
\]

and

\[
\boxed{
\mathcal R_4^{(3)}(x|y)(d)
=
L_y(d)q.
}
\]

The depth-two components are

\[
\boxed{
D_{12}(x|y)(d_1,d_2)
=
pd_2L_x(d_1),
}
\]

\[
\boxed{
D_{13}(x|y)(d_1,d_2)
=
L_y(d_2)L_x(d_1),
}
\]

and

\[
\boxed{
D_{23}(x|y)(d_1,d_2)
=
L_y(d_2)d_1q.
}
\]

Finally,

\[
\boxed{
A_4(x|y)(d_1,d_2,d_3)
=
L_y(d_3)d_2L_x(d_1).
}
\]

### Proof

It is enough to prove the formulas on pure words and extend bilinearly.

Let

\[
x=r|s,
\qquad
y=t|u.
\]

Then

\[
q=sr,
\qquad
p=ut,
\]

and

\[
L_x(d)=sdr,
\qquad
L_y(d)=udt.
\]

Reversed compression gives

\[
m_4(r|s|t|u)=utsr=pq.
\]

For depth one,

\[
m_5(r|d|s|t|u)=utsdr=pL_x(d),
\]

\[
m_5(r|s|d|t|u)=utdsr=pdq,
\]

and

\[
m_5(r|s|t|d|u)=udtsr=L_y(d)q.
\]

For depth two,

\[
m_6(r|d_1|s|d_2|t|u)
=utd_2sd_1r
=pd_2L_x(d_1),
\]

\[
m_6(r|d_1|s|t|d_2|u)
=ud_2tsd_1r
=L_y(d_2)L_x(d_1),
\]

and

\[
m_6(r|s|d_1|t|d_2|u)
=ud_2td_1sr
=L_y(d_2)d_1q.
\]

For depth three,

\[
m_7(r|d_1|s|d_2|t|d_3|u)
=ud_3td_2sd_1r
=L_y(d_3)d_2L_x(d_1).
\]

This proves all formulas. \(\square\)

### 3.2 Orientation is structural

The order in the middle component is

\[
L_y(d_2)L_x(d_1),
\]

not

\[
L_x(d_1)L_y(d_2).
\]

Likewise, the value is

\[
pq,
\]

not \(qp\).

The right factor acts on the left under reversed quaternionic compression. This orientation must not be commuted or silently conjugated.

---

## 4. The first direct residual-residual interaction

Separate each length-two response into its value-lift and residual parts:

\[
L_x(d)=L_q(d)-2S(d),
\]

\[
L_y(d)=L_p(d)-2T(d),
\]

where

\[
L_q(d)
=
\langle\operatorname{Im}q,d\rangle
-
\frac{\operatorname{Re}q}{3}d,
\]

and similarly for \(L_p\).

The middle depth-two component expands as

\[
\begin{aligned}
D_{13}(x|y)(d_1,d_2)
&=
L_y(d_2)L_x(d_1)\\
&=
L_p(d_2)L_q(d_1)
-2L_p(d_2)S(d_1)\\
&\quad
-2T(d_2)L_q(d_1)
+4T(d_2)S(d_1).
\end{aligned}
\]

The final term

\[
\boxed{
4T(d_2)S(d_1)
}
\]

is the first direct residual-residual interaction in the reconstructed core.

Because \(S(d_1),T(d_2)\in V\), it has scalar and vector parts

\[
4T(d_2)S(d_1)
=
-4\langle T(d_2),S(d_1)\rangle
+
4T(d_2)\times S(d_1).
\]

Thus the cross-boundary interaction records both an inner-product channel and an oriented cross-product channel.

The order remains

\[
T(d_2)S(d_1).
\]

In general it cannot be replaced by \(S(d_1)T(d_2)\).

### 4.1 Depth-three expansion

The all-gap response similarly expands as

\[
\begin{aligned}
A_4(x|y)(d_1,d_2,d_3)
&=
L_y(d_3)d_2L_x(d_1)\\
&=
L_p(d_3)d_2L_q(d_1)
-2L_p(d_3)d_2S(d_1)\\
&\quad
-2T(d_3)d_2L_q(d_1)
+4T(d_3)d_2S(d_1).
\end{aligned}
\]

The depth-three residual-residual term is therefore

\[
\boxed{
4T(d_3)d_2S(d_1).
}
\]

---

## 5. Pure residual collision

Take

\[
x=S\in U_2=S^2_0V,
\qquad
y=T\in U_2=S^2_0V.
\]

Then

\[
q=p=0,
\qquad
L_x(d)=-2S(d),
\qquad
L_y(d)=-2T(d).
\]

The composite satisfies

\[
\boxed{
m_4(S|T)=0.
}
\]

Every depth-one internal response also vanishes:

\[
\boxed{
\mathcal R_4^{(1)}(S|T)
=
\mathcal R_4^{(2)}(S|T)
=
\mathcal R_4^{(3)}(S|T)
=0.
}
\]

At depth two,

\[
D_{12}(S|T)=0,
\qquad
D_{23}(S|T)=0,
\]

but the cross-boundary component is

\[
\boxed{
D_{13}(S|T)(d_1,d_2)
=
4T(d_2)S(d_1).
}
\]

At depth three,

\[
\boxed{
A_4(S|T)(d_1,d_2,d_3)
=
4T(d_3)d_2S(d_1).
}
\]

### Theorem 5.1 — Nonzero decomposable residual pairs ignite at depth two

If

\[
S\ne0,
\qquad
T\ne0,
\]

then

\[
D_{13}(S|T)\ne0.
\]

### Proof

Since \(S\ne0\), choose \(d_1\in V\) with

\[
S(d_1)\ne0.
\]

Since \(T\ne0\), choose \(d_2\in V\) with

\[
T(d_2)\ne0.
\]

The quaternions form a division algebra, so the product of two nonzero pure imaginary quaternions is nonzero. Therefore

\[
4T(d_2)S(d_1)\ne0.
\]

Hence \(D_{13}(S|T)\ne0\). \(\square\)

Thus every nonzero decomposable pure residual pair has exact first detection depth two:

\[
\boxed{
\delta(S|T)=2
\qquad(S,T\ne0).
}
\]

This is a concrete multiplication phenomenon:

> two zero-valued factors can produce a composite that remains zero-valued and depth-one invisible, while carrying a necessarily nonzero cross-boundary response at depth two.

No temporal or interpretive primitive is required for this statement.

---

## 6. Sectorwise probe-depth filtration

Let

\[
D_4^{\le d}
\]

denote compression together with every internal distinct-gap insertion profile through depth \(d\), and set

\[
F_d^{(4)}:=\ker D_4^{\le d}.
\]

The exact certificate computes both the full ranks and their restrictions to the four factor sectors.

### Theorem 6.1 — Exact sectorwise kernel table

The dimensions of the remaining invisible subspaces are:

| sector | dimension | \(F_0\) | \(F_1\) | \(F_2\) | \(F_3\) |
|---|---:|---:|---:|---:|---:|
| \(VV\) | 16 | 12 | 0 | 0 | 0 |
| \(VR\) | 20 | 20 | 12 | 0 | 0 |
| \(RV\) | 20 | 20 | 12 | 0 | 0 |
| \(RR\) | 25 | 25 | 25 | 9 | 0 |
| **total** | **81** | **77** | **49** | **9** | **0** |

Here \(F_d\) in a sector means the intersection of \(F_d^{(4)}\) with that sector.

The corresponding full profile ranks are

\[
\boxed{
\begin{array}{c|c|c}
\text{maximum depth}&\text{rank}&\text{kernel dimension}\\
\hline
0&4&77\\
1&32&49\\
2&72&9\\
3&81&0
\end{array}
}
\]

All ranks are computed over exact integer or rational arithmetic.

### 6.2 Representation refinement

The \(VV\) sector has

\[
VV\cong2V_0\oplus3V_1\oplus V_2.
\]

Compression detects one \(V_0\oplus V_1\) value copy. Its remaining compression kernel is

\[
F_0\cap VV
\cong
V_0\oplus2V_1\oplus V_2,
\]

and depth one detects this entire remainder:

\[
F_1\cap VV=0.
\]

For the mixed sector

\[
VR\cong V_1\oplus2V_2\oplus V_3,
\]

compression detects nothing. Depth one detects a quotient isomorphic to

\[
V_1\oplus V_2,
\]

leaving a distinguished late copy

\[
F_1\cap VR
\cong
V_2^{\mathrm{late}}\oplus V_3.
\]

Depth two detects the remainder. The same statement holds for \(RV\).

For the residual-residual sector,

\[
RR
\cong
V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4.
\]

Compression and all depth-one responses vanish identically on \(RR\):

\[
F_0\cap RR
=
F_1\cap RR
=
RR.
\]

Depth two detects

\[
V_0\oplus V_1\oplus V_2\oplus V_3,
\]

leaving exactly

\[
\boxed{
F_2\cap RR=V_4=S^4_0V.
}
\]

Depth three detects this final top-spin sector.

### 6.3 Exact explanation of the length-four multiplicity split

Adding the sector contributions, the part first detected at depth one is

\[
\begin{aligned}
&\bigl(V_0\oplus2V_1\oplus V_2\bigr)
&&\text{from }VV,\\
&\bigl(V_1\oplus V_2\bigr)
&&\text{from }VR,\\
&\bigl(V_1\oplus V_2\bigr)
&&\text{from }RV.
\end{aligned}
\]

Therefore depth one detects

\[
\boxed{
V_0\oplus4V_1\oplus3V_2.
}
\]

At depth two, the two mixed sectors contribute

\[
2V_2\oplus2V_3,
\]

while \(RR\) contributes

\[
V_0\oplus V_1\oplus V_2\oplus V_3.
\]

Thus depth two detects

\[
\boxed{
V_0\oplus V_1\oplus3V_2\oplus3V_3.
}
\]

Depth three detects the remaining

\[
\boxed{V_4.}
\]

This reproduces the length-four spin-depth table, but now explains where the multiplicities come from.

The six copies of \(V_2\) are distributed across four factor sectors:

\[
1+2+2+1=6.
\]

Three copies are detected at depth one and three at depth two. The split is therefore not an unexplained defect of the spin label. It is the visible trace of distinct factor-origin and cross-boundary channels.

---

## 7. The residual-residual hierarchy

On the full \(RR\) sector, the only potentially nonzero depth-two component is the middle cross-boundary response

\[
D_{13}.
\]

The exact restricted rank is

\[
\boxed{
\operatorname{rank}\bigl(D_{13}|_{RR}\bigr)=16.
}
\]

Since

\[
\dim RR=25,
\]

its kernel has dimension nine. The dimension count alone does not identify the kernel: \(V_0\oplus V_1\oplus V_2\) also has dimension nine. The identification uses the full depth-two profile.

Compression and every depth-one response vanish on \(RR\), and \(D_{13}\) is the only depth-two component that can be nonzero there. Hence

\[
\ker\bigl(D_{13}|_{RR}\bigr)=F_2^{(4)}\cap RR.
\]

The independently verified length-four subspace equality is

\[
F_2^{(4)}=S^4_0V,
\]

and \(S^4_0V\subset RR\). Therefore

\[
\boxed{
\ker\bigl(D_{13}|_{RR}\bigr)=S^4_0V=V_4.
}
\]

The rank calculation \(25-16=9=\dim V_4\) is a consistency check, not the sole identification argument.

The all-length vertical-response theorem gives

\[
A_4(R)=-8C_R
\qquad(R\in S^4_0V),
\]

so \(A_4\) is injective on the nine-dimensional survivor.

Consequently,

\[
\boxed{
(D_{13},A_4):RR\longrightarrow
\operatorname{Hom}(V^{\otimes2},\mathbb H)
\oplus
\operatorname{Hom}(V^{\otimes3},\mathbb H)
}
\]

is injective.

### 7.1 No nonzero decomposable tensor survives to depth three

Theorem 5.1 showed that

\[
D_{13}(S|T)\ne0
\]

for every nonzero decomposable residual pair \(S|T\).

Therefore the depth-three survivor

\[
V_4\subset RR
\]

contains no nonzero decomposable tensor of the form

\[
S\otimes T.
\]

It consists of linear superpositions whose depth-two cross-boundary responses cancel.

Thus the hierarchy has a sharp interpretation internal to the mathematics:

- a single nonzero residual pair is already visible at depth two;
- coherent combinations of several residual pairs can cancel every depth-two response;
- the remaining top-spin coherence is detected only at depth three.

This is the first exact transition from pairwise residual interaction to a higher coherent residual sector.

---

## 8. Finite complete grade-four signature

Define

\[
\mathcal J_4^{\mathrm{exact}}:B_4\longrightarrow\mathcal O_4
\]

by

\[
\boxed{
\mathcal J_4^{\mathrm{exact}}(z)
=
\bigl(
 m_4(z),
 \mathcal R_4^{(1)}(z),
 \mathcal R_4^{(2)}(z),
 \mathcal R_4^{(3)}(z),
 D_{12}(z),
 D_{13}(z),
 D_{23}(z),
 A_4(z)
\bigr).
}
\]

The codomain is

\[
\mathcal O_4
=
\mathbb H
\oplus
\operatorname{Hom}(V,\mathbb H)^{\oplus3}
\oplus
\operatorname{Hom}(V^{\otimes2},\mathbb H)^{\oplus3}
\oplus
\operatorname{Hom}(V^{\otimes3},\mathbb H).
\]

Its ambient dimension is

\[
4+3\cdot12+3\cdot36+108=256.
\]

This codomain is deliberately redundant.

### Theorem 8.1 — Exact finite observability at length four

\[
\boxed{
\mathcal J_4^{\mathrm{exact}}
\text{ is injective on }B_4.
}
\]

### Proof

The exact profile matrix through depth three has rank

\[
81.
\]

Since

\[
\dim B_4=3^4=81,
\]

its kernel is zero. \(\square\)

Thus

\[
\boxed{
\text{value + all depth-one channels + all depth-two channels + the all-gap depth-three channel determine }B_4.
}
\]

### 8.2 Exact product law from grade-two coordinates

Let

\[
\Psi_2:\mathbb H\oplus S^2_0V\longrightarrow B_2
\]

be the inverse length-two coordinate map.

The composite

\[
\widehat\Pi_{2,2}
:=
\mathcal J_4^{\mathrm{exact}}
\circ
(\Psi_2\otimes\Psi_2)
\]

defines a linear map

\[
\widehat\Pi_{2,2}:
(\mathbb H\oplus S^2_0V)
\otimes
(\mathbb H\oplus S^2_0V)
\longrightarrow
\mathcal O_4.
\]

The factorisation formulas of Theorem 3.1 give this map explicitly, and injectivity of \(\mathcal J_4^{\mathrm{exact}}\) gives

\[
\boxed{
\widehat\Pi_{2,2}:
(\mathbb H\oplus S^2_0V)^{\otimes2}
\xrightarrow{\ \cong\ }
\operatorname{im}\mathcal J_4^{\mathrm{exact}}.
}
\]

This is the first exact finite composition law for two nontrivial Free Number coordinates in the quaternionic boundary-word model.

It is not a multiplication

\[
(\mathbb H\oplus S^2_0V)
\times
(\mathbb H\oplus S^2_0V)
\longrightarrow
\mathbb H\oplus S^2_0V.
\]

The output belongs to the deeper grade-four response object.

---

## 9. Closure verdict

The smallest response-profile product program is now complete in the quaternionic boundary-word model:

\[
B_1\times B_1\to B_2,
\]

\[
B_2\times B_1\to B_3,
\qquad
B_1\times B_2\to B_3,
\]

and

\[
B_2\times B_2\to B_4.
\]

For the final product, the exact factor coordinates

\[
(q,S,p,T)
\]

determine a complete finite output signature. Therefore no additional cross-boundary input variable is required at this grade.

What is required is a richer output object containing the deeper response channels generated by composition.

The correct low-grade closure statement is therefore:

\[
\boxed{
\text{exact factor states compose without information loss, but not into a fixed-format residual decoration.}
}
\]

This supplies strong concrete evidence for Capability C5, compositional propagation, and C6, closure with remainder.

It does not yet prove a universal all-grade composition law for the abstract core.

---

## 10. Exact certificate

The companion certificate is

```text
certificates/core07_cross_boundary_certificate.py
```

It uses SymPy exact integer and rational arithmetic. It contains no floating-point rank calculation and no rounded Casimir stage.

It verifies:

1. every pure-word factorisation formula in Theorem 3.1 for all basis words and basis probes;
2. the full grade-four profile ranks
   \[
   4,32,72,81;
   \]
3. the sectorwise remaining-kernel table;
4. rank \(16\) of \(D_{13}\) on \(RR\);
5. rank \(25\) of \((D_{13},A_4)\) on \(RR\).

Run from the repository root:

```bash
python3 certificates/core07_cross_boundary_certificate.py
```

Expected output ends with:

```text
5209 exact checks passed
ALL CHECKS PASSED
```

---

## 11. What is proved and what remains open

### Proved here

1. Exact factorisation of every internal distinct-gap response through depth three for \(B_2\times B_2\to B_4\).
2. The direct residual-residual term
   \[
   4T(d_2)S(d_1).
   \]
3. Every nonzero decomposable pure residual pair is first detected at depth two.
4. Exact four-sector decomposition of \(B_4\) by length-two value/residual origin.
5. Exact sectorwise probe-depth kernel dimensions.
6. A factor-sector explanation of the length-four multiplicity-depth split.
7. \(D_{13}|_{RR}\) has rank \(16\) and kernel \(V_4\).
8. \((D_{13},A_4)\) is injective on \(RR\).
9. \(\mathcal J_4^{\mathrm{exact}}\) is injective on \(B_4\).
10. Exact grade-two coordinates compose into a finite complete grade-four signature without an additional input datum.

### Not claimed

1. The codomain of \(\mathcal J_4^{\mathrm{exact}}\) is not claimed minimal.
2. The four factor sectors are not yet the final intrinsic grade-four Free Number coordinates.
3. No universal all-grade finite-depth theorem is claimed.
4. No closed formula for the general spin-multiplicity-depth filtration is claimed.
5. No final standalone equality relation has been fixed.
6. No associative multiplication on one fixed carrier has been constructed.
7. The quaternionic boundary-word model is not claimed universal.
8. The Residual Chart OS is not used to define any theorem in this note.
9. No Time Engine, causal, conscious, or ethical interpretation is used as a premise.

---

## 12. Next decision gate

The grade-four product now has two exact but different descriptions:

1. the factorised coordinate
   \[
   (\mathbb H\oplus S^2_0V)^{\otimes2},
   \]
   which has the correct dimension \(81\) and preserves factor origin;
2. the complete observational signature
   \[
   \mathcal J_4^{\mathrm{exact}},
   \]
   which exposes probe depth but lives in a redundant 256-dimensional codomain.

The next task is to connect them by an intrinsic filtered coordinate of dimension \(81\):

```text
core/08-grade-four-intrinsic-filtered-coordinate.md
```

The target is not merely another decomposition. It is a coordinate object that simultaneously preserves:

- exact reconstruction;
- factor-origin sectors;
- probe-depth grading;
- the residual-residual interaction;
- the nine-dimensional top-spin survivor;
- and composition compatibility with the lower grades.

The decisive question is:

\[
\boxed{
\text{Can the redundant complete response profile be compressed to an intrinsic 81-dimensional filtered coordinate without losing compositional meaning?}
}
\]
