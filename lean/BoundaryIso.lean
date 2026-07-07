import Minimal

/-
FreeNumKernel / BoundaryIso.lean

First finite-certificate layer for boundary isomorphism.

This file does not replace Minimal.lean or Certified.lean.
It introduces a conservative finite boundary certificate object and a first
certificate-level isomorphism relation.

First version:
  - BoundaryCert stores finite structural tags.
  - BoundaryCertIso is equality on BoundaryCert.
  - Reflexivity, symmetry, transitivity, and decidability are proved.
  - certOfBoundary embeds the current Minimal.Boundary into BoundaryCert.

Later versions can replace equality with a genuine finite structural
isomorphism, including reversal and richer incidence data.
-/

namespace FreeNumKernel

/-- Boundary order marker.

The first version records the tag but does not yet use reversal as an
identification rule.
-/
inductive OrderTag where
  | forward
  | reversed
deriving Repr, DecidableEq

/-- Finite boundary certificate.

These fields are intentionally conservative. The current Minimal.Boundary has
only chart and local-id endpoints. The additional tags are placeholders for the
finite structural data used by the prose theory: structural origin, incidence,
attachments, and residual-visible sites.
-/
structure BoundaryCert where
  leftChart    : Chart
  leftId       : LocalId
  rightChart   : Chart
  rightId      : LocalId
  originTag    : Nat
  incidenceTag : Nat
  attachTag    : Nat
  residualTag  : Nat
  orderTag     : OrderTag
deriving Repr, DecidableEq

/-- Conservative certificate isomorphism.

For the first Lean layer, certificate isomorphism is equality of finite
certificates. This is intentionally stronger than the eventual structural
isomorphism, but it is safe and decidable.
-/
def BoundaryCertIso (c c' : BoundaryCert) : Prop :=
  c = c'

theorem boundaryCertIso_refl (c : BoundaryCert) :
  BoundaryCertIso c c := by
  rfl

theorem boundaryCertIso_symm {c c' : BoundaryCert} :
  BoundaryCertIso c c' -> BoundaryCertIso c' c := by
  intro h
  exact h.symm

theorem boundaryCertIso_trans {c c' c'' : BoundaryCert} :
  BoundaryCertIso c c' -> BoundaryCertIso c' c'' -> BoundaryCertIso c c'' := by
  intro h1 h2
  exact h1.trans h2

instance boundaryCertIso_decidable (c c' : BoundaryCert) :
  Decidable (BoundaryCertIso c c') := by
  unfold BoundaryCertIso
  infer_instance

/-- Embed the current Minimal.Boundary into a finite certificate.

The extra structural tags are set to conservative defaults. Later versions can
replace this map with one that records real structural origin, incidence,
attachment, and residual-visible data.
-/
def certOfBoundary (B : Boundary) : BoundaryCert :=
  {
    leftChart    := B.leftChart
    leftId       := B.leftId
    rightChart   := B.rightChart
    rightId      := B.rightId
    originTag    := 0
    incidenceTag := 0
    attachTag    := 0
    residualTag  := 0
    orderTag     := OrderTag.forward
  }

/-- Boundary-level conservative isomorphism induced by certificates. -/
def BoundaryIsoFromCert (B B' : Boundary) : Prop :=
  BoundaryCertIso (certOfBoundary B) (certOfBoundary B')

theorem boundaryIsoFromCert_refl (B : Boundary) :
  BoundaryIsoFromCert B B := by
  rfl

theorem boundaryIsoFromCert_symm {B B' : Boundary} :
  BoundaryIsoFromCert B B' -> BoundaryIsoFromCert B' B := by
  intro h
  exact h.symm

theorem boundaryIsoFromCert_trans {B B' B'' : Boundary} :
  BoundaryIsoFromCert B B' ->
  BoundaryIsoFromCert B' B'' ->
  BoundaryIsoFromCert B B'' := by
  intro h1 h2
  exact h1.trans h2

instance boundaryIsoFromCert_decidable (B B' : Boundary) :
  Decidable (BoundaryIsoFromCert B B') := by
  unfold BoundaryIsoFromCert
  infer_instance

end FreeNumKernel
