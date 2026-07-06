# Note 12 — Certified Red and Restricted Weak Confluence

This note fixes the confluence statement for the restricted generated-normalization
core.

The confluence theorem is not stated for a raw reduction relation with arbitrary
independent predicates. It is stated for the certified relation obtained by
putting the `If / Otherwise` structure of generated normalization into the type
of the rule.

The governing principle is:

```text
Do not allow naked folds.
Make every fold carry its certificate.
```

---

## 1. Raw Red is not the target

The current minimal kernel contains abstract placeholders of the form

```text
ExistingBoundary : Boundary -> Boundary -> Prop
FreshBoundary    : Boundary -> Prop
```

If these are treated as arbitrary independent predicates, confluence cannot be
claimed. A raw model could allow both the existing and fresh branches for the
same generated boundary, or it could allow a fold into a boundary whose
certificate is not boundary-isomorphic to the source.

Thus the theorem is not about this raw relation.

The intended generated-normalization clause is:

```text
If the generated chart is admissibly equivalent to an existing chart, fold it.
Otherwise, retain it as a new normalized generated chart.
```

This clause is a single decision, not two unrelated tests.

---

## 2. Certified Red

Let `R` be the finite registry of existing normalized generated boundaries.

For each generated boundary `B`, the certified system uses one decision object:

```text
GenDecision(B, R)
  = existing(B', w)
  | fresh(h)
```

The existing branch carries a witness

```text
w : ExistingFoldWitness(B, B')
```

including the finite certificate data required for a sound fold:

```text
BoundaryIso(cert(B), cert(B'))
ResidualPurity(B, B')
EqAdm(B, B')
boundary-origin preservation
```

The fresh branch carries negative finite evidence:

```text
h : for every B' in R, no ExistingFoldWitness(B, B') exists.
```

`CertifiedRed` is the restricted reduction relation whose generated-boundary
step is driven by this `GenDecision`.

The old predicates `ExistingBoundary` and `FreshBoundary` are recovered only as
projections of this decision object. They are not independent primitives.

---

## 3. BoundaryIso as a finite structural isomorphism

`BoundaryIso` is not semantic equality under all future contexts.

It is a finite structural isomorphism of boundary certificates. The finite
certificate data includes:

```text
boundary ports
structural-origin labels
incidence data
order or reversal tag
attachment data
product-tree addresses
residual-signature-visible sites
```

A `BoundaryIso` witness is a finite correspondence preserving this data.

This immediately gives the structural facts needed below.

### Lemma 12.1 — BoundaryIso is an equivalence relation

`BoundaryIso` is reflexive, symmetric, and transitive.

Proof sketch.

Reflexivity is the identity correspondence on the finite certificate. Symmetry
is obtained by inverting the finite correspondence; the reversal tag is
involutive. Transitivity is composition of finite correspondences, with
preservation of ports, origins, incidence, order data, attachments, tree
addresses, and visible residual sites preserved under composition.

Thus `BoundaryIso` is an equivalence relation on boundary certificates.

---

## 4. Restricted rules

The restricted certified core uses the following rule families.

```text
G1: local multiplication of atoms
G3: generated boundary folds into an existing normalized boundary
G4: generated boundary is retained as a fresh normalized boundary
```

In `CertifiedRed`, G3 and G4 are not independent rules. They are the two
branches of `GenDecision`.

```text
existing(B', w)  gives  gen(B) -> normGen(B')
fresh(h)         gives  gen(B) -> normGen(B)
```

---

## 5. Local structural lemmas

The critical-pair analysis uses three structural lemmas. They are not extra
assumptions on the theorem; they follow from the definitions of the restricted
system and boundary certificates.

### Lemma 12.2 — G1 preserves boundary certificates

An inner G1 step preserves the boundary certificate up to `BoundaryIso`.

```text
B -> B1 by an inner G1 step
implies BoundaryIso(cert(B), cert(B1)).
```

Proof sketch.

G1 is local multiplication inside the chart-level atom algebra. It performs

```text
mul(atom, atom) -> atom
```

inside the local core. It does not rewrite the generated-boundary identity
itself. The boundary certificate records structural origin, incidence,
attachment, order, and visible residual sites. Since G1 is an admissible local
transition with zero residual signature and does not alter the boundary-origin
data, the certificate before and after the inner G1 step is the same up to the
identity `BoundaryIso`.

