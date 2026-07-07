# Free Numbers - Local Quaternionic Closure & Global Residual Charts

**Version:** v0.2-pre  
**License:** MIT  
**Status:** public draft candidate with active technical notes

Free Numbers is a formal project for a **non-collapsing quaternionic chart algebra**.

Locally, each elementary closure has quaternionic form.  
Globally, local charts are not collapsed into a single ambient quaternion algebra unless admissible structure-preserving transitions justify the identification.

Free Numbers are not a theory of flow.  
They are a theory of **failed identification under compression**.

Compression is not disappearance.

The project is intentionally limited to the algebraic, residual, and rewriting core.

## Repository Structure

| Layer | Contents | Status |
|---|---|---|
| `/paper/` | LaTeX draft, PDF draft, and TikZ figure source | v0.2-pre |
| `/lean/` | Lean 4 mini-kernel: `Minimal.lean` for restricted termination; `Certified.lean` for the certified reduction skeleton | restricted / certified kernels |
| `/docs/` | `axioms.md`, release notes, license notes | v0.2-pre |
| `/notes/` | technical notes on residual response, probe-depth profiles, spin-depth filtration, and certified weak confluence | active notes |

## Core Claim

The local closure `F_1` has quaternionic algebraic form:

```text
F_1 ~= H
```

However, the global free-number structure `F` is not identified with a single quaternion algebra.

Local charts remain distinct unless connected by admissible equivalence.

In this sense, residual mismatch is not erased by compression.  
It is tracked as structure.

## Compression and Residual Visibility

For each word length `n >= 1`, define the boundary-word space

```text
B_n = V^{tensor n}
```

where

```text
V = Im H = span_R {i, j, k}.
```

The reversed compression map sends a boundary word to a quaternionic value:

```text
m_n(a_1 | a_2 | ... | a_n) = a_n ... a_2 a_1.
```

A residual may vanish under `m_n` without being structurally absent.

The probe-depth response profile records how residuals behave after inserting probes into boundary-word slots and recompressing.

The theorem below proves visibility only for the highest-spin component `S^n_0 V` through the canonical vertical component `A_n`.

It does not classify all residual components.

## Vertical Response Theorem

Notes 05 and 06 introduce the general probe-depth profile and prove the scalar coefficient for the canonical vertical component.

The theorem concerns the highest-spin symmetric trace-free component

```text
S^n_0 V subset V^{tensor n}
```

and the canonical internal vertical response `A_n`.

For

```text
S in S^n_0 V, n >= 2
```

the canonical vertical response satisfies

```text
A_n(S) = (-2)^(n-1) C_S
```

where `C_S` is the contraction map obtained from `S`.

Thus the previously verified low-length computations

```text
A_2 = -2 C
A_3 =  4 C
A_4 = -8 C
```

are recovered as the first instances of the theorem.

They are no longer merely a suggested pattern.

The coefficient `(-2)^(n-1)` is not inserted into the definition of `A_n`.  
It is the output of repeated two-index quaternionic collapse.

## What This Theorem Does Not Claim

The Vertical Response Theorem concerns only the canonical internal vertical component.

It does not claim:

1. that the full depth response profile is equivalent to the canonical vertical component;
2. a complete classification of all full-null or internal-null residual spaces;
3. that every residual invisible at one depth is visible at the next;
4. a full-profile infinite ladder theorem;
5. a completed global semantic theory of free numbers.

The result proves only the scalar coefficient of the canonical vertical response on `S^n_0 V`.

## Spin-Depth Filtration

Note 11 records the first place where a tempting simplification fails.

The simple diagonal spin-depth rule is false.

In length 4, the same spin can split across different probe depths. The failure is not disorder; it reveals a finer multiplicity-space filtration.

The certified computations show:

```text
K_4 = 2V_0 + 5V_1 + 6V_2 + 3V_3 + V_4
```

