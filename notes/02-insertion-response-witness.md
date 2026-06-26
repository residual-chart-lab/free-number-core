# Insertion-Response Witness for Non-Aligned Compression Kernels

This note records a minimal positive example after the single-compression no-go.

The point is not to claim a complete algebra of free numbers.

The point is narrower:

> A component killed by one compression map can still be detected by a non-aligned insertion-response witness at the next stage.

We keep only the two robust steps.

The possible infinite residual ladder is not claimed here. It is mentioned only as a direction requiring a separate treatment of boundary-word retention versus value compression.

---

## 1. Setup

Let $\mathbb{H}$ be the quaternion algebra, with imaginary basis $i,j,k$, satisfying

$$
i^2=j^2=k^2=-1,\qquad ij=k,\qquad ji=-k.
$$

Let $B_n$ be the real vector space spanned by boundary words

$$
a_1|a_2|\cdots|a_n,
$$

where each $a_r$ is an imaginary quaternionic unit.

Define the reversed compression map

$$
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
$$

Thus, for two-letter words,

$$
m_2(a|b)=ba.
$$

---

## 2. Single-compression no-go

A single compression map cannot serve both as a judge of local closure and as a witness of residual history.

If a witness factors through $m_n$, then it cannot distinguish elements inside the same $m_n$-fiber.

In particular, it cannot detect a nonzero element inside $\ker m_n$.

So the residual witness must be non-aligned with the judging compression.

This motivates the use of insertion-response profiles.

---

## 3. Insertion-response profile

For a word

$$
w=a_1|\cdots|a_n,
$$

define insertion at position $r$, where $0\le r\le n$, by

$$
I_c^{(r)}(w)=a_1|\cdots|a_r|c|a_{r+1}|\cdots|a_n.
$$

Define the $r$-th insertion response by

$$
\mathcal R_n^{(r)}(x)(c)=m_{n+1}(I_c^{(r)}x).
$$

The full insertion-response profile is

$$
\mathcal R_n(x)=\left(\mathcal R_n^{(0)}(x),\mathcal R_n^{(1)}(x),\ldots,\mathcal R_n^{(n)}(x)\right).
$$

For a word $w=a_1|\cdots|a_n$, set

$$
P_r(w)=a_r\cdots a_1,\qquad Q_r(w)=a_n\cdots a_{r+1}.
$$

Then

$$
m_{n+1}(I_c^{(r)}w)=Q_r(w)cP_r(w).
$$

This formula is the basic mechanism.

If $x\in\ker m_n$, then the two exterior insertions vanish:

$$
\mathcal R_n^{(0)}(x)(c)=m_n(x)c=0.
$$

$$
\mathcal R_n^{(n)}(x)(c)=cm_n(x)=0.
$$

Therefore, for kernel elements, only internal insertions can detect residual structure.

This is not a hand-chosen feature. It follows from the reversed compression structure.

---

## 4. First iron example: a kernel element detected at the next stage

Define

$$
\sigma=i|j+j|i.
$$

Then

$$
m_2(i|j)=ji=-k.
$$

$$
m_2(j|i)=ij=k.
$$

Therefore

$$
m_2(\sigma)=0.
$$

So

$$
\sigma\in\ker m_2.
$$

Now take the internal insertion response

$$
L_\sigma(c)=\mathcal R_2^{(1)}(\sigma)(c).
$$

By definition,

$$
L_\sigma(c)=m_3(i|c|j+j|c|i).
$$

Since $m_3(a|b|c)=cba$, we get

$$
L_\sigma(c)=jci+icj.
$$

Write

$$
c=\alpha i+\beta j+\gamma k.
$$

A direct computation gives

$$
L_\sigma(c)=-2\beta i-2\alpha j.
$$

Hence

$$
\ker L_\sigma=\mathbb{R} k.
$$

And

$$
\mathrm{Im}\,L_\sigma=\mathrm{span}_{\mathbb{R}}\{i,j\}.
$$

Thus $\sigma$ is killed by $m_2$, but it is detected by the next-stage insertion-response witness.

In compact form:

$$
\sigma\in\ker m_2,\qquad \mathcal R_2(\sigma)\neq0.
$$

More precisely,

$$
\mathcal R_2(\sigma)=(0,L_\sigma,0).
$$

So exterior insertion sees nothing, but internal insertion detects the residual.

---

## 5. Why this is not a hand-made tag

This witness is not obtained by choosing a special value of $c$.

The whole response operator $L_\sigma:V\to\mathbb{H}$ is used.

Its structure is quaternionic:

$$
\ker L_\sigma=\mathbb{R} k.
$$

$$
\mathrm{Im}\,L_\sigma=\mathrm{span}_{\mathbb{R}}\{i,j\}.
$$

The original word $\sigma=i|j+j|i$ belongs to the $i,j$-plane.

The response vanishes in the normal direction $k=i\times j$, and its image lies in the original plane.

So the witness is determined by the quaternionic plane-normal decomposition, not by an external tag.

---

## 6. Coordinate-free form

