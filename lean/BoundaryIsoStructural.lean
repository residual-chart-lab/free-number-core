import Minimal

/-
FreeNumKernel / BoundaryIsoStructural.lean

Structural-reversal skeleton for boundary-certificate isomorphism.

This file does not replace BoundaryIso.lean or Certified.lean yet.
It isolates the reversal calculus needed before integrating structural
BoundaryIso into the certified kernel.

Main idea:
  - structural certificate fields are left/right sided;
  - reversal is a single involution `StructuralBoundaryCert.rev`;
  - structural isomorphism is equality, up to that involution.

This proves the certificate-level equivalence relation and decidability for
the safe structural v1 skeleton:
  BoundaryCertStructIso c c' := c = c' OR c = rev c'

ResidualPurity remains outside this file.
-/

namespace FreeNumKernel

/-- A finite tag with left/right orientation. -/
structure SidedTag where
  left  : Nat
  right : Nat
deriving Repr, DecidableEq

namespace SidedTag

/-- Swap left and right sides. -/
def flip (s : SidedTag) : SidedTag :=
  { left := s.right, right := s.left }

theorem flip_flip (s : SidedTag) :
    (flip (flip s)) = s := by
  cases s
  rfl

end SidedTag

/-- Boundary orientation marker for the structural certificate skeleton. -/
inductive StructOrder where
  | forward
  | reversed
deriving Repr, DecidableEq

namespace StructOrder

/-- Reverse the orientation marker. -/
def flip : StructOrder -> StructOrder
  | forward  => reversed
  | reversed => forward

theorem flip_flip (o : StructOrder) :
    flip (flip o) = o := by
  cases o <;> rfl

end StructOrder

/--
Safe structural boundary certificate, v1.

The endpoint ports are still retained. The structural tags are sided so that
reversal can be represented by one global involution on certificates.
-/
structure StructuralBoundaryCert where
  leftChart    : Chart
  leftId       : LocalId
  rightChart   : Chart
  rightId      : LocalId
  originTag    : SidedTag
  incidenceTag : SidedTag
  attachTag    : SidedTag
  residualTag  : SidedTag
  orderTag     : StructOrder
deriving Repr, DecidableEq

namespace StructuralBoundaryCert

/-- Reverse a structural boundary certificate. -/
def rev (c : StructuralBoundaryCert) : StructuralBoundaryCert :=
  {
    leftChart    := c.rightChart
    leftId       := c.rightId
    rightChart   := c.leftChart
    rightId      := c.leftId
    originTag    := c.originTag.flip
    incidenceTag := c.incidenceTag.flip
    attachTag    := c.attachTag.flip
    residualTag  := c.residualTag.flip
    orderTag     := c.orderTag.flip
  }

/-- Reversal is an involution. -/
theorem rev_rev (c : StructuralBoundaryCert) :
    rev (rev c) = c := by
  cases c with
  | mk leftChart leftId rightChart rightId origin incidence attach residual order =>
      cases origin
      cases incidence
      cases attach
      cases residual
      cases order <;> rfl

end StructuralBoundaryCert

/--
Safe structural isomorphism for boundary certificates.

The first structural step identifies a certificate either with the same
certificate or with its reversed certificate.
-/
def BoundaryCertStructIso (c c' : StructuralBoundaryCert) : Prop :=
  c = c' ∨ c = c'.rev

theorem boundaryCertStructIso_refl (c : StructuralBoundaryCert) :
    BoundaryCertStructIso c c := by
  left
  rfl

theorem boundaryCertStructIso_symm {c c' : StructuralBoundaryCert} :
    BoundaryCertStructIso c c' -> BoundaryCertStructIso c' c := by
  intro h
  cases h with
  | inl hEq =>
      left
      exact hEq.symm
  | inr hRev =>
      right
      have h2 : c.rev = c' := by
        calc
          c.rev = (c'.rev).rev := congrArg StructuralBoundaryCert.rev hRev
          _ = c' := StructuralBoundaryCert.rev_rev c'
      exact h2.symm

theorem boundaryCertStructIso_trans {c c' c'' : StructuralBoundaryCert} :
    BoundaryCertStructIso c c' ->
    BoundaryCertStructIso c' c'' ->
    BoundaryCertStructIso c c'' := by
  intro h1 h2
  cases h1 with
  | inl h1Eq =>
      cases h2 with
      | inl h2Eq =>
          left
          exact h1Eq.trans h2Eq
      | inr h2Rev =>
          right
          exact h1Eq.trans h2Rev
  | inr h1Rev =>
      cases h2 with
      | inl h2Eq =>
          right
          exact h1Rev.trans (congrArg StructuralBoundaryCert.rev h2Eq)
      | inr h2Rev =>
          left
          calc
            c = c'.rev := h1Rev
            _ = (c''.rev).rev := congrArg StructuralBoundaryCert.rev h2Rev
            _ = c'' := StructuralBoundaryCert.rev_rev c''

instance boundaryCertStructIso_decidable (c c' : StructuralBoundaryCert) :
    Decidable (BoundaryCertStructIso c c') := by
  unfold BoundaryCertStructIso
  infer_instance

/--
Conservative embedding from the current Minimal.Boundary to a structural
certificate.

The structural tags are placeholders at this layer. The purpose here is to
test the structural-reversal calculus, not yet to recover full provenance.
-/
def structuralCertOfBoundary (B : Boundary) : StructuralBoundaryCert :=
  {
    leftChart    := B.leftChart
    leftId       := B.leftId
    rightChart   := B.rightChart
    rightId      := B.rightId
    originTag    := { left := 0, right := 0 }
    incidenceTag := { left := 0, right := 0 }
    attachTag    := { left := 0, right := 0 }
    residualTag  := { left := 0, right := 0 }
    orderTag     := StructOrder.forward
  }

/-- Boundary-level structural isomorphism induced by structural certificates. -/
def BoundaryStructIsoFromCert (B B' : Boundary) : Prop :=
  BoundaryCertStructIso (structuralCertOfBoundary B) (structuralCertOfBoundary B')

theorem boundaryStructIsoFromCert_refl (B : Boundary) :
    BoundaryStructIsoFromCert B B := by
  exact boundaryCertStructIso_refl (structuralCertOfBoundary B)

theorem boundaryStructIsoFromCert_symm {B B' : Boundary} :
    BoundaryStructIsoFromCert B B' ->
    BoundaryStructIsoFromCert B' B := by
  intro h
  exact boundaryCertStructIso_symm h

theorem boundaryStructIsoFromCert_trans {B B' B'' : Boundary} :
    BoundaryStructIsoFromCert B B' ->
    BoundaryStructIsoFromCert B' B'' ->
    BoundaryStructIsoFromCert B B'' := by
  intro h1 h2
  exact boundaryCertStructIso_trans h1 h2

instance boundaryStructIsoFromCert_decidable (B B' : Boundary) :
    Decidable (BoundaryStructIsoFromCert B B') := by
  unfold BoundaryStructIsoFromCert
  infer_instance

end FreeNumKernel
