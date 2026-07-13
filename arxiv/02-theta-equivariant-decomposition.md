# Gate A — equivariant decomposition of the local decoder

Status: proved working note for the arXiv manuscript.

## 1. The local map

Let

\[
V=\operatorname{Im}\mathbb H,
\qquad
\Theta:V\otimes\mathbb H\longrightarrow\operatorname{Hom}(V,\mathbb H),
\]

with

\[
\Theta\!\left(\sum_{a=1}^3 e_a\otimes h_a\right)(d)
=
\sum_{a=1}^3 e_a d h_a.
\]

The action of a unit quaternion \(q\) on \(V\) and \(\mathbb H\) is conjugation,

\[
x\longmapsto qxq^{-1}.
\]

With the induced action on \(V\otimes\mathbb H\) and

\[
(q\cdot F)(d)=qF(q^{-1}dq)q^{-1},
\]

\(\Theta\) is equivariant. Thus its structure can be read on the irreducible \(SO(3)\)-summands.

## 2. Domain and codomain decomposition

As real \(SO(3)\)-modules,

\[
\mathbb H\cong \mathbb R\oplus V,
\]

and therefore

\[
V\otimes\mathbb H
\cong
V\oplus(V\otimes V)
\cong
V_1\oplus(V_0\oplus V_1\oplus V_2).
\]

Hence

\[
V\otimes\mathbb H
\cong
V_0\oplus 2V_1\oplus V_2.
\]

Using \(V^*\cong V\), the same decomposition holds for

\[
\operatorname{Hom}(V,\mathbb H)
\cong
V^*\otimes\mathbb H.
\]

The multiplicity-one sectors are \(V_0\) and \(V_2\); the spin-one sector has multiplicity two.

## 3. Coordinate decomposition

Write

\[
h_a=\alpha_a+u_a,
\]

with \(\alpha_a\in\mathbb R\) and \(u_a\in V\). Set

\[
\alpha=\sum_a\alpha_a e_a,
\qquad
Ue_a=u_a.
\]

Decompose \(U\in\operatorname{End}(V)\) as

\[
U=tI+A_p+S,
\]

where

- \(t=\tfrac13\operatorname{tr}U\);
- \(A_p(d)=p\times d\) is skew;
- \(S\in S^2_0V\) is symmetric trace-free.

For \(d\in V\), write

\[
\Theta(\alpha,U)(d)=\sigma(d)+W(d),
\]

with scalar part \(\sigma(d)\in\mathbb R\) and vector part \(W(d)\in V\). Quaternion multiplication gives

\[
\boxed{
\sigma(d)=(-\alpha+2p)\cdot d,
}
\]

and

\[
\boxed{
W(d)=\alpha\times d+t\,d-2S(d).
}
\]

Thus the four irreducible pieces transform independently as follows.

### Scalar sector \(V_0\)

\[
t\longmapsto t.
\]

The scalar block has multiplier \(1\).

### Symmetric trace-free sector \(V_2\)

\[
S\longmapsto -2S.
\]

The spin-two block has multiplier \(-2\) on a five-dimensional space.

### Two spin-one sectors \(2V_1\)

Identify the codomain spin-one copies by

- the scalar functional \(d\mapsto \beta\cdot d\);
- the skew vector map \(d\mapsto r\times d\).

Then

\[
\begin{pmatrix}
\beta\\
r
\end{pmatrix}
=
\begin{pmatrix}
-1&2\\
1&0
\end{pmatrix}
\begin{pmatrix}
\alpha\\
p
\end{pmatrix}.
\]

The multiplicity-space matrix has determinant \(-2\).

## 4. Determinant factorization

The determinant of \(\Theta\) in the standard real bases factors by irreducible sectors:

\[
\det\Theta
=
(1)^1
\bigl(\det\begin{pmatrix}-1&2\\1&0\end{pmatrix}\bigr)^3
(-2)^5.
\]

Therefore

\[
\boxed{
\det\Theta
=
1\cdot(-2)^3\cdot(-2)^5
=256.
}
\]

This explains the previously computed determinant structurally. The number \(256\) is not an unexplained output of a twelve-by-twelve calculation: it is the product of one scalar block, three identical spin-one multiplicity blocks, and one five-dimensional spin-two block.

## 5. Explicit inverse in decomposed coordinates

Given the codomain data \((\beta,r,t,S')\), where

\[
\sigma(d)=\beta\cdot d,
\qquad
W(d)=r\times d+t\,d+S'(d),
\]

with \(S'\) symmetric trace-free, the inverse is

\[
\boxed{
\alpha=r,
\qquad
p=\frac{\beta+r}{2},
\qquad
t=t,
\qquad
S=-\frac12S'.
}
\]

Thus every irreducible block is explicitly invertible. This is equivalent to the coordinate formula

\[
h_a
=
\frac12\sum_{b,c=1}^3
\varepsilon_{abc}\,e_bF(e_c),
\]

but the equivariant decomposition shows why the inverse exists and where every numerical factor comes from.

## 6. Novelty boundary

The standard module decomposition

\[
V\otimes V\cong V_0\oplus V_1\oplus V_2
\]

is not a new claim. Nor should the existence of some abstract vector-space isomorphism between two twelve-dimensional spaces be presented as novel.

The model-specific content is stronger:

1. the multiplication-defined map \(\Theta(v\otimes h)(d)=vdh\) is equivariant;
2. every irreducible block is nonzero, with explicit factors \(1\), \(-2\), and the spin-one matrix \(\bigl[\begin{smallmatrix}-1&2\\1&0\end{smallmatrix}\bigr]\);
3. this exact inverse is reused unchanged at every tensor grade;
4. the repeated local inversion peels one boundary layer at a time and yields all-grade reconstruction.

The arXiv manuscript should therefore not sell \(\det\Theta=256\) as an isolated numerical curiosity. It should present the determinant as the finite local certificate whose equivariant block structure drives the global peeling theorem.

## 7. Reviewer-facing summary

> The local decoder is not invertible merely because its source and target both have dimension twelve. Under the natural \(SO(3)\)-action it decomposes as \(V_0\oplus2V_1\oplus V_2\), with block factors \(1\), \(\bigl[\begin{smallmatrix}-1&2\\1&0\end{smallmatrix}\bigr]\), and \(-2\). Hence every irreducible sector is detected, \(\det\Theta=256\), and the same explicit inverse can be iterated at every finite grade.
