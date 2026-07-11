# Free Numbers Core Reconstruction — Continuity Handoff

**Status:** continuity checkpoint and recovery protocol, not a theorem note  
**Branch:** `core-reconstruction`  
**Scope:** standalone Free Numbers core and its quaternionic boundary-word model  
**Do not merge automatically:** this branch is still reconstructive and contains open design choices

## 0. Purpose

This document is a model-continuity checkpoint.

It exists so that a new researcher or successor model can recover the current board without reconstructing the entire project from conversation history. It does not replace the source notes, and it must not be cited as proof of a statement whose proof belongs elsewhere.

The governing rule is:

> Preserve proved capabilities, preserve layer boundaries, and never promote a plausible continuation formula to theorem status without checking it under the fixed conventions.

If this file conflicts with a theorem note, exact computation, or checked formal artifact, the theorem note or artifact takes precedence.

---

## 1. Fifteen-minute recovery route

Read in this order.

1. `core/00-capability-ledger.md`
   - establishes what the reconstructed core is not allowed to lose;
   - takes priority over elegance and publication convenience.

2. `core/01-abstract-core.md`
   - gives the abstract scaffold;
   - distinguishes primitive candidates, derived targets, open choices, and model-specific facts.

3. `core/03-independence-audit.md`
   - proves that the local compression-fiber response distinction is independent of the Time Engine;
   - states clearly what remains unproved.

4. `core/04-length-two-exact-splitting.md`
   - gives the first exact concrete coordinate theorem;
   - fixes the sign, wedge, Hodge-star, and compression conventions used below.

5. `core/05-length-three-propagation.md`
   - gives exact one-step propagation from grade two to grade three;
   - proves finite complete observability at grade three through a depth-two component.

6. `core/02-conditioned-zero.md`
   - read this as an origin-and-design note, filtered through the independence audit;
   - it still contains interpretive vocabulary that must not become a core primitive.

For supporting concrete proofs, then read:

- `notes/03-length-2-and-3-residual-filtration.md`;
- `notes/04-length-3-depth-2-response.md`;
- `notes/06-general-vertical-response-theorem.md`;
- `notes/11-spin-depth-filtration.md`.

---

## 2. Current theory in one statement

The standalone reconstruction studies graded representatives

\[
B_0,B_1,B_2,\ldots
\]

with many-to-one compression maps

\[
m_n:B_n\to A,
\]

admissible contextual probes, and composition

\[
\Vert:B_m\times B_n\to B_{m+n},
\]

such that equality after compression does not erase distinctions that can reappear under continuation.

The target object must therefore retain, in a composition-compatible way:

\[
\boxed{
\text{compressed value}
\;+
\text{contextual response structure}
\;+
\text{residual depth}
}
\]

This is the standalone mathematical core.

No temporal ontology is required to state it.

---

## 3. Layer firewall

Keep the following layers separate.

### Layer A — Abstract standalone core

May use:

- grades or structural lengths;
- representatives;
- compression;
- admissible contexts and probes;
- response profiles;
- residual filtrations;
- composition;
- standalone equality or equivalence.

Must not use as primitives:

- future;
- terminal requirement;
- consciousness;
- ethics;
- ASI;
- Y-axis terminology;
- Time Engine ontology;
- chart registry or normalization machinery.

### Layer B — Quaternionic boundary-word model

Provides the current serious concrete realization:

\[
V=\operatorname{Im}\mathbb H,
\qquad
B_n=V^{\otimes n},
\qquad
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
\]

Theorems proved here are concrete-model theorems unless an abstract proof is supplied separately.

### Layer C — Certified Residual Chart OS

May provide:

- registries;
- boundary comparison;
- provenance;
- trace integrity;
- certified fold decisions;
- rewriting and normalization.

The OS may depend on the core. The existence of a Free Number must not depend on the OS merely because the OS was implemented first.

### Layer D — Originating interpretation

The Time Engine and Y-axis theory explain why the required capabilities were sought.

They may interpret a control datum as a terminal requirement, but that interpretation cannot serve as proof of a core law.

---

## 4. Fixed quaternionic conventions

Do not change these signs silently.

Let

\[
V=\operatorname{Im}\mathbb H
=\operatorname{span}_{\mathbb R}\{i,j,k\}
\]

with the Euclidean metric and quaternionic orientation.

For \(u,v\in V\),

\[
uv=-\langle u,v\rangle+u\times v.
\]

Boundary compression is reversed:

\[
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
\]

Thus

\[
m_2(u|v)=vu.
\]

For an oriented orthonormal basis \(e_1,e_2,e_3\), define

\[
g=\sum_{a=1}^3e_a|e_a.
\]

