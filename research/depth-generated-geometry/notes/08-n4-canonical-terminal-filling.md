# Note 08 — \(n=4\) Canonical Terminal Filling

## compatible pair boundary の一意な \(SO(3)\)-equivariant completion

**Status:** theorem; all dimensions, Casimir projectors, restricted ranks, and the coefficient (-8) certified by exact rational arithmetic  
**Depends on:** Notes 02, 03, 05, 07; Free Numbers Core v1, Notes 06 and 11  
**Claim boundary:** this note proves a canonical terminal filling theorem relative to the distinguished \(SO(3)\)-action. It does not identify the terminal interior mode with curvature or physical force.

---

## 0. Main result

Note 07 constructs the compatible pair-boundary space

\[
\mathcal P_{4,2}=\ker\partial
\]

and the exact sequence

\[
0\longrightarrow S^4_0V
\longrightarrow V^{\otimes4}
\xrightarrow{\ \mathbf H\ }
\mathcal P_{4,2}
\longrightarrow0.
\tag{0.1}
\]

Thus every compatible response triangle has a filler, but (0.1) alone presents
its fillers as an affine space over \(S^4_0V\cong V_4\).

The distinguished \(SO(3)\)-action removes this ambiguity canonically. There is
a unique \(SO(3)\)-equivariant section

\[
\boxed{
s_{\mathrm{tf}}:\mathcal P_{4,2}\longrightarrow V^{\otimes4}
}
\]

of \(\mathbf H\). It is characterized by

\[
\boxed{
\mathbf Hs_{\mathrm{tf}}=\operatorname{id},
\qquad
P_4s_{\mathrm{tf}}=0,
}
\tag{0.2}
\]

where \(P_4\) is the Casimir spectral projector onto the unique top-spin
summand \(S^4_0V\cong V_4\).

Consequently every filler has the unique normal form

\[
\boxed{
T=s_{\mathrm{tf}}(p)+S,
\qquad
S\in S^4_0V.
}
\tag{0.3}
\]

On the intrinsic terminal-response side, every \(F\in\mathfrak Q_4\) has the
unique decomposition

\[
\boxed{
F=F_{\mathrm{tf}}(p)-8C_S,
\qquad
p\in\mathcal P_{4,2},\quad S\in S^4_0V.
}
\tag{0.4}
\]

The first term is forced by the compatible pair boundary. The second is the
entire boundary-invisible terminal birth.

---

## 1. The exact filling problem

Let

\[
\mathbf H=(H_{12},H_{13},H_{23}):
V^{\otimes4}\longrightarrow\mathcal B^{\oplus3}
\]

be the joint pair-response map of Note 07. That note proves

\[
\operatorname{im}\mathbf H=\mathcal P_{4,2},
\qquad
\ker\mathbf H=S^4_0V\cong V_4,
\]

with

\[
\dim\mathcal P_{4,2}=72,
\qquad
\dim S^4_0V=9.
\]

For \(p\in\mathcal P_{4,2}\), the fiber is therefore

\[
\mathbf H^{-1}(p)=T_0+S^4_0V.
\]

This proves existence of fillers and identifies their full ambiguity. It does
not yet choose one filler.

---

## 2. The explicit Casimir complement

Use the Casimir convention

\[
\Omega|_{V_j}=-j(j+1)\operatorname{id}.
\]

At length four,

\[
V^{\otimes4}
\cong
3V_0\oplus6V_1\oplus6V_2\oplus3V_3\oplus V_4.
\tag{2.1}
\]

The top spin occurs with multiplicity one. Its spectral projector is the
explicit polynomial

\[
\boxed{
P_4
=
\frac1{40320}
\prod_{j=0}^{3}
\bigl(\Omega+j(j+1)\operatorname{id}\bigr).
}
\tag{2.2}
\]

Indeed the numerator acts on \(V_4\) by

\[
(-20)(-18)(-14)(-8)=40320=8!,
\]

and vanishes on every \(V_j\) with \(0\le j\le3\).

Define

\[
W_{\le3}:=\ker P_4=\operatorname{im}(1-P_4).
\]

Then

\[
\boxed{
V^{\otimes4}=W_{\le3}\oplus S^4_0V,
}
\tag{2.3}
\]

and

\[
W_{\le3}
\cong
3V_0\oplus6V_1\oplus6V_2\oplus3V_3,
\qquad
\dim W_{\le3}=72.
\tag{2.4}
\]

