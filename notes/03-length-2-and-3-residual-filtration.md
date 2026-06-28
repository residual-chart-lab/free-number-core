# Length-2 and Length-3 Residual Filtration

This note records the first two residual-filtration steps for the boundary-word compression maps.

It is a follow-up to:

- `notes/01-non-aligned-compression-kernels.md`
- `notes/02-insertion-response-witness.md`

The purpose is narrow.

We prove the length-2 residual decomposition, and then record the length-3 null residual by Schur containment plus an exact integer rank calculation.

This note does not claim a general theorem for all lengths.

It also does not claim a full infinite residual ladder.

---

## 1. Setup

Let

$$V=\mathrm{Im}\,\mathbb{H} =\mathrm{span}_{\mathbb{R}}\{i,j,k\}.$$

For pure imaginary quaternions $u,v\in V$, we use

$$uv=-u\cdot v+u\times v.$$

Let

$$B_n=V^{\otimes n}$$

be the real vector space spanned by boundary words

$$a_1|\cdots|a_n.$$

The reversed compression map is

$$m_n(a_1|\cdots|a_n)=a_n\cdots a_1.$$

Thus

$$m_2(u|v)=vu,$$

and

$$m_3(a|b|c)=cba.$$

For insertion, define

$$I_d^{(r)}(a_1|\cdots|a_n) = a_1|\cdots|a_r|d|a_{r+1}|\cdots|a_n,$$

where $0\le r\le n$.

The $r$-th insertion response is

$$\mathcal{R}_n^{(r)}(x)(d) = m_{n+1}(I_d^{(r)}x).$$

For a word $w=a_1|\cdots|a_n$, set

$$P_r(w)=a_r\cdots a_1, \qquad Q_r(w)=a_n\cdots a_{r+1}.$$

Then

$$m_{n+1}(I_d^{(r)}w)=Q_r(w)dP_r(w).$$

For kernel elements $x\in\ker m_n$, the two exterior responses vanish:

$$\mathcal{R}_n^{(0)}(x)(d)=m_n(x)d=0,$$

and

$$\mathcal{R}_n^{(n)}(x)(d)=dm_n(x)=0.$$

So for residual detection, the internal insertions are the essential ones.

Define

$$K_n=\ker m_n.$$

Define the next-null residual space by

$$K_n^{\mathrm{null}} = K_n\cap\ker\mathcal{R}_n,$$

where $\ker\mathcal{R}_n$ means vanishing under all internal insertion responses.

---

## 2. Length-2 residual decomposition

We identify

$$B_2=V\otimes V.$$

As an $SO(3)$ representation,

$$V\otimes V = \mathbb{R}g \oplus \Lambda^2V \oplus S^2_0V.$$

The dimensions are

$$9=1+3+5.$$

Here:

- $\mathbb{R}g$ is the trace / metric component;
- $\Lambda^2V$ is the antisymmetric component;
- $S^2_0V$ is the symmetric trace-free component.

---

## 3. Lemma: $\ker m_2=S^2_0V$

Let

$$x=\sum_{a,b}T_{ab}\,e_a|e_b,$$

where

$$e_1=i,\qquad e_2=j,\qquad e_3=k.$$

Then

$$m_2(x) = \sum_{a,b}T_{ab}\,e_be_a.$$

Using

$$e_be_a=-\delta_{ab}+e_b\times e_a,$$

we get

$$m_2(x) = -\mathrm{tr}(T) + \sum_{a,b}T_{ab}(e_b\times e_a).$$

The real part is

$$-\mathrm{tr}(T).$$

So the real part vanishes exactly when

$$\mathrm{tr}(T)=0.$$

The vector part only sees the antisymmetric part of $T$, because $e_b\times e_a$ is antisymmetric in $a,b$.

Moreover,

$$\Lambda^2V\to V$$

is an isomorphism via the cross product.

Therefore the vector part vanishes exactly when the antisymmetric part of $T$ is zero.

Thus

$$m_2(x)=0$$

if and only if $T$ is symmetric and trace-free.

Hence

$$\ker m_2=S^2_0V.$$

---

## 4. Lemma: $\mathcal{R}_2$ recovers the killed component

Let

