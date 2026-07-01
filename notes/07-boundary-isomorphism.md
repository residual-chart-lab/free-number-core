# Boundary Isomorphism and Generated Boundary Identity

This note isolates the boundary-isomorphism condition needed before admissible
equivalence and transport can be restored.

The purpose is narrow.

Boundary isomorphism is not an isomorphism of quaternion algebras.  
It is an admissible correspondence between generated boundary identities.

This distinction protects the local/global separation of free numbers.

## 1. Purpose

The local closure of a single chart may have quaternionic form:

```text
F_1 ~= H
```

But this local fact does not identify all generated charts inside one global
ambient quaternion algebra.

A generated chart carries boundary data.  
That boundary data records how the chart was produced, where it attaches, and
which generated identity it inherits.

BoundaryIso is introduced to say when two such generated boundary identities may
be regarded as the same boundary identity.

Its role is upstream of both reduction and transport.

Later reduction systems, admissible equivalences, and transport policies must
respect this boundary-identity condition.

## 2. Generated boundaries

A generated chart is not represented only by its local quaternionic value.

It also carries a generated boundary identity. In the notation of the main text,
the boundary of a generated chart is recorded as

```text
partial gamma = (alpha, x; beta, y)
```

This record is part of the generated identity.

Here `alpha` and `beta` denote the two chart-side or term-side positions involved
in the generation event, and `x` and `y` denote the boundary data attached at
those positions.

This note does not need to expand the internal construction of `alpha`, `beta`,
`x`, or `y`. It uses only the fact that the four-part record is part of the
identity of the generated boundary.

Thus a generated boundary is not merely a value in `H`.

It is a boundary identity with provenance.

## 3. Boundary identity versus algebraic isomorphism

Two local closures may both be quaternionic.

That is not enough to identify their generated boundaries.

The following implication is invalid:

```text
local algebraic isomorphism of H-closures
therefore
boundary identity
```

The local algebraic form records what each chart looks like after local closure.

The generated boundary identity records how that chart was produced and how it
sits in the global residual structure.

A BoundaryIso must preserve the generated identity, not merely the algebraic
shape of the local closure.

In particular, equality of compressed values is not sufficient.

```text
m_n(u) = m_n(v)
```

does not imply that `u` and `v` have the same generated boundary identity.

Compression can identify values while leaving boundary history, insertion
response, or residual structure nontrivial.

## 4. Definition of BoundaryIso

Let `b` and `b'` be generated boundary identities.

Write their boundary records as

```text
b  = (alpha,  x; beta,  y)
b' = (alpha', x'; beta', y')
```

A BoundaryIso between `b` and `b'` is an invertible admissible correspondence
between generated boundary identities.

Equivalently, it is a structured witness

```text
theta : b <-> b'
```

such that both directions preserve the boundary data specified in Section 5.

Thus BoundaryIso is a symmetric relation:

```text
BoundaryIso(b, b') iff BoundaryIso(b', b)
```

The witness `theta` sends boundary incidence pairs to boundary incidence pairs.

In the orientation-preserving case, it sends

```text
(alpha, x) to (alpha', x')
(beta,  y) to (beta',  y')
```

as generated boundary positions, not merely as algebraic values.

If an orientation-reversing boundary correspondence is allowed, it is represented
by an explicit reversal tag. In that case, the reversal swaps the two incidence
pairs:

```text
(alpha, x; beta, y) <-> (beta', y'; alpha', x')
```

The reversal tag is involutive and is recorded in both directions. It does not
destroy the symmetry of BoundaryIso.

Thus BoundaryIso is a structured relation:

```text
BoundaryIso(b, b')
```

means

```text
b and b' have admissibly corresponding generated boundary identities
```

not

```text
the local quaternion algebras around b and b' are isomorphic
```

## 5. Preservation requirements

This is the main constraint of the note.

A BoundaryIso must preserve exactly the boundary information needed for later
admissible equivalence, without prematurely assuming residual purity or
confluence.

The preservation requirements are the following.

### 5.1 Generated provenance

Generated boundaries must correspond to generated boundaries.

A generated boundary may not be identified with a primitive, forgotten, or
structureless boundary unless the generation record itself provides an
admissible correspondence.

In particular, the fact that two boundary words compress to the same quaternionic
value does not erase their provenance.

### 5.2 Incidence data

The incidence of the boundary record must be preserved.

