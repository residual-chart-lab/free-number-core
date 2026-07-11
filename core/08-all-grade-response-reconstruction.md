# All-Grade Canonical Response Reconstruction

**Status:** proved all-grade theorem in the quaternionic boundary-word model  
**Branch:** `core-reconstruction`  
**Depends on:** `core/01-abstract-core.md`, `core/05-length-three-propagation.md`, `core/07-length-four-cross-boundary-propagation.md`, `notes/06-general-vertical-response-theorem.md`  
**Model:** quaternionic boundary words in every finite structural grade

## 0. Purpose

The low-grade calculations established complete finite observability at lengths two, three, and four.

This note proves that the phenomenon is not confined to those grades.

For every finite length

\[
n\ge 1,
\]

the canonical all-gap response

\[
A_n:B_n\longrightarrow\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\]

is injective.

Thus one canonical response component at depth \(n-1\) already determines the entire length-\(n\) boundary representative.

The note also proves a uniform composition law:

\[
\boxed{
A_{m+n}(x|y)
=
A_n(y)\;\delta\;A_m(x)
}
\]

with the bridge probe \(\delta\) inserted between the two factors in the order forced by reversed quaternionic compression.

This gives an exact graded response algebra for the concrete model.

It does not yet declare the abstract universal Free Numbers core complete. That audit is reserved for the next closure note.

---

## 1. Setup

Let

\[
V=\operatorname{Im}\mathbb H
=\operatorname{span}_{\mathbb R}\{i,j,k\}.
\]

Let

\[
B_n=V^{\otimes n}.
\]

A pure boundary word is written

\[
a_1|\cdots|a_n.
\]

Compression is reversed quaternionic multiplication:

\[
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
\]

For \(n=1\), define

\[
A_1(a)=a\in V\subset\mathbb H.
\]

For \(n\ge2\), define the canonical all-gap response

\[
A_n:B_n\longrightarrow
\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\]

on pure words by

\[
\boxed{
A_n(a_1|\cdots|a_n)(d_1,\ldots,d_{n-1})
=
a_nd_{n-1}a_{n-1}\cdots d_1a_1.
}
\]

This is exactly the canonical vertical component already used in the vertical-response theorem.

It is obtained by inserting one probe in every original internal gap and then applying reversed compression.

The previous all-length theorem states that on the highest-spin sector,

\[
A_n(S)=(-2)^{n-1}C_S
\qquad(S\in S^n_0V).
\]

The result below is stronger in a different direction: it proves that \(A_n\) is injective on the whole of \(B_n\), not only on \(S^n_0V\).

---

## 2. The local decoder

The induction is controlled by one twelve-dimensional map.

Define

\[
\Theta:
V\otimes\mathbb H
\longrightarrow
\operatorname{Hom}(V,\mathbb H)
\]

by

\[
\boxed{
\Theta\!\left(\sum_{a=1}^3e_a\otimes h_a\right)(d)
=
\sum_{a=1}^3e_a d h_a.
}
\]

Here \((e_1,e_2,e_3)\) is any oriented orthonormal basis of \(V\).

Both domain and codomain have real dimension twelve.

The important point is not only that \(\Theta\) is invertible, but that its inverse is explicit.

### Lemma 2.1 — Explicit local decoding

Let

\[
F\in\operatorname{Hom}(V,\mathbb H).
\]

Define

\[
\boxed{
h_a
=
\frac12
\sum_{b,c=1}^3
\varepsilon_{abc}\,e_bF(e_c),
}
\]

where \(\varepsilon_{abc}\) is the Levi-Civita symbol.

Then

\[
\boxed{
F(d)=\sum_{a=1}^3e_a d h_a
\qquad(d\in V).
}
\]

Equivalently,

\[
\boxed{
\Theta^{-1}(F)
=
\sum_{a=1}^3e_a\otimes
\left(
\frac12\sum_{b,c}\varepsilon_{abc}e_bF(e_c)
\right).
}
\]

