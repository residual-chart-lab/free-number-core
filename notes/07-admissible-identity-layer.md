# The Admissible Identity Layer

This note consolidates the admissible identity conditions for generated charts.

It replaces the separate boundary-isomorphism, admissible-equivalence, and
residual-purity notes with a single layer.

The guiding question is:

> What is allowed to count as identity?

The answer has three parts.

| condition | role |
|---|---|
| `BoundaryIso` | controls generated boundary identity |
| `EqAdm` | controls admissible equivalence of generated chart elements |
| `ResidualPurity` | controls retained residual mismatch and forbids inadmissible inference from projection to identity |

Together, these conditions define the admissible identity layer of free numbers.

This note does not prove weak confluence.

This note does not choose a transport implementation.

## 1. Purpose

The local closure of a single chart may have quaternionic form:

$$F_1 \simeq \mathbb{H}.$$

But this local fact does not identify all generated charts inside one global
ambient quaternion algebra.

The global free-number structure is controlled by admissible identity, not by
compressed value alone.

Compression can identify values while leaving generation history, boundary
identity, product tree, insertion response, or residual structure nontrivial.

> Compression is not disappearance.

This note fixes the identity layer that prevents inadmissible collapse.

It sits above local quaternionic closure and below the later transport,
residual-normalization, and weak-confluence stages.

## 2. Compression, projection, and identity

Two generated elements may have the same compressed value:

$$m_n(u) = m_n(v).$$

This does not imply that they are admissibly identical.

Likewise, two elements may have the same projected value:

$$\rho(X) = \rho(Y).$$

This does not imply any of the following:

- $X = Y$;
- $\mathrm{EqAdm}(X,Y)$;
- the residual between $X$ and $Y$ is erased.

Compressed equality and projected equality are value-level facts.

They do not by themselves decide generated identity.

The admissible identity layer exists to make that distinction explicit.

## 3. BoundaryIso: generated boundary identity

A generated chart is not represented only by its local quaternionic value.

It also carries a generated boundary identity. In the notation of the main text,
the boundary of a generated chart is recorded as

$$\partial\gamma = (\alpha, x;\, \beta, y).$$

This record is part of the generated identity.

Here $\alpha$ and $\beta$ denote the two chart-side or term-side positions
involved in the generation event, and $x$ and $y$ denote the boundary data
attached at those positions.

### 3.1 Boundary identity is not algebraic isomorphism

Two local closures may both be quaternionic.

That is not enough to identify their generated boundaries.

The following implication is invalid:

```text
local algebraic isomorphism of H-closures
therefore
boundary identity
```

A boundary identity records how a chart was produced and how it sits in the
global residual structure.

A `BoundaryIso` must preserve that generated identity.

It is not merely an isomorphism of local quaternion algebras.

### 3.2 Definition of BoundaryIso

Let $b$ and $b'$ be generated boundary identities:

$$b=(\alpha,x;\,\beta,y), \qquad b'=(\alpha',x';\,\beta',y').$$

A `BoundaryIso` between $b$ and $b'$ is an invertible admissible correspondence
between generated boundary identities.

Equivalently, it is a structured witness

$$\theta : b \leftrightarrow b'$$

such that both directions preserve the boundary data specified below.

Thus `BoundaryIso` is symmetric:

$$\mathrm{BoundaryIso}(b,b') \quad\Longleftrightarrow\quad \mathrm{BoundaryIso}(b',b).$$

In the orientation-preserving case, it sends the two incidence pairs as generated
boundary positions:

$$(\alpha,x) \mapsto (\alpha',x'), \qquad (\beta,y) \mapsto (\beta',y').$$

If an orientation-reversing boundary correspondence is allowed, it is represented
by an explicit reversal tag. In that case, the reversal swaps the two incidence
pairs:

$$(\alpha,x;\,\beta,y) \leftrightarrow (\beta',y';\,\alpha',x').$$

The reversal tag is involutive and is recorded in both directions.

No reversal is implicit.

No commutativity of boundary generation is assumed.

### 3.3 BoundaryIso preservation requirements

A `BoundaryIso` must preserve the following data.

| data | requirement |
|---|---|
| generated provenance | the generated origin is preserved |
| incidence data | incidence pairs are preserved, up to explicit reversal |
| boundary order | boundary order is preserved, or an explicit reversal tag is recorded |
| attachment labels | boundary attachments remain part of the correspondence |
| compression compatibility | compatible compressed values are required |
| encoded residual information | residual information already encoded in boundary identity is retained |

