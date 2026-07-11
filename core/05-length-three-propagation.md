# Length-Three Propagation from Exact Length-Two Coordinates

**Status:** working theorem note  
**Branch:** `core-reconstruction`  
**Depends on:** `core/04-length-two-exact-splitting.md`, `notes/03-length-2-and-3-residual-filtration.md`, `notes/04-length-3-depth-2-response.md`

## 0. Purpose

Length two admits exact value-residual coordinates

\[
\Phi_2(x)=(q,S)
\in
\mathbb H\oplus S^2_0V,
\]

where

\[
q=m_2(x),
\qquad
S=\rho_2(x).
\]

This note asks what happens when one more boundary element

\[
u\in V=\operatorname{Im}\mathbb H
\]

is attached on the right or on the left.

The goals are:

1. derive exact formulas for compression and the first response levels;
2. determine whether the length-two coordinates propagate without an extra cross-boundary datum;
3. identify the genuinely new residual sector born at length three;
4. give a finite complete observational signature for \(B_3\).

The answer is two-sided:

- one-step left and right extension are exactly computable from \((q,S)\) and \(u\);
- nevertheless, the grade-three depth-one signature has a new seven-dimensional blind sector \(S^3_0V\), detected only at depth two.

---

## 1. Setup and conventions

Let

\[
B_n=V^{\otimes n},
\qquad
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
\]

For \(x\in B_2\), write

\[
x=\sigma_2(q)+S,
\qquad
q=m_2(x),
\qquad
S=\rho_2(x)\in S^2_0V.
\]

Write the quaternionic value as

\[
q=a+w,
\qquad
a=\operatorname{Re}q\in\mathbb R,
\qquad
w=\operatorname{Im}q\in V.
\]

The canonical internal length-two response is

\[
\mathcal R_2(x)(d)
:=
\mathcal R_2^{(1)}(x)(d)
=
m_3(I_d^{(1)}x).
\]

For a pure word \(r|s\),

\[
\mathcal R_2(r|s)(d)=sdr.
\]

---

## 2. Exact length-two response in \((q,S)\)-coordinates

The exact coordinate pair does more than recover \(x\). It also determines its full internal continuation response.

### 2.1 Response of the canonical value lift

Recall

\[
\sigma_2(a+w)
=
-\frac a3g
-\frac12*^{-1}(w).
\]

For \(d\in V\), the metric tensor satisfies

\[
\mathcal R_2(g)(d)
=
\sum_{r=1}^3e_rde_r
=d.
\]

For the oriented antisymmetric lift,

\[
\mathcal R_2(*^{-1}(w))(d)
=
-2\langle w,d\rangle,
\]

where the right-hand side is regarded as a real quaternion.

Therefore

\[
\boxed{
\mathcal R_2(\sigma_2(q))(d)
=
\langle w,d\rangle
-\frac a3d.
}
\]

Define

\[
L_q(d)
:=
\langle\operatorname{Im}q,d\rangle
-\frac{\operatorname{Re}q}{3}d.
\]

Then

\[
\mathcal R_2(\sigma_2(q))=L_q.
\]

### 2.2 Residual contribution

For \(S\in S^2_0V\), the established length-two response theorem gives

\[
\mathcal R_2(S)(d)
=
-2S(d),
\]

where \(S(d)\) denotes metric contraction, regarded as an element of \(V\subset\mathbb H\).

Hence every \(x\in B_2\) with exact coordinate \((q,S)\) has response

\[
\boxed{
\mathcal R_2(x)(d)
=
L_q(d)-2S(d).
}
\]

It is convenient to name this map

\[
\boxed{
L_{q,S}(d)
:=
\langle\operatorname{Im}q,d\rangle
-\frac{\operatorname{Re}q}{3}d
-2S(d).
}
\]

Thus

\[
L_{q,S}=\mathcal R_2(x).
\]

The pair \((q,S)\) therefore determines both the compressed value and the complete internal length-two response.

---

## 3. Right extension

Let

\[
E_R:B_2\times V\to B_3,
\qquad
E_R(x,u)=x|u.
\]

For a pure term \(r|s\) in \(x\),

\[
E_R(r|s,u)=r|s|u.
\]

### Theorem 3.1 — Exact right-propagation formulas

Let \(\Phi_2(x)=(q,S)\). Then for all \(u,d,d_1,d_2\in V\),

\[
\boxed{
m_3(x|u)=uq,
}
\]

\[
\boxed{
\mathcal R_3^{(1)}(x|u)(d)
=
uL_{q,S}(d),
}
\]

\[
\boxed{
\mathcal R_3^{(2)}(x|u)(d)
=
udq,
}
\]

and for the canonical internal-internal depth-two component,

