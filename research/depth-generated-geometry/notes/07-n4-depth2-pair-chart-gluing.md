# Note 07 — \(n=4\) Depth-Two Pair-Chart Gluing

## 40次元 birth layer の局在分解と response triangle

**Status:** boundary identities proved directly; completeness, exactness, dimensions, and \(SO(3)\)-types certified by exact rational arithmetic  
**Depends on:** Notes 03, 05, 06; Free Numbers Core v1, Note 11  
**Claim boundary:** this note proves a response-gluing theorem. It does not identify the gluing obstruction or the 40-dimensional birth layer with gauge curvature.

---

## 0. Main result

Let

\[
E:=\operatorname{Hom}_{\mathbb R}(V,\mathbb H),
\qquad
\mathcal B:=\operatorname{Hom}_{\mathbb R}(V^{\otimes2},\mathbb H).
\]

Thus \(\dim E=12\) and \(\dim\mathcal B=36\).

At length four there are three depth-two components,

\[
H_{12},\ H_{13},\ H_{23}\in\mathcal B.
\]

There are canonical boundary maps

\[
\pi_{12}^{1},\pi_{12}^{2},
\pi_{13}^{1},\pi_{13}^{3},
\pi_{23}^{2},\pi_{23}^{3}:
\mathcal B\longrightarrow E
\]

such that a triple \((H_{12},H_{13},H_{23})\) is realizable if and only if

\[
\boxed{
\pi_{12}^{1}H_{12}=\pi_{13}^{1}H_{13},
}
\]

\[
\boxed{
\pi_{12}^{2}H_{12}=\pi_{23}^{2}H_{23},
}
\]

\[
\boxed{
\pi_{13}^{3}H_{13}=\pi_{23}^{3}H_{23}.
}
\]

The resulting compatibility operator

\[
\partial:\mathcal B^{\oplus3}\longrightarrow E^{\oplus3}
\]

has rank 36. Its kernel is exactly the 72-dimensional depth-two response space. More precisely, there is an exact sequence

\[
\boxed{
0\longrightarrow S^4_0V
\longrightarrow V^{\otimes4}
\xrightarrow{\ \mathbf H\ }
\mathcal B^{\oplus3}
\xrightarrow{\ \partial\ }
E^{\oplus3}
\longrightarrow0.
}
\]

The 40-dimensional layer first visible at depth two is not the space of matching equations. After all depth-one data are fixed to zero, it splits canonically by pair origin:

\[
\boxed{
K_{4,2}^{\mathrm{birth}}
\cong
\mathcal A_{12}\oplus\mathcal A_{13}\oplus\mathcal A_{23},
}
\]

with

\[
\dim(\mathcal A_{12},\mathcal A_{13},\mathcal A_{23})=(12,16,12),
\]

and

\[
\boxed{
\mathcal A_{12}\cong V_2\oplus V_3,
}
\]

\[
\boxed{
\mathcal A_{13}\cong V_0\oplus V_1\oplus V_2\oplus V_3,
}
\]

\[
\boxed{
\mathcal A_{23}\cong V_2\oplus V_3.
}
\]

Hence

\[
12+16+12=40
\]

and

\[
K_{4,2}^{\mathrm{birth}}
\cong
V_0\oplus V_1\oplus3V_2\oplus3V_3.
\]

---

## 1. The three pair charts

For a pure word

\[
T=a|b|c|d\in V^{\otimes4},
\]

reversed compression gives

\[
q=dcba.
\]

The three depth-one responses are

\[
F_1(x)=dcbxa,
\]

\[
F_2(y)=dcyba,
\]

\[
F_3(z)=dzcba.
\]

The three depth-two responses are

\[
\boxed{
H_{12}(x,y)=dcybxa,
}
\]

\[
\boxed{
H_{13}(x,z)=dzcbxa,
}
\]

\[
\boxed{
H_{23}(y,z)=dzcyba.
}
\]

Each individual map

\[
V^{\otimes4}\longrightarrow\mathcal B,
\qquad
T\longmapsto H_{rs}(T),
\]

is onto. Thus an isolated pair chart is an arbitrary element of the full 36-dimensional space \(\mathcal B\). Structure appears only when two or more pair charts are required to come from the same length-four state.

---

## 2. Two one-variable decoders

Fix an oriented orthonormal basis \((e_1,e_2,e_3)\) of \(V\).

Define

\[
\Theta_L:V\otimes\mathbb H\longrightarrow E,
\qquad
\Theta_L\!\left(\sum_a e_a\otimes h_a\right)(x)
=\sum_a e_axh_a,
\]

and its right-handed mirror

\[
\Theta_R:\mathbb H\otimes V\longrightarrow E,
\qquad
\Theta_R\!\left(\sum_a h_a\otimes e_a\right)(x)
=\sum_a h_axe_a.
\]

