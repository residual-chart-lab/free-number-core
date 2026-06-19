# Axioms & Deferred Components - v0.2-pre

The v0.2-pre release separates three kinds of components:

1. **Definitions** used directly in the restricted Lean kernel.
2. **Abstract relations** declared in the kernel but not yet made concrete.
3. **Deferred components** required for the full free-number system.

The minimal kernel proves only the restricted termination claim:

```lean
Red X Y -> weight Y < weight X
```

This establishes termination for the restricted Gen-normalization core, not for the full admissible transport system.

| Label | Lean Symbol | Type | Purpose / Later Proof |
|---|---|---|---|
| **A1** | `LocalMul` | Abstract relation | Local atom x atom -> atom relation. Intended later replacement: concrete multiplication table for local quaternionic closure. |
| **A2** | `ExistingBoundary` | Abstract relation | Determines when `gen` can fold into `normGen` through an existing boundary. |
| **A3** | `FreshBoundary` | Abstract relation | Determines when a generated chart cannot fold and must be retained as `normGen`. |
| **A4** | `PureMove` | Abstract relation | Admissible transport. Declared but excluded from `Red` in v0.2-pre. |
| **A5** | `BoundaryIso` | Deferred component | Structural isomorphism of generated boundaries. |
| **A6** | `ResidualPurity` | Deferred component | Purity predicate for residual signatures. |
| **A7** | `EqAdm` | Deferred component | Admissible equivalence relation among terms. |
| **A8** | `WeakConfluence` | Deferred theorem | Weak uniqueness of normal forms modulo `EqAdm`. |
| **A9** | `EffectiveMagProjection` | Deferred component | Non-constant, admissible, residual-sensitive scalar projection. |
| **A10** | `TransportNormalizedReduction` | Deferred component | Restoration of admissible transport into reduction after a transport cost, normality condition, or preprocessing phase is introduced. |

## Current Proven Kernel Claim

The restricted kernel contains:

- `Term`
- `Red`
- `RedRel`
- `RedStar`
- `NormalForm`
- `IsNFOf`
- `openGenCount`
- `termSize`
- `weight`
- `red_weight_decreases`

The central checked statement is:

```lean
theorem red_weight_decreases
  {X Y : Term} (h : Red X Y) :
  weight Y < weight X
```

This does not prove weak confluence, uniqueness of normal forms, or full transport-normalized reduction.

## Why `PureMove` is excluded from `Red`

In earlier sketches, admissible transport was included as a `G2_transport` reduction. This was removed in v0.2-pre because transport may preserve both `openGenCount` and `termSize`, leaving no immediate decreasing measure.

It will return only after one of the following is introduced:

1. `transportCost`;
2. `TransportNormal`;
3. a separate preprocessing relation outside `Red`.

This prevents the restricted termination proof from relying on an unproven transport decrease condition.
