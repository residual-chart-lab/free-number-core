# General Probe-Depth Response Profile

This note fixes the general notation for probe-depth response profiles in quaternionic
boundary-word spaces.

The purpose is definitional.  The coefficient theorem for the canonical vertical component
is proved separately in Note 06.

## 1. Boundary word spaces

Let

$$
V=\mathrm{Im}\mathbb H=\mathrm{span}_{\mathbb R}\{i,j,k\}.
$$

For each word length $n\geq 1$, define the boundary-word space

$$
B_n=V^{\otimes n}.
$$

A basis word is written

$$
a_1|a_2|\cdots|a_n.
$$

The reversed compression map is

$$
m_n(a_1|a_2|\cdots|a_n)=a_n\cdots a_2a_1.
$$

Thus $m_n:B_n\to\mathbb H$.

## 2. Slots and probe insertion

A word of length $n$ has $n+1$ slots:

```text
0 | a1 | 1 | a2 | 2 | ... | an | n
```

The internal slots are

$$
1,2,\ldots,n-1.
$$

A depth-$d$ insertion profile is specified by an ordered tuple of distinct slots

$$
\vec r=(r_1<r_2<\cdots<r_d),
$$

where each $r_t\in\{0,1,\ldots,n\}$.

Given probes

$$
\vec x=(x_1,\ldots,x_d)\in V^d,
$$

write

$$
I_{\vec x}^{\vec r}(a_1|\cdots|a_n)
$$

for the word obtained by inserting $x_t$ into slot $r_t$.

The resulting word has length $n+d$.

## 3. Probe-depth response profile

For $T\in B_n$, define the response component

$$
\mathcal R_{n,d}^{\vec r}(T)(x_1,\ldots,x_d)=m_{n+d}(I_{\vec x}^{\vec r}T).
$$

Equivalently,

$$
\mathcal R_{n,d}^{\vec r}:B_n\to\mathrm{Hom}(V^{\otimes d},\mathbb H).
$$

The full depth-$d$ response profile is the collection of all such components over all
distinct slot choices $\vec r$.

This note distinguishes the full distinct-slot profile from selected internal components.
A selected component can prove visibility of a residual, but it is not a replacement for
the full distinct-slot profile.

## 4. Full-null and internal-null residuals

Let $\mathcal S_{n,d}^{full}$ be the set of all depth-$d$ distinct slot choices

$$
\vec r=(r_1<\cdots<r_d),\qquad r_t\in\{0,1,\ldots,n\}.
$$

Let $\mathcal S_{n,d}^{int}$ be the set of all depth-$d$ distinct internal slot choices

$$
\vec r=(r_1<\cdots<r_d),\qquad r_t\in\{1,\ldots,n-1\}.
$$

Define the full-null residual space through depth $d$ by

$$
K_{n,d}^{full-null}=\ker m_n\cap\bigcap_{1\leq d'\leq d}\bigcap_{\vec r\in\mathcal S_{n,d'}^{full}}\ker\mathcal R_{n,d'}^{\vec r}.
$$

Define the internal-null residual space through depth $d$ by

$$
K_{n,d}^{int-null}=\ker m_n\cap\bigcap_{1\leq d'\leq d}\bigcap_{\vec r\in\mathcal S_{n,d'}^{int}}\ker\mathcal R_{n,d'}^{\vec r}.
$$

The full-null condition is stronger than the internal-null condition:

$$
K_{n,d}^{full-null}\subseteq K_{n,d}^{int-null}.
$$

This separation prevents a selected internal component from being mistaken for the full
response profile.

## 5. The canonical vertical component

For $n\geq2$, the canonical vertical component is the internal response of depth $n-1$
obtained by inserting one probe into each internal slot:

$$
\vec r_{vert}=(1,2,\ldots,n-1).
$$

Define

$$
A_n=\mathcal R_{n,n-1}^{\vec r_{vert}}.
$$

Since there are exactly $n-1$ internal slots, $\vec r_{vert}$ is the unique depth-$(n-1)$
internal slot choice.

For a basis word

$$
e_{a_1}|e_{a_2}|\cdots|e_{a_n},
$$

and probes

$$
x_1,\ldots,x_{n-1}\in V,
$$

this means

$$
e_{a_1}|x_1|e_{a_2}|x_2|\cdots|x_{n-1}|e_{a_n}.
$$

After reversed compression,

$$
A_n(e_{a_1}|\cdots|e_{a_n})(x_1,\ldots,x_{n-1})=e_{a_n}x_{n-1}e_{a_{n-1}}\cdots x_1e_{a_1}.
$$

The definition of $A_n$ contains no coefficient.  Any coefficient such as $-2$, $4$,
or $-8$ is an output of the quaternionic computation, not part of the definition.

## 6. Contraction map on the highest-spin component

Let

$$
S^n_0V\subseteq S^nV\subseteq V^{\otimes n}
$$

denote the symmetric trace-free component.

For $S\in S^n_0V$, define the contraction map

$$
C_S(x_1,\ldots,x_{n-1})=S(x_1,\ldots,x_{n-1}).
$$

Thus

$$
C_S\in\mathrm{Hom}(V^{\otimes(n-1)},V)\subseteq\mathrm{Hom}(V^{\otimes(n-1)},\mathbb H).
$$

The vertical response question is whether $A_n$ restricts to a scalar multiple of $C_S$
on $S^n_0V$.

## 7. Verified low-length cases

With the above definition of $A_n$, the verified low-length computations are:

$$
A_2(S)=-2C_S\qquad(S\in S^2_0V).
$$

$$
A_3(S)=4C_S\qquad(S\in S^3_0V).
$$

$$
A_4(S)=-8C_S\qquad(S\in S^4_0V).
$$

These are verified computations for $n=2,3,4$.

Note 06 proves the general vertical response theorem

$$
A_n(S)=(-2)^{n-1}C_S\qquad(S\in S^n_0V,\ n\geq2).
$$

## 8. Representation-theoretic visibility

The target of a depth-$d$ response is

$$
\mathrm{Hom}(V^{\otimes d},\mathbb H)\simeq\mathbb H\otimes V^{\otimes d}.
$$

Since

$$
\mathbb H\simeq V_0\oplus V_1
$$

as an $SO(3)$-module, the highest spin that can appear in the target is $V_{d+1}$.

Therefore the highest-spin source component

$$
S^n_0V\simeq V_n
$$

cannot appear in the depth-$d$ target when

$$
d<n-1.
$$

The first depth at which $V_n$ can appear is

$$
d=n-1.
$$

This explains why the canonical vertical component $A_n$ is the natural first place to
test visibility of the highest-spin residual.

This is a representation-theoretic visibility statement.  The scalar coefficient of the
canonical vertical component is proved separately in Note 06.

## 9. Non-claims

This note does not claim:

1. that the full depth-$d$ response profile is equivalent to the canonical vertical component;
2. that every residual invisible at one depth is visible at the next;
3. a complete classification of all $K_{n,d}^{full-null}$ or $K_{n,d}^{int-null}$;
4. an infinite full-profile ladder theorem;
5. a completed global semantic theory of free numbers.

The current note only fixes the notation and the canonical vertical component used in the
next result.

## 10. Summary

Compression is not disappearance.

A component may vanish under one compression map without being structurally absent.

The probe-depth response profile records how such residuals behave when the depth of
insertion is increased.

The first three verified vertical responses are

$$
A_2=-2C,\qquad A_3=4C,\qquad A_4=-8C.
$$

The general vertical response theorem is proved in Note 06.
