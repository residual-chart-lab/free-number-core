# Free Numbers v0.2-pre.2

**Date:** 2026-06-21  
**Status:** public audit patch  
**Scope:** Lean mini-kernel clarification and paper consistency patch

## Summary

This patch clarifies the scope and dependency profile of the restricted Lean mini-kernel.

No mathematical claim is strengthened in this patch.

## Changed

- Clarified that the abstract relations in the Lean mini-kernel are declared with `axiom`.

- Clarified that the termination theorem is proved relative to Lean's standard `propext` axiom together with the abstract relations `LocalMul`, `ExistingBoundary`, and `FreshBoundary`.

- Running

```lean
#print axioms FreeNumKernel.red_weight_decreases
```

is expected to list exactly these dependencies:

```text
propext
FreeNumKernel.ExistingBoundary
FreeNumKernel.FreshBoundary
FreeNumKernel.LocalMul
```

- Clarified that `PureMove` remains declared but is not part of `Red` in the restricted kernel, and therefore is not expected to appear in the dependency list of `red_weight_decreases`.

- Updated the paper so that the displayed weight definition matches the Lean implementation.

The restricted termination weight is written as:

```text
weight(X) = openGenCount(X) + openGenCount(X) + termSize(X)
```

This is mathematically equal to:

```text
2 * openGenCount(X) + termSize(X)
```

but the repeated-addition form is used to match the Lean kernel exactly.

- Added an explicit scope note that `Chart := Nat` and `LocalId := Nat` are provisional syntactic labels.

- Clarified that chart distinctness, disjoint-copy semantics, and boundary isomorphism are not yet enforced at the kernel level.

## Current Kernel Claim

The restricted Lean kernel proves only the following termination statement:

```lean
Red X Y -> weight Y < weight X
```

This is a restricted Gen-normalization termination claim.

It is not a proof of weak confluence, global normal-form uniqueness, full admissible transport, or full chart-distinctness semantics.

## Known Deferred Components

- Weak confluence modulo admissible equivalence
- Boundary isomorphism
- Chart distinctness at the kernel level
- Disjoint-copy semantics at the kernel level
- Residual purity
- `EqAdm`
- Effective scalar projection
- Full admissible transport inside `Red`

## Build Notes

The restricted Lean mini-kernel has been checked with Lean 4 on Windows.

The file

```text
lean/Minimal.lean
```

typechecks successfully. Lean produces no output on success.

Before committing this release, remove any temporary diagnostic line such as:

```lean
#print axioms FreeNumKernel.red_weight_decreases
```

from `lean/Minimal.lean`.

## Release Tag

```text
v0.2-pre.2
```
