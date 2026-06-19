# Free Numbers v0.2-pre

**Date:** 2026-06-19  
**Status:** public draft candidate  
**Scope:** algebraic and restricted rewriting core

## Added

- Section 5: local quaternionic closure proof.
  - Introduces a two-dimensional primitive fold plane `U`.
  - Distinguishes two primitive generators from three pure directions.
  - Shows the local closure `F_1 ~= H`.

- Figure 1: local closure versus global collapse.
  - Solid arrow: admissible transition.
  - Dashed arrow: residual transition.

- Lean mini-kernel draft.
  - `Term`
  - restricted `Red`
  - `RedRel`
  - `RedStar`
  - `NormalForm`
  - `openGenCount`
  - `termSize`
  - `weight`
  - `red_weight_decreases`

- `docs/axioms.md`.
  - Lists abstract relations and deferred components.

## Changed

- Abstract wording softened:
  - from "global composition is not assumed to be associative"
  - to "global composition need not be globally associative".

- `G3_existing` now reduces:

```lean
Term.gen B -> Term.normGen B'
```

instead of:

```lean
Term.gen B -> Term.gen B'
```

This prevents unresolved generated charts from remaining open after folding into an existing boundary.

- `G2_transport` removed from `Red` in the restricted kernel.
  - `PureMove` remains declared.
  - Transport will be restored only after a decreasing transport measure, transport normality condition, or separate preprocessing phase is introduced.

- Added explicit "Deferred Proof: Weak Confluence" section.

## Current Kernel Claim

The restricted Lean kernel includes the termination measure:

```lean
Red X Y -> weight Y < weight X
```

This supports termination of the restricted Gen-normalization core.

## Known Gaps

- Weak confluence modulo admissible equivalence is deferred.
- Boundary isomorphism is deferred.
- Residual purity is deferred.
- `EqAdm` is deferred.
- Effective scalar projection is deferred.
- Full admissible transport is not yet part of `Red`.

## Build Notes

The restricted Lean mini-kernel has been typechecked with Lean 4 on Windows. It does not require mathlib.

The file `lean/Minimal.lean` typechecks successfully. Lean produces no output on success.

Suggested minimal check:

```bash
lake new free_num_kernel
cd free_num_kernel
mkdir -p FreeNumKernel
cp ../lean/Minimal.lean FreeNumKernel/Minimal.lean
lake build
```

If the project root does not import the file, add:

```lean
import FreeNumKernel.Minimal
```

A direct check may also work:

```bash
lake env lean FreeNumKernel/Minimal.lean
```

Do not use:

```bash
lean -run lean/Minimal.lean
```

because `Minimal.lean` is not an executable program.

## Release Tag

Planned tag:

```text
v0.2-pre
```

## DOI

A DOI may be minted after the PDF and repository structure are frozen.