### Proof

It is enough to evaluate at a basis vector \(e_r\).

Substituting the proposed coefficients gives

\[
\begin{aligned}
\sum_ae_ae_rh_a
&=
\frac12
\sum_{a,b,c}
\varepsilon_{abc}
 e_ae_re_bF(e_c).
\end{aligned}
\]

The quaternionic basis multiplication table gives the exact identity

\[
\boxed{
\frac12
\sum_{a,b}
\varepsilon_{abc}
 e_ae_re_b
=
\delta_{rc}1_{\mathbb H}.
}
\]

Therefore

\[
\sum_ae_ae_rh_a
=
\sum_c\delta_{rc}F(e_c)
=
F(e_r).
\]

By linearity, the equality holds for every \(d\in V\). ∎

### Corollary 2.2

\[
\boxed{
\Theta
\text{ is a real-linear isomorphism.}
}
\]

In the ordered bases induced by \((i,j,k)\) and \((1,i,j,k)\), its exact determinant is

\[
\boxed{
\det\Theta=256.
}
\]

The determinant is a certificate of the same invertibility proved by the explicit inverse formula.

---

## 3. Recursive form of the canonical response

Fix an oriented orthonormal basis

\[
e_1,e_2,e_3
\]

of \(V\).

Every element

\[
x\in B_n=B_{n-1}\otimes V
\]

has a unique expansion

\[
\boxed{
x=\sum_{a=1}^3x_a|e_a,
\qquad
x_a\in B_{n-1}.
}
\]

For

\[
\mathbf d=(d_1,\ldots,d_{n-2})
\]

and \(d\in V\), the definition of \(A_n\) gives

\[
\boxed{
A_n(x)(\mathbf d,d)
=
\sum_{a=1}^3
 e_a d\,A_{n-1}(x_a)(\mathbf d).
}
\]

For each fixed \(\mathbf d\), this is exactly

\[
\Theta\!\left(
\sum_{a=1}^3
 e_a\otimes A_{n-1}(x_a)(\mathbf d)
\right)(d).
\]

Thus the last probe variable exposes, through the local decoder \(\Theta^{-1}\), the complete collection of length-\((n-1)\) responses of the three coefficient tensors \(x_a\).

---

## 4. All-Grade Reconstruction Theorem

### Theorem 4.1

For every integer

\[
n\ge1,
\]

the canonical all-gap response

\[
A_n:B_n\longrightarrow
\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\]

is injective.

Equivalently,

\[
\boxed{
A_n(x)=A_n(y)
\iff
x=y
\qquad(x,y\in B_n).
}
\]

### Proof

Proceed by induction on \(n\).

For \(n=1\),

\[
A_1:V\hookrightarrow\mathbb H
\]

is the standard inclusion, hence injective.

Assume \(A_{n-1}\) is injective.

Let

\[
x=\sum_{a=1}^3x_a|e_a\in B_n
\]

and suppose

\[
A_n(x)=0.
\]

Fix arbitrary

\[
\mathbf d\in V^{\otimes(n-2)}.
\]

Then the map in the final probe variable is zero:

\[
d\longmapsto
A_n(x)(\mathbf d,d)
=0.
\]

By the recursive formula,

\[
\Theta\!\left(
\sum_{a=1}^3
 e_a\otimes A_{n-1}(x_a)(\mathbf d)
\right)=0.
\]

Since \(\Theta\) is injective,

\[
A_{n-1}(x_a)(\mathbf d)=0
\qquad
\text{for every }a.
\]

Because \(\mathbf d\) was arbitrary,

\[
A_{n-1}(x_a)=0
\qquad
\text{for every }a.
\]

The induction hypothesis gives

\[
x_a=0
\qquad
\text{for every }a.
\]

Therefore

\[
x=0.
\]

Thus \(A_n\) is injective. ∎

---

## 5. Immediate consequences

### 5.1 Exact rank in every grade

Since

\[
\dim B_n=3^n,
\]