Use the unnormalised wedge

\[
u\wedge v=u|v-v|u
\]

and the orientation isomorphism

\[
*:\Lambda^2V\to V,
\qquad
*(u\wedge v)=u\times v.
\]

With these conventions,

\[
m_2(g)=-3,
\qquad
m_2|_{\Lambda^2V}=-2*.
\]

For insertion after the first \(r\) original entries,

\[
I_d^{(r)}(a_1|\cdots|a_n)
=
a_1|\cdots|a_r|d|a_{r+1}|\cdots|a_n,
\]

and

\[
\mathcal R_n^{(r)}(x)(d)=m_{n+1}(I_d^{(r)}x).
\]

Exterior insertions vanish on compression-kernel elements. Internal insertions carry the nontrivial residual tests.

---

## 5. Status ledger

The labels below are strict.

### 5.1 Proved in the quaternionic boundary-word model

1. Length-two tensor decomposition:

   \[
   B_2
   =
   \mathbb Rg\oplus\Lambda^2V\oplus S^2_0V.
   \]

2. Length-two compression kernel:

   \[
   \ker m_2=S^2_0V.
   \]

3. Explicit section:

   for \(q=a+w\in\mathbb H\),

   \[
   \sigma_2(q)
   =
   -\frac a3g-\frac12*^{-1}(w),
   \qquad
   m_2\sigma_2=\operatorname{id}_{\mathbb H}.
   \]

4. Residual projection:

   \[
   \rho_2
   =
   \operatorname{id}_{B_2}-\sigma_2m_2.
   \]

5. Exact length-two coordinate theorem:

   \[
   \Phi_2:B_2\xrightarrow{\cong}\mathbb H\oplus S^2_0V,
   \qquad
   \Phi_2(x)=(m_2(x),\rho_2(x)).
   \]

6. Canonical length-two response:

   \[
   A_2(S)=-2C_S
   \qquad(S\in S^2_0V).
   \]

   Hence the length-two value plus canonical internal response is injective.

7. Length-three depth-one signature:

   \[
   T_3
   =
   m_3\oplus\mathcal R_3^{(1)}\oplus\mathcal R_3^{(2)}
   \]

   has

   \[
   \operatorname{rank}T_3=20,
   \qquad
   \ker T_3=S^3_0V.
   \]

8. Canonical depth-two recovery at length three:

   \[
   A_3(R)=4C_R
   \qquad(R\in S^3_0V).
   \]

9. Finite complete length-three signature:

   \[
   \mathcal J_3^{\mathrm{exact}}
   =
   \bigl(
   m_3,
   \mathcal R_3^{(1)},
   \mathcal R_3^{(2)},
   A_3
   \bigr)
   \]

   is injective on \(B_3\).

10. Highest-spin vertical response for every \(n\ge2\):

    \[
    A_n(S)=(-2)^{n-1}C_S
    \qquad(S\in S^n_0V).
    \]

    This theorem concerns the canonical highest-spin component only. It is not a classification of the full residual profile.

11. Length four exhibits probe-depth splitting inside repeated representation multiplicities. Spin type alone does not determine detection depth.

### 5.2 Proved local independence result

The statement

