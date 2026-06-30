# The Vertical Response Theorem

This note proves the general scalar coefficient for the canonical vertical response
component introduced in Note 05.

The theorem concerns only the canonical internal vertical component

$$
A_n=\mathcal R_{n,n-1}^{(1,2,\ldots,n-1)}.
$$

It does not identify the full response profile with this component.

## 1. Statement

Let

$$
V=\operatorname{Im}\mathbb H=\operatorname{span}_{\mathbb R}\{i,j,k\}.
$$

Let

$$
S^n_0V\subseteq V^{\otimes n}
$$

be the symmetric trace-free component.

For $S\in S^n_0V$, let

$$
C_S(x_1,\ldots,x_{n-1})=S(x_1,\ldots,x_{n-1})
$$

be the contraction map into $V\subset\mathbb H$.

The canonical vertical component is

$$
A_n(e_{a_1}|\cdots|e_{a_n})(x_1,\ldots,x_{n-1})=e_{a_n}x_{n-1}e_{a_{n-1}}\cdots x_1e_{a_1}.
$$

The theorem is:

$$
A_n(S)=(-2)^{n-1}C_S\qquad(S\in S^n_0V,\ n\geq2).
$$

Thus the highest-spin component is detected at the first depth where it can appear,
namely depth $n-1$.

## 2. The two-index collapse lemma

The basic length-2 identity is the following.

**Lemma 2.1.** If $M\in S^2_0V$, then

$$
\sum_{a,b}M_{ab}\,e_bxe_a=-2M(x).
$$

Equivalently,

$$
A_2(M)=-2C_M.
$$

This is the length-2 insertion-response lemma.  It is the local two-index collapse that
drives the general vertical theorem.

## 3. Trace-free contraction

For $S\in S^n_0V$ and $x\in V$, define the one-variable contraction

$$
S_x(v_1,\ldots,v_{n-1})=S(v_1,\ldots,v_{n-1},x).
$$

Then

$$
S_x\in S^{n-1}_0V.
$$

Indeed, symmetry is inherited from $S$.  Trace-freeness is also inherited, because tracing
any two remaining variables of $S_x$ is the same as tracing those two variables of $S$ and
then evaluating the remaining slot at $x$.

Equivalently, $S\in S^n_0V$ means that all pairwise traces vanish.  In particular, after
fixing any remaining variables, the trace over any chosen pair of slots is zero.

## 4. Recursive collapse of the vertical response

Let $S\in S^n_0V$ with $n\geq3$.

Write

$$
S=\sum S_{a_1\cdots a_n}\,e_{a_1}|\cdots|e_{a_n}.
$$

Using the definition of $A_n$,

$$
A_n(S)(x_1,\ldots,x_{n-1})=\sum S_{a_1\cdots a_n}\,e_{a_n}x_{n-1}e_{a_{n-1}}\cdots x_1e_{a_1}.
$$

Fix the first $n-2$ indices.  Since $S$ is symmetric and trace-free, the two-index slice

$$
M^{a_1,\ldots,a_{n-2}}_{ab}=S_{a_1\cdots a_{n-2}ab}
$$

lies in $S^2_0V$.

The point is that symmetry gives

$$
M^{a_1,\ldots,a_{n-2}}_{ab}=M^{a_1,\ldots,a_{n-2}}_{ba},
$$

and trace-freeness gives

$$
\sum_a M^{a_1,\ldots,a_{n-2}}_{aa}=\sum_a S_{a_1\cdots a_{n-2}aa}=0.
$$

Applying Lemma 2.1 to the last two indices gives

$$
\sum_{a,b}S_{a_1\cdots a_{n-2}ab}\,e_bx_{n-1}e_a=-2\sum_c(S_{x_{n-1}})_{a_1\cdots a_{n-2}c}\,e_c.
$$

Substituting this into the definition of $A_n$ gives the recursion

$$
A_n(S)(x_1,\ldots,x_{n-1})=-2A_{n-1}(S_{x_{n-1}})(x_1,\ldots,x_{n-2}).
$$

This recursion contains the entire coefficient pattern.

## 5. Proof of the theorem

The base case $n=2$ is Lemma 2.1:

$$
A_2(S)=-2C_S.
$$

Assume the theorem holds for $n-1$.  Since $S_{x_{n-1}}\in S^{n-1}_0V$, the induction
hypothesis gives

$$
A_{n-1}(S_{x_{n-1}})=(-2)^{n-2}C_{S_{x_{n-1}}}.
$$

Using the recursion,

$$
A_n(S)(x_1,\ldots,x_{n-1})=-2(-2)^{n-2}C_{S_{x_{n-1}}}(x_1,\ldots,x_{n-2}).
$$

But

$$
C_{S_{x_{n-1}}}(x_1,\ldots,x_{n-2})=C_S(x_1,\ldots,x_{n-1}).
$$

Therefore

$$
A_n(S)=(-2)^{n-1}C_S.
$$

This proves the theorem for all $n\geq2$.

## 6. First verified rungs

The theorem recovers the previously verified low-length computations:

$$
A_2(S)=-2C_S\qquad(S\in S^2_0V).
$$

$$
A_3(S)=4C_S\qquad(S\in S^3_0V).
$$

$$
A_4(S)=-8C_S\qquad(S\in S^4_0V).
$$

The length-4 computation remains useful as an independent exact check of the sign:

```text
dim S^4_0 V = 9
A4 + 8C vanishes on basis: True
A4 - 8C vanishes on basis: False
rank A4 on S^4_0 V = 9
rank C on S^4_0 V = 9
```

The line `A4 - 8C vanishes on basis: False` is included to make the sign check explicit.

## 7. Interpretation

The coefficient is a repeated two-index collapse.

Each vertical step contributes the same factor

$$
-2.
$$

After $n-1$ vertical collapses, the total coefficient is

$$
(-2)^{n-1}.
$$

This is not inserted into the definition of $A_n$.  It is the output of repeatedly applying
the length-2 collapse lemma along the canonical vertical response.

## 8. Consequence

The canonical vertical response detects the highest-spin symmetric trace-free component:

$$
A_n|_{S^n_0V}=(-2)^{n-1}C.
$$

Since $(-2)^{n-1}\neq0$ and $C$ is injective on $S^n_0V$, the restriction of $A_n$ to
$S^n_0V$ is injective.

Thus the highest-spin component is not structurally absent.  It is visible at the canonical
vertical depth $n-1$.

## 9. Non-claims

This theorem does not claim:

1. that the full depth-$d$ response profile is equivalent to the canonical vertical component;
2. a complete description of all residual spaces $K_{n,d}^{full-null}$ or $K_{n,d}^{int-null}$;
3. that every residual invisible at one depth is visible at the next;
4. a full-profile infinite ladder theorem;
5. a completed global semantic theory of free numbers.

It proves only the scalar coefficient of the canonical vertical response on $S^n_0V$.

## 10. Summary

Compression is not disappearance.

For the highest-spin residual

$$
S^n_0V,
$$

the canonical vertical response satisfies

$$
A_n(S)=(-2)^{n-1}C_S.
$$

The first three rungs

$$
-2,\quad4,\quad-8
$$

are therefore the beginning of a general vertical response theorem, not isolated accidents.