Theorem 4.1 gives

\[
\boxed{
\operatorname{rank}A_n=3^n.
}
\]

The ambient response space has dimension

\[
\dim\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
=4\cdot3^{n-1}.
\]

Therefore the image has codimension

\[
\boxed{
4\cdot3^{n-1}-3^n=3^{n-1}.
}
\]

An arbitrary multilinear map into \(\mathbb H\) is not automatically an admissible Free Numbers response. The exact response space is a proper structured subspace.

### 5.2 One canonical component is complete

At each finite grade, the single component

\[
A_n
\]

already determines the entire representative.

Thus the larger signatures used at lengths three and four were correct but redundant as equality certificates.

For example,

\[
A_3:B_3\to\operatorname{Hom}(V^{\otimes2},\mathbb H)
\]

is itself injective, and

\[
A_4:B_4\to\operatorname{Hom}(V^{\otimes3},\mathbb H)
\]

is itself injective.

The lower-depth channels remain essential for measuring first detection depth. They are not required for final reconstruction once the all-gap response is retained.

### 5.3 No absolutely invisible finite representative

If the all-gap response is admitted as a probe, then for every finite grade,

\[
\boxed{
A_n(x)=0
\Longrightarrow
x=0.
}
\]

Hence the absolutely invisible class in the quaternionic boundary-word model is trivial:

\[
\boxed{
F_n^{\infty}=0
\qquad(n<\infty).
}
\]

Every nonzero finite representative becomes visible by depth at most

\[
n-1.
\]

This is a finite-grade theorem. It does not address infinite words, completions, or limiting objects.

### 5.4 Every lower observation factors through \(A_n\)

Let

\[
O:B_n\to W
\]

be any linear observation, including compression or a lower-depth response component.

Since \(A_n\) is an isomorphism from \(B_n\) onto its image, define

\[
\overline O
:=
O\circ A_n^{-1}
\]

on \(\operatorname{im}A_n\).

Then

\[
\boxed{
O=\overline O\circ A_n.
}
\]

In particular, compressed value and every truncated response profile are recoverable from the canonical all-gap coordinate.

This is an existence statement for the transported observation. It does not claim that every such transported map already has a minimal closed formula.

---

## 6. Explicit recursive reconstruction algorithm

The proof gives an actual decoder.

Let

\[
F=A_n(x).
\]

For each fixed

\[
\mathbf d=(d_1,\ldots,d_{n-2}),
\]

consider the last-variable slice

\[
F_{\mathbf d}:V\to\mathbb H,
\qquad
F_{\mathbf d}(d)=F(\mathbf d,d).
\]

Apply the local inverse:

\[
\Theta^{-1}(F_{\mathbf d})
=
\sum_{a=1}^3e_a\otimes h_a(\mathbf d),
\]

where

\[
\boxed{
h_a(\mathbf d)
=
\frac12
\sum_{b,c}
\varepsilon_{abc}
 e_bF(\mathbf d,e_c).
}
\]

The recursive identity proves that

\[
\boxed{
h_a=A_{n-1}(x_a).
}
\]

Decode each \(h_a\) recursively to recover \(x_a\), then reconstruct

\[
\boxed{
x=\sum_{a=1}^3x_a|e_a.
}
\]

Thus reconstruction requires no search through the full tensor basis. It peels off one boundary letter at a time by repeated application of the same twelve-dimensional local inverse.

---

## 7. Exact response coordinate spaces

Define

\[
\boxed{
\mathfrak A_n:=\operatorname{im}A_n
\subseteq
\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H).
}
\]

Then

\[
A_n:B_n\xrightarrow{\cong}\mathfrak A_n
\]

is a linear isomorphism.

Therefore

\[
\boxed{
\dim\mathfrak A_n=3^n.
}
\]

The family

\[
\mathfrak A_1,\mathfrak A_2,\ldots
\]

is the exact-response realization of the graded quaternionic boundary-word model.