For

```text
partial gamma = (alpha, x; beta, y)
```

the correspondence must preserve which boundary datum is attached to which
chart-side or term-side position.

In the orientation-preserving case, `(alpha, x)` corresponds to `(alpha', x')`
and `(beta, y)` corresponds to `(beta', y')`.

In the orientation-reversing case, the single reversal operation swaps the two
incidence pairs.

There is no separate unrecorded exchange of incidence data.

### 5.3 Boundary order and reversal

The ordered boundary form

```text
(alpha, x; beta, y)
```

is part of the identity.

A BoundaryIso must preserve this order unless a single explicit boundary-reversal
tag is present.

This note treats incidence-pair exchange and boundary-order reversal as the same
primitive reversal operation at the boundary level.

No order reversal is implicit.

No commutativity of boundary generation is assumed.

### 5.4 Attachment labels

Attachment labels must correspond as labels, not only through their compressed
values.

If `x` is an attachment datum at `alpha`, then `theta(x)` must be the
corresponding attachment datum at `alpha'` in the orientation-preserving case, or
at the reversed incidence position in the orientation-reversing case.

The same applies to `y`.

This requirement prevents a boundary correspondence from discarding the
attachment event and retaining only the resulting local algebraic value.

### 5.5 Compression compatibility

BoundaryIso is stronger than equality after compression, but it must still be
compatible with compression.

If a generated boundary correspondence is admissible, then recompressing
corresponding boundary words must give compatible quaternionic values under the
local identifications already assigned to the two charts.

In schematic form:

```text
BoundaryIso(b, b') implies compatible compressed values
```

The converse is not assumed.

```text
compatible compressed values do not imply BoundaryIso(b, b')
```

### 5.6 Residual status encoded in the boundary identity

A BoundaryIso must preserve residual information only insofar as that information
is already encoded in the generated boundary identity.

It must not erase residual markers, generated-history tags, or boundary
distinctions that are present in the boundary record.

However, this note does not assert full residual purity.

It does not require preservation of every possible response profile.

It does not classify all residual components.

Those conditions belong to later residual-purity and confluence stages.

## 6. Relation to admissible equivalence

EqAdm is the later admissible-equivalence criterion.

Operationally, EqAdm is expected to preserve several structures, including:

```text
unit
multiplication
conjugation
trace
boundary identity
```

This note supplies the boundary component of that list.

A candidate admissible equivalence satisfies the boundary requirement only if it
sends generated boundary identities to BoundaryIso-generated boundary identities.

In schematic form:

```text
EqAdm(f) requires BoundaryIso(b, f(b)) for generated boundary identities b
```

Thus BoundaryIso is an upstream condition for EqAdm.

It is not derived from EqAdm after the fact.

## 7. Independence from transport implementation

BoundaryIso is independent of the later implementation of transport.

Transport may later be represented in one of several ways:

```text
costed reduction step
transport normality condition
preprocessing relation
```

This note does not choose between those options.

In all cases, any transport implementation must preserve BoundaryIso.

Thus the dependency direction is:

```text
BoundaryIso first
transport policy later
```

not

```text
transport policy first
BoundaryIso later
```

A transport move that identifies boundaries while failing to preserve generated
boundary identity is not admissible transport.

## 8. Non-claims

This note does not claim:

1. that algebraic isomorphism of local quaternionic closures is enough for global
   identification;
2. that equality of compressed values implies boundary identity;
3. that BoundaryIso is a reduction rule;
4. that BoundaryIso chooses a transport implementation;
5. that full residual purity has been proved;
6. that all residual components are classified;
7. that weak confluence follows from BoundaryIso alone.

The only claim is that generated boundary identity must be preserved before
later admissible equivalence or transport can identify generated charts.

## 9. Summary

Boundary isomorphism is not algebraic isomorphism.

It is an invertible admissible correspondence between generated boundary
identities.

The boundary record

```text
partial gamma = (alpha, x; beta, y)
```

is part of the generated identity.

A BoundaryIso must preserve provenance, incidence, boundary order, attachment
labels, and compression compatibility.

A single explicit reversal tag may reverse the boundary order by swapping the two
incidence pairs, but no reversal is implicit.

BoundaryIso must not erase residual information already present in the boundary
identity.

This gives the boundary-preservation component needed before EqAdm, transport
policy, residual purity, and weak confluence can be addressed.
