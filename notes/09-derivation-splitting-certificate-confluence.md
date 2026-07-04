# Note 09 — Derivation Splitting and Certificate-Level Confluence

This note sets up the confluence question for the restricted `Red` system and
fixes the level at which it should be asked.

Transport is not part of `Red`. It was separated in the transport-policy note, so
the confluence question here concerns the restricted reduction relation alone.

The organizing idea is a single move. A derivation is not projected onto a
coarser object that forgets how it was formed; it is *split*, without loss, into
two coordinates — a boundary certificate and a residual trace. Confluence is
stated on the first coordinate. The second coordinate is retained by the shape of
the object, not by an external reminder. The residual trace is defined so that it
is neither the full derivation path nor a bare multiset, but a dependency-aware
trace over the certificate; this is what makes the splitting, if proved, an
information-preservation statement rather than bookkeeping.

## 1. Scope

This note does not prove confluence. It fixes the level at which the restricted
confluence question is well posed, and states the resulting proof obligations.

Syntactic confluence,

```text
Red X Y and Red X Z  implies  Y = Z,
```

is too strong: fresh generated boundaries may carry different labels or arise
through different admissible presentations. The intended target is confluence up
to `BoundaryIso` on boundary certificates, where `BoundaryIso` is the admissible
identity relation of Note 07, applied to certificates and not redefined here.

Trace-level confluence is not asserted anywhere in this note.

## 2. Why a projection is refused

A standard rewriting development introduces a forgetful map

```text
π : Derivation → NormalData,
```

treats two derivations with `π(d₁) = π(d₂)` as the same for the theorem's
purposes, and does not study the fiber of `π`.

Free numbers cannot take this as harmless. The governing principle of the
framework is that a collapse of values is not a disappearance of structure. If
derivations were projected onto a certificate and the fiber ignored, the residual
events produced along a derivation would be silently treated as immaterial —
exactly the collapse the residual side exists to prevent.

So the note does not begin with a forgetful projection. It begins with a
splitting, and the burden it accepts is to show that the splitting loses nothing.

## 3. Boundary certificates

The `BoundaryCertificate` of a derivation records the surviving
generated-boundary identity: the ordered boundary data, the incidence structure,
the attachment data, the product-tree shape, and the local provenance relevant to
the generated boundary. It records neither fresh label names, nor
reduction-path noise, nor the full derivation log.

A fresh-label change does not change the certificate. A product-tree or provenance
change may change it. The certificate is thus neither a raw label nor a full
history; it is the surviving boundary identity carrying exactly the local
structure needed to prevent inadmissible collapse. It is the level at which
`BoundaryIso` is tested.

The certificate is the admissible, boundary-identity coordinate of the
derivation. It and the residual trace of the next sections are not complementary
subsets of the derivation log — not "what survived" against "what was removed" —
but two coordinates extracted by different criteria, the second typed over the
first. That they are non-degenerate rather than complementary is made an explicit
obligation in §9.

## 4. Residual event schemas and their independence

The residual trace is built from residual events. These are not a new primitive:
they are the residual transitions the framework already has. But they are taken
as *schemas* over a certificate, not as tokens extracted from a particular
derivation — otherwise defining the trace would already require reading off the
whole derivation the splitting is meant to analyze.

**Residual event schemas.** A step of a derivation is either an admissible
transition, which preserves the required structure, or a residual transition,
whose residual signature

```text
Res(S) = (Δe, Δmul, Δstar, ΔQ)
```

is nonzero. Over a certificate `c`, the residual events

```text
ResidualEvent_c
```

form an *alphabet* of residual-step occurrence schemas. Each schema `e` is
determined by its rule tag, its anchor site over `c`, its support footprint
`support_c(e)`, and its nonzero residual signature `ResSig(e)`. A schema is a
kind of residual event that can occur over `c`, not a logged occurrence: the same
schema may occur several times in one derivation, and a derivation's residual
trace is a *word* over this alphabet, so the multiplicity `a a` is retained and
not collapsed to a set.

Two schemas with the same rule tag and residual signature but different support
are different letters of the alphabet. Only when rule tag, anchor, support, and
residual signature all coincide are they the same schema `a`.

**Support.** The footprint `support_c(e)` records where `e` acts on the
certificate: the boundary and product-tree positions it reads, the positions it
writes or fixes, the signature positions where its residual arises, and the
product-tree nodes it touches. Product-tree positions are structural addresses
inside `c` — node, port, and the minimal ancestry slice needed to identify the
product-tree position — not compressed values. Thus `(XY)Z` and `X(YZ)` occupy
different tree sites even where their values agree, and non-associativity is
preserved; and the ancestry recorded is the minimal slice that fixes the
product-tree identity, not the whole history and not the whole certificate.

**Independence.** Two schemas are independent over `c` when they are distinct and
their footprints do not interfere:

```text
I_c(a, b)   iff   a ≠ b   and   support_c(a) # support_c(b),
```

