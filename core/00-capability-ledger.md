# Free Numbers Core Capability Ledger

**Status:** reconstruction guide, not an axiom list  
**Branch:** `core-reconstruction`

## Purpose

The standalone Free Numbers theory must preserve the capabilities that originally made it necessary, while remaining definable, computable, and provable without reference to the Time Engine or the Y-axis theory.

This document is a completion ledger. A proposed formalization may be elegant and internally consistent, but it is not an acceptable Free Numbers core if it loses one of the required capabilities below.

The public mathematical theory and its originating interpretation are therefore separated:

- **Originating requirement:** preserve the operations needed by the Time Engine.
- **Standalone mathematical status:** define and prove those operations without importing the Time Engine vocabulary.
- **Residual Chart OS:** provide certified transport, registration, comparison, and normalization around the core, but do not define the core itself.

---

## Required capabilities

### C1. Result-conditioned history distinction

The theory must distinguish histories that reach the same compressed value when their later responses differ.

A value equality

\[
m(x)=m(y)
\]

must not by itself imply equality of Free Numbers.

The core must retain enough structure to answer:

- which history was used,
- which differences were erased by compression,
- and whether those differences can reappear under an admissible context.

### C2. Non-collapsing compression

Compression must be a genuine many-to-one map, not an instruction to discard its kernel.

For a compression map

\[
m:B\to A,
\]

the kernel \(\ker m\) is not automatically zero information. It is a candidate space of latent residual structure.

The theory must distinguish:

- equality after compression,
- equality under all admissible observations,
- and actual equality in the Free Numbers object.

### C3. Contextual re-observability

A difference killed by one observation may become visible after an admissible insertion, extension, or contextual action.

The core must express the possibility that

\[
x\in\ker m_n
\]

while, for an admissible context operator \(I\),

\[
m_{n+r}(I(x))\neq 0.
\]

This is not an implementation detail. It is one of the central phenomena the theory must preserve.

### C4. Residual depth

Residual structure must admit a notion of detection depth.

The core must be able to state and study:

- the minimum probe depth at which a residual becomes visible,
- residuals invisible up to a specified depth,
- and filtrations induced by increasing observational depth.

A valid formulation should support invariants such as a depth profile, detection order, or equivalent finite signature.

### C5. Compositional propagation

Free Numbers must compose.

For admissible objects \(x\) and \(y\), the theory must define a product or composition and determine how compressed values and residual responses propagate through it.

The central closure question is whether a response profile \(J\) admits a composition law of the form

\[
J(x\Vert y)=J(x)\star J(y),
\]

possibly with additional cross-boundary terms that are themselves part of the Free Numbers data.

If the profile does not close, the failure of closure must be retained and classified rather than silently discarded.

### C6. Closure with remainder

The theory must represent both:

- what closes into a value,
- and what remains after closure.

A successful operation is therefore not required to erase its remainder. The remainder may carry future response capacity.

The core must make it possible to separate:

\[
\text{closed value}
\qquad\text{from}\qquad
\text{unabsorbed residual structure}.
\]

### C7. Reinterpretation without deletion

The theory must distinguish reassignment or reinterpretation of history from deletion of the fact that an operation occurred.

A later result may select, reclassify, or compare histories. It must not thereby erase the operation count, structural length, or equivalent monotone record unless an explicit operation of deletion is part of the theory.

This capability is required to prevent retrospective identification from becoming literal cancellation of generated structure.

### C8. Standalone equality

Free Numbers require their own equality or admissible equivalence relation.

Two representatives should be identified only when the chosen standalone theory proves them indistinguishable under all required structure-preserving operations.

At minimum, equality must not reduce to quaternionic value equality alone.

The relation must be checked for compatibility with:

- addition,
- multiplication or composition,
- involution or reversal when present,
- compression,
- and admissible probes.

### C9. Finite observability where possible