Both are real-linear isomorphisms. The left decoder is the decoder used in Note 02. The right decoder follows from it by quaternionic conjugation. Explicitly,

\[
\Theta_L^{-1}(F)
=\sum_a e_a\otimes
\left(
\frac12\sum_{b,c}\varepsilon_{abc}e_bF(e_c)
\right),
\]

and

\[
\Theta_R^{-1}(F)
=\sum_a
\left(
-\frac12\sum_{b,c}\varepsilon_{abc}F(e_c)e_b
\right)\otimes e_a.
\]

These fixed local decoders allow a missing single-gap response to be recovered from a two-gap chart without referring back to a tensor representative.

---

## 3. The six boundary maps

### 3.1 The chart \(H_{12}\)

For fixed \(y\), right-decode the map \(x\mapsto H(x,y)\):

\[
\Theta_R^{-1}(H(-,y))
=\sum_a h_a(y)\otimes e_a.
\]

Define

\[
\boxed{
(\pi_{12}^{1}H)(x)
:=
\sum_a
\left(\sum_bh_a(e_b)e_b\right)xe_a,
}
\]

and

\[
\boxed{
(\pi_{12}^{2}H)(y)
:=
\sum_bH(e_b,y)e_b.
}
\]

For the actual chart \(H_{12}(x,y)=dcybxa\), direct quaternionic contraction gives

\[
\pi_{12}^{1}H_{12}=F_1,
\qquad
\pi_{12}^{2}H_{12}=F_2.
\]

### 3.2 The chart \(H_{13}\)

Define the two outer contractions

\[
\boxed{
(\pi_{13}^{1}H)(x)
:=
\sum_b e_bH(x,e_b),
}
\]

\[
\boxed{
(\pi_{13}^{3}H)(z)
:=
\sum_bH(e_b,z)e_b.
}
\]

Then

\[
\pi_{13}^{1}H_{13}=F_1,
\qquad
\pi_{13}^{3}H_{13}=F_3.
\]

### 3.3 The chart \(H_{23}\)

For fixed \(y\), left-decode the map \(z\mapsto H(y,z)\):

\[
\Theta_L^{-1}(H(y,-))
=\sum_a e_a\otimes k_a(y).
\]

Define

\[
\boxed{
(\pi_{23}^{2}H)(y)
:=
\sum_b e_bH(y,e_b),
}
\]

and

\[
\boxed{
(\pi_{23}^{3}H)(z)
:=
\sum_a e_az
\left(\sum_be_bk_a(e_b)\right).
}
\]

Then

\[
\pi_{23}^{2}H_{23}=F_2,
\qquad
\pi_{23}^{3}H_{23}=F_3.
\]

All six identities are identities of linear maps, so the pure-word calculation extends to every element of \(V^{\otimes4}\).

---

## 4. The corner identity

Recall

\[
r(F):=\sum_aF(e_a)e_a,
\qquad
\ell(F):=\sum_ae_aF(e_a).
\]

For every arbitrary \(H\in\mathcal B\), not merely an actual response, the central chart satisfies

\[
\boxed{
r(\pi_{13}^{1}H)=\ell(\pi_{13}^{3}H).
}
\]

Indeed, both sides equal

\[
\sum_{a,b}e_bH(e_a,e_b)e_a.
\]

Thus the two outer boundaries extracted from \(H_{13}\) automatically possess one common quaternionic value.

This four-dimensional identity explains why

\[
\operatorname{rank}
(\pi_{13}^{1}\oplus\pi_{13}^{3})
=20
\]

rather than 24.

---

## 5. Direct pair-chart presentation

Define

\[
\partial(H_{12},H_{13},H_{23})
:=
\begin{pmatrix}
\pi_{12}^{1}H_{12}-\pi_{13}^{1}H_{13}\\
\pi_{12}^{2}H_{12}-\pi_{23}^{2}H_{23}\\
\pi_{13}^{3}H_{13}-\pi_{23}^{3}H_{23}
\end{pmatrix}
\in E^{\oplus3}.
\]

Let

\[
\mathcal P_{4,2}:=\ker\partial\subset\mathcal B^{\oplus3}.
\]

### Theorem 5.1 — pair-chart gluing

The actual depth-two pair-response map

\[
\mathbf H:V^{\otimes4}\longrightarrow\mathcal B^{\oplus3},
\qquad
T\longmapsto(H_{12}(T),H_{13}(T),H_{23}(T))
\]

satisfies

\[
\boxed{
\operatorname{im}\mathbf H=\mathcal P_{4,2}.
}
\]

Moreover,

\[
\operatorname{rank}\partial=36,
\qquad
\dim\mathcal P_{4,2}=108-36=72,
\]

and

\[
\ker\mathbf H=S^4_0V\cong V_4.
\]

#### Proof

The six factorization identities in Section 3 give