$$S=\sum_{a,b}S_{ab}\,e_a|e_b$$

be in $S^2_0V$.

Thus

$$S_{ab}=S_{ba}, \qquad \sum_a S_{aa}=0.$$

The internal response is

$$\mathcal{R}_2^{(1)}(S)(c) = m_3(I_c^{(1)}S) = \sum_{a,b}S_{ab}\,e_bce_a.$$

For pure imaginary $u,c,v\in V$, the triple-product identity is

$$ucv = -(u\cdot c)v -\det(u,c,v) +c(u\cdot v) -u(c\cdot v).$$

Apply this with $u=e_b$ and $v=e_a$.

Then

$$e_bce_a = -(e_b\cdot c)e_a -\det(e_b,c,e_a) +c(e_b\cdot e_a) -e_b(c\cdot e_a).$$

Now sum against $S_{ab}$.

The determinant term vanishes because it is antisymmetric in $a,b$, while $S_{ab}$ is symmetric.

The trace term vanishes because

$$\sum_{a,b}S_{ab}\delta_{ab} = \mathrm{tr}(S)=0.$$

The two remaining terms are both $-S(c)$.

Therefore

$$\mathcal{R}_2^{(1)}(S)(c)=-2S(c).$$

So

$$\mathcal{R}_2^{(1)}|_{S^2_0V} = -2\,\mathrm{id}.$$

In particular,

$$K_2^{\mathrm{null}}=0.$$

Length 2 is therefore fully visible at the next insertion-response stage.

---

## 5. Length-2 summary

At length 2,

$$V\otimes V = \mathbb{R}g \oplus \Lambda^2V \oplus S^2_0V.$$

The compression $m_2$ sees the trace component and the antisymmetric component.

It kills exactly the symmetric trace-free component:

$$\ker m_2=S^2_0V.$$

The internal response then recovers that killed component as

$$S\mapsto -2S.$$

Thus

$$K_2^{\mathrm{null}}=0.$$

This is the first residual-filtration step.

---

## 6. Length 3: representation-theoretic setup

Now let

$$B_3=V^{\otimes3}.$$

The $SO(3)$ decomposition is

$$V^{\otimes3} \simeq V_0 \oplus 3V_1 \oplus 2V_2 \oplus V_3.$$

The dimensions are

$$1+3\cdot3+2\cdot5+7=27.$$

The highest-spin component is

$$V_3=S^3_0V,$$

the completely symmetric trace-free third-order component.

The compression map is

$$m_3:V^{\otimes3}\to\mathbb{H}.$$

As an $SO(3)$ representation,

$$\mathbb{H}\simeq V_0\oplus V_1.$$

Hence $m_3$ can only see spin $0$ and spin $1$ components.

The response maps are

$$\mathcal{R}_3^{(1)},\mathcal{R}_3^{(2)}: V^{\otimes3}\to\mathrm{Hom}(V,\mathbb{H}).$$

Since

$$\mathrm{Hom}(V,\mathbb{H}) \simeq V\otimes(V_0\oplus V_1),$$

we get

$$\mathrm{Hom}(V,\mathbb{H}) \simeq V_0\oplus2V_1\oplus V_2.$$

Therefore the response codomain contains no $V_3$ component.

By Schur's lemma,

$$V_3\subseteq\ker m_3$$

and

$$V_3\subseteq\ker\mathcal{R}_3.$$

Thus

$$S^3_0V=V_3\subseteq K_3^{\mathrm{null}}.$$

This containment is representation-theoretic and does not depend on the rank calculation below.

---

## 7. Length 3: exact rank computation

To prove equality, we compute the dimension of $K_3^{\mathrm{null}}$.

Let

$$T_3 = m_3 \oplus \mathcal{R}_3^{(1)} \oplus \mathcal{R}_3^{(2)}.$$

Thus

$$T_3: V^{\otimes3} \to \mathbb{H} \oplus \mathrm{Hom}(V,\mathbb{H}) \oplus \mathrm{Hom}(V,\mathbb{H}).$$

The domain has dimension $27$.

The codomain has dimension

$$4+12+12=28.$$

So $T_3$ is represented by a $28\times27$ integer matrix in the basis

$$e_a|e_b|e_c, \qquad a,b,c\in\{1,2,3\}.$$