\[
\boxed{
A_3(x|u)(d_1,d_2)
=
ud_2L_{q,S}(d_1).
}
\]

### Proof

For a pure word \(r|s|u\),

\[
m_3(r|s|u)=usr=u\,m_2(r|s).
\]

By linearity,

\[
m_3(x|u)=u\,m_2(x)=uq.
\]

The two internal insertion responses are

\[
\mathcal R_3^{(1)}(r|s|u)(d)
=usd r
=u\,\mathcal R_2(r|s)(d),
\]

and

\[
\mathcal R_3^{(2)}(r|s|u)(d)
=udsr
=ud\,m_2(r|s).
\]

After linear extension,

\[
\mathcal R_3^{(1)}(x|u)(d)
=u\mathcal R_2(x)(d)
=uL_{q,S}(d),
\]

\[
\mathcal R_3^{(2)}(x|u)(d)
=udm_2(x)
=udq.
\]

Finally,

\[
A_3(r|s|u)(d_1,d_2)
=ud_2sd_1r
=ud_2\mathcal R_2(r|s)(d_1),
\]

so

\[
A_3(x|u)(d_1,d_2)
=ud_2L_{q,S}(d_1).
\]

\(\square\)

### 3.2 Orientation of the residual channel

The residual tensor \(S\) enters the first internal response through

\[
-2uS(d),
\]

but does not enter the second response independently of \(q\):

\[
\mathcal R_3^{(2)}(x|u)(d)=udq.
\]

Thus right extension transports the length-two residual through the response channel adjacent to the original internal boundary.

This asymmetry is not a defect. It records the order-sensitive geometry of reversed quaternionic compression.

---

## 4. Left extension

Let

\[
E_L:V\times B_2\to B_3,
\qquad
E_L(u,x)=u|x.
\]

For a pure term \(r|s\) in \(x\),

\[
E_L(u,r|s)=u|r|s.
\]

### Theorem 4.1 — Exact left-propagation formulas

Let \(\Phi_2(x)=(q,S)\). Then for all \(u,d,d_1,d_2\in V\),

\[
\boxed{
m_3(u|x)=qu,
}
\]

\[
\boxed{
\mathcal R_3^{(1)}(u|x)(d)
=qdu,
}
\]

\[
\boxed{
\mathcal R_3^{(2)}(u|x)(d)
=L_{q,S}(d)u,
}
\]

and

\[
\boxed{
A_3(u|x)(d_1,d_2)
=
L_{q,S}(d_2)d_1u.
}
\]

### Proof

For a pure word \(u|r|s\),

\[
m_3(u|r|s)=sru=m_2(r|s)u.
\]

Hence

\[
m_3(u|x)=qu.
\]

The first internal response is

\[
\mathcal R_3^{(1)}(u|r|s)(d)
=srd u
=m_2(r|s)du,
\]

while the second is

\[
\mathcal R_3^{(2)}(u|r|s)(d)
=sdru
=\mathcal R_2(r|s)(d)u.
\]

Therefore

\[
\mathcal R_3^{(1)}(u|x)(d)=qdu,
\]

\[
\mathcal R_3^{(2)}(u|x)(d)=L_{q,S}(d)u.
\]

For the depth-two component,

\[
A_3(u|r|s)(d_1,d_2)
=sd_2rd_1u
=\mathcal R_2(r|s)(d_2)d_1u,
\]

and hence

\[
A_3(u|x)(d_1,d_2)
=L_{q,S}(d_2)d_1u.
\]

\(\square\)

### 4.2 Left-right mirror

Under right extension, the residual-bearing map \(L_{q,S}\) appears in \(\mathcal R_3^{(1)}\).

Under left extension, it appears in \(\mathcal R_3^{(2)}\).

Thus the two propagation laws are mirror images, but not identical:

\[
\begin{array}{c|c|c}
&\text{value-only internal channel}&\text{residual-bearing internal channel}\\
\hline
x|u&\mathcal R_3^{(2)}(d)=udq&\mathcal R_3^{(1)}(d)=uL_{q,S}(d)\\
u|x&\mathcal R_3^{(1)}(d)=qdu&\mathcal R_3^{(2)}(d)=L_{q,S}(d)u
\end{array}
\]

This is the first exact orientation-sensitive propagation law of the reconstructed core.

---

## 5. First closure verdict

The formulas above prove the following limited but exact result.

### Corollary 5.1 — One-step extension closure

For the products

\[
B_2\times B_1\to B_3
\]

and

\[
B_1\times B_2\to B_3,
\]

the data

\[
(q,S,u)
\]

determine:

- the compressed length-three value;
- both internal depth-one responses;
- the canonical internal-internal depth-two response.

No additional cross-boundary datum is required for these one-step extensions once the full exact length-two coordinate \((q,S)\) is retained.

