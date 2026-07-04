# Free Numbers: Depth-One Detection in Length Three

Let $V=\operatorname{Im}\mathbb H$ be the space of imaginary quaternions, with
basis $i,j,k$. For length three, the boundary-word space is

$$
B_3 = V\otimes V\otimes V.
$$

The reversed compression map

$$
m_3(a\mid b\mid c)=cba
$$

has a large kernel. The vertical-response theorem detects the top-spin part
$S^3_0V\cong V_3$ of this kernel at depth two. This note records what happens one
depth earlier: the depth-one insertion profile detects exactly the remaining,
non-top-spin part of the kernel.

The main statement is

$$
K_3\cap \ker D_3 = S^3_0V,
$$

where $K_3=\ker m_3$ and $D_3$ is the full depth-one profile.

Thus, in length three, the residual kernel is completely detected by depths one
and two:

$$
\begin{aligned}
\text{depth }1 &\text{ detects } 2V_1\oplus 2V_2,\\
\text{depth }2 &\text{ detects } V_3.
\end{aligned}
$$

## 1. Compression in length three

Let

$$
V=\operatorname{Im}\mathbb H=\operatorname{span}_{\mathbb R}\{i,j,k\},
$$

with quaternion multiplication on imaginary elements

$$
uv=-(u\cdot v)+(u\times v).
$$

The length-three boundary-word space is

$$
B_3=V^{\otimes 3},
$$

with basis words written

$$
a\mid b\mid c.
$$

The reversed compression map is

$$
m_3:B_3\to \mathbb H,\qquad m_3(a\mid b\mid c)=cba.
$$

Let

$$
K_3=\ker m_3.
$$

The map $m_3$ is $SO(3)$-equivariant and surjective onto

$$
\mathbb H\cong V_0\oplus V_1.
$$

For example, it has nonzero scalar and imaginary outputs:

$$
m_3(i\mid j\mid k)=kji=1,
$$

and

$$
m_3(i\mid i\mid i)=iii=-i.
$$

Hence

$$
\operatorname{rank} m_3=4,\qquad \dim K_3=27-4=23.
$$

## 2. The representation decomposition

The standard Clebsch-Gordan decomposition gives

$$
V_1\otimes V_1 = V_0\oplus V_1\oplus V_2.
$$

Therefore

$$
\begin{aligned}
V^{\otimes 3}
  &= (V_1\otimes V_1)\otimes V_1\\
  &= (V_0\oplus V_1\oplus V_2)\otimes V_1\\
  &= V_0\oplus 3V_1\oplus 2V_2\oplus V_3.
\end{aligned}
$$

Since $m_3$ is $SO(3)$-equivariant, Schur's lemma separates the calculation by
isotypic component. The target contains only $V_0$ and $V_1$, so the $V_2$ and
$V_3$ source components lie in the kernel. The scalar example

$$
m_3(i\mid j\mid k)=1
$$

shows that the unique source copy of $V_0$ maps nontrivially to the target $V_0$,
hence is not in the kernel. The imaginary example

$$
m_3(i\mid i\mid i)=-i
$$

shows that the map from the $3V_1$ isotypic component to the target $V_1$ is
nonzero. By Schur's lemma this map has rank one on the multiplicity space, so its
kernel inside $3V_1$ is $2V_1$.

Therefore

$$
K_3\cong 2V_1\oplus 2V_2\oplus V_3.
$$

The top-spin summand is

$$
V_3\cong S^3_0V,
$$

the symmetric trace-free tensors of rank three. Its dimension is

$$
\dim S^3_0V = 2\cdot 3+1=7.
$$

## 3. The depth-one profile

There are two internal gaps in a length-three word. The depth-one profile inserts
one probe variable into either gap and then compresses.

For a basis word $a\mid b\mid c$, define

$$
D_3^{(1)}(a\mid b\mid c)(x)=cbxa,
$$

and

$$
D_3^{(2)}(a\mid b\mid c)(x)=cxba,
$$

where $x\in V$.

The full depth-one profile is

$$
D_3=(D_3^{(1)},D_3^{(2)}):B_3\to \operatorname{Hom}(V,\mathbb H)\oplus \operatorname{Hom}(V,\mathbb H).
$$

Equivalently,

$$
D_3:B_3\to 2(\mathbb H\otimes V).
$$

Since

$$
\mathbb H\otimes V
  \cong (V_0\oplus V_1)\otimes V_1
  \cong V_0\oplus 2V_1\oplus V_2,
$$

the target of $D_3$ decomposes as

$$
2(\mathbb H\otimes V)\cong 2V_0\oplus 4V_1\oplus 2V_2.
$$

In particular, the target contains no $V_3$. Since $D_3$ is $SO(3)$-equivariant,
every source summand of type $V_3$ maps to zero. In length three, the source has
a unique $V_3$ summand, namely

$$
S^3_0V\cong V_3.
$$

Hence

$$
S^3_0V\subset \ker D_3.
$$

Also, since $m_3$ has target $V_0\oplus V_1$, the same top-spin summand lies in
the compression kernel:

$$
S^3_0V\subset K_3.
$$

Therefore