Let $a,b$ be orthogonal unit imaginary quaternions, and set

$$
n=a\times b.
$$

Define the symmetric boundary component

$$
\sigma_{a,b}=a|b+b|a.
$$

Then

$$
m_2(\sigma_{a,b})=ba+ab=0.
$$

So

$$
\sigma_{a,b}\in\ker m_2.
$$

Define

$$
L_{a,b}(c)=m_3(a|c|b+b|c|a).
$$

Then

$$
L_{a,b}(c)=-2\{(c\cdot b)a+(c\cdot a)b\}.
$$

Therefore

$$
\ker L_{a,b}=\mathbb{R}(a\times b).
$$

And

$$
\mathrm{Im}\,L_{a,b}=\mathrm{span}_{\mathbb{R}}\{a,b\}.
$$

This shows that the residual is governed by the oriented two-plane and its normal direction.

---

## 7. Relation to the antisymmetric component

For the same orthogonal pair $a,b$, define

$$
\Delta_{a,b}=a|b-b|a.
$$

Then

$$
m_2(\Delta_{a,b})=ba-ab.
$$

Since

$$
ab=a\times b=n,\qquad ba=-n,
$$

we get

$$
m_2(\Delta_{a,b})=-2n.
$$

So the antisymmetric component is seen directly by $m_2$ as the normal direction.

By contrast, the symmetric component is killed by $m_2$, but seen by the insertion-response witness as a plane-valued response.

Thus the two basic modes are:

- antisymmetric mode: directly visible as the normal direction;
- symmetric mode: killed by $m_2$, but visible by next-stage internal insertion.

This is the minimal place where the judge and the witness separate.

---

## 8. Second iron example: a three-letter kernel element reappears at four letters

Define

$$
\tau_k=i|k|j+j|k|i.
$$

Compute its three-letter compression:

$$
m_3(i|k|j)=jki=-1.
$$

$$
m_3(j|k|i)=ikj=1.
$$

Hence

$$
m_3(\tau_k)=0.
$$

So

$$
\tau_k\in\ker m_3.
$$

Now insert

$$
d=pi+qj+rk
$$

into the first internal position.

That is, consider

$$
\mathcal R_3^{(1)}(\tau_k)(d)=m_4(i|d|k|j+j|d|k|i).
$$

A direct computation gives

$$
\mathcal R_3^{(1)}(\tau_k)(d)=-2pi+2qj.
$$

Thus, if $d$ has a component in the $i,j$-plane, this response is nonzero.

So

$$
\tau_k\in\ker m_3,\qquad \mathcal R_3(\tau_k)\neq0.
$$

This gives a second robust step:

a component killed by $m_3$ can still reappear under a non-aligned four-letter insertion response.

---

## 9. What is claimed here

This note claims the following minimal mechanism.

There exist nonzero boundary components $x$ such that

$$
x\in\ker m_n
$$

but

$$
\mathcal R_n(x)\neq0.
$$

The witness $\mathcal R_n$ is not a tag.

It is induced canonically by all insertion positions and the next compression map $m_{n+1}$.

This gives a concrete way to separate:

- the judging compression $m_n$;
- the witnessing response profile $\mathcal R_n$.

The first kills the component.

The second can still detect its residual shadow.

---

## 10. What is not claimed here

This note does not claim a complete free-number algebra.

It also does not claim the full infinite residual ladder.

The two-step phenomenon above suggests a possible residual ladder, but the full ladder requires a separate treatment of boundary-word retention versus value compression.

In other words, one must carefully distinguish:

- the boundary word space $B_n$, where words are retained;
- the compression map $m_n:B_n\to\mathbb{H}$, where words are evaluated.

That distinction is essential, but it is not developed fully in this note.

Here we only record the iron core:

$$
\sigma\in\ker m_2,\qquad \mathcal R_2(\sigma)\neq0.
$$

And

$$
\tau_k\in\ker m_3,\qquad \mathcal R_3(\tau_k)\neq0.
$$

These are the minimal insertion-response witnesses for non-aligned compression kernels.

---

## 11. Summary

A single compression map cannot both collapse and witness residual history.

However, a next-stage insertion-response profile can detect what the previous compression killed.

The minimal example is

$$
\sigma=i|j+j|i\in\ker m_2.
$$

Yet

$$
L_\sigma(c)=m_3(i|c|j+j|c|i)
$$

is nonzero, with

$$
L_\sigma(\alpha i+\beta j+\gamma k)=-2\beta i-2\alpha j.
$$

Thus

$$
\ker L_\sigma=\mathbb{R} k,\qquad \mathrm{Im}\,L_\sigma=\mathrm{span}_{\mathbb{R}}\{i,j\}.
$$

This is the first canonical insertion-response witness.

The second robust step is

$$
\tau_k=i|k|j+j|k|i\in\ker m_3,
$$

while

$$
\mathcal R_3^{(1)}(\tau_k)(pi+qj+rk)=-2pi+2qj.
$$

Together, these two examples show that residual structure can survive as a non-aligned response profile even after being killed by the judging compression.