This does **not** mean that length three contains no new residual sector.

It means that the new sector is generated deterministically from the full input state, rather than appearing as missing input data.

If the output is then compressed to an insufficient grade-three signature, that new sector can still be lost.

---

## 6. The depth-one grade-three signature

Define

\[
T_3
:=
m_3
\oplus
\mathcal R_3^{(1)}
\oplus
\mathcal R_3^{(2)}.
\]

Thus

\[
T_3:
B_3
\longrightarrow
\mathbb H
\oplus
\operatorname{Hom}(V,\mathbb H)
\oplus
\operatorname{Hom}(V,\mathbb H).
\]

The existing exact integer computation gives

\[
\operatorname{rank}T_3=20.
\]

Since

\[
\dim B_3=27,
\]

we have

\[
\dim\ker T_3=7.
\]

Representation theory identifies the full kernel as

\[
\boxed{
\ker T_3=S^3_0V.
}
\]

Equivalently, there is an exact sequence

\[
0
\longrightarrow
S^3_0V
\longrightarrow
B_3
\xrightarrow{\ T_3\ }
\operatorname{im}T_3
\longrightarrow
0,
\]

with dimensions

\[
27=7+20.
\]

Therefore compression together with every depth-one internal response still fails to determine a general length-three representative.

The missing information is exactly the highest-spin symmetric trace-free sector.

---

## 7. The new grade-three residual

The appearance of \(S^3_0V\) has a precise meaning.

At length two,

\[
\bigl(m_2,\mathcal R_2^{(1)}\bigr)
\]

is already injective.

At length three,

\[
\bigl(m_3,\mathcal R_3^{(1)},\mathcal R_3^{(2)}\bigr)
\]

is not injective.

A new residual sector has moved one level deeper:

\[
S^3_0V
\subseteq
\ker m_3
\cap
\ker\mathcal R_3^{(1)}
\cap
\ker\mathcal R_3^{(2)}.
\]

This sector may already occur in an extended tensor \(x|u\) or \(u|x\). The propagation formulas determine it implicitly because \((q,S,u)\) determines the full extended tensor.

However, if only \(T_3\) is retained after extension, the \(S^3_0V\) component is erased.

Thus the exact length-two pair

\[
(q,S)
\]

does not evolve into a fixed-format pair of the same type.

The grade-three state requires a deeper response tier.

This is the first proof that a standalone Free Numbers structure must be graded or hierarchical rather than a single fixed residual decoration of a quaternionic value.

---

## 8. Depth-two recovery

Define the canonical internal-internal depth-two component

\[
A_3:B_3\to\operatorname{Hom}(V^{\otimes2},\mathbb H)
\]

by

\[
A_3(e_a|e_b|e_c)(d_1,d_2)
=
e_cd_2e_bd_1e_a.
\]

For

\[
R\in S^3_0V,
\]

the established response theorem gives

\[
\boxed{
A_3(R)=4C_R,
}
\]

where

\[
C_R:V^{\otimes2}\to V
\]

is contraction by \(R\).

Since

\[
R\mapsto C_R
\]

is injective, the restriction

\[
A_3|_{S^3_0V}
\]

is injective.

Thus the sector invisible to all depth-one data becomes fully visible at the canonical depth-two component.

---

## 9. Finite complete length-three signature

Define

\[
\mathcal J_3^{\mathrm{exact}}
:
B_3
\longrightarrow
\mathbb H
\oplus
\operatorname{Hom}(V,\mathbb H)^{\oplus2}
\oplus
\operatorname{Hom}(V^{\otimes2},\mathbb H)
\]

by

\[
\boxed{
\mathcal J_3^{\mathrm{exact}}(t)
=
\bigl(
 m_3(t),
 \mathcal R_3^{(1)}(t),
 \mathcal R_3^{(2)}(t),
 A_3(t)
\bigr).
}
\]

### Theorem 9.1 — Exact finite observability at length three

\[
\boxed{
\mathcal J_3^{\mathrm{exact}}
\text{ is injective.}
}
\]

### Proof

Suppose

\[
\mathcal J_3^{\mathrm{exact}}(t)=0.
\]

Then

\[
T_3(t)=0,
\]

so

\[
t\in\ker T_3=S^3_0V.
\]

Also

\[
A_3(t)=0.
\]

But \(A_3\) is injective on \(S^3_0V\). Therefore

\[
t=0.
\]

Hence \(\mathcal J_3^{\mathrm{exact}}\) is injective. \(\square\)

This signature is finite and complete.

It is not claimed to be codomain-minimal. Its total codomain contains redundant coordinates, while the image has rank exactly

\[
27.
\]

The structural statement is the important one:

\[
\boxed{
\text{value + depth-one response + one canonical depth-two component determines }B_3.
}
\]

