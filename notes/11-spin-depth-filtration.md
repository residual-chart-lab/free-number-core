# Note 11 — The Spin-Depth Filtration

*Free Numbers. A probe-depth ladder for residual detection.*

Compression $m_n:V^{\otimes n}\to\mathbb H$ kills a large kernel $K_n=\ker\,m_n$.
This note measures that kernel by probe depth: how much of $K_n$ becomes visible
when one, two, three, or more internal probes are inserted before compressing.

The result proved here is exact for $n=2,3,4$. These verified cases give a
filtration of $K_n$ by probe depth, refined by $SO(3)$ spin.

The all-$n$ theorem used here is narrower: the highest-spin component
$S^n_0V\cong V_n$ is detected by the canonical vertical response at depth
$n-1$ with coefficient $(-2)^{n-1}$. The full multiplicity-depth filtration for
all $n$ is not yet known.

Throughout, $V=\mathrm{Im}\,\mathbb H\cong V_1$, and $V^{\otimes n}$ is decomposed
as an $SO(3)$ representation.

---

## 1. The probe-depth profiles

For a length-$n$ word, a depth-$d$ profile inserts up to $d$ probe variables into
distinct internal gaps and then compresses.

Write $D_n^{\le d}$ for the combined map consisting of compression together with
all internal insertion profiles of depth at most $d$.

For the verified cases in this note, define

$$
F_d^{(n)}=\ker\,D_n^{\le d}.
$$

Thus

$$
F_0^{(n)}=K_n.
$$

The successive kernels form a decreasing chain:

$$
K_n=F_0^{(n)}\supseteq F_1^{(n)}\supseteq F_2^{(n)}\supseteq\cdots.
$$

The quotient

$$
F_{d-1}^{(n)}/F_d^{(n)}
$$

is the residual part first detected at probe depth $d$.

In the exact certificates for $n=2,3,4$, the chain terminates at depth $n-1$.
This note does not claim a full-profile termination theorem for every $n$.

---

## 2. The verified tables for n = 2, 3, 4

Each entry is the multiplicity of $V_s$ in $F_d^{(n)}=\ker D_n^{\le d}$, computed
by exact rational arithmetic and confirmed as a genuine $SO(3)$ subrepresentation
via the Casimir.

The companion certificate reproduces every entry.

### n = 2

At length two,

$$
K_2=S^2_0V\cong V_2.
$$

| remaining kernel | $V_2$ | dimension |
|---|---:|---:|
| $F_0^{(2)}=K_2$ | 1 | 5 |
| $F_1^{(2)}$ | 0 | 0 |

### n = 3

At length three,

$$
K_3\cong 2V_1\oplus2V_2\oplus V_3.
$$

| remaining kernel | $V_1$ | $V_2$ | $V_3$ | dimension |
|---|---:|---:|---:|---:|
| $F_0^{(3)}=K_3$ | 2 | 2 | 1 | 23 |
| $F_1^{(3)}$ | 0 | 0 | 1 | 7 |
| $F_2^{(3)}$ | 0 | 0 | 0 | 0 |

Thus depth one detects $2V_1\oplus2V_2$, and depth two detects the remaining $V_3$.

### n = 4

At length four,

$$
V^{\otimes4}\cong3V_0\oplus6V_1\oplus6V_2\oplus3V_3\oplus V_4.
$$

The compression map has rank $4$, and therefore

$$
K_4\cong2V_0\oplus5V_1\oplus6V_2\oplus3V_3\oplus V_4.
$$

The remaining-kernel table is:

| remaining kernel | $V_0$ | $V_1$ | $V_2$ | $V_3$ | $V_4$ | dimension |
|---|---:|---:|---:|---:|---:|---:|
| $F_0^{(4)}=K_4$ | 2 | 5 | 6 | 3 | 1 | 77 |
| $F_1^{(4)}$ | 1 | 1 | 3 | 3 | 1 | 49 |
| $F_2^{(4)}$ | 0 | 0 | 0 | 0 | 1 | 9 |
| $F_3^{(4)}$ | 0 | 0 | 0 | 0 | 0 | 0 |

The corresponding detected multiplicities are:

| first detected at | $V_0$ | $V_1$ | $V_2$ | $V_3$ | $V_4$ | dimension |
|---|---:|---:|---:|---:|---:|---:|
| depth 1 | 1 | 4 | 3 | 0 | 0 | 28 |
| depth 2 | 1 | 1 | 3 | 3 | 0 | 40 |
| depth 3 | 0 | 0 | 0 | 0 | 1 | 9 |

This is the first multiplicity-depth splitting.

---

## 3. The all-n top-spin theorem

The general theorem available for all $n$ is the vertical-response theorem.