A length-\(n\) Free Number representative may be carried without loss either as

\[
x\in B_n
\]

or as its exact response coordinate

\[
A_n(x)\in\mathfrak A_n.
\]

The latter coordinate contains compressed value, residual information, and every lower-depth response implicitly.

---

## 8. General cross-boundary factorisation

Let

\[
x\in B_m,
\qquad
y\in B_n.
\]

Write internal probes for \(x\) as

\[
\mathbf d=(d_1,\ldots,d_{m-1}),
\]

the new cross-boundary probe as

\[
\delta\in V,
\]

and internal probes for \(y\) as

\[
\mathbf e=(e_1,\ldots,e_{n-1}).
\]

### Theorem 8.1 — Uniform all-grade composition formula

For every \(m,n\ge1\),

\[
\boxed{
A_{m+n}(x|y)(\mathbf d,\delta,\mathbf e)
=
A_n(y)(\mathbf e)\,\delta\,A_m(x)(\mathbf d).
}
\]

### Proof

It is enough to prove the formula on pure words.

Let

\[
x=a_1|\cdots|a_m,
\qquad
y=b_1|\cdots|b_n.
\]

After inserting probes into every internal gap of the concatenated word, reversed compression gives

\[
\begin{aligned}
&A_{m+n}(x|y)(\mathbf d,\delta,\mathbf e)\\
&=
 b_ne_{n-1}b_{n-1}\cdots e_1b_1
 \;\delta\;
 a_md_{m-1}a_{m-1}\cdots d_1a_1.
\end{aligned}
\]

The left block is exactly

\[
A_n(y)(\mathbf e),
\]

and the right block is exactly

\[
A_m(x)(\mathbf d).
\]

Therefore

\[
A_{m+n}(x|y)
=
A_n(y)\,\delta\,A_m(x).
\]

Extend bilinearly. ∎

The length-four formula

\[
A_4(x|y)(d_1,d_2,d_3)
=
L_y(d_3)d_2L_x(d_1)
\]

is precisely the case

\[
m=n=2.
\]

---

## 9. The exact response product

Let

\[
F\in\mathfrak A_m,
\qquad
G\in\mathfrak A_n.
\]

Define

\[
F\star G
\in
\operatorname{Hom}(V^{\otimes(m+n-1)},\mathbb H)
\]

by

\[
\boxed{
(F\star G)(\mathbf d,\delta,\mathbf e)
:=
G(\mathbf e)\,\delta\,F(\mathbf d).
}
\]

Theorem 8.1 gives

\[
\boxed{
A_m(x)\star A_n(y)
=
A_{m+n}(x|y).
}
\]

Therefore

\[
\boxed{
\star:
\mathfrak A_m\times\mathfrak A_n
\longrightarrow
\mathfrak A_{m+n}
}
\]

is a well-defined bilinear graded product.

### Theorem 9.1 — Associativity

The product \(\star\) is strictly associative on positive grades.

### Proof

Let

\[
F\in\mathfrak A_m,
\quad
G\in\mathfrak A_n,
\quad
H\in\mathfrak A_r.
\]

Using two ordered bridge probes \(\delta,\eta\), both bracketings evaluate as

\[
H\,\eta\,G\,\delta\,F.
\]

Equivalently, since concatenation is strictly associative and each \(A_k\) is injective,

\[
(F\star G)\star H
=
F\star(G\star H).
\]

∎

### Corollary 9.2 — Composition-compatible equality

Define exact response equality by

\[
F=F'
\qquad\text{inside }\mathfrak A_n.
\]

Then

\[
F=F',
\qquad
G=G'
\]

implies

\[
F\star G=F'\star G'.
\]

Under \(A_n\), this is exactly representative equality in \(B_n\).

Thus the concrete model has a finite, exact, composition-compatible equality in every grade.

### Orientation

The product is not commutative.

The right factor appears on the left in quaternionic multiplication:

\[
(F\star G)=G\,\delta\,F.
\]