This complement is not chosen by a basis or an arbitrary inner product. It is
fixed by the already distinguished \(SO(3)\)-action through the polynomial
(2.2).

---

## 3. Canonical Top-Spin-Free Filling Theorem

### Theorem 3.1

The restriction

\[
\boxed{
\mathbf H|_{W_{\le3}}:
W_{\le3}\xrightarrow{\ \cong\ }\mathcal P_{4,2}
}
\tag{3.1}
\]

is an \(SO(3)\)-equivariant isomorphism.

Hence

\[
\boxed{
s_{\mathrm{tf}}
:=
\left(\mathbf H|_{W_{\le3}}\right)^{-1}
}
\tag{3.2}
\]

is a canonical top-spin-free filler.

#### Proof

Note 07 identifies

\[
\ker\mathbf H=S^4_0V=\operatorname{im}P_4.
\]

Therefore

\[
W_{\le3}\cap\ker\mathbf H=0,
\]

so the restriction in (3.1) is injective. Both its source and target have
dimension 72, hence it is surjective. All maps are \(SO(3)\)-equivariant, since
the response maps use quaternion multiplication and the projector is a
polynomial in the Casimir. ∎

### Corollary 3.2 — projector construction of the filler

If \(T\) is any filler of \(p\), then

\[
\boxed{
s_{\mathrm{tf}}(p)=(1-P_4)T.
}
\tag{3.3}
\]

This is independent of the initial filler. Indeed, two fillers differ by an
element of \(\operatorname{im}P_4\), which \(1-P_4\) annihilates.

Thus the construction requires no arbitrary preliminary section.

---

## 4. Why the equivariant section is unique

The quotient has \(SO(3)\)-content

\[
\boxed{
\mathcal P_{4,2}
\cong
3V_0\oplus6V_1\oplus6V_2\oplus3V_3.
}
\tag{4.1}
\]

In particular it contains no \(V_4\). Therefore

\[
\boxed{
\operatorname{Hom}_{SO(3)}(\mathcal P_{4,2},V_4)=0.
}
\tag{4.2}
\]

Let \(s_1,s_2\) be two \(SO(3)\)-equivariant sections of \(\mathbf H\). Their
difference satisfies

\[
\mathbf H(s_1-s_2)=0,
\]

so it is an equivariant map

\[
s_1-s_2:\mathcal P_{4,2}\longrightarrow\ker\mathbf H\cong V_4.
\]

Equation (4.2) forces \(s_1-s_2=0\). Hence:

\[
\boxed{
\text{the \(SO(3)\)-equivariant section of \(\mathbf H\) exists and is unique.}
}
\tag{4.3}
\]

The multiplicities in the lower-spin sector do not create an ambiguity. The
difference of two sections must land in the kernel, and the kernel contains
only \(V_4\).

---

## 5. Intrinsic terminal-response form

Note 02 constructs the terminal exact-response space \(\mathfrak Q_4\) first
and proves the representation theorem

\[
A_4:V^{\otimes4}\xrightarrow{\ \cong\ }\mathfrak Q_4,
\qquad
\Psi_4=A_4^{-1}.
\]

Transport the pair-face map and the top-spin projector to the response side:

\[
\boxed{
\Phi:=\mathbf H\Psi_4:
\mathfrak Q_4\longrightarrow\mathcal P_{4,2},
}
\tag{5.1}
\]

Under the identifications

\[
\mathcal Q_{4,3}\cong\mathfrak Q_4,
\qquad
\mathcal Q_{4,2}\cong\mathcal P_{4,2},
\]

this is precisely the terminal forgetting map \(\pi_{4,3}\).

### 5.1 Direct terminal face formulas

The map \(\Phi\) has a local response-side formula that does not require a full
tensor reconstruction.  Apply only the last-variable decoder of Note 02:

\[
\mathcal D_4F=\sum_a e_a\otimes F_a,
\]

\[
\boxed{
F_a(x,y)
=
\frac12\sum_{b,c}\varepsilon_{abc}e_bF(x,y,e_c).
}
\tag{5.2}
\]

Define

\[
\boxed{
\begin{aligned}
(\rho_{12}F)(x,y)
&:=\sum_a e_aF(x,y,e_a),\\
(\rho_{13}F)(x,z)
&:=\sum_a e_az\left(\sum_b e_bF_a(x,e_b)\right),\\
(\rho_{23}F)(y,z)
&:=\sum_a F(e_a,y,z)e_a.
\end{aligned}
}
\tag{5.3}
\]