$$
S^3_0V\subset K_3\cap \ker D_3.
$$

The question is whether anything else remains invisible at depth one.

## 4. Exact rank computation

Use the ordered basis

$$
\{i,j,k\}^{\otimes 3}
$$

for $B_3$, and the ordered basis

$$
\{1,i,j,k\}
$$

for $\mathbb H$.

The matrices of $m_3$ and $D_3$ in these bases have integer entries. Direct
row-reduction over $\mathbb Q$ gives

$$
\operatorname{rank} m_3=4,
$$

and

$$
\operatorname{rank}(D_3|_{K_3})=16.
$$

Equivalently,

$$
\begin{aligned}
\dim(K_3\cap \ker D_3)
  &= \dim K_3-\operatorname{rank}(D_3|_{K_3})\\
  &= 23-16\\
  &= 7.
\end{aligned}
$$

A second exact check identifies the seven-dimensional kernel with the harmonic
subspace. The symmetric tensors in $S^3V$ have dimension $10$; imposing the three
trace equations gives

$$
\dim S^3_0V=7.
$$

The inclusion

$$
S^3_0V\subset K_3\cap \ker D_3
$$

and the equality of dimensions therefore imply equality of subspaces:

$$
K_3\cap \ker D_3 = S^3_0V.
$$

The computation is exact: no numerical approximation is involved. An accompanying
SymPy certificate can reproduce these ranks and the subspace equality over the
rationals.

## 5. Main proposition

**Proposition (Depth-one detection in length three).** Let

$$
K_3=\ker m_3\subset V^{\otimes 3}
$$

and let

$$
D_3:V^{\otimes 3}\to \operatorname{Hom}(V,\mathbb H)\oplus \operatorname{Hom}(V,\mathbb H)
$$

be the full depth-one insertion profile. Then

$$
K_3\cap \ker D_3 = S^3_0V.
$$

Equivalently, the only length-three residuals invisible both to compression and
to every depth-one insertion probe are the highest-spin harmonic tensors.

*Proof.* We already have

$$
S^3_0V\subset K_3\cap \ker D_3
$$

because neither $m_3$ nor $D_3$ has a $V_3$ target component.

By exact row-reduction,

$$
\dim(K_3\cap \ker D_3)=7.
$$

But

$$
\dim S^3_0V=7.
$$

Hence the inclusion is an equality:

$$
K_3\cap \ker D_3=S^3_0V.\qquad \square
$$

## 6. Consequence: complete detection of $K_3$

The kernel decomposes as

$$
K_3\cong 2V_1\oplus 2V_2\oplus V_3.
$$

The proposition says that the depth-one profile misses exactly the $V_3$ summand.
Therefore it detects the whole non-top-spin part:

$$
D_3 \text{ detects } 2V_1\oplus 2V_2.
$$

The vertical-response theorem gives the depth-two response on the top-spin
component:

$$
A_3(S)=4C_S,\qquad S\in S^3_0V.
$$

Since $C$ is injective, depth two detects the remaining $V_3$.

Thus the length-three residual kernel is completely detected by depths one and
two:

$$
K_3=(2V_1\oplus 2V_2)\oplus V_3,
$$

with

$$
\begin{aligned}
\text{depth }1 &\text{ detecting } 2V_1\oplus 2V_2,\\
\text{depth }2 &\text{ detecting } V_3.
\end{aligned}
$$

This is the first complete spin-depth profile.

## 7. Multiplicity-space refinement

The statement above is independent of a choice of basis in the multiplicity
spaces. In particular, on the $V_2$-isotypic part of $K_3$,

$$
(K_3)_{V_2}\cong 2V_2,
$$

the depth-one response induces an injective map of $SO(3)$-modules into the
$V_2$-isotypic part of the target

$$
2(\mathbb H\otimes V)\cong 2V_0\oplus 4V_1\oplus 2V_2.
$$

Equivalently, after choosing bases of the two multiplicity spaces, the $V_2$
response is represented by a full-rank $2\times 2$ matrix.

The concrete entries of that matrix depend on the chosen multiplicity bases. The
basis-free statement is the rank statement: the depth-one response is injective
on the $V_2$-isotypic part of $K_3$.

The same applies to the $V_1$-isotypic part:

$$
(K_3)_{V_1}\cong 2V_1,
$$

which is also detected at depth one.

## 8. Summary

Length three has the first nontrivial residual kernel:

$$
K_3\cong 2V_1\oplus 2V_2\oplus V_3.
$$

Compression kills all of it. The depth-one insertion profile recovers exactly the
intermediate-spin part,

$$
2V_1\oplus 2V_2,
$$

and misses exactly the top-spin part,

$$
V_3=S^3_0V.
$$

The top-spin part is then recovered by the depth-two vertical response,

$$
A_3(S)=4C_S.
$$

So, in length three, the probe-depth filtration is complete:

$$
\begin{aligned}
\text{depth }1 &: \text{ intermediate spins},\\
\text{depth }2 &: \text{ top spin}.
\end{aligned}
$$

The top-spin theorem is therefore not an isolated phenomenon. It is the upper
edge of a spin-depth visibility profile already visible in length three.
