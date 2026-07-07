import Minimal

/-
FreeNumKernel / Certified.lean

Certified reduction skeleton for Note 12.

This file does not replace Minimal.lean.
Minimal.lean keeps the raw restricted termination kernel.
Certified.lean introduces the certified generated-boundary decision used by
Note 12.

First conservative version:
  - BoundaryIso is equality on Boundary.
  - ResidualPurity is True.
  - EqAdm / ExistingFoldWitness are witness structures.
  - Generated-boundary reduction is driven by one GenDecision object.
  - The certified reduction still strictly decreases the existing weight.

The point of this first version is not full boundary semantics.
The point is to put "do not allow naked folds" into the Lean shape.
-/

namespace FreeNumKernel

/-- Conservative boundary isomorphism.

This first version uses equality.
Later versions can replace this with finite structural isomorphism of boundary
certificates.
-/
def BoundaryIso (B B' : Boundary) : Prop :=
  B = B'

theorem boundaryIso_refl (B : Boundary) :
  BoundaryIso B B := by
  rfl

theorem boundaryIso_symm {B B' : Boundary} :
  BoundaryIso B B' -> BoundaryIso B' B := by
  intro h
  exact h.symm

theorem boundaryIso_trans {B B' B'' : Boundary} :
  BoundaryIso B B' -> BoundaryIso B' B'' -> BoundaryIso B B'' := by
  intro h1 h2
  exact h1.trans h2

/-- Conservative residual purity placeholder.

This is intentionally permissive in the first certified skeleton.
Later versions should replace it with the finite residual-purity checks.
-/
def ResidualPurity (_B _B' : Boundary) : Prop :=
  True

/-- Admissible-equivalence witness for a fold.

The first version keeps only the certified boundary relation and residual-purity
slot. More finite preservation checks can be added later.
-/
structure EqAdmWitness (B B' : Boundary) where
  boundaryIso  : BoundaryIso B B'
  residualPure : ResidualPurity B B'

/-- Existing fold witness.

A fold into an existing boundary is not naked: it carries its admissibility data.
-/
structure ExistingFoldWitness (B B' : Boundary) where
  eqAdm : EqAdmWitness B B'

/-- Certified generated-boundary decision.

For a boundary B and finite registry R:
  - either B folds into an existing target B' with a witness;
  - or B is fresh, with evidence that no listed existing target has a witness.
-/
inductive GenDecision (R : List Boundary) (B : Boundary) where
  | existing (B' : Boundary) (w : ExistingFoldWitness B B') :
      GenDecision R B
  | fresh
      (h : forall B' : Boundary, B' ∈ R -> ExistingFoldWitness B B' -> False) :
      GenDecision R B

/-- The normalized target selected by a certified generated-boundary decision. -/
def normTarget {R : List Boundary} {B : Boundary} :
  GenDecision R B -> Boundary
  | GenDecision.existing B' _ => B'
  | GenDecision.fresh _       => B

/-- Certified restricted one-step reduction.

The generated-boundary step is driven by a single decision object. Therefore the
old G3/G4 overlap is not represented as two independent rules.
-/
inductive CertifiedRed
    (R : List Boundary)
    (decideGen : (B : Boundary) -> GenDecision R B) :
    Term -> Term -> Prop where

  | G1_local {x y z : LocalElem} :
      LocalMul x y z ->
      CertifiedRed R decideGen
        (Term.mul (Term.atom x) (Term.atom y))
        (Term.atom z)

  | G_gen {B : Boundary} :
      CertifiedRed R decideGen
        (Term.gen B)
        (Term.normGen (normTarget (decideGen B)))

/-- CertifiedRed seen in the decreasing direction for well-founded recursion. -/
def CertifiedRedRel
    (R : List Boundary)
    (decideGen : (B : Boundary) -> GenDecision R B) :
    Term -> Term -> Prop :=
  fun Y X => CertifiedRed R decideGen X Y

/-- CertifiedRed still never increases open generated nodes. -/
theorem certifiedRed_openGen_noninc
    {R : List Boundary}
    {decideGen : (B : Boundary) -> GenDecision R B}
    {X Y : Term}
    (h : CertifiedRed R decideGen X Y) :
    openGenCount Y <= openGenCount X := by
  cases h <;> simp [openGenCount]

/-- CertifiedRed strictly decreases the same termination weight as Minimal.Red. -/
theorem certifiedRed_weight_decreases
    {R : List Boundary}
    {decideGen : (B : Boundary) -> GenDecision R B}
    {X Y : Term}
    (h : CertifiedRed R decideGen X Y) :
    weight Y < weight X := by
  cases h <;> simp [weight, openGenCount, termSize]

/-- Same decrease expressed in the CertifiedRedRel direction. -/
theorem certifiedRedRel_weight_decreases
    {R : List Boundary}
    {decideGen : (B : Boundary) -> GenDecision R B}
    {X Y : Term}
    (h : CertifiedRedRel R decideGen Y X) :
    weight Y < weight X := by
  exact certifiedRed_weight_decreases h

end FreeNumKernel
