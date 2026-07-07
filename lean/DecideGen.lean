import Certified

/-
FreeNumKernel / DecideGen.lean

First concrete registry-based decision procedure for certified generation.

This file connects the GenDecision shape from Certified.lean to a finite
registry search in the first conservative setting:
  - Certified.BoundaryIso is equality on Boundary.
  - Certified.ResidualPurity is True.
  - Therefore an existing-fold witness can be built from boundary equality.

This is not the full structural BoundaryIso/EqAdm decision procedure yet.
It is the first equality-based root for decideGen.
-/

namespace FreeNumKernel

/-- Build an existing-fold witness from boundary equality. -/
def existingWitnessOfEq {B B' : Boundary} (h : B = B') :
    ExistingFoldWitness B B' :=
  {
    eqAdm := {
      boundaryIso  := h
      residualPure := trivial
    }
  }

/--
Construct a certified generated-boundary decision from a finite registry.

First conservative version:
  - existing if B is equal to some boundary already in R;
  - fresh otherwise.

This turns `decideGen` from a mysterious external parameter into a concrete
finite registry scan in the equality-based certified kernel.
-/
def decideGenFromRegistry : (R : List Boundary) -> (B : Boundary) -> GenDecision R B
  | [], _B =>
      GenDecision.fresh (by
        intro B' hmem _w
        cases hmem)

  | B0 :: R, B =>
      if h : B = B0 then
        GenDecision.existing B0 (existingWitnessOfEq h)
      else
        match decideGenFromRegistry R B with
        | GenDecision.existing B' w =>
            GenDecision.existing B' w
        | GenDecision.fresh hfresh =>
            GenDecision.fresh (by
              intro B' hmem w
              have hcases : B' = B0 ∨ B' ∈ R := by
                simpa using hmem
              cases hcases with
              | inl hhead =>
                  exact h (w.eqAdm.boundaryIso.trans hhead)
              | inr htail =>
                  exact hfresh B' htail w)

end FreeNumKernel