Then

\[
\boxed{
\Phi(F)
=
\bigl(\rho_{12}F,\rho_{13}F,\rho_{23}F\bigr).
}
\tag{5.4}
\]

For the pure terminal response

\[
F(x,y,z)=dzcybxa,
\]

the first and third identities follow directly from

\[
\sum_a e_aue_a=u
\qquad(u\in V).
\]

For the middle face, the decoder gives the length-three inner terminal
responses \(F_a\); contracting their second variable produces the inner
single-gap response, and multiplication by \(e_az\) re-encodes the removed
outer layer. Hence

\[
\rho_{12}F=H_{12},
\qquad
\rho_{13}F=H_{13},
\qquad
\rho_{23}F=H_{23}.
\]

Linearity proves the formulas for all \(F\in\mathfrak Q_4\). Thus all three
terminal-to-pair faces are now explicit; only the middle face requires one
local decode/re-encode step.

\[
\boxed{
\widehat P_4:=A_4P_4\Psi_4:
\mathfrak Q_4\longrightarrow\mathfrak Q_4.
}
\tag{5.5}
\]

The decoder \(\Psi_4\) is the finite local decoder recursion of Note 02, so
these are derived response operations rather than a new state-first
definition.

Equivalently, let \(\widehat\Omega\) be the Casimir of the natural \(SO(3)\)
action on

\[
\mathfrak Q_4\subset\operatorname{Hom}(V^{\otimes3},\mathbb H).
\]

Then the projector is already intrinsic to the response representation:

\[
\boxed{
\widehat P_4
=
\frac1{40320}
\prod_{j=0}^{3}
\bigl(\widehat\Omega+j(j+1)\operatorname{id}\bigr).
}
\tag{5.6}
\]

Let

\[
\mathfrak H_4:=A_4(S^4_0V)=\operatorname{im}\widehat P_4
\]

and

\[
\mathfrak Q_4^{\mathrm{tf}}:=\ker\widehat P_4.
\]

Then

\[
\boxed{
0\longrightarrow\mathfrak H_4
\longrightarrow\mathfrak Q_4
\xrightarrow{\ \Phi\ }
\mathcal P_{4,2}
\longrightarrow0
}
\tag{5.7}
\]

is exact, and

\[
\boxed{
\Phi|_{\mathfrak Q_4^{\mathrm{tf}}}:
\mathfrak Q_4^{\mathrm{tf}}
\xrightarrow{\ \cong\ }
\mathcal P_{4,2}.
}
\tag{5.8}
\]

Define

\[
\boxed{
s_{\mathrm{tf}}^{\mathrm{resp}}
:=
A_4s_{\mathrm{tf}}
=
\left(\Phi|_{\mathfrak Q_4^{\mathrm{tf}}}\right)^{-1}.
}
\tag{5.9}
\]

This gives the canonical response-side splitting

\[
\boxed{
\mathfrak Q_4
=
s_{\mathrm{tf}}^{\mathrm{resp}}(\mathcal P_{4,2})
\oplus
\mathfrak H_4.
}
\tag{5.10}
\]

---

## 6. The terminal coefficient and the normal form

For \(S\in S^4_0V\), the all-length vertical-response theorem gives

\[
\boxed{
A_4(S)=(-2)^3C_S=-8C_S.
}
\tag{6.1}
\]

Therefore every terminal response with pair boundary \(p\) has a unique form

\[
\boxed{
F
=
s_{\mathrm{tf}}^{\mathrm{resp}}(p)
-8C_S,
\qquad
S\in S^4_0V.
}
\tag{6.2}
\]

Equivalently,

\[
\underbrace{F_{\mathrm{tf}}(p)}_{\text{boundary-determined}}
+
\underbrace{(-8C_S)}_{\text{boundary-invisible terminal birth}}.
\]

The coefficient \(-8\) is not chosen to normalize the splitting. It is the
depth principal symbol produced by the three successive quaternionic collapse
steps.

---

## 7. The four descriptions of the terminal interior

At \(n=4\), four independently defined objects are canonically identified:

