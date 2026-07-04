# Free Numbers: Depth-One Detection in Length Three

Let `V = Im H` be the space of imaginary quaternions, with basis `i, j, k`.
For length three, the boundary-word space is

```text
B_3 = V ⊗ V ⊗ V.
```

The reversed compression map

```text
m_3(a | b | c) = c b a
```

has a large kernel. The vertical-response theorem detects the top-spin part
`S^3_0 V ≅ V_3` of this kernel at depth two. This note records what happens one
depth earlier: the depth-one insertion profile detects exactly the remaining,
non-top-spin part of the kernel.

The main statement is

```text
K_3 ∩ ker D_3 = S^3_0 V,
```

where `K_3 = ker m_3` and `D_3` is the full depth-one profile.

Thus, in length three, the residual kernel is completely detected by depths one
and two:

```text
depth 1 detects  2V_1 ⊕ 2V_2,
depth 2 detects  V_3.
```

## 1. Compression in length three

Let

```text
V = Im H = span_R{i, j, k},
```

with quaternion multiplication on imaginary elements

```text
uv = -(u · v) + (u × v).
```

The length-three boundary-word space is

```text
B_3 = V^{⊗3},
```

with basis words written

```text
a | b | c.
```

The reversed compression map is

```text
m_3 : B_3 → H,
m_3(a | b | c) = c b a.
```

Let

```text
K_3 = ker m_3.
```

The map `m_3` is `SO(3)`-equivariant and surjective onto

```text
H ≅ V_0 ⊕ V_1.
```

For example, it has nonzero scalar and imaginary outputs:

```text
m_3(i | j | k) = k j i = 1,
m_3(i | i | i) = i i i = -i.
```

Hence

```text
rank m_3 = 4,
dim K_3 = 27 - 4 = 23.
```

## 2. The representation decomposition

The standard Clebsch-Gordan decomposition gives

```text
V_1 ⊗ V_1 = V_0 ⊕ V_1 ⊕ V_2.
```

Therefore

```text
V^{⊗3}
  = (V_1 ⊗ V_1) ⊗ V_1
  = (V_0 ⊕ V_1 ⊕ V_2) ⊗ V_1
  = V_0 ⊕ 3V_1 ⊕ 2V_2 ⊕ V_3.
```

Since `m_3` is `SO(3)`-equivariant, Schur's lemma separates the calculation
by isotypic component. The target contains only `V_0` and `V_1`, so the `V_2`
and `V_3` source components lie in the kernel. The scalar example

```text
m_3(i | j | k) = 1
```

shows that the unique source copy of `V_0` maps nontrivially to the target
`V_0`, hence is not in the kernel. The imaginary example

```text
m_3(i | i | i) = -i
```

shows that the map from the `3V_1` isotypic component to the target `V_1` is
nonzero. By Schur's lemma this map has rank one on the multiplicity space, so its
kernel inside `3V_1` is `2V_1`.

Therefore

```text
K_3 ≅ 2V_1 ⊕ 2V_2 ⊕ V_3.
```

The top-spin summand is

```text
V_3 ≅ S^3_0 V,
```

the symmetric trace-free tensors of rank three. Its dimension is

```text
dim S^3_0 V = 2·3 + 1 = 7.
```

## 3. The depth-one profile

There are two internal gaps in a length-three word. The depth-one profile inserts
one probe variable into either gap and then compresses.

For a basis word `a | b | c`, define

```text
D_3^{(1)}(a | b | c)(x) = c b x a,
D_3^{(2)}(a | b | c)(x) = c x b a,
```

where `x ∈ V`.

The full depth-one profile is

```text
D_3 = (D_3^{(1)}, D_3^{(2)})
    : B_3 → Hom(V, H) ⊕ Hom(V, H).
```

Equivalently,

```text
D_3 : B_3 → 2(H ⊗ V).
```

Since

```text
H ⊗ V
  ≅ (V_0 ⊕ V_1) ⊗ V_1
  ≅ V_0 ⊕ 2V_1 ⊕ V_2,
```

the target of `D_3` decomposes as

```text
2(H ⊗ V) ≅ 2V_0 ⊕ 4V_1 ⊕ 2V_2.
```

In particular, the target contains no `V_3`. Since `D_3` is `SO(3)`-equivariant,
every source summand of type `V_3` maps to zero. In length three, the source has
a unique `V_3` summand, namely

```text
S^3_0 V ≅ V_3.
```

Hence

```text
S^3_0 V ⊂ ker D_3.
```

Also, since `m_3` has target `V_0 ⊕ V_1`, the same top-spin summand lies in the
compression kernel:

```text
S^3_0 V ⊂ K_3.
```

Therefore

```text
S^3_0 V ⊂ K_3 ∩ ker D_3.
```

