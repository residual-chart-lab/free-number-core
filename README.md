# Free Numbers

**Local quaternionic closure. Global residual charts.**

**Version:** v0.2-pre  
**License:** MIT  
**Status:** public draft candidate with active technical notes

Free Numbers is a formal project for a **non-collapsing quaternionic chart algebra**.

The local unit of the theory has quaternionic form. Globally, however, local charts are **not** automatically collapsed into one ambient quaternion algebra. They can be identified only when an admissible, structure-preserving certificate justifies the identification.

> Compression is not disappearance.

The project is intentionally limited to the algebraic, residual, and rewriting core.

---

## What this project is about

Free Numbers studies what remains when a value-level compression forgets too much.

A boundary word can compress to a quaternionic value, but different boundary histories may still carry different residual structure. The purpose of the framework is to keep that structure visible instead of erasing it.

In short:

- local closures look quaternionic;
- global charts remain distinct unless certified otherwise;
- residual mismatch is tracked as structure;
- value equality is too coarse to be the final identity test.

---

## Main results so far

### 1. Vertical response theorem

The canonical vertical response on the highest-spin component is now proved for all lengths.

The low-length pattern

- length 2: coefficient −2
- length 3: coefficient 4
- length 4: coefficient −8

is not merely experimental. It is the first part of the general coefficient rule.

Scope: this theorem concerns the canonical vertical component on the highest-spin symmetric trace-free part. It does **not** classify the full residual profile.

See: `notes/06-general-vertical-response-theorem.md`

---

### 2. Spin-depth filtration

A tempting simplification fails.

The simple diagonal spin-depth rule is **false**.

In length 4, the same spin can split across different probe depths. The failure is not disorder; it reveals a finer multiplicity-space filtration.

What survives is stronger than the failed simplification:

- value-level compression is too coarse;
- probe-depth filtration retains residual structure;
- multiplicity spaces carry real information.

See: `notes/11-spin-depth-filtration.md`

---

### 3. Certified weak confluence

Raw reduction is not the theorem target.

Certified reduction is.

The raw minimal kernel has separate abstract placeholders for existing and fresh generated boundaries. That is not enough to state the confluence theorem safely.

The certified system uses one generated-boundary decision:

- either a boundary folds into an existing target with a certificate;
- or it is retained as fresh with evidence that no certified fold exists.

An existing fold is never naked. It carries its admissibility witness.

The main theorem of Note 12:

> Restricted CertifiedRed is weakly confluent up to BoundaryIso on boundary certificates.

This is not a claim of syntactic confluence, trace-level confluence, or transport-inclusive confluence.

See: `notes/12-certified-red-restricted-weak-confluence.md`

---

## Lean files

| File | Role |
|---|---|
| `lean/Minimal.lean` | Raw restricted rewriting core and termination weight |
| `lean/Certified.lean` | Certified reduction skeleton for Note 12 |

`Minimal.lean` keeps the original restricted termination kernel.

`Certified.lean` introduces the certified generated-boundary decision. The first version is conservative: `BoundaryIso` is equality, `ResidualPurity` is a placeholder, and the certified reduction is proved to strictly decrease the same weight.

This puts the key design into Lean:

> Do not allow naked folds. Make every fold carry its certificate.

---

## Quick Lean check

From the repository root:

```bash
cd lean
lean Minimal.lean
lean Certified.lean
```

A successful check usually produces no output.

If using a generated Lake project:

```bash
lake new free_num_kernel
cd free_num_kernel
mkdir -p FreeNumKernel
cp ../lean/Minimal.lean FreeNumKernel/Minimal.lean
cp ../lean/Certified.lean FreeNumKernel/Certified.lean
```

Then add imports if needed:

```lean
import FreeNumKernel.Minimal
import FreeNumKernel.Certified
```

and run:

```bash
lake build
```

Do not use `lean -run` for these files. They are theorem/kernel files, not executable programs.

---

## Repository structure

| Layer | Contents | Status |
|---|---|---|
| `paper/` | LaTeX draft, PDF draft, and figure source | v0.2-pre |
| `lean/` | Lean mini-kernel and certified reduction skeleton | active |
| `docs/` | Axioms, release notes, license notes | active |
| `notes/` | Technical notes on residual visibility, filtration, and confluence | active |

---

## What is proved, what is not claimed

### Proved or certified in the current notes

- The local closure has quaternionic form.
- The vertical response coefficient on the highest-spin component is proved.
- The simple diagonal spin-depth rule fails at length 4.
- A finer spin-depth filtration survives.
- Restricted CertifiedRed is weakly confluent up to boundary-certificate isomorphism.
- The Lean skeleton now separates raw reduction from certified reduction.

### Not claimed

- A completed theory of meaning, cognition, time, or physical reality.
- Full trace-level confluence.
- Transport-inclusive confluence.
- Decidability of semantic equality under all future contexts.
- A completed Lean formalization of full BoundaryIso, EqAdm, ResidualPurity, or GenDecision.

---

## Why “Free”?

“Free” means local closures are not automatically collapsed into a single global ambient algebra.

The point is not that compression fails.

The point is that compression can identify values while leaving boundary history, insertion response, or residual structure nontrivial.

Residual mismatch is tracked rather than erased.

---

## Current scope

The current release is limited to:

- local quaternionic closure;
- boundary-word compression;
- highest-spin residual visibility through the canonical vertical response;
- low-length spin-depth filtration;
- restricted rewriting termination;
- certified reduction skeleton;
- restricted certified weak confluence at the boundary-certificate level.

Broader residual-based reconstruction is outside the scope of v0.2-pre.

---

## License

Released under the MIT License.

Copyright (c) 2026 Free Number Authors.