where `#` is symmetric non-interference: neither writes a site the other writes,
neither writes a site the other reads, their residual-signature sites are
disjoint or dependency-compatible, and neither lies in the causal ancestry the
other needs. So defined, `I_c` is symmetric, irreflexive (`not I_c(a, a)`: a
schema shares its own support, hence depends on itself, so a repeated schema
`a a` never commutes with itself), and local (it depends only on the two
footprints). These are exactly the independence axioms a trace monoid requires.

Incidence-disjointness of the underlying boundaries is a useful intuition for
`#`, but the formal condition is non-interference of read, write, residual, and
product-tree support. All of this is read off existing structure — residual
events from the admissible/residual distinction, support from the certificate's
structural addresses — with no new primitive introduced.

## 5. The residual trace

The `ResidualTrace` of a derivation records its residual events. It is *not* the
full derivation log — that distinction is the whole point.

If the trace were defined as all information not in the certificate,

```text
d = (cert(d), everything-else(d)),
```

the splitting would be a tautology, not a theorem. If instead the trace forgot
all order, keeping only which residual signatures occurred and how often — a bare
multiset — it would generally be too weak, identifying derivations that the
kernel keeps distinct.

The intended level is between the two. Over a certificate `c`, the residual trace
is the partially commutative trace on the alphabet `ResidualEvent_c`: words of
residual event schemas, with only independent neighbours allowed to commute.

```text
ResidualTraceOver(c)
  = FreeMonoid(ResidualEvent_c)
    / adjacent swaps of I_c-independent events.
```

This is the trace monoid — equivalently the dependency heap — of residual events
over `c`. Because it is a word quotient and not a set, a schema occurring twice
survives as `a a`; because `I_c` is irreflexive, such a repetition never commutes
away. It keeps dependency-relevant order and quotients only administrative
ordering. The three levels line up as:

- full derivation word — keeps all order — too strong;
- multiset of residual signatures — forgets all order — too weak;
- trace monoid over `c` — keeps dependency order, commutes only independent
  events — the intended level.

The residual trace is the residual, non-collapsible coordinate of the derivation.

## 6. Administrative equivalence

Administrative equivalence is fixed *after* the independence relation, not before,
so that it cannot silently decide which trace information matters.

With `I_c` fixed, administrative equivalence is generated by fresh-label
renaming, adjacent swaps of `I_c`-independent residual events, and commuting
conversions that change neither the boundary certificate nor the element of the
residual trace monoid. An exchange is thus admissible only when it preserves both
coordinates:

```text
BoundaryCertificate  and  ResidualTraceOver(c).
```

Administrative equivalence is downstream of the trace structure. It is not a
licence to erase history.

## 7. The derivation splitting

The intended structure is a dependent splitting:

```text
Derivation / ~admin
  ≃
Σ c : BoundaryCertificate, ResidualTraceOver(c).
```

A derivation, modulo administrative equivalence, is intended to be recoverable
from its certificate `c` together with its residual trace over `c`. The dependent
form matters: the trace is not an independent object beside the certificate but a
trace *over* it. Informally one may write

```text
Derivation / ~admin  ≃  BoundaryCertificate ⋉ ResidualTrace,
```

but the formal shape is the dependent sum above. The splitting is the
derivation-level lift of the admissible/residual distinction: the admissible part
becomes the certificate, the residual part becomes the trace over it.

Stating this as an isomorphism rather than as a projection with a remembered
fiber is the substance of the note. Under a projection the collapsed multiplicity
disappears the moment the fiber stops being read, and becomes nothing through the
accumulation of not reading it. Under the splitting there is no such moment: the
trace is the second coordinate, present by the type of the object, and the
inverse map reconstructs the derivation. There is nothing one must remember to
look at, because nothing has been put out of sight.

## 8. What makes the splitting nontrivial

The splitting is meaningful only if the trace is strictly smaller than the full
log and still sufficient, with the certificate, to recover the derivation. This
is the difficulty, and it is a two-sided one:

- if the trace is too strong (the whole remaining path), the splitting is
  tautological;
- if the trace is too weak (a bare multiset), injectivity fails — distinct
  derivations share a certificate and a trace.

The trace-monoid level is the claimed middle point. Whether it actually sits at
that point is not assumed; it is the content of the obligations below. If proved,
the splitting is an information-preservation theorem for an operation that looks
like forgetting.

## 9. Proof obligations

The splitting is stated as the intended structure, not as an established
bijection. It carries the following obligations.

**Swap soundness.** If `I_c(a, b)`, then the two local derivation fragments
`… a ; b …` and `… b ; a …` are administratively equivalent: the swap preserves
both the boundary certificate and the element of `ResidualTraceOver(c)`. This is
the safety direction — it checks that `I_c` is not too permissive, that no swap it
licenses changes either coordinate.

**Swap completeness.** If two derivations have the same certificate and the same
trace-monoid element, then their administrative paths are connected by
`I_c`-swaps and fresh-label renaming. This is the completeness direction — it
checks that `I_c` is not too strict, and it is the substance of injectivity.