\[
\partial\mathbf H=0,
\]

so \(\operatorname{im}\mathbf H\subseteq\ker\partial\).

Exact rational elimination gives

\[
\operatorname{rank}\partial=36
\]

and

\[
\operatorname{rank}\mathbf H=72.
\]

Therefore both \(\operatorname{im}\mathbf H\) and \(\ker\partial\) have dimension 72, proving equality.

The kernel of \(\mathbf H\) has dimension \(81-72=9\). Exact \(SO(3)\) Casimir projection identifies it as the unique \(V_4=S^4_0V\) summand. ∎

### Corollary 5.2 — exact response sequence

Since \(\partial\) has full target rank, Theorem 5.1 gives

\[
\boxed{
0\longrightarrow S^4_0V
\longrightarrow V^{\otimes4}
\xrightarrow{\mathbf H}
\mathcal B^{\oplus3}
\xrightarrow{\partial}
E^{\oplus3}
\longrightarrow0.
}
\]

This is an exact response-gluing complex, not merely a dimension coincidence.

### Corollary 5.3 — lower-depth data are redundant at depth two

Given a compatible triple, define the common boundaries

\[
F_1:=\pi_{12}^{1}H_{12}=\pi_{13}^{1}H_{13},
\]

\[
F_2:=\pi_{12}^{2}H_{12}=\pi_{23}^{2}H_{23},
\]

\[
F_3:=\pi_{13}^{3}H_{13}=\pi_{23}^{3}H_{23}.
\]

The corner identity gives

\[
q:=r(F_1)=\ell(F_3).
\]

Thus the projection from the full depth-two profile to its three exact-depth-two components is an isomorphism:

\[
\boxed{
\mathcal Q_{4,2}\cong\mathcal P_{4,2}.
}
\]

---

## 6. The overlap pattern

Let \(R_{12},R_{13},R_{23}\subset(V^{\otimes4})^*\otimes\mathbb H\) denote the row spaces of the three pair-response maps. Exact elimination gives

\[
\boxed{
R_{12}\cap R_{13}=\operatorname{row}(F_1),
\qquad \dim=12,
}
\]

\[
\boxed{
R_{12}\cap R_{23}=\operatorname{row}(q,F_2),
\qquad \dim=16,
}
\]

\[
\boxed{
R_{13}\cap R_{23}=\operatorname{row}(F_3),
\qquad \dim=12,
}
\]

and

\[
\boxed{
R_{12}\cap R_{13}\cap R_{23}=\operatorname{row}(q),
\qquad \dim=4.
}
\]

Accordingly,

\[
3\cdot36-(12+16+12)+4=72.
\]

The middle overlap contains \((q,F_2)\), rather than \(F_2\) alone, because the middle depth-one chart does not determine the depth-zero value. By contrast, \(F_1\) and \(F_3\) already carry \(q\) through \(r(F_1)\) and \(\ell(F_3)\).

This is a precise augmented-Čech pattern for the three internal gaps:

- singleton gap data: \(F_1,F_2,F_3\);
- pair-gap charts: \(H_{12},H_{13},H_{23}\);
- common augmentation: \(q\).

The statement concerns the incidence structure of response data. It does not yet identify this response nerve with physical space.

---

## 7. The 40-dimensional birth layer

Let

\[
K_1:=\ker D_4^{\le1},
\qquad
K_2:=\ker D_4^{\le2}=S^4_0V.
\]

Then

\[
\dim K_1=49,
\qquad
\dim K_2=9,
\]

and

\[
K_{4,2}^{\mathrm{birth}}\cong K_1/K_2.
\]

Define the zero-boundary part of each pair chart by

\[
\mathcal A_{12}
:=
\ker(\pi_{12}^{1}\oplus\pi_{12}^{2}),
\]

\[
\mathcal A_{13}
:=
\ker(\pi_{13}^{1}\oplus\pi_{13}^{3}),
\]

\[
\mathcal A_{23}
:=
\ker(\pi_{23}^{2}\oplus\pi_{23}^{3}).
\]

Their dimensions are

\[
\dim\mathcal A_{12}=36-24=12,
\]

\[
\dim\mathcal A_{13}=36-20=16,
\]

\[
\dim\mathcal A_{23}=36-24=12.
\]

The central 16 arises because its two extracted outer boundaries satisfy the four-dimensional corner identity.

### Theorem 7.1 — canonical pair-origin splitting

The three pair responses induce an isomorphism

\[
\boxed{
K_1/K_2
\xrightarrow{\ \cong\ }
\mathcal A_{12}\oplus\mathcal A_{13}\oplus\mathcal A_{23}.
}
\]

#### Proof

If \(T\in K_1\), then \(F_1=F_2=F_3=0\). The factorization identities imply