For $S\in S^n_0V$, the canonical vertical response satisfies

$$
A_n(S)=(-2)^{n-1}C_S.
$$

Since $(-2)^{n-1}\neq0$ and $C$ is injective on $S^n_0V$, the highest-spin
component is detected by the canonical vertical response at depth $n-1$.

This theorem concerns the canonical vertical component on the highest-spin
summand. It does not, by itself, prove the full depth filtration for all $n$.

In the verified cases $n=2,3,4$, the certificate also checks the stronger
last-survivor equality

$$
F_{n-2}^{(n)}=S^n_0V
$$

as a subspace equality.

This stronger equality is currently a verified pattern for $n=2,3,4$, not yet a
general theorem of the full profile.

---

## 4. Why the top spin is special

The highest spin $V_n$ occurs in $V^{\otimes n}$ with multiplicity one.

There is therefore no multiplicity space for the filtration to split. The single
copy of $V_n$ is either visible at a given depth or it is not. The vertical
response theorem proves that it is read out at canonical vertical depth $n-1$,
with coefficient $(-2)^{n-1}$.

This explains why the top-spin theorem has a clean universal form, while the
intermediate-spin profile does not.

The vertical-response theorem is the multiplicity-free edge of the filtration.

---

## 5. Where the simple diagonal fails

For $n=2$ and $n=3$, the tables look like a clean spin-depth diagonal. One is
tempted to conjecture:

> spin $s$ is detected at depth $s-1$.

The length-four table shows that this is false as a full-profile rule.

At $n=4$, the six copies of $V_2$ do not all appear at one depth. Three copies are
detected at depth one, and three more survive to depth two. The five copies of
$V_1$ also split: four are detected at depth one, and one survives to depth two.

Thus the multiplicity space of a fixed spin is itself filtered by probe depth.

The $V_2$ splitting is genuine, not a coincidence of dimensions. Inside the
30-dimensional $V_2$-isotypic part of $K_4$, the depth-one-invisible part is a
15-dimensional $SO(3)$ subrepresentation, properly contained in the full
$V_2$-isotypic part of $K_4$.

So, at the level of $SO(3)$ subrepresentations,

$$
6V_2=(3V_2\ \text{detected at depth }1)\oplus(3V_2\ \text{surviving to depth }2).
$$

This direct-sum splitting is verified by subspace containment in the certificate.

The filtration cuts through multiplicity space cleanly, but not along the naive
spin diagonal.

---

## 6. The open problem

The genuine object is a three-way refinement:

$$
\text{spin}\times\text{multiplicity}\times\text{probe depth}.
$$

For each spin $V_s$, the multiplicity space carries a probe-depth filtration.

Representation-theoretically, the relevant multiplicity space is

$$
\mathrm{Hom}_{SO(3)}(V_s,V^{\otimes n}).
$$

The open problem is to compute the depth-$d$ detected part of this multiplicity
space as a closed function of $n$, $s$, and $d$.

Equivalently, one wants a formula for

$$
\dim\,\mathrm{gr}_d\,\mathrm{Hom}_{SO(3)}(V_s,V^{\otimes n}),
$$

where $\mathrm{gr}_d$ denotes the part first detected at probe depth $d$.

The top-spin case is already solved by the vertical-response theorem: the
multiplicity is one, and the single copy is detected at depth $n-1$.

The intermediate-spin splitting law remains open.

---

## 7. Certificate

The accompanying certificate is

$$
\texttt{certificates/note11_certificate.py}.
$$

It verifies, over exact rational arithmetic:

- the spin-multiplicity tables for $n=2,3,4$;
- the subspace equality $F_{n-2}^{(n)}=S^n_0V$ for $n=2,3,4$;
- for $n=4$, the $V_2$ multiplicity split $6=3+3$ as genuine $SO(3)$
  subrepresentations, not merely as a dimension count.

The expected final line is:

```text
ALL CHECKS PASSED
```

---

## 8. Scope and non-claims

This note does not claim the diagonal rule “spin $s$ is detected at depth
$s-1$” as a general law. It holds in the first small cases only and fails at
$n=4$.

This note does not claim a closed formula for intermediate-spin detection counts.

This note does not prove the full multiplicity-depth filtration for all $n$.

What it does claim is:

1. exact spin-depth tables for $n=2,3,4$;
2. the all-$n$ vertical-response theorem on the highest-spin component;
3. verified top-spin last-survivor equality for $n=2,3,4$;
4. the first genuine multiplicity-depth splitting at $n=4$.

Compression is not disappearance: a residual killed by $m_n$ is stratified by the
depth at which its spin components — and, beginning at $n=4$, copies inside a
single spin component — become visible to probe-depth response.