**Well-definedness.** For every derivation `d`, the data `cert(d)` and `trace(d)`
are well defined modulo administrative equivalence.

**Injectivity — no hidden collapse.** If `cert(d₁) = cert(d₂)` and
`trace(d₁) = trace(d₂)`, then `d₁ ~admin d₂`. Failure means certificate and trace
together miss some derivation-relevant structure — the trace is too weak.
(Injectivity is exactly what swap completeness delivers.)

**Surjectivity — no phantom pairs.** Every admissible pair `(c, t)` is realized by
some derivation `d` with `cert(d) = c` and `trace(d) = t`. Failure means the trace
permits combinations the reduction system cannot produce.

**Coordinate non-degeneracy.** The splitting must not be a complement
decomposition. The certificate is not defined as the non-trace part of a
derivation, and the trace is not defined as the derivation log remaining once the
certificate is removed; the trace coordinate is defined positively, as the trace
monoid of residual-event schemas over the certificate. Although
`ResidualTraceOver(c)` depends on `c`, the certificate must not determine the
trace: the dependence is type-level indexing (the trace is typed over `c`), not
value-level determination (`c` fixing the trace). Concretely, one certificate must
carry genuinely different traces, and one trace element must sit over different
certificates. Without this, `Σ c, ResidualTraceOver(c)` collapses to a disguised
projection and the splitting is the tautology of §8, not an information-
preservation statement.

**BoundaryIso compatibility.** When two certificates correspond under
`BoundaryIso`, their residual trace structures are transportable only where the
relevant residual-event dependencies are preserved. This note records the
obligation; it does not assert transportability in general.

## 10. Certificate-level confluence

With the splitting in place, the restricted confluence target is stated on the
first coordinate:

```text
If Red X Y and Red X Z, then there exist Y', Z' with
  RedStar Y Y', RedStar Z Z', and BoundaryIso(cert(Y'), cert(Z')).
```

The theorem speaks only about certificates. It does not assert
`trace(Y') = trace(Z')`, nor that derivations with corresponding certificates
carry the same trace. Certificate-level confluence does not imply trace-level
confluence.

## 11. One-step branch analysis

For one-step branching `Red X Y` and `Red X Z`, the cases separate as follows.

Same rule and same witness: the reductions coincide, `Y = Z`, joinable
immediately. Same rule, different fresh label: same certificate, identified by
fresh-label renaming, hence by `BoundaryIso` on certificates. Same certificate,
different administrative path: the difference lies in the trace coordinate or in
administrative equivalence; the certificate-level theorem may identify them while
the trace-level statement is withheld. Different certificate: not resolved by
renaming — handled by the `BoundaryIso` criterion of Note 07, with no new
event-level criterion introduced here.

Two overlaps must be controlled by the kernel and are recorded as side
conditions: that an existing-boundary step and a fresh-boundary step do not both
apply to one generated boundary in incompatible ways (`ExistingFreshExclusive`),
and that the listed cases exhaust the rule overlaps (`RuleOverlapExhaustive`).

## 12. Intended theorem schema

The local theorem is intended to take the form: assuming `ExistingFreshExclusive`,
`RuleOverlapExhaustive`, and `BoundaryIso` compatibility for the listed
certificate cases, restricted `Red` is locally confluent at the certificate
level. In a Lean-oriented shape:

```text
theorem restricted_local_confluence_certificate
  (h_excl   : ExistingFreshExclusive)
  (h_overlap: RuleOverlapExhaustive)
  (h_biso   : BoundaryIsoCompatibleCases) :
  LocalConfluenceUpToBoundaryCertificate Red
```

Together with termination of restricted `Red`, this is intended to yield
restricted normal-form uniqueness up to `BoundaryIso` on boundary certificates.
It does not yield trace-level uniqueness.

## 13. Non-claims

This note does not claim full transport-inclusive confluence, syntactic
confluence, trace-level confluence, or global normal-form uniqueness. It does not
claim that the residual trace is determined by the boundary certificate, that the
splitting isomorphism is already proved, that trace transport along `BoundaryIso`
is automatic, or that derivations with the same certificate carry the same trace.

It also does not claim that residual traces are irrelevant. The trace coordinate
lies outside the present confluence claim, but it is not erased — that it remains
a coordinate of the derivation-level object is the entire point of the splitting.

## 14. Summary

The restricted confluence problem is posed at the boundary-certificate level. A
derivation is not projected onto a certificate by forgetting its fiber; it is
intended to split, without loss, as

```text
Derivation / ~admin  ≃  Σ c : BoundaryCertificate, ResidualTraceOver(c),
```

where the residual trace is not the full path log but a dependency-aware trace
monoid of residual events over the certificate. Confluence is a theorem about the
first coordinate; the second remains present by construction.

```text
Compression is not disappearance — and neither is confluence.
```