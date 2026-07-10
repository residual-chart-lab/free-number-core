# Free Numbers Abstract Core — Reconstruction Scaffold

**Status:** working scaffold, not a final axiom system  
**Branch:** `core-reconstruction`  
**Depends on:** `core/00-capability-ledger.md`

## 0. Purpose

This document begins the reconstruction of Free Numbers as a standalone mathematical theory.

The goal is not to force the existing quaternionic boundary-word model into the role of a universal definition. The goal is to identify the minimum abstract structure required to preserve the capabilities listed in the Core Capability Ledger, while keeping the concrete quaternionic model available as the first serious test case.

The abstract core must satisfy two constraints at once:

1. it must be independent of the Time Engine, the Y-axis theory, and the Residual Chart OS;
2. it must remain strong enough to recover the operations for which Free Numbers were originally required.

Accordingly, every item below is marked by status:

- **Primitive candidate:** plausible input to the abstract theory;
- **Derived target:** expected to be defined from more primitive data;
- **Open design choice:** not yet fixed;
- **Model-specific:** currently justified only in a concrete realization.

---

## 1. Minimal ambient data

### 1.1 Grades or structural lengths

**Primitive candidate.**

There is a family of representative spaces

\[
B_0,B_1,B_2,\ldots
\]

or equivalently a graded carrier

\[
B=\bigoplus_{n\ge 0} B_n.
\]

The grade \(n\) records structural length, operation count, or an equivalent monotone quantity. It is not automatically identified with compressed value.

The theory must not permit later reinterpretation of a representative to erase its grade unless an explicit deletion or contraction operation is separately defined.

This preserves the distinction between reinterpretation and deletion required by C7.

### 1.2 Value space

**Primitive candidate.**

There is a value object \(A\). Depending on the model, \(A\) may be an algebra, module, category of outputs, or another structure supporting the compressed result of a representative.

The abstract theory does not initially require

\[
A=\mathbb H.
\]

The quaternionic case is a concrete model candidate.

### 1.3 Compression

**Primitive candidate.**

For every grade \(n\), there is a compression map

\[
m_n:B_n\to A.
\]

Compression is allowed, and expected, to be many-to-one.

The equality

\[
m_n(x)=m_n(y)
\]

expresses equality of compressed value only. It does not define equality in the Free Numbers core.

The kernel or equalizer fibers of \(m_n\) are retained as possible carriers of latent residual structure.

### 1.4 Composition of representatives

**Primitive candidate, exact form open.**

There is a partial or total composition

\[
\Vert:B_m\times B_n\to B_{m+n},
\qquad (x,y)\mapsto x\Vert y.
\]

In word models this is concatenation. In a more general realization it may be another grade-preserving composition.

Associativity may be required strictly,

\[
(x\Vert y)\Vert z=x\Vert(y\Vert z),
\]

or only up to a specified coherent equivalence. This is an open design choice.

The abstract core must eventually determine how compression and residual response behave under this composition.

---

## 2. Contexts and probes

### 2.1 Admissible contexts

**Primitive candidate.**

For grades \(n,r\ge 0\), let

\[
\mathcal C_{n,r}
\]

denote a family of admissible context operators

\[
I:B_n\to B_{n+r}.
\]

A context may represent insertion, extension, left or right composition, internal insertion, or another allowed operation that places a representative into a larger structure.

Not every map \(B_n\to B_{n+r}\) is necessarily admissible. The admissible class is part of the theory.

### 2.2 Probes

**Derived target or distinguished subclass.**

A probe is an admissible context used specifically to test whether a difference hidden by compression becomes visible at a larger grade.

For a probe \(I\in\mathcal C_{n,r}\), define its observed response by

\[
\mathcal R_I(x):=m_{n+r}(I(x)).
\]

If

\[
m_n(x)=0
\qquad\text{but}\qquad
\mathcal R_I(x)\ne 0,
\]

then \(x\) is compression-invisible at grade \(n\) but contextually re-observable through \(I\).

This phenomenon is required by C3.

### 2.3 Probe depth

**Open design choice with concrete evidence.**

Each admissible probe is assigned a nonnegative depth

\[
\operatorname{depth}(I)\in\mathbb N.
\]

Depth may measure the number of inserted arguments, the number of nested contextual actions, the largest internal displacement, or another model-independent complexity.

