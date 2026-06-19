# Free Numbers - Local Quaternionic Closure & Global Residual Charts

**Version:** v0.2-pre  
**License:** MIT  
**Status:** public draft candidate

Free Numbers is a formal project for a **non-collapsing quaternionic chart algebra**: locally, each closure has quaternionic form; globally, local charts are not collapsed unless admissible structure-preserving transitions justify the identification.

The project is intentionally limited to the algebraic and rewriting core.

## Repository Structure

| Layer | Contents | Status |
|---|---|---|
| `/paper/` | LaTeX draft, PDF draft, and TikZ figure source | v0.2-pre |
| `/lean/` | Lean 4 mini-kernel: `Term`, restricted `Red`, `RedStar`, `NormalForm`, and `weight` | restricted kernel |
| `/docs/` | `axioms.md`, release notes, license notes | v0.2-pre |

## Core Claim

The local closure `F_1` has quaternionic algebraic form:

```text
F_1 ~= H
```

However, the global free-number structure `F` is not identified with a single quaternion algebra. Local charts remain distinct unless connected by admissible equivalence.

The restricted Lean kernel proves the following termination measure for the Gen-normalization core:

```lean
Red X Y -> weight Y < weight X
```

This is a restricted result. Pure admissible transport is declared but excluded from `Red` in v0.2-pre. It will be restored only after introducing a transport cost, a transport normality condition, or a separate preprocessing relation.

## Quick Build: Minimal Lean Project

The restricted Lean mini-kernel typechecks under Lean 4 on Windows and does not require mathlib.

The checked file is `lean/Minimal.lean`. A successful check produces no output from Lean.

```bash
lake new free_num_kernel
cd free_num_kernel
mkdir -p FreeNumKernel
cp ../lean/Minimal.lean FreeNumKernel/Minimal.lean
```

Depending on the generated Lake layout, add the following import line to the project root file if needed:

```lean
import FreeNumKernel.Minimal
```

Then run:

```bash
lake build
```

A direct syntax/typecheck check may also be possible:

```bash
lake env lean FreeNumKernel/Minimal.lean
```

Do not use `lean -run` for `Minimal.lean`; it is a theorem/kernel file, not an executable program.

## Optional: Mathlib Project

A mathlib-based project is not required for v0.2-pre. If later versions use mathlib, create a mathlib project separately:

```bash
lake +leanprover-community/mathlib4:lean-toolchain new free_num_kernel math
cd free_num_kernel
lake exe cache get
lake build
```

## Why "Free"?

The term "free" refers to the fact that local closures are not automatically collapsed into a single global ambient algebra. Residual mismatch is tracked rather than erased.

Local closure:

```text
F_1 ~= H
```

Global structure:

```text
F = Term_R (disjoint union of local closures) / admissible equivalence
```

See Section 5 of the paper for the local quaternionic closure and Figure 1 for the local/global distinction.

## Scope

This project does not claim a completed theory of meaning, cognition, time, or physical reality. The current release is limited to the algebraic and rewriting core of free numbers.

Possible extensions to residual-based reconstruction are outside the scope of v0.2-pre.

## License

Released under the MIT License.

Copyright (c) 2026 Free Number Authors.