This order is inherited from reversed compression and must not be exchanged.

---

## 10. Closure versus depth spectrum

Theorem 4.1 separates two questions that had previously been entangled.

### 10.1 Reconstruction question

How much data is sufficient to recover the entire representative?

Answer:

\[
\boxed{
A_n
\text{ alone is sufficient at every finite grade.}
}
\]

This question is now closed in the quaternionic boundary-word model.

### 10.2 Detection-depth question

At what minimum depth does each irreducible or multiplicity component first become visible?

This remains a rich open classification problem.

The filtrations

\[
F_0^{(n)}\supseteq F_1^{(n)}\supseteq\cdots\supseteq F_{n-1}^{(n)}=0
\]

measure how long a component remains invisible before the complete coordinate is reached.

The all-grade reconstruction theorem proves termination at depth \(n-1\), but it does not classify the intermediate quotients.

Thus:

\[
\boxed{
\text{finite reconstruction is closed; the residual-depth spectrum remains open.}
}
\]

The highest-spin theorem

\[
A_n(S)=(-2)^{n-1}C_S
\]

is now understood as the multiplicity-free last-survivor edge of a globally injective response coordinate.

---

## 11. Capability impact

Inside the quaternionic boundary-word model, the following are now exact for every finite grade.

1. **Non-collapsing compression:** compressed value does not define equality.
2. **Contextual re-observability:** information killed at shallow depth is recovered by deeper all-gap response.
3. **Finite observability:** every grade \(n\) has a finite complete certificate \(A_n\).
4. **Residual-depth termination:** every nonzero finite representative is detected by depth at most \(n-1\).
5. **Composition:** exact response coordinates compose by \(\star\).
6. **Composition-compatible equality:** equality in \(\mathfrak A_n\) is a graded congruence.
7. **Quaternionic recovery:** compressed quaternionic value factors through the exact response coordinate.
8. **Closure with remainder:** the full response coordinate retains everything omitted by compression.

This closes the central operational problem in the concrete model:

\[
\boxed{
\text{complete finite signatures exist in every grade and compose uniformly.}
}
\]

The next note must decide how much of this structure is promoted to the standalone abstract Free Numbers core and which parts remain model-specific.

---

## 12. Non-claims

This note does not claim:

1. that \(A_n\) is surjective onto the full multilinear response space;
2. that depth \(n-1\) is minimal for every representative;
3. a closed formula for the full spin-multiplicity-depth spectrum;
4. that the quaternionic boundary-word model is universal, initial, or unique;
5. that the final abstract Free Numbers equality must be literal representative equality;
6. a completed grade-zero unit construction for the response product;
7. a treatment of infinite words, topological completions, or limiting response objects;
8. a temporal, causal, conscious, ethical, or physical interpretation;
9. that the Residual Chart OS is required for the existence of these objects.

The proved theorem is narrower and stronger:

\[
\boxed{
A_n
\text{ is an injective canonical coordinate for every finite }B_n,
}
\]

and

\[
\boxed{
A_{m+n}(x|y)
=
A_m(x)\star A_n(y)
}
\]

with the explicit ordered bridge product.

---

## 13. Next closure gate

The next note should be:

```text
core/09-core-closure-theorem.md
```

It should audit the all-grade response realization against the Capability Ledger and decide the status of:

1. the concrete graded response algebra
   \[
   \mathfrak A=\bigoplus_{n\ge1}\mathfrak A_n;
   \]
2. the abstract primitives required to state its reconstruction theorem;
3. grade zero and a unit, if required;
4. the final standalone equality or equivalence;
5. the separation between Core v1 and the open residual-depth spectrum;
6. the exact boundary between Free Numbers Core, Residual Chart OS, and originating interpretation.

The intended stopping rule is now precise:

\[
\boxed{
\text{close Core v1 after the all-grade reconstruction and composition laws are abstractly audited.}
}
\]

Further spin-depth tables belong to the next research program, not to the completion requirement of the first core.