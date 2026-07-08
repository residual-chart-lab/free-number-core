import Certified

/-
FreeNumKernel / DecideGen.lean

Concrete registry-based decision procedure for certified generation.

This version connects the registry scan to the structural BoundaryIso layer:
  - Certified.BoundaryIso is induced by BoundaryIsoStructural.lean.
  - ResidualPurity is still True.
  - An existing-fold witness can be built from a BoundaryIso witness.

This is not the full structural BoundaryIso/EqAdm/ResidualPurity decision
procedure yet. It is the finite registry scan over the current structural
certificate skeleton.
-/

namespace FreeNumKernel

/-- Build an existing-fold witness from a boundary-isomorphism witness. -/
def existingWitnessOfIso {B B' : Boundary} (h : BoundaryIso B B') :
    ExistingFoldWitness B B' :=
  {
    eqAdm := {
      boundaryIso  := h
      residualPure := trivial
    }
  }

/--
Construct a certified generated-boundary decision from a finite registry.

Structural skeleton version:
  - existing if B is boundary-isomorphic to some boundary already in R;
  - fresh otherwise.

The head contradiction in the fresh branch now uses the BoundaryIso witness
carried by ExistingFoldWitness directly, rather than reducing everything to
raw boundary equality.
-/
def decideGenFromRegistry : (R : List Boundary) -> (B : Boundary) -> GenDecision R B
  | [], _B =>
      GenDecision.fresh (by
        intro B' hmem _w
        cases hmem)

  | B0 :: R, B =>
      if h : BoundaryIso B B0 then
        GenDecision.existing B0 (existingWitnessOfIso h)
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
                  have hb0 : BoundaryIso B B0 := by
                    simpa [hhead] using w.eqAdm.boundaryIso
                  exact h hb0
              | inr htail =>
                  exact hfresh B' htail w)

end FreeNumKernel
