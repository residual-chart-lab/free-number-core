# Conditioned Zero and Value-Preserving Response Deformation

**Status:** working core note, not a final axiom system  
**Branch:** `core-reconstruction`  
**Depends on:** `core/00-capability-ledger.md`, `core/01-abstract-core.md`

## 0. Purpose

This note isolates the smallest mathematical phenomenon from which the Free Numbers program was originally required:

> two states may have the same present compressed value, including the same null value, while differing in their admissible future response.

The intended abstract form is

\[
z\neq z_{\lambda},
\qquad
m_n(z)=m_n(z_{\lambda})=0_A,
\]

while for at least one admissible probe or continuation \(I\),

\[
\mathcal R_I(z)\neq \mathcal R_I(z_{\lambda}).
\]

The symbol \(\lambda\) denotes conditioning data. In the originating interpretation it may be read as a terminal requirement, but no temporal ontology is assumed here. The standalone mathematics requires only a datum capable of changing response without changing present compressed value.

This note does **not** yet declare conditioned zero to be the universal definition of a Free Number. It records the birth kernel that every acceptable reconstruction must be able to express.

---

## 1. The first necessary distinction

### 1.1 Additive zero is not the same as zero-valued state

Assume the value object \(A\) has a distinguished null value \(0_A\). Define the zero fiber at grade \(n\) by

\[
Z_n:=m_n^{-1}(0_A).
\]

An element of \(Z_n\) is **zero-valued after compression**. It need not be the additive zero of \(B_n\), even when \(B_n\) is linear.

If \(B_n\) has an additive zero, write it as

\[
0_{B_n}.
\]

Then generally

\[
0_{B_n}\in Z_n,
\]

but the core must permit

\[
Z_n\neq\{0_{B_n}\}.
\]

This distinction is mandatory. The notation

\[
0[\lambda]
\]

must initially mean a **zero-valued representative carrying nontrivial response structure**, not automatically the additive zero decorated by a label.

A decorative label with no structural or observational consequence is not a Free Number distinction.

### 1.2 Bare zero is not yet canonical

The phrase “unconditioned zero” suggests a preferred baseline element

\[
\zeta_n\in Z_n.
\]

The abstract core does not yet assume that such a canonical baseline exists.

There may instead be:

- several inequivalent baseline zero-valued states;
- a model-specific preferred basepoint;
- only relative comparison between two members of the same zero fiber;
- or a canonical additive zero together with nontrivial conditioned states elsewhere in the fiber.

The existence and uniqueness of \(\zeta_n\) are open design choices.

---

## 2. Minimal conditioned-zero witness

### 2.1 Birth witness

A **conditioned-zero witness** at grade \(n\) consists provisionally of

\[
(z,z_{\lambda},I),
\]

where

\[
z,z_{\lambda}\in Z_n
\]

and \(I\) is an admissible probe such that

\[
\mathcal R_I(z)\neq\mathcal R_I(z_{\lambda}).
\]

Equivalently,

\[
J_d(z)\neq J_d(z_{\lambda})
\]

for some finite depth \(d\), when a truncated response profile is available.

The minimum content is therefore:

1. equality of present compressed value;
2. inequality of admissible response;
3. retention of both states as distinct Free Number candidates.

### 2.2 Strong birth requirement

A standalone Free Numbers core should admit at least one nontrivial witness satisfying

\[
m_n(z)=m_n(z_{\lambda})
\quad\text{but}\quad
z\not\equiv_{\mathrm{obs}} z_{\lambda}.
\]

If no such witness exists in any grade, then the theory collapses to compressed-value mathematics and fails the Capability Ledger.

### 2.3 Condition labels must earn their existence

Two formal labels \(\lambda\) and \(\mu\) are not mathematically distinct merely because their names differ.

At a state \(z\), they are operationally distinct only if some admissible observation separates them:

\[
J(z_{\lambda})\neq J(z_{\mu}).
\]