The abstract theory should not fix the definition before checking which notion is preserved across models.

For each \(d\), let

\[
\mathcal P_{n}^{\le d}
\]

be the admissible probes of depth at most \(d\).

---

## 3. Response profiles

### 3.1 Truncated response profile

**Derived target.**

For \(x\in B_n\), define its depth-\(d\) response profile formally by

\[
J_d(x)
:=
\left(
 m_n(x),
 \bigl(\mathcal R_I(x)\bigr)_{I\in\mathcal P_n^{\le d}}
\right).
\]

This expression is schematic. A concrete theory must specify the codomain, indexing, symmetries, and finite presentation of the profile.

### 3.2 Residual filtration

**Derived target.**

Define the depth-\(d\) invisible subspace or class by

\[
F_n^{>d}
:=
\{x\in B_n: J_d(x)=0\}.
\]

When linear structure is present, this is expected to be a kernel. Increasing depth should produce a descending filtration

\[
B_n\supseteq F_n^{>0}\supseteq F_n^{>1}\supseteq F_n^{>2}\supseteq\cdots.
\]

The minimum detection depth of \(x\) is then

\[
\delta(x)
:=
\min\{d:J_d(x)\ne 0\},
\]

when such a minimum exists.

If no admissible probe detects \(x\), then \(x\) belongs to the absolutely invisible class

\[
F_n^{\infty}
:=
\bigcap_{d\ge 0}F_n^{>d}.
\]

Whether \(F_n^{\infty}\) should be quotiented out is an open design choice. It must not be removed before proving that doing so preserves C1–C10.

### 3.3 Closure with remainder

**Derived target.**

A representative should expose at least two kinds of data:

\[
\text{compressed value}
\qquad\text{and}\qquad
\text{residual response capacity}.
\]

A provisional Free Number datum may therefore have the form

\[
\mathbf F(x)
=
\bigl(m_n(x),J_{>0}(x)\bigr),
\]

where \(J_{>0}\) denotes the nontrivial contextual response data.

This is not yet the definition of a Free Number. It records the minimum separation required by C6.

---

## 4. Equality candidates

The theory needs an equality stronger than compressed-value equality and compatible with all admitted operations.

### 4.1 Representative equality

\[
x=y\quad\text{in }B_n.
\]

This is generally too strict for the final theory, because distinct presentations may encode the same observable Free Number.

### 4.2 Value equality

\[
x\equiv_0 y
\iff
m_n(x)=m_n(y).
\]

This is too weak and is rejected by C1, C2, C3, and C8.

### 4.3 Depth-\(d\) observational equivalence

**Derived candidate.**

\[
x\equiv_d y
\iff
J_d(x)=J_d(y).
\]

This relation captures indistinguishability through bounded probe depth.

### 4.4 Full admissible observational equivalence

**Leading candidate, not yet accepted.**

\[
x\equiv_{\mathrm{obs}}y
\iff
\mathcal R_I(x)=\mathcal R_I(y)
\quad\text{for every admissible context }I.
\]

A final standalone equality may be \(\equiv_{\mathrm{obs}}\), or a finer relation if the theory requires structural data not exhausted by admissible observation.

Before adoption, the relation must be proved compatible with:

- grade;
- composition;
- addition when present;
- involution or reversal when present;
- compression;
- all admissible contexts.

### 4.5 Quotient candidate

If compatibility is established, one may define

\[
\mathbb F_n:=B_n/\!\equiv_{\mathrm{obs}}.
\]

This quotient is only a candidate. It must not be accepted if it destroys finite depth, multiplicity data, provenance-independent structure, or compositional closure.

---

## 5. Algebraic operations

### 5.1 Addition

**Open design choice.**

If each \(B_n\) is linear, addition may be inherited gradewise. The final equivalence relation must be a congruence for addition.

If the abstract theory is nonlinear, an additive structure may be absent or replaced by another combination law.

### 5.2 Multiplication or composition

**Required target.**

Composition must descend from representatives to Free Numbers.

The central test is whether response data admit a law

\[
J(x\Vert y)=J(x)\star J(y).
\]

The operation \(\star\) may require cross-boundary terms. If so, those terms are part of the Free Number data and must not be discarded as implementation noise.

### 5.3 Unit

**Expected target.**

If \(B_0\) contains a distinguished element \(e\), then

\[
e\Vert x=x=x\Vert e
\]