### Lemma 12.3 — GenDecision is stable under BoundaryIso

If generated boundaries have boundary-isomorphic certificates, then the
generated-boundary decision is stable up to `BoundaryIso`.

```text
BoundaryIso(cert(B), cert(B1))
implies the decisions for B and B1 produce BoundaryIso-compatible results.
```

Proof sketch.

`GenDecision` inspects only the finite certificate data used by
`BoundaryIso`, `EqAdm`, `ResidualPurity`, and boundary-origin preservation. These
checks are invariant under `BoundaryIso` of certificates. This lemma uses Lemma
12.1 to transport witnesses across `BoundaryIso`.

If `B` has an existing fold witness to `B'`, then transport along the
`BoundaryIso(cert(B), cert(B1))` correspondence gives a corresponding existing
fold witness for `B1` to a certificate-isomorphic target. If no existing witness
exists for `B`, then no witness exists for `B1`; otherwise the inverse transport
would produce one for `B`.

Thus the existing and fresh outcomes are stable up to certificate isomorphism.

### Lemma 12.4 — Restricted rule overlaps are exhausted

For the restricted system, every one-step branch is one of the following forms:

```text
G3 / G4 branch on the same generated boundary
two existing targets for the same generated boundary
G1 / G1
inner G1 / outer generated-boundary decision
same rule, same witness
same rule, administratively different witness
```

No other critical-pair shape occurs in the restricted core.

This is a syntactic exhaustion of the listed restricted rules.

---

## 6. Critical pair analysis

### 6.1 G3 / G4 overlap

There is no G3 / G4 critical pair in `CertifiedRed`.

For a fixed generated boundary `B`, `GenDecision(B, R)` has exactly one of the
following forms:

```text
existing(B', w)
fresh(h)
```

It cannot be both. Thus the old `ExistingFreshExclusive` side condition is no
longer an external assumption. It is the shape of the decision object.

### 6.2 Multiple existing targets

If two existing witnesses are available,

```text
existing(B1, w1)
existing(B2, w2)
```

then the witnesses contain

```text
BoundaryIso(cert(B), cert(B1))
BoundaryIso(cert(B), cert(B2)).
```

By Lemma 12.1, the two targets are certificate-isomorphic:

```text
BoundaryIso(cert(B1), cert(B2)).
```

Thus multiple existing targets do not create a certificate-level obstruction.

### 6.3 G1 / G1

There is no nontrivial nested G1 / G1 overlap in the atom-level local
multiplication rule. Atoms are leaves for this restricted rule.

Parallel G1 steps either coincide or commute by disjointness of support. Hence
G1 / G1 branches are locally joinable.

### 6.4 Inner G1 / outer generated-boundary decision

The remaining nontrivial shape is an inner G1 step inside a generated boundary
together with an outer generated-boundary decision.

By Lemma 12.2, the inner G1 step preserves the boundary certificate up to
`BoundaryIso`. By Lemma 12.3, the generated-boundary decision is stable under
that certificate isomorphism.

Therefore reducing inside first or deciding the generated boundary first gives
certificate-isomorphic results.

---

## 7. Local confluence

### Proposition 12.5 — Local confluence of restricted CertifiedRed

Restricted `CertifiedRed` is locally confluent up to `BoundaryIso` on boundary
certificates.

Proof.

By Lemma 12.4, the critical-pair shapes are exhausted by the cases in Section 6.
G3 / G4 overlap is impossible by `GenDecision`. Multiple existing targets are
joined by Lemma 12.1. G1 / G1 branches are trivial or parallel. Inner G1 / outer
generated-boundary branches are joined by Lemmas 12.2 and 12.3.

Thus every one-step branch is joinable up to `BoundaryIso` on boundary
certificates.

---

## 8. Restricted weak confluence

Termination of the restricted generated-normalization core was already supplied
by the strict decrease measure for restricted `Red`.

Using that prior termination result, Newman-style reasoning gives the main
theorem.

### Theorem 12.6 — Restricted weak confluence for CertifiedRed

Restricted `CertifiedRed` is weakly confluent up to `BoundaryIso` on boundary
certificates.

Equivalently:

```text
If CertifiedRed X Y and CertifiedRed X Z,
then there exist Y', Z' such that
CertifiedRedStar Y Y',
CertifiedRedStar Z Z',
and BoundaryIso(cert(Y'), cert(Z')).
```

Proof.

By the prior termination theorem, restricted `CertifiedRed` is terminating. By
Proposition 12.5, it is locally confluent up to `BoundaryIso` on boundary
certificates. Therefore, by Newman-style reasoning, it is weakly confluent up to
`BoundaryIso` on boundary certificates.

---

## 9. Decidability of the generated-boundary decision

Logical confluence is separate from computability of the decision procedure.

For an executable normalization engine, one needs:

```text
GenDecisionComputable:
  for every generated boundary B and finite registry R,
  GenDecision(B, R) is computable.
```

The route is finite.

```text
BoundaryCertificateFinite
BoundaryIsoDecidable
EqAdmDecidable
ResidualPurityDecidable
ExistingFoldWitnessDecidable
FreshDecisionDecidable over finite registries
```

### 9.1 BoundaryIso decidability

Since `BoundaryIso` is a finite structural isomorphism of finite boundary
certificates, it is decidable by finite search over finite correspondences.

The search checks preservation of finite data:

```text
ports
structural origins
incidence
order or reversal tag
attachment data
tree addresses
visible residual sites
```

Each component has decidable equality, and the certificate is finite.

### 9.2 EqAdm decidability

`EqAdm` remains decidable when it is restricted to the intended finite
preservation checks:

```text
unit preservation
local multiplication preservation
conjugation preservation
trace preservation
boundary preservation
```

The boundary part uses `BoundaryIso`. The local algebraic checks take place in
the finite syntactic presentation of the local chart data and the quaternionic
core used by the restricted kernel.

The definition must not be enlarged to mean equality under all future contexts.
That would change the problem.

### 9.3 Fresh decision

Freshness is the negative branch:

```text
fresh(B, R) iff for every B' in R, no ExistingFoldWitness(B, B') exists.
```

Because `R` is finite and `ExistingFoldWitness` is decidable, freshness is
decidable by finite search.

Thus `GenDecision` is computable for finite registries.

---

## 10. What is proved, and what remains deferred

This note separates three levels.

### Logical confluence

For `CertifiedRed`, restricted weak confluence up to `BoundaryIso` follows from
the certified decision structure, the local structural lemmas above, and the
prior termination theorem.

This is the main result of the note.

### Principle of computability

If boundary certificates are represented as finite structural data and
`BoundaryIso`, `EqAdm`, and `ResidualPurity` are implemented as finite checks,
then `GenDecision` is computable.

Thus the certified normalization engine is executable in principle.

### Formal implementation

The current minimal Lean kernel does not yet implement the full decision
procedure for `BoundaryIso`, `EqAdm`, `ResidualPurity`, or `GenDecision`.

That formalization is deferred.

The deferred item is not the mathematical confluence theorem for
`CertifiedRed`; it is the full machine-checked implementation of the decision
procedure and its soundness proofs.

---

## 11. Non-claims

This note does not claim:

```text
confluence for RawRed with arbitrary ExistingBoundary and FreshBoundary;
syntactic confluence of all terms;
trace-level confluence;
transport-inclusive confluence;
decidability of semantic equality under all contexts;
completed Lean formalization of BoundaryIso / EqAdm / GenDecision.
```

It claims the restricted certificate-level confluence theorem for `CertifiedRed`,
and the finite-data route by which the certified decision can be made computable.

---

## 12. Summary

The confluence problem is resolved at the certified level.

The old G3 / G4 critical pair disappears when the `If / Otherwise` structure is
represented as a single `GenDecision`. Existing folds carry their
`BoundaryIso`-sound witnesses. Freshness is the certified absence of such a
witness in a finite registry.

BoundaryIso is an equivalence relation because it is finite structural
isomorphism. G1 preserves boundary certificates because it is a local admissible
transition that does not touch boundary-origin data. GenDecision is stable under
BoundaryIso because it inspects only BoundaryIso-invariant finite certificate
data.

Therefore restricted `CertifiedRed` is weakly confluent up to
boundary-certificate isomorphism.

The next engineering step is not another confluence theorem. It is the concrete
finite decision procedure for boundary certificates.

```text
Do not allow naked folds.
Make every fold carry its certificate.
```