For a basis word $e_a|e_b|e_c$,

$$m_3(e_a|e_b|e_c)=e_ce_be_a.$$

For $d\in\{e_1,e_2,e_3\}$,

$$\mathcal{R}_3^{(1)}(e_a|e_b|e_c)(d) = e_ce_bde_a.$$

And

$$\mathcal{R}_3^{(2)}(e_a|e_b|e_c)(d) = e_cde_be_a.$$

The exact integer rank of this matrix is

$$\mathrm{rank}\,T_3=20.$$

Therefore

$$\dim\ker T_3=27-20=7.$$

But

$$\ker T_3 = \ker m_3\cap\ker\mathcal{R}_3 = K_3^{\mathrm{null}}.$$

So

$$\dim K_3^{\mathrm{null}}=7.$$

Since

$$S^3_0V\subseteq K_3^{\mathrm{null}}$$

and

$$\dim S^3_0V=7,$$

we conclude

$$K_3^{\mathrm{null}}=S^3_0V.$$

---

## 8. Reproducible rank check

The following script constructs the exact integer matrix $T_3$ and computes its rank.

```python
import sympy as sp

# Quaternion basis order:
# 0 = 1, 1 = i, 2 = j, 3 = k

def qmul(x, y):
    a0, a1, a2, a3 = x
    b0, b1, b2, b3 = y
    return [
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + a1*b0 + a2*b3 - a3*b2,
        a0*b2 - a1*b3 + a2*b0 + a3*b1,
        a0*b3 + a1*b2 - a2*b1 + a3*b0,
    ]

basis = [
    [1, 0, 0, 0],  # 1
    [0, 1, 0, 0],  # i
    [0, 0, 1, 0],  # j
    [0, 0, 0, 1],  # k
]

imag = [basis[1], basis[2], basis[3]]

def prod(seq):
    v = basis[0]
    for x in seq:
        v = qmul(v, x)
    return v

cols = []

for a in range(3):
    for b in range(3):
        for c in range(3):
            ea, eb, ec = imag[a], imag[b], imag[c]
            col = []

            # m_3(e_a|e_b|e_c) = e_c e_b e_a
            col += prod([ec, eb, ea])

            # R_3^(1)(e_a|e_b|e_c)(d) = e_c e_b d e_a
            for d in range(3):
                ed = imag[d]
                col += prod([ec, eb, ed, ea])

            # R_3^(2)(e_a|e_b|e_c)(d) = e_c d e_b e_a
            for d in range(3):
                ed = imag[d]
                col += prod([ec, ed, eb, ea])

            cols.append(col)

M = sp.Matrix.hstack(*[sp.Matrix(col) for col in cols])

print(M.shape)
print(M.rank())
```

Expected output:

```text
(28, 27)
20
```

This is an exact integer rank computation, not a floating-point calculation.

---

## 9. Length-3 null residual lemma

We can now state the length-3 result.

Let

$$K_3=\ker m_3.$$

Let

$$K_3^{\mathrm{null}} = K_3\cap\ker\mathcal{R}_3.$$

Then

$$K_3^{\mathrm{null}}=S^3_0V.$$

Equivalently,

the part of $V^{\otimes3}$ killed by both $m_3$ and the full internal insertion response is exactly the highest-spin component $V_3$.

---

## 10. First two filtration steps

The first two residual-filtration steps are:

$$K_2^{\mathrm{null}}=0.$$

And

$$K_3^{\mathrm{null}}=S^3_0V.$$

Thus, at length 2, every killed residual is recovered by the next insertion response.

At length 3, the highest-spin component $S^3_0V$ becomes the first true next-null residual.

This is the first place where the filtration becomes nontrivial.

---

## 11. What is not claimed here

This note does not claim a general theorem for all $n$.

It does not claim

$$K_n^{\mathrm{null}}=S^n_0V$$

for all $n$.

It also does not claim a full infinite residual ladder.

The purpose of this note is only to record the first two residual-filtration steps:

$$n=2: \quad K_2^{\mathrm{null}}=0.$$

$$n=3: \quad K_3^{\mathrm{null}}=S^3_0V.$$

The general pattern, if any, requires a separate treatment.