The question is whether anything else remains invisible at depth one.

## 4. Exact rank computation

Use the ordered basis

```text
{i, j, k}^{⊗3}
```

for `B_3`, and the ordered basis

```text
{1, i, j, k}
```

for `H`.

The matrices of `m_3` and `D_3` in these bases have integer entries. Direct
row-reduction over `Q` gives

```text
rank m_3 = 4,
rank D_3|_{K_3} = 16.
```

Equivalently,

```text
dim(K_3 ∩ ker D_3) = dim K_3 - rank(D_3|_{K_3})
                   = 23 - 16
                   = 7.
```

A second exact check identifies the seven-dimensional kernel with the harmonic
subspace. The symmetric tensors in `S^3 V` have dimension `10`; imposing the
three trace equations gives

```text
dim S^3_0 V = 7.
```

The inclusion

```text
S^3_0 V ⊂ K_3 ∩ ker D_3
```

and the equality of dimensions therefore imply equality of subspaces:

```text
K_3 ∩ ker D_3 = S^3_0 V.
```

The computation is exact: no numerical approximation is involved. An accompanying
SymPy certificate can reproduce these ranks and the subspace equality over the
rationals.

## 5. Main proposition

**Proposition (Depth-one detection in length three).** Let

```text
K_3 = ker m_3 ⊂ V^{⊗3}
```

and let

```text
D_3 : V^{⊗3} → Hom(V,H) ⊕ Hom(V,H)
```

be the full depth-one insertion profile. Then

```text
K_3 ∩ ker D_3 = S^3_0 V.
```

Equivalently, the only length-three residuals invisible both to compression and
to every depth-one insertion probe are the highest-spin harmonic tensors.

*Proof.* We already have

```text
S^3_0 V ⊂ K_3 ∩ ker D_3
```

because neither `m_3` nor `D_3` has a `V_3` target component.

By exact row-reduction,

```text
dim(K_3 ∩ ker D_3) = 7.
```

But

```text
dim S^3_0 V = 7.
```

Hence the inclusion is an equality:

```text
K_3 ∩ ker D_3 = S^3_0 V. ∎
```

## 6. Consequence: complete detection of `K_3`

The kernel decomposes as

```text
K_3 ≅ 2V_1 ⊕ 2V_2 ⊕ V_3.
```

The proposition says that the depth-one profile misses exactly the `V_3` summand.
Therefore it detects the whole non-top-spin part:

```text
D_3 detects  2V_1 ⊕ 2V_2.
```

The vertical-response theorem gives the depth-two response on the top-spin
component:

```text
A_3(S) = 4 C_S,     S ∈ S^3_0 V.
```

Since `C` is injective, depth two detects the remaining `V_3`.

Thus the length-three residual kernel is completely detected by depths one and
two:

```text
K_3 = (2V_1 ⊕ 2V_2) ⊕ V_3,
```

with

```text
depth 1 detecting  2V_1 ⊕ 2V_2,
depth 2 detecting  V_3.
```

This is the first complete spin-depth profile.

## 7. Multiplicity-space refinement

The statement above is independent of a choice of basis in the multiplicity
spaces. In particular, on the `V_2`-isotypic part of `K_3`,

```text
(K_3)_{V_2} ≅ 2V_2,
```

the depth-one response induces an injective map of `SO(3)`-modules into the
`V_2`-isotypic part of the target

```text
2(H ⊗ V) ≅ 2V_0 ⊕ 4V_1 ⊕ 2V_2.
```

Equivalently, after choosing bases of the two multiplicity spaces, the `V_2`
response is represented by a full-rank `2 × 2` matrix.

The concrete entries of that matrix depend on the chosen multiplicity bases. The
basis-free statement is the rank statement: the depth-one response is injective
on the `V_2`-isotypic part of `K_3`.

The same applies to the `V_1`-isotypic part:

```text
(K_3)_{V_1} ≅ 2V_1,
```

which is also detected at depth one.

## 8. Summary

Length three has the first nontrivial residual kernel:

```text
K_3 ≅ 2V_1 ⊕ 2V_2 ⊕ V_3.
```

Compression kills all of it. The depth-one insertion profile recovers exactly the
intermediate-spin part,

```text
2V_1 ⊕ 2V_2,
```

and misses exactly the top-spin part,

```text
V_3 = S^3_0 V.
```

The top-spin part is then recovered by the depth-two vertical response,

```text
A_3(S) = 4 C_S.
```

So, in length three, the probe-depth filtration is complete:

```text
depth 1:  intermediate spins,
depth 2:  top spin.
```

The top-spin theorem is therefore not an isolated phenomenon. It is the upper
edge of a spin-depth visibility profile already visible in length three.