The theory should identify finite certificates whenever a bounded object can be distinguished by bounded data.

For fixed length or finite presentation, the core should seek computable signatures such as:

- compressed value,
- response values through depth \(d\),
- representation type,
- multiplicity coordinate,
- and minimal detection depth.

This requirement does not assert that every equality problem is finitely decidable. It requires finite data whenever the mathematics supports it.

### C10. Quaternionic recovery without quaternionic confinement

The quaternionic sector must be recoverable as a local or compressed part of the theory.

The core should explain why ordinary quaternionic value appears, but it must not identify the full Free Numbers object with \(\mathbb H\).

The quaternionic boundary-word construction is currently the first concrete model candidate, not yet the universal definition of Free Numbers.

---

## Current concrete evidence

The existing quaternionic boundary-word program already supplies evidence for several capabilities:

1. Boundary-word spaces
   \[
   B_n=V^{\otimes n},\qquad V=\operatorname{Im}\mathbb H.
   \]

2. Compression maps
   \[
   m_n:B_n\to\mathbb H.
   \]

3. A nontrivial compression kernel, including
   \[
   \ker m_2=S^2_0V.
   \]

4. Internal insertion responses that recover information killed by compression.

5. An all-length highest-spin vertical response law of the form
   \[
   A_n(S)=(-2)^{n-1}C_S.
   \]

6. Probe-depth filtrations and, at length four, depth splitting inside repeated spin multiplicities.

These are established components or verified experimental results of the present repository. They are not yet, by themselves, a complete standalone Free Numbers algebra.

---

## Separation of layers

### Layer I — Standalone Free Numbers Core

Expected contents:

- objects and representatives,
- compression,
- admissible contexts and probes,
- residual response,
- equality or admissible equivalence,
- algebraic operations,
- depth and structural invariants,
- concrete models and theorems.

This layer must stand without Time Engine terminology.

### Layer II — Certified Residual Chart OS

Expected contents:

- registries,
- boundary isomorphism,
- provenance,
- residual purity or trace integrity,
- certified generation decisions,
- rewriting and normalization.

This layer may depend on the core. The core must not depend on it for its mathematical definition.

### Layer III — Originating interpretation

The Time Engine and Y-axis theory explain why these capabilities were required and how they may be interpreted. They are not axioms of the standalone public mathematics.

---

## Immediate research tests

### T1. Response-profile product closure

Compute the smallest products and determine whether response data close under composition:

- \(B_1\times B_1\),
- \(B_2\times B_1\),
- \(B_1\times B_2\),
- \(B_2\times B_2\).

Record all cross-boundary terms explicitly.

### T2. Minimal standalone equality

Determine the weakest equivalence relation compatible with compression, probes, and composition that preserves C1–C10.

### T3. Abstract core versus quaternionic model

For every proposed axiom, determine whether it is:

- intrinsically required by the capability ledger,
- specific to the quaternionic boundary-word model,
- or required only by the Residual Chart OS.

### T4. Finite depth signatures

For fixed length \(n\), determine whether the full admissible response class is captured by probes through a finite maximum depth, and identify the minimum sufficient signature where possible.

---

## Rejection criteria

A proposed Free Numbers core is rejected if it:

1. identifies objects solely by compressed quaternionic value;
2. treats \(\ker m\) as disposable by definition;
3. cannot express re-observation under context;
4. has no compositional law or no explicit account of its failure;
5. depends on registry, chart, or normalization machinery for the existence of its basic objects;
6. imports Time Engine terminology as mathematical primitives;
7. sacrifices a required capability merely to obtain a simpler presentation.

---

## Completion criterion

The reconstruction is complete only when the following statement is true:

> The capabilities originally required by the Time Engine are definable, computable where appropriate, and provable inside a standalone Free Numbers theory; the Time Engine may interpret the theory, but is not needed to state it.

Until then, this ledger takes priority over elegance, publication convenience, and operating-system expansion.