\[
\boxed{
\begin{aligned}
S^4_0V\cong V_4
&\quad\text{(highest-spin representation)},\\
\ker\mathbf H
&\quad\text{(invisible to all pair boundaries)},\\
K_{4,3}^{\mathrm{birth}}
&\quad\text{(born at the terminal depth)},\\
\mathfrak H_4=A_4(S^4_0V)
&\quad\text{(terminal interior response)}.
\end{aligned}
}
\tag{7.1}
\]

These are not literally the same subset of one ambient space. They are the
same nine-dimensional \(SO(3)\)-module under the canonical maps already present
in the response tower.

Thus the precise content of the often abbreviated equality is

\[
\boxed{
\text{highest spin}
\simeq
\text{pair-boundary kernel}
\simeq
\text{terminal birth}
\simeq
\text{pure terminal interior}.
}
\tag{7.2}
\]

This is stronger than the dimension identity \(81=72+9\). It identifies the
meaning of both summands and makes the decomposition canonical relative to the
distinguished symmetry.

---

## 8. All-length reduction

The filling argument has a clean conditional all-length form.

### Proposition 8.1

Fix \(n\ge2\). Suppose the terminal last-survivor equality holds:

\[
\widehat F_{n-2}^{(n)}=A_n(S^n_0V)\cong V_n.
\tag{8.1}
\]

Then the terminal forgetting map

\[
\pi_{n,n-1}:\mathcal Q_{n,n-1}\longrightarrow\mathcal Q_{n,n-2}
\]

has a unique \(SO(3)\)-equivariant section. Every terminal response decomposes
uniquely into

\[
\boxed{
\text{canonical top-spin-free completion}
+
(-2)^{n-1}C_S,
\qquad S\in S^n_0V.
}
\tag{8.2}
\]

#### Proof

The top spin \(V_n\) occurs in \(V^{\otimes n}\) with multiplicity one. Under
(8.1), it is exactly the kernel of terminal forgetting. The Casimir spectral
projector onto \(V_n\) supplies an invariant complement. The quotient contains
no \(V_n\), so the difference of two equivariant sections is zero. The
coefficient in (8.2) is the all-length vertical-response theorem. ∎

For \(n=2,3,4\), hypothesis (8.1) has been exact-checked. For general \(n\), it
remains the full-profile last-survivor conjecture. Consequently the next
all-length problem is sharper than a generic search for fillers:

\[
\boxed{
\widehat F_{n-2}^{(n)}\stackrel{?}{=}A_n(S^n_0V).
}
\tag{8.3}
\]

If (8.3) is proved, canonical terminal filling follows formally.

---

## 9. What is closed and what remains open

### Closed at \(n=4\)

- every compatible pair-response triangle has terminal fillers;
- the ambiguity is exactly the top-spin \(V_4\);
- the Casimir complement gives a canonical top-spin-free filler;
- the \(SO(3)\)-equivariant section is unique;
- the remaining terminal freedom is detected as \(-8C_S\).

Thus the existence and abstract uniqueness part of the \(n=4,d=3\) filling law
is no longer open.

### Still open

- write \(s_{\mathrm{tf}}^{\mathrm{resp}}\) as a short direct response-side
  local formula, rather than an inverse on the Casimir complement;
- prove or disprove the all-length last-survivor equality (8.3);
- define transport between response charts;
- compare two reconstruction paths with common endpoints;
- determine whether the resulting residual lands naturally in an interior
  birth sector and satisfies a nontrivial flatness or curvature theorem.

In particular,

\[
\boxed{
\text{terminal interior mode}\ne\text{curvature}
}

at the present stage. A path-comparison theorem is still required.

---

## 10. Exact certificate

Run

```bash
python3 certificates/n4_canonical_filling_certificate.py
```

from `research/depth-generated-geometry/`.

The certificate uses only Python's standard library and exact
`fractions.Fraction` arithmetic. It verifies:

- the full spin multiplicities of \(V^{\otimes4}\);
- the normalized Casimir projector onto \(V_4\);
- the complementary 72-dimensional top-spin-free projector;
- the three direct terminal-to-pair face formulas, including the one-layer
  decoded middle face;
- equality of the pair-chart kernel with the projected \(V_4\);
- rank 72 of the pair map on the top-spin-free complement;
- the \(72+9\) terminal-response decomposition;
- the signed terminal coefficient \(A_4=-8C\) on \(V_4\).

Expected final line:

```text
ALL CHECKS PASSED
```