---

## 10. Exact propagation theorem

Combining Sections 3, 4, and 9 gives the main result of this note.

### Theorem 10.1 — Length-two to length-three exact propagation

Let

\[
\Phi_2(x)=(q,S).
\]

For every \(u\in V\), the complete finite signatures

\[
\mathcal J_3^{\mathrm{exact}}(x|u)
\]

and

\[
\mathcal J_3^{\mathrm{exact}}(u|x)
\]

are determined by \((q,S,u)\) through the explicit formulas

\[
L_{q,S}(d)
=
\langle\operatorname{Im}q,d\rangle
-\frac{\operatorname{Re}q}{3}d
-2S(d),
\]

followed by

\[
\begin{aligned}
m_3(x|u)&=uq,\\
\mathcal R_3^{(1)}(x|u)(d)&=uL_{q,S}(d),\\
\mathcal R_3^{(2)}(x|u)(d)&=udq,\\
A_3(x|u)(d_1,d_2)&=ud_2L_{q,S}(d_1),
\end{aligned}
\]

and

\[
\begin{aligned}
m_3(u|x)&=qu,\\
\mathcal R_3^{(1)}(u|x)(d)&=qdu,\\
\mathcal R_3^{(2)}(u|x)(d)&=L_{q,S}(d)u,\\
A_3(u|x)(d_1,d_2)&=L_{q,S}(d_2)d_1u.
\end{aligned}
\]

Therefore the exact length-two state propagates to a complete length-three observational state without loss.

Loss occurs only if the propagated state is subsequently compressed to a profile that omits the depth-two channel.

---

## 11. What closes and what does not

### Closed at this stage

The following are now exact:

1. the complete length-two coordinate
   \[
   B_2\cong\mathbb H\oplus S^2_0V;
   \]
2. the full internal length-two response \(L_{q,S}\);
3. right propagation \(B_2\times B_1\to B_3\);
4. left propagation \(B_1\times B_2\to B_3\);
5. finite complete observability of \(B_3\) through depth two.

### Not closed yet

The following remain open:

1. a minimal coordinate object replacing the redundant codomain of \(\mathcal J_3^{\mathrm{exact}}\);
2. an intrinsic multiplication law between arbitrary grade-three Free Number coordinates;
3. the product \(B_2\times B_2\to B_4\);
4. whether exact signatures compose by a uniform all-grade law;
5. how multiplicity-space depth splitting at length four enters the coordinate system.

---

## 12. Consequence for the abstract core

The length-two result could have suggested a fixed object of the form

\[
\mathbb H\oplus\text{one residual space}.
\]

Length three rules out that simplification.

The exact standalone structure must permit:

- a value sector;
- response sectors indexed by context depth and position;
- new residuals that are invisible at one depth but visible at a later depth;
- orientation-sensitive propagation;
- finite complete signatures at bounded grade when proved available.

Thus the current evidence supports a graded response object

\[
\mathbf F_n
\sim
\bigl(
\text{value},
\text{depth-1 profile},
\text{depth-2 profile},
\ldots
\bigr),
\]

with no assumption that every grade needs the same maximum depth or the same representation content.

The grade-two and grade-three facts are:

\[
\begin{array}{c|c|c}
\text{grade}&\text{first invisible residual}&\text{first detecting depth}\\
\hline
2&S^2_0V&1\\
3&S^3_0V&2
\end{array}
\]

This table records proved low-grade behavior, not an assumed universal diagonal rule.

---

## 13. Non-claims

This note does not claim:

1. that \(\mathcal J_3^{\mathrm{exact}}\) is a minimal signature;
2. that \(S^n_0V\) is the only residual sector at every length;
3. that all residual depth follows a simple diagonal pattern;
4. that the length-three signature already carries a completed associative multiplication;
5. that the quaternionic boundary-word model is the universal Free Numbers model;
6. that every full depth-two probe is determined by the single component \(A_3\);
7. that the current formulas settle \(B_2\times B_2\) or length four.

The proved statement is narrower and exact:

\[
\boxed{
(q,S,u)
\text{ determines complete one-step propagation through an injective length-three signature.}
}
\]

---

## 14. Next decision gate

The next nontrivial product is

\[
B_2\times B_2\to B_4.
\]

It asks whether two exact pairs

\[
(q,S),
\qquad
(p,T)
\]

determine a bounded complete length-four signature by a finite formula, and which genuinely new cross-boundary terms appear.

Length four is also where repeated spin multiplicities split across different probe depths. Therefore the next step cannot assume that representation type alone determines residual depth.

The next note should separate:

1. inherited left and right response data;
2. cross-boundary interaction of \(S\) and \(T\);
3. newly generated multiplicity coordinates;
4. the minimum depth required for complete observation.