and the `V_2` multiplicity splits across depth:

```text
6V_2 = 3V_2 + 3V_2
```

Thus value-level compression is too coarse to see the full residual structure. Probe-depth filtration retains structure that the value map erases.

## Certified Red and Restricted Weak Confluence

Note 12 separates the raw rewrite target from the certified rewrite target.

RawRed is not the theorem target.

CertifiedRed is the theorem target.

The raw minimal kernel uses abstract placeholders:

```text
ExistingBoundary : Boundary -> Boundary -> Prop
FreshBoundary    : Boundary -> Prop
```

These are not enough to state the confluence theorem without further structure.

The certified system replaces the two independent predicates by a single generated-boundary decision:

```text
GenDecision(B, R)
  = existing(B', witness)
  | fresh(no-existing-witness)
```

An existing fold is not naked. It carries an admissibility certificate, including boundary-isomorphism data.

The main theorem of Note 12 is:

```text
Restricted CertifiedRed is weakly confluent
up to BoundaryIso on boundary certificates.
```

This is not a claim of syntactic confluence, trace-level confluence, or transport-inclusive confluence.

The finite-data route to computability is also identified: BoundaryIso, EqAdm, ResidualPurity, ExistingFoldWitness, and FreshDecision are decidable when implemented as finite structural checks over finite registries.

The Lean file `lean/Certified.lean` is the first conservative skeleton of this certified relation. It does not yet formalize the full confluence theorem. It puts the certified reduction shape into Lean and proves that the certified reduction still strictly decreases the existing termination weight.

## Quick Build: Minimal Lean Project

The restricted Lean mini-kernel typechecks under Lean 4 on Windows and does not require mathlib.

The checked files are:

```text
lean/Minimal.lean
lean/Certified.lean
```

A successful check produces no output from Lean.

Direct checks from the repository's `lean` directory:

```bash
cd lean
lean Minimal.lean
lean Certified.lean
```

If using a generated Lake project:

```bash
lake new free_num_kernel
cd free_num_kernel
mkdir -p FreeNumKernel
cp ../lean/Minimal.lean FreeNumKernel/Minimal.lean
cp ../lean/Certified.lean FreeNumKernel/Certified.lean
```

Depending on the generated Lake layout, add the following import lines to the project root file if needed:

```lean
import FreeNumKernel.Minimal
import FreeNumKernel.Certified
```

Then run:

```bash
lake build
```

A direct syntax/typecheck check may also be possible:

```bash
lake env lean FreeNumKernel/Minimal.lean
lake env lean FreeNumKernel/Certified.lean
```

Do not use `lean -run` for these files; they are theorem/kernel files, not executable programs.

## Optional: Mathlib Project

A mathlib-based project is not required for v0.2-pre. If later versions use mathlib, create a mathlib project separately:

```bash
lake +leanprover-community/mathlib4:lean-toolchain new free_num_kernel math
cd free_num_kernel
lake exe cache get
lake build
```

## Why "Free"?

The term "free" refers to the fact that local closures are not automatically collapsed into a single global ambient algebra.

Residual mismatch is tracked rather than erased.

Local closure:

```text
F_1 ~= H
```

Global structure:

```text
F = Term_R(disjoint union of local closures) / admissible equivalence
```

The point is not that compression fails.

The point is that compression can identify values while leaving boundary history, insertion response, or residual structure nontrivial.

## Scope

This project does not claim a completed theory of meaning, cognition, time, or physical reality.

The current release is limited to:

```text
local quaternionic closure
boundary-word compression
highest-spin residual visibility through the canonical vertical response
spin-depth filtration in low lengths
restricted rewriting termination
certified reduction skeleton
restricted certified weak confluence at the boundary-certificate level
```

Possible extensions to broader residual-based reconstruction are outside the scope of v0.2-pre.

## License

Released under the MIT License.

Copyright (c) 2026 Free Number Authors.