If no admissible context distinguishes them, then either:

- they represent the same Free Number under observational equality;
- the admissible probe class is incomplete;
- or the theory intentionally retains finer structural data than observation alone.

The choice must be explicit.

---

## 3. Conditioning as an operation

The birth witness can be stated without assuming a global conditioning operator. A stronger theory may introduce one.

### 3.1 Grade-preserving candidate

Let \(\Lambda\) be a class of conditioning data. A grade-preserving conditioning action would be a partial or total map

\[
\Gamma_{\lambda,n}:D_{\lambda,n}\subseteq B_n\to B_n
\]

such that

\[
m_n(\Gamma_{\lambda,n}(x))=m_n(x)
\]

on its domain.

Thus \(\Gamma_{\lambda,n}\) is value-preserving but need not be response-preserving.

A condition is **effective at** \(x\) when

\[
J(\Gamma_{\lambda,n}(x))\neq J(x).
\]

It is **observationally null at** \(x\) when equality holds for all admitted probes.

### 3.2 Structural or grade-changing realization

A concrete model may realize conditioning by adding structure rather than by acting internally at fixed grade:

\[
\widetilde\Gamma_{\lambda,n}:B_n\to B_{n+r}.
\]

Such a realization is value-preserving at \(x\) when

\[
m_{n+r}(\widetilde\Gamma_{\lambda,n}(x))=m_n(x).
\]

This possibility must remain open because the conditioning operation may carry an irreversible structural count even when it changes no compressed value.

Comparing a grade-changing conditioned state to an unconditioned state may require a neutral lift

\[
\eta_{n,r}:B_n\to B_{n+r}
\]

or another explicit comparison map. No neutral lift is assumed yet.

### 3.3 State-level action versus representative realization

It may eventually be preferable to define conditioning on Free Number equivalence classes while allowing representatives to realize it by grade-changing extensions.

The following are therefore distinct questions:

1. Does conditioning preserve the Free Number grade?
2. Does every representative realization preserve structural length?
3. Is added conditioning structure observable immediately or only after continuation?
4. Can different realizations of the same condition be proved equivalent?

These questions must not be collapsed into one definition prematurely.

---

## 4. A fundamental linearity obstruction

Suppose \(B_n\) is linear and \(\Gamma_{\lambda,n}:B_n\to B_n\) is linear. Then

\[
\Gamma_{\lambda,n}(0_{B_n})=0_{B_n}.
\]

Therefore a linear grade-preserving operator cannot generate a nontrivial conditioned zero from the additive zero.

This gives an immediate design fork. A nontrivial state written informally as

\[
0[\lambda]\neq 0_{B_n}
\]

requires at least one of the following:

1. the baseline \(z\) is zero-valued but not the additive zero;
2. conditioning is affine or nonlinear;
3. the condition enters as an additional argument or tensor factor;
4. conditioning changes grade;
5. the Free Number state contains condition data not represented by the underlying linear carrier alone.

This is not a technical nuisance. It determines where the additional causal or response information actually lives.

### 4.1 Kernel displacement form

When subtraction is available and conditioning preserves value,

\[
m_n(\Gamma_{\lambda,n}(x))=m_n(x),
\]

we have

\[
\kappa_{\lambda}(x)
:=
\Gamma_{\lambda,n}(x)-x
\in\ker m_n.
\]

Hence every value-preserving deformation is a displacement inside a compression fiber.

Formally,

\[
\Gamma_{\lambda,n}(x)=x+\kappa_{\lambda}(x),
\qquad
\kappa_{\lambda}(x)\in\ker m_n.
\]

The crucial issue is not whether the displacement lies in the kernel. It must. The issue is whether the displaced kernel component changes later response.

For the additive zero,

\[
0[\lambda]
=
\Gamma_{\lambda,n}(0_{B_n})
=
\kappa_{\lambda}(0_{B_n}).
\]

A nonzero result therefore forces \(\Gamma_{\lambda,n}\) to be non-linear or affine, unless the notation is realized by another design route above.