Incidence-pair exchange and boundary-order reversal are treated as the same
primitive boundary-reversal operation.

There is no second unrecorded reversal.

Compression compatibility is one-way:

$$\mathrm{BoundaryIso}(b,b') \Longrightarrow \text{compatible compressed values}.$$

The converse is not assumed:

$$\text{compatible compressed values} \not\Longrightarrow \mathrm{BoundaryIso}(b,b').$$

`BoundaryIso` does not assert full residual purity.

It only says what it means for generated boundary identities to correspond.

## 4. EqAdm: admissible equivalence before transport

The global free-number structure is defined modulo admissible equivalence:

$$F = \mathrm{Term}_{R} \left( \bigsqcup \text{local closures} \right) /\mathrm{EqAdm}.$$

The quotient is only as meaningful as the equivalence relation `EqAdm`.

If `EqAdm` is too weak, distinct generated histories collapse and residual
structure is lost.

If `EqAdm` is defined through a later normalization or transport step, then it is
no longer an equivalence condition on the structure itself.

It becomes a by-product of a procedure.

This note fixes `EqAdm` as a condition on the candidate correspondence itself,
before any transport implementation is chosen.

### 4.1 Candidate admissible equivalence

Let $T$ be a candidate correspondence between generated chart elements.

`T` is a candidate admissible equivalence when it preserves the structures listed
in this section.

The requirement is not that $T$ becomes admissible after transport or
normalization.

The requirement is that $T$ preserves the listed structures directly.

If $T$ fails any preservation requirement before transport, no later transport
step can make $T$ admissible.

### 4.2 Boundary identity is the shared spine

The preservation requirements are not a flat parallel list.

Unit, local algebra, internal trace, generated-product tree compatibility, and
boundary identity must be compatible with the same generated boundary
correspondence.

Boundary identity is the shared spine of admissible equivalence.

### 4.3 Unit preservation as generated-unit correspondence

For charts $\alpha$ and $\beta$, a candidate equivalence must send the
distinguished local unit of the source to the distinguished local unit of the
target:

$$T(e_{0,\alpha}) = e_{0,\beta}.$$

This is not read as the abstract statement that both units are the same $1$ in
$\mathbb{H}$.

It is read as a generated-unit correspondence.

The generated-unit identity at $\alpha$ corresponds to the generated-unit
identity at $\beta$ under the same admissible boundary correspondence used for
`BoundaryIso`.

Thus unit preservation does not identify units merely because both local closures
are algebraically isomorphic to $\mathbb{H}$.

### 4.4 Local algebra preservation

This requirement concerns only operations internal to a single local chart, where
the local closure has quaternionic form $F_1\simeq\mathbb{H}$.

For elements $x$ and $y$ inside a common local chart $\alpha$:

$$T(x *_\alpha y) = T(x) *_\beta T(y).$$

This is a condition inside the local closure only.

It does not address products that generate a new chart.

For an element $x$ inside a local chart, local conjugation is preserved as

$$T(x^*) = T(x)^*.$$

Conjugation is a local return operation.

Its preservation is a one-variable local condition and does not by itself cross
generated charts.

### 4.5 Internal trace preservation

A candidate equivalence must preserve the local self-consistency trace:

$$Q_\beta(T(x)) = Q_\alpha(x).$$

Here $Q_\alpha$ is the internal local trace form, the internal norm-like quantity
$N_F$ associated with the local chart.

It is not the external projection.

This is an internal trace condition.

It is not a condition on an external projection $\rho$.

In particular,

$$\rho(x)=\rho(y)$$

must not be used to create admissible equivalence.

Equality after projection does not imply `EqAdm`.

Compression compatibility belongs to `BoundaryIso`.

It is not duplicated as a trace condition.

### 4.6 Generated-product tree compatibility

A product that crosses generated charts does not merely produce a value.

It generates a new chart with a generated boundary identity, and the way the
product was formed is part of that identity.

A generated product is therefore indexed by its product tree.

No global associativity is assumed.

The two product trees

$$(XY)Z \qquad \text{and} \qquad X(YZ)$$

may carry different generated boundary identities.

`EqAdm` does not identify them unless an admissible `BoundaryIso` between their
generated boundary identities is provided.

The requirement is therefore stated on trees, not on flat products.

A candidate equivalence $T$ must send each source product tree to an admissibly
corresponding target product tree, so that the generated boundary identity of the
source tree corresponds under `BoundaryIso` to the generated boundary identity of
the target tree.

This condition does not assert that a corresponding target product tree always
exists.

If no admissibly corresponding target product tree exists, then the candidate
correspondence fails the generated-product requirement.

The existence of such corresponding trees is not proved here.

Questions about whether different generated product trees admit a common
admissible target belong to the later weak-confluence stage.

### 4.7 Transport cannot repair failed admissibility

All `EqAdm` preservation requirements are conditions on the candidate
correspondence before transport.

Trace preservation is the sharpest example.

If a candidate correspondence fails to preserve the internal trace $Q_\alpha$
before transport, transport cannot make it admissible.

> Transport cannot repair a failed trace condition.

The same independence holds for unit, local algebra, boundary identity, and
generated-product tree compatibility.

Transport is selected later.

Any later transport implementation must respect an `EqAdm` that is already fixed.

## 5. ResidualPurity: retained mismatch and forbidden inference

`ResidualPurity` is not downstream of `EqAdm` as a definition.

It is complementary to `EqAdm`.

`EqAdm` says when generated chart elements may be identified.

`ResidualPurity` says when a mismatch that is not identified may be retained as a
coherent residual.

### 5.1 Residual signature anchored in a mismatch identity

For a candidate transition $S$ between local closures, the main text records a
residual signature.

In this note, the signature is read as anchored in a generated mismatch identity
$\gamma$:

$$\mathrm{Res}_{\gamma}(S) = (\Delta^e,\Delta^\cdot,\Delta^*,\Delta^Q).$$

This is not a detached tuple.

All four components are measured relative to the same generated mismatch
identity $\gamma$.

The components measure failure to preserve the unit, the multiplication, the
conjugation, and the internal local trace $Q_\alpha$.

The trace component $\Delta^Q$ is internal.

It is measured against $Q_\alpha$ and $N_F$.

It is not measured against an external projection $\rho$ or an external magnitude
defect $\Gamma$.

### 5.2 Purity is not vanishing

If one required

$$\mathrm{Res}_{\gamma}(S)=0$$

for all four components, then $S$ would preserve unit, multiplication,
conjugation, and internal trace.

That is an admissible transition, not a retained residual.

Requiring the signature to vanish erases the residual.

Thus purity cannot be vanishing.

### 5.3 Purity is not arbitrary residual

If every nonzero signature were accepted as pure, then unrelated failures of
unit, multiplication, conjugation, and trace could be combined arbitrarily.

Each combination would generate a retained residual chart.

That would readmit uncontrolled unresolved generation.

Thus purity cannot be arbitrary nonzero residual.

Purity lies between vanishing and arbitrary residual.

### 5.4 The forbidden inference

The danger is not that a projection assigns equal values.

A projection collapsing two elements to the same value is a neutral fact.

The inadmissible step is the inference from projected equality to identity:

```text
rho(X) = rho(Y)
therefore
X = Y
```

or

```text
rho(X) = rho(Y)
therefore
EqAdm(X, Y)
```

or

```text
rho(X) = rho(Y)
therefore
the residual between X and Y is erased
```

These inferences are not admissible.

Projected equality is permitted to occur.

It is not permitted to invalidate a referential mismatch.

> Projected equality must not invalidate referential mismatch.

This is the residual-side counterpart of the equivalence-side statement that
transport cannot repair a failed condition.

There, a procedure was forbidden from creating admissibility.

Here, an inference is forbidden from creating identity.

### 5.5 Coherent witness

A residual signature is pure when it remains a coherent witness of referential
mismatch.

Coherence is internal to the signature.

It is not visibility at some probe depth.

It is not agreement of an external projection.

A signature is a coherent witness when its four components

$$(\Delta^e,\Delta^\cdot,\Delta^*,\Delta^Q)$$

are mutually consistent as the record of a single generated mismatch identity
$\gamma$, rather than an incompatible collection of unrelated failures.

Thus:

> A residual signature is pure when it remains a coherent witness of referential
> mismatch and is not invalidated by projected equality.

Purity is judged from the internal consistency of a signature anchored in the
same generated mismatch identity.

It is not judged from an external projection, and it is not judged from whether
the mismatch becomes visible at a deeper probe.

### 5.6 Referential mismatch as status

The identity being protected is not ordinary equality.

It is the status of a mismatch: two elements that may agree in value while not
agreeing in reference.

```text
same value
does not mean
same reference
```

Residual purity retains this mismatch as structure.

It does not identify across it.

## 6. Dependency structure

The dependency structure is not a single straight ladder.

There is a direct dependency:

$$\mathrm{BoundaryIso} \longrightarrow \mathrm{EqAdm}.$$

`EqAdm` uses `BoundaryIso` as its boundary component and depends on it for
generated-product tree compatibility.

`ResidualPurity` is not defined downstream of `EqAdm`.

It is complementary to `EqAdm`.

| condition | governs |
|---|---|
| `EqAdm` | admissible identification |
| `ResidualPurity` | retained mismatch when identification is not admissible |

The three conditions together provide the identity layer used before weak
confluence.

```text
BoundaryIso
EqAdm
ResidualPurity
then weak confluence later
```

Weak confluence may later ask whether different generated histories or product
trees admit a common admissible target.

That question is not answered here.

## 7. Relation to transport policy

The admissible identity layer is independent of the later implementation of
transport.

Transport may later be represented as a costed reduction step, a transport
normality condition, or a preprocessing relation.

This note does not choose among these.

In every case, any transport implementation must respect the identity layer.

A transport move that identifies elements while failing to preserve
`BoundaryIso`, `EqAdm`, or `ResidualPurity` is not admissible transport.

Thus the dependency direction is:

$$\text{admissible identity layer first} \qquad \text{transport policy later}.$$

Transport may not create identity.

Transport may not repair failed admissibility.

Transport may not erase retained residual mismatch by procedure.

This procedural prohibition is distinct from the inference prohibition in
Section 5.4.

Section 5.4 says that projected equality may not be used to infer identity.

Section 7 says that transport may not procedurally create identity.

## 8. Relation to weak confluence

This note does not prove weak confluence.

It supplies the identity layer that weak confluence must respect.

In particular, this note does not assert:

```text
every source product tree has a corresponding target product tree
```

It only states what must be preserved if such a correspondence is claimed.

The existence of common admissible targets for different generation histories is
a later weak-confluence question.

If weak confluence is later proved, it must use the identity layer without
overriding it.

## 9. Non-claims

This note does not claim:

1. that equality of compressed values implies admissible identity;
2. that equality after external projection implies admissible identity;
3. that algebraic isomorphism of local quaternionic closures is enough for global
   identification;
4. that global associativity holds for generated products;
5. that a corresponding target product tree always exists for every source
   product tree;
6. that a pure residual is a vanishing residual;
7. that every nonzero residual signature is pure;
8. that residual purity is decided by an external projection $\rho$;
9. that residual purity is decided by the magnitude defect $\Gamma$;
10. that residual purity is decided by visibility at some probe depth;
11. that weak confluence follows from the identity layer alone;
12. that this note chooses a transport implementation;
13. that all residual components are classified.

The only claim is that admissible identity for generated charts is controlled by
boundary identity, admissible equivalence, and residual purity, and that none of
these may be replaced by compressed value equality, projected equality, or later
transport normalization.

## 10. Summary

The admissible identity layer answers the question:

> What is allowed to count as identity?

`BoundaryIso` says that generated boundary identities may correspond only through
an invertible admissible correspondence.

`EqAdm` says that generated chart elements may be identified only when unit,
local algebra, internal trace, boundary identity, and generated-product tree
compatibility are preserved before transport.

`ResidualPurity` says that retained residual mismatch is neither erased into
equality nor admitted as arbitrary noise.

A pure residual signature is anchored in a generated mismatch identity $\gamma$.

Its components are coherent as the record of that mismatch, and projected equality
does not invalidate it.

> Projected equality must not invalidate referential mismatch.

The dependency structure is branched, not a single ladder.

$$\mathrm{BoundaryIso}\longrightarrow\mathrm{EqAdm}$$

while `ResidualPurity` is complementary to `EqAdm`.

`BoundaryIso`, `EqAdm`, and `ResidualPurity` are used before weak confluence.

Transport and weak confluence come later.

They must respect this identity layer.