\[
H_{12}(T)\in\mathcal A_{12},
\quad
H_{13}(T)\in\mathcal A_{13},
\quad
H_{23}(T)\in\mathcal A_{23}.
\]

The kernel of the resulting map from \(K_1\) is precisely \(K_2\). Hence it induces an injection from \(K_1/K_2\). Both source and target have dimension

\[
49-9=12+16+12=40.
\]

Therefore the induced map is an isomorphism. Exact rank computation independently confirms that the joint restricted rank is the sum of the three marginal restricted ranks. ∎

### Theorem 7.2 — spin content by pair origin

Exact Casimir projection gives

\[
\boxed{
\mathcal A_{12}\cong V_2\oplus V_3,
}
\]

\[
\boxed{
\mathcal A_{13}\cong V_0\oplus V_1\oplus V_2\oplus V_3,
}
\]

\[
\boxed{
\mathcal A_{23}\cong V_2\oplus V_3.
}

Thus the known spin decomposition

\[
K_{4,2}^{\mathrm{birth}}
\cong
V_0\oplus V_1\oplus3V_2\oplus3V_3
\]

has acquired a canonical gap-pair origin.

---

## 8. What the 40 dimensions are — and are not

The calculation separates two objects that were previously easy to conflate.

### Matching structure

The operator

\[
\partial:\mathcal B^3\to E^3
\]

measures whether three arbitrary pair charts possess the same singleton-gap boundaries. This is genuine cross-chart matching data.

### Birth freedom

The 40-dimensional birth layer is what remains inside the three pair charts after all singleton-gap boundaries have already been fixed. It is

\[
\mathcal A_{12}\oplus\mathcal A_{13}\oplus\mathcal A_{23},
\]

and the three factors are independent.

Therefore

\[
\boxed{
\text{depth-two compatibility}\ne
\text{depth-two birth layer}.
}
\]

The first is a 36-dimensional system of matching equations in the 108-dimensional ambient pair-chart space. The second is a 40-dimensional fiber over fixed depth-one data inside the 72-dimensional realizable space.

---

## 9. Curvature status

Define the matching defect of an arbitrary triple by

\[
\Omega_{\mathrm{match}}
:=\partial(H_{12},H_{13},H_{23}).
\]

This is an obstruction to realizability. For every actual response profile,

\[
\Omega_{\mathrm{match}}=0.
\]

Moreover,

\[
\operatorname{im}\mathbf H=\ker\partial,
\]

so the response complex is exact at \(\mathcal B^3\). There is no nonzero gluing cohomology at this stage.

Consequently, neither \(\Omega_{\mathrm{match}}\) nor the 40-dimensional birth layer should yet be called gauge curvature. A curvature theorem still requires a transport composition, two paths with common endpoints, and a nontrivial path-comparison or holonomy class.

What is now proved is narrower and cleaner:

> depth two produces a canonical triangle of pair charts, explicit boundary maps to depth-one charts, and an exact matching complex.

This is stronger evidence for a depth-indexed response geometry, while remaining distinct from a physical curvature claim.

---

## 10. Exact certificate

Run

```bash
python3 certificates/n4_depth2_structure_certificate.py
```

from `research/depth-generated-geometry/`.

The certificate uses only Python's standard library and exact `fractions.Fraction` arithmetic. It verifies:

- surjectivity of each 36-dimensional pair chart;
- all six boundary factorizations;
- the corner identity;
- rank 36 of the matching operator;
- rank 72 of the actual pair-chart map;
- equality of the actual image and the intrinsic matching kernel;
- the exact kernel \(V_4\);
- the \(12+16+12\) birth splitting;
- independence of the three birth factors;
- the spin type of every factor.

Expected final line:

```text
ALL CHECKS PASSED
```

---

## 11. Terminal filling status

The internal gap set for \(n=4\) is \(\{1,2,3\}\). Exact-depth responses are indexed by its subsets:

- depth zero: the augmented value \(q\);
- depth one: singleton charts \(F_i\);
- depth two: pair charts \(H_{ij}\);
- depth three: the full chart \(H_{123}=A_4\).

Note 07 proves the face maps and exact matching law from pair charts to singleton charts. The terminal all-gap response supplies fillers because

\[
0\longrightarrow S^4_0V
\longrightarrow V^{\otimes4}
\xrightarrow{\ \mathbf H\ }
\mathcal P_{4,2}
\longrightarrow0
\]

is exact. Note 08 strengthens this observation: the Casimir complement to the
last-surviving

\[
S^4_0V\cong V_4
\]

gives the unique \(SO(3)\)-equivariant top-spin-free filler, while the remaining
terminal freedom is detected with coefficient

\[
(-2)^3=-8.
\]

Thus the existence and abstract uniqueness of the terminal filling law are
closed. What remains is a short direct response-side formula for that filler.
Relating its interior mode to curvature or force still requires an additional
transport and path-comparison theorem.