should hold strictly or up to the chosen equivalence.

### 5.4 Reversal, involution, or conjugation

**Open design choice.**

Some concrete models carry a reversal of structural order, an algebraic involution, or quaternionic conjugation. These operations must not be identified prematurely.

The abstract theory should distinguish:

- reversing the representative order;
- applying an involution in the value algebra;
- reversing a context orientation;
- and reinterpreting a history.

They may coincide in a model, but they are not identical by definition.

---

## 6. Required laws and non-laws

### 6.1 Required laws

A viable core should eventually prove:

1. compression is compatible with the stated value operations;
2. admissible contexts respect the chosen equivalence;
3. composition preserves equivalence;
4. residual depth is invariant under equivalence;
5. finite signatures are complete whenever a bounded completeness theorem is available;
6. the quaternionic value sector is recovered in the quaternionic model.

### 6.2 Deliberate non-laws

The abstract theory must not assume:

1. equal compressed values imply equal Free Numbers;
2. every compression-kernel element is zero information;
3. every residual is visible at depth one;
4. response profiles automatically close under composition;
5. all admissible observational equivalence is finitely decidable;
6. the quaternionic model is universal;
7. registry membership, chart normalization, or certified rewriting is required for a Free Number to exist.

---

## 7. Boundary between core and models

### 7.1 Abstract core responsibilities

The abstract core should define or constrain:

- representatives and grade;
- value objects and compression;
- composition;
- admissible contexts;
- response profiles;
- residual depth;
- standalone equality;
- closure with remainder;
- congruence and invariance laws.

### 7.2 Quaternionic boundary-word model responsibilities

The first concrete model should supply:

\[
V=\operatorname{Im}\mathbb H,
\qquad
B_n=V^{\otimes n},
\qquad
m_n(a_1|\cdots|a_n)=a_n\cdots a_1,
\]

along with explicit insertion operators, representation decomposition, response maps, and finite certificates.

It should then prove which abstract requirements it satisfies.

### 7.3 Residual Chart OS responsibilities

The OS may supply:

- registries;
- boundary comparison;
- provenance;
- trace integrity or residual purity;
- certified fold decisions;
- rewriting and normalization.

These structures may depend on the core. They do not define the existence or equality of the standalone core objects unless a later theorem explicitly establishes such a reduction.

---

## 8. First proof obligations

### O1. Context congruence

Prove that the proposed equality is preserved by every admissible context.

### O2. Composition congruence

Prove that

\[
x\equiv x',\quad y\equiv y'
\Longrightarrow
x\Vert y\equiv x'\Vert y'.
\]

### O3. Response-profile product law

Compute the response of the smallest composites and identify all cross-boundary data required for closure:

- \(B_1\times B_1\);
- \(B_2\times B_1\);
- \(B_1\times B_2\);
- \(B_2\times B_2\).

### O4. Finite-depth completeness at fixed grade

For fixed \(n\), determine whether there exists a finite \(d(n)\) such that

\[
x\equiv_{\mathrm{obs}}y
\iff
J_{d(n)}(x)=J_{d(n)}(y).
\]

### O5. Recovery theorem

In the quaternionic model, prove that the compressed sector recovers ordinary quaternionic value without collapsing the residual sector.

---

## 9. Provisional abstract package

A first candidate package is

\[
\mathcal F
=
\left(
(B_n)_{n\ge0},
A,
(m_n)_{n\ge0},
\Vert,
\mathcal C,
\operatorname{depth},
\equiv
\right).
\]

This package is accepted as a Free Numbers core only if it satisfies the capability ledger and the proof obligations above.

At present, the following remain deliberately unresolved:

- whether the carrier must be linear;
- whether composition is strictly associative;
- the universal definition of probe depth;
- the final equality relation;
- whether absolutely invisible structure is quotiented out;
- whether response data close finitely under composition;
- whether the quaternionic model is initial, universal, or merely exemplary.

---

## 10. Reconstruction rule

No proposed simplification is accepted merely because it produces a familiar algebra.

A definition is accepted only if it preserves the capabilities in `00-capability-ledger.md` and survives the concrete quaternionic tests.

The present document therefore fixes a research boundary, not a finished theory:

> A standalone Free Numbers core consists of graded representatives with compressible values, admissible contextual re-observation, residual depth, and a composition-compatible equality that preserves what compression alone cannot see.