\[
m_n(z)=m_n(z')=0_A,
\qquad
J(z)\ne J(z')
\]

is definitionally and model-theoretically independent of the Time Engine.

A minimal non-quaternionic witness exists using coordinate projection on \(\mathbb R^2\).

This proves independence of the local birth phenomenon, not completion of the full theory.

### 5.3 Partially closed

1. Response-profile composition is exact for:

   \[
   B_1\times B_1\to B_2,
   \qquad
   B_2\times B_1\to B_3,
   \qquad
   B_1\times B_2\to B_3.
   \]

2. For \(x\in B_2\) with

   \[
   \Phi_2(x)=(q,S),
   \]

   define

   \[
   L_{q,S}(d)
   =
   \langle\operatorname{Im}q,d\rangle
   -\frac{\operatorname{Re}q}{3}d
   -2S(d).
   \]

   Then

   \[
   L_{q,S}=\mathcal R_2(x).
   \]

3. Right extension by \(u\in V\):

   \[
   \begin{aligned}
   m_3(x|u)&=uq,\\
   \mathcal R_3^{(1)}(x|u)(d)&=uL_{q,S}(d),\\
   \mathcal R_3^{(2)}(x|u)(d)&=udq,\\
   A_3(x|u)(d_1,d_2)&=ud_2L_{q,S}(d_1).
   \end{aligned}
   \]

4. Left extension by \(u\in V\):

   \[
   \begin{aligned}
   m_3(u|x)&=qu,\\
   \mathcal R_3^{(1)}(u|x)(d)&=qdu,\\
   \mathcal R_3^{(2)}(u|x)(d)&=L_{q,S}(d)u,\\
   A_3(u|x)(d_1,d_2)&=L_{q,S}(d_2)d_1u.
   \end{aligned}
   \]

These are orientation-sensitive mirror laws, not commutative copies of one formula.

### 5.4 Open

1. Final abstract axiom system.
2. Final standalone equality.
3. Proof that observational equivalence is a congruence for every required operation.
4. Universal definition of admissible probes and probe depth.
5. Uniform all-grade response-profile product law.
6. Minimal complete coordinate object for grade three.
7. Complete grade-four coordinate and depth structure.
8. Product

   \[
   B_2\times B_2\to B_4.
   \]

9. Whether absolutely invisible structure exists and, if so, whether it may be quotiented out.
10. A canonical construction

    \[
    \lambda\mapsto z_\lambda
    \]

    for conditioned-zero notation.
11. Any claim that the quaternionic model is initial, universal, or unique.
12. Full-theory independence from the originating interpretation.

---

## 6. What the reconstruction has already forced

The exact grade-two pair

\[
(q,S)\in\mathbb H\oplus S^2_0V
\]

might suggest a fixed-format number consisting of one quaternion plus one residual decoration.

Grade three rules this out.

The depth-one grade-three signature loses exactly

\[
S^3_0V,
\]

and a depth-two component is required to recover it.

Therefore the current evidence forces a graded or hierarchical response object:

\[
\mathbf F_n
\sim
\bigl(
\text{value},
\text{depth-1 response},
\text{depth-2 response},
\ldots
\bigr),
\]

with no assumption that all grades require the same depth, codomain, or representation content.

This is a structural result of the low-grade calculations, not an originating interpretation.

---

## 7. Forbidden shortcuts

A successor must reject the following moves unless a new proof explicitly changes the board.

1. **Do not identify Free Numbers by quaternionic value alone.**

   \[
   m_n(x)=m_n(y)
   \not\Rightarrow
   x\equiv y.
   \]

2. **Do not call every kernel element zero information.**

3. **Do not identify additive zero with every zero-valued representative.**

4. **Do not treat the notation \(0[\lambda]\) as a constructed object.**

   No accepted map \(\lambda\mapsto z_\lambda\) currently exists.

5. **Do not claim that \(S^2_0V\) is the universal condition space.**

6. **Do not infer a universal residual ladder from the highest-spin theorem.**

7. **Do not infer detection depth from spin alone.**

   Length four already invalidates this simplification through multiplicity splitting.

8. **Do not identify reversal, quaternionic conjugation, context orientation, and reinterpretation.**

9. **Do not claim that \(\mathbb H\oplus S^2_0V\) already has the final Free Numbers multiplication.**

   It is currently an exact coordinate space at grade two.

10. **Do not claim that the single component \(A_3\) is the entire depth-two profile.**

    It is sufficient, together with depth-zero and depth-one data, for injectivity at grade three.

11. **Do not use floating-point rank or rounded Casimir output as a proof claim.**

    New decisive computations should use exact integer or rational arithmetic.

12. **Do not make the abstract core depend on the Residual Chart OS.**

13. **Do not import Time Engine language as a mathematical primitive.**

14. **Do not simplify merely to recover a familiar algebra if a Capability Ledger item is lost.**

---

## 8. Next cut: exact grade-four propagation

The next theorem note should be:

```text
core/07-length-four-cross-boundary-propagation.md
```

Its first product is

\[
B_2\times B_2\longrightarrow B_4.
\]

Let

\[
\Phi_2(x)=(q,S),
\qquad
\Phi_2(y)=(p,T),
\]

and write

\[
L_x=L_{q,S},
\qquad
L_y=L_{p,T}.
\]

Because \((q,S)\) and \((p,T)\) recover \(x\) and \(y\) exactly, the full tensor \(x|y\) is determined. The nontrivial problem is not existence of a formula. It is to expose a finite, intrinsic response formula and identify the new grade-four coordinates without expanding blindly back to all representatives.

### 8.1 First identities to verify

The following are the expected pure-word factorisations under the fixed reversed-compression convention.

They are recorded here as the first verification targets. They must be checked and proved in the next theorem note before being promoted to established status.

For \(d\in V\):

\[
\boxed{
\begin{aligned}
m_4(x|y)&=pq,\\
\mathcal R_4^{(1)}(x|y)(d)&=pL_x(d),\\
\mathcal R_4^{(2)}(x|y)(d)&=pdq,\\
\mathcal R_4^{(3)}(x|y)(d)&=L_y(d)q.
\end{aligned}
}
\]

For insertions in two distinct original internal gaps, define provisional components \(D_{12},D_{13},D_{23}\). The expected factorisations are

\[
\boxed{
\begin{aligned}
D_{12}(x|y)(d_1,d_2)
&=p\,d_2\,L_x(d_1),\\
D_{13}(x|y)(d_1,d_2)
&=L_y(d_2)L_x(d_1),\\
D_{23}(x|y)(d_1,d_2)
&=L_y(d_2)d_1q.
\end{aligned}
}
\]

For insertion in all three original internal gaps, the expected canonical factorisation is

\[
\boxed{
A_4(x|y)(d_1,d_2,d_3)
=
L_y(d_3)d_2L_x(d_1).
}
\]

Again: these are next-step targets, not theorem claims of this handoff.

### 8.2 First genuine residual-residual interaction

The middle depth-two component

\[
D_{13}(x|y)(d_1,d_2)
=
L_y(d_2)L_x(d_1)
\]

contains the direct bilinear interaction of the two length-two residuals.

Expanding only the residual-residual term predicts the ordered contribution

\[
\boxed{
4\,T(d_2)S(d_1).
}
\]

Since quaternion multiplication is noncommutative, its scalar and vector parts are

\[
-4\langle T(d_2),S(d_1)\rangle
\]

and

\[
4\,T(d_2)\times S(d_1),
\]

respectively.

The order \(T\) then \(S\) is structural and must not be symmetrised away.

### 8.3 Grade-four representation warning

The rotation-module decomposition is

\[
V^{\otimes4}
\simeq
3V_0\oplus6V_1\oplus6V_2\oplus3V_3\oplus V_4,
\]

with dimension check

\[
81=3+18+30+21+9.
\]

Repeated multiplicities are therefore unavoidable.

The next note must not ask only which spin is visible. It must ask which copy inside each multiplicity space is visible at each probe depth.

### 8.4 Required computations

The next note should perform these steps in order.

1. Prove the factorisation formulas above by pure-word calculation and linear extension.
2. Expand all value-value, value-residual, residual-value, and residual-residual channels.
3. Identify which terms cross the central boundary between the two grade-two factors.
4. Construct exact integer or rational matrices for the chosen grade-four signatures.
5. Compute ranks and kernels exactly at each depth.
6. Decompose repeated spin multiplicities using exact equivariant projectors or another exact method.
7. Compare the result with the existing length-four spin-depth filtration evidence.
8. Determine whether a finite complete signature is obtained through depth three.
9. If complete, seek a smaller intrinsic coordinate object; do not confuse a large injective signature with a minimal one.
10. Record any closure failure as new Free Numbers data rather than quotienting it away.

### 8.5 Acceptance gate for the next theorem note

Do not call grade four closed until all of the following are supplied:

- exact propagation identities;
- exact rank data;
- identification of every remaining blind subspace;
- explicit treatment of multiplicity coordinates;
- a statement of the minimum proved detecting depth;
- a precise distinction between a complete signature and a minimal coordinate;
- explicit non-claims preventing universal extrapolation.

---

## 9. Abstract-core update gate

Do not modify `core/01-abstract-core.md` merely because the quaternionic formulas look suggestive.

Promote a concrete pattern into the abstract scaffold only after deciding which of the following it is:

1. intrinsically required by the Capability Ledger;
2. forced by every acceptable model;
3. specific to quaternionic boundary words;
4. an artifact of the selected probe family;
5. an implementation requirement of the Residual Chart OS.

The current strongest abstract conclusion is still:

> A standalone Free Numbers core consists of graded representatives with compressible values, admissible contextual re-observation, residual depth, and a composition-compatible equality that preserves what compression alone cannot see.

The quaternionic model now proves that this demand is nonempty and structurally rich through grade three.

---

## 10. Current checkpoint verdict

The reconstruction has passed three major gates.

### Gate 1 — Independent birth phenomenon

\[
\text{same compressed value}
\not\Rightarrow
\text{same response profile}
\]

stands without the originating ontology.

### Gate 2 — First exact Free Number coordinate

\[
B_2\cong\mathbb H\oplus S^2_0V
\]

gives a complete value-residual coordinate at grade two.

### Gate 3 — First exact propagation and forced hierarchy

Grade-two coordinates propagate exactly to a complete finite grade-three signature, while grade three creates a new residual sector one depth lower than the value surface.

The next gate is the first collision of two nontrivial residual-bearing factors:

\[
\boxed{
B_2\times B_2\to B_4.
}
\]

That calculation will decide whether the emerging hierarchy admits a controlled finite composition law or whether a new kind of cross-boundary remainder must become part of the Free Numbers data.