---

## 5. Response deformation

### 5.1 Relative response

The primary observable is not the label \(\lambda\) itself but the response change it induces.

At finite depth define the comparison

\[
\Delta^{\lambda}_d J(x)
:=
\bigl(J_d(\Gamma_{\lambda,n}(x)),J_d(x)\bigr).
\]

This ordered-pair definition does not require subtraction.

In a linear response model one may instead write

\[
\Delta^{\lambda}_d J(x)
:=
J_d(\Gamma_{\lambda,n}(x))-J_d(x).
\]

The condition is detected through depth \(d\) precisely when

\[
\Delta^{\lambda}_d J(x)\neq 0.
\]

### 5.2 Conditioning depth

Define the minimum conditioning-detection depth, when it exists, by

\[
\delta_{\lambda}(x)
:=
\min\{d:J_d(\Gamma_{\lambda,n}(x))\neq J_d(x)\}.
\]

This separates:

- immediately visible conditioning;
- latent conditioning visible only after deeper probes;
- conditioning invisible to the current admissible probe family.

A condition may preserve value and every shallow profile while changing a deeper response.

### 5.3 Response capacity, not hidden value

A conditioned zero is not required to contain a concealed nonzero value waiting to be uncovered.

The stronger and more general statement is:

> its present compressed value is null, but its capacity to respond under admissible continuation is nontrivial.

Thus the mathematical content belongs to response structure, not to a hidden ordinary scalar.

---

## 6. Continuation tests

The smallest concrete tests should avoid a complete general probe theory at first.

Let \(z,z_{\lambda}\in Z_n\). For a right continuation \(y\in B_r\), test whether

\[
m_{n+r}(z\Vert y)
\neq
m_{n+r}(z_{\lambda}\Vert y).
\]

Likewise, for a left continuation \(x\in B_r\), test whether

\[
m_{r+n}(x\Vert z)
\neq
m_{r+n}(x\Vert z_{\lambda}).
\]

Internal insertion may detect distinctions invisible to both boundary continuations.

These tests define three potentially different response sectors:

1. left-boundary response;
2. right-boundary response;
3. internal response.

The abstract theory must not assume that one sector determines the others.

---

## 7. Composition obligations

Conditioning and composition create the first serious closure problem.

For \(x\in B_m\), \(y\in B_n\), and condition \(\lambda\), compare:

\[
\Gamma_{\lambda,m+n}(x\Vert y),
\]

\[
\Gamma_{\lambda,m}(x)\Vert y,
\]

\[
x\Vert\Gamma_{\lambda,n}(y),
\]

and, when meaningful,

\[
\Gamma_{\lambda,m}(x)\Vert\Gamma_{\lambda,n}(y).
\]

No equality among these expressions is assumed.

Their differences may encode:

- localization of the condition;
- cross-boundary interaction;
- duplication of a condition that should act only once;
- loss of global terminal information under factorization;
- or a new remainder required for compositional closure.

### 7.1 First closure question

The first decisive question is:

> Can the conditioned response profile of \(x\Vert y\) be reconstructed from the conditioned and unconditioned profiles of \(x\) and \(y\), together with finitely specified cross-boundary data?

Symbolically, seek a law of the form

\[
J(\Gamma_{\lambda}(x\Vert y))
=
\Phi_{\lambda}
\bigl(
J(x),J(y),J(\Gamma_{\lambda}x),J(\Gamma_{\lambda}y),X_{\lambda}(x,y)
\bigr),
\]

where \(X_{\lambda}(x,y)\) is explicit cross-boundary information.

If no such finite law exists, the failure itself must be recorded rather than hidden by quotienting.

---

## 8. Equality consequences

Compressed-value equality identifies all members of \(Z_n\):

\[
z\equiv_0 z_{\lambda}.
\]

A valid Free Numbers equality must distinguish them whenever their admitted response differs:

\[
J(z)\neq J(z_{\lambda})
\quad\Longrightarrow\quad
z\not\equiv z_{\lambda}.
\]

Therefore conditioned-zero witnesses are direct rejection tests for any proposed quotient.

A quotient is unacceptable if it forces

\[
Z_n/\!\equiv
\]

to be a singleton before proving that all members of the zero fiber have identical admissible response.

---

## 9. Relation to the quaternionic boundary-word model

The existing model supplies a natural zero fiber:

\[
B_n=V^{\otimes n},
\qquad
m_n:B_n\to\mathbb H,
\qquad
Z_n=\ker m_n.
\]

At length two,

\[
Z_2=\ker m_2=S^2_0V.
\]

Nonzero elements of \(S^2_0V\) are already zero-valued representatives with nontrivial insertion response. They therefore provide concrete candidates for the role abstractly denoted by \(0[\lambda]\).

What is not yet established is the map from an abstract condition \(\lambda\) to a specific kernel representative:

\[
\lambda\longmapsto z_{\lambda}\in\ker m_n.
\]

Nor is it established whether:

- every effective condition corresponds to one kernel element;
- one condition requires a family across several grades;
- the correspondence is linear, affine, nonlinear, or relational;
- the same condition can have multiple equivalent representative realizations;
- or quaternionic boundary words realize only one sector of the general phenomenon.

These are model-construction questions, not facts to assume.

---

## 10. Deliberate non-claims

This note does not claim:

1. that a future object already exists;
2. that information travels backward in physical time;
3. that every zero-valued state contains a condition;
4. that every condition is finitely detectable;
5. that a condition must be represented by a scalar label;
6. that conditioning is linear;
7. that the quaternionic kernel is the universal condition space;
8. that observational equality is already the final Free Numbers equality;
9. that a successful terminal result ethically or mathematically justifies every path to it.

The standalone claim is narrower:

> equal present compressed value does not exhaust state identity when admissible continuation can reveal different response.

---

## 11. Immediate proof and computation program

### P1. Zero-fiber inventory

For the quaternionic model, classify the response types inside

\[
Z_n=\ker m_n
\]

for the smallest grades.

### P2. Minimal condition realization

Find the weakest explicit data that can parameterize a nontrivial family

\[
\lambda\mapsto z_{\lambda}\in Z_n
\]

without making \(\lambda\) a decorative label.

### P3. Linearity decision

Determine whether the useful realization is:

- a choice of nonzero kernel representative;
- an affine displacement;
- a nonlinear action;
- a grade-changing extension;
- or an external condition paired with a representative.

### P4. Detection depth

Compute

\[
\delta_{\lambda}(z)
\]

for the first nontrivial examples and compare it with the established probe-depth filtration.

### P5. Small composition table

Compute conditioned and unconditioned products for:

\[
B_1\times B_1,
\qquad
B_2\times B_1,
\qquad
B_1\times B_2,
\qquad
B_2\times B_2.
\]

Record every cross-boundary term that changes response while preserving or collapsing compressed value.

### P6. Quotient rejection test

Apply each proposed equality relation to the conditioned-zero witnesses. Reject any relation that erases a proven response distinction.

---

## 12. Decision gate

This note is ready to feed into the abstract core only after the following question is answered:

> Where does conditioning live mathematically?

The first candidates are:

\[
\text{kernel representative},
\quad
\text{affine/nonlinear action},
\quad
\text{grade extension},
\quad
\text{external paired datum},
\]

or a controlled combination of them.

Until one candidate survives the smallest composition and probe tests, conditioned zero remains a required phenomenon rather than a finalized primitive.

The non-negotiable birth statement is:

\[
\boxed{
\text{same null value does not imply same future response}
}
\]

or, in representative form,

\[
\boxed{
z\neq z_{\lambda},
\quad
m_n(z)=m_n(z_{\lambda})=0_A,
\quad
J(z)\neq J(z_{\lambda}).
}
\]
