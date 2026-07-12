# Free Numbers Claims Ledger

**Snapshot date:** 2026-07-12  
**Repository state audited:** `main` through the structural `BoundaryIso` connection  
**Purpose:** separate proved results, exact computations, Lean-checked statements, specifications, conjectures, superseded formulations, and open problems.

This ledger is a status record, not a claim that every listed result is new in the literature. Priority and novelty require a separate prior-art review.

## Status vocabulary

| Status | Meaning |
|---|---|
| `PROVED` | A mathematical proof is given in the cited paper or note. |
| `EXACT-CHECK` | Verified by exact integer or rational computation with a reproducible certificate. |
| `LEAN` | Typechecked in the current Lean kernel, subject to the stated axioms and placeholders. |
| `SPECIFICATION` | A definition, design constraint, or policy; not an existence theorem. |
| `CONJECTURE` | Proposed but not proved. |
| `REFUTED` | A previously tempting claim is shown false. |
| `SUPERSEDED` | Retained for history but replaced by a later formulation. |
| `OPEN` | Explicitly unresolved. |
| `INDEPENDENT` | A detachable appendix result that is not part of the Free Numbers theorem chain. |

---

## A. Core architecture

### FN-ARCH-001 — Local quaternionic closure

- **Status:** `PROVED` in the main paper; not yet fully formalized in Lean.
- **Claim:** The local closure used by the project has quaternionic form, written \(F_1\simeq\mathbb H\).
- **Evidence:** `paper/free_numbers.tex`; summarized in `README.md` and Note 07.
- **Caveat:** This local identification does not imply that all generated charts are one global ambient copy of \(\mathbb H\).

### FN-ARCH-002 — Global identity is not compressed-value equality

- **Status:** `SPECIFICATION`.
- **Claim:** Generated charts are not automatically identified merely because their quaternionic compressed values agree.
- **Evidence:** `README.md`; `notes/07-admissible-identity-layer.md`.
- **Caveat:** This is a governing identity rule. It is not by itself a theorem excluding all alternative global models.

### FN-ARCH-003 — Boundary-word compression

- **Status:** `SPECIFICATION`.
- **Claim:** For \(V=\operatorname{Im}\mathbb H\), the boundary-word spaces are \(B_n=V^{\otimes n}\), with reversed compression
  \[
  m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
  \]
- **Evidence:** Notes 01–06.

---

## B. Observation kernels and insertion response

### FN-OBS-001 — Same-eye observation no-go

- **Status:** `PROVED`.
- **Claim:** If \(\Omega\in\ker\Phi\), then no observation factoring through \(\Phi\) can detect \(\Omega\). The same observation cannot both define collapse and witness a distinction erased by that collapse.
- **Evidence:** `notes/01-non-aligned-compression-kernels.md`; `notes/no-go-single-compression.md`.
- **Caveat:** This does not imply that every second observation detects the residual. The second observation must be non-aligned.

### FN-OBS-002 — Canonical insertion-response profile

- **Status:** `SPECIFICATION`.
- **Claim:** Internal probe insertion followed by the next compression defines response maps
  \[
  \mathcal R_n^{(r)}(x)(c)=m_{n+1}(I_c^{(r)}x).
  \]
  For \(x\in\ker m_n\), exterior insertions vanish, so internal insertions are the relevant residual witnesses.
- **Evidence:** `notes/02-insertion-response-witness.md`.

### FN-OBS-003 — First non-aligned residual witness

- **Status:** `PROVED`.
- **Claim:** For
  \[
  \sigma=i|j+j|i,
  \]
  one has \(\sigma\in\ker m_2\), while the internal response is nonzero:
  \[
  \mathcal R_2^{(1)}(\sigma)(\alpha i+\beta j+\gamma k)
  =-2\beta i-2\alpha j.
  \]
- **Evidence:** `notes/02-insertion-response-witness.md`.

### FN-OBS-004 — Second-stage witness at length three

- **Status:** `PROVED`.
- **Claim:** For
  \[
  \tau_k=i|k|j+j|k|i,
  \]
  one has \(\tau_k\in\ker m_3\), but a length-four insertion response is nonzero:
  \[
  \mathcal R_3^{(1)}(\tau_k)(pi+qj+rk)=-2pi+2qj.
  \]
- **Evidence:** `notes/02-insertion-response-witness.md`.
- **Caveat:** These examples do not by themselves prove an infinite residual ladder.

---

## C. Length-two and length-three residual structure

### FN-L2-001 — Length-two kernel decomposition

- **Status:** `PROVED`.
- **Claim:** Under
  \[
  V\otimes V=\mathbb Rg\oplus\Lambda^2V\oplus S^2_0V,
  \]
  the compression sees the trace and antisymmetric sectors and kills exactly the symmetric trace-free sector:
  \[
  \ker m_2=S^2_0V.
  \]
- **Evidence:** `notes/03-length-2-and-3-residual-filtration.md`.

### FN-L2-002 — Length-two response recovery

- **Status:** `PROVED`.
- **Claim:** On \(S^2_0V\), the internal response is
  \[
  \mathcal R_2^{(1)}=-2\,\mathrm{id},
  \]
  hence
  \[
  K_2^{\mathrm{null}}=0.
  \]
- **Evidence:** `notes/03-length-2-and-3-residual-filtration.md`.

### FN-L3-001 — Length-three next-null residual

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:** With the full depth-one internal response,
  \[
  K_3^{\mathrm{null}}=S^3_0V\cong V_3.
  \]
- **Evidence:** Representation-theoretic containment plus an exact integer rank-20 computation in `notes/03-length-2-and-3-residual-filtration.md`.

### FN-L3-002 — Length-three depth-two recovery

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:** The internal-internal depth-two component satisfies
  \[
  A_3(S)=4C_S\qquad(S\in S^3_0V),
  \]
  so the length-three top-spin residual is invisible at depth one but visible at depth two.
- **Evidence:** `notes/04-length-3-depth-2-response.md`.

### FN-L3-003 — Complete length-three spin-depth profile

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:**
  \[
  K_3\cong2V_1\oplus2V_2\oplus V_3.
  \]
  Depth one detects \(2V_1\oplus2V_2\), and depth two detects the remaining \(V_3\).
- **Evidence:** `notes/10-depth-one-detection-in-length-three.md`; `certificates/depth_one_detection_certificate.py`.

---

## D. General probe depth and vertical response

### FN-DEPTH-001 — Probe-depth filtration

- **Status:** `SPECIFICATION`.
- **Claim:** The combined compression and internal response maps define decreasing residual kernels
  \[
  K_n=F_0^{(n)}\supseteq F_1^{(n)}\supseteq F_2^{(n)}\supseteq\cdots,
  \]
  where \(F_{d-1}^{(n)}/F_d^{(n)}\) is the part first detected at probe depth \(d\).
- **Evidence:** `notes/05-general-probe-depth-profile.md`; `notes/11-spin-depth-filtration.md`.

### FN-DEPTH-002 — Representation-theoretic lower bound for top-spin visibility

- **Status:** `PROVED`.
- **Claim:** The highest-spin source component \(S^n_0V\cong V_n\) cannot occur in a depth-\(d\) response target for \(d<n-1\). The first possible depth is \(d=n-1\).
- **Evidence:** `notes/05-general-probe-depth-profile.md`.

### FN-VERT-001 — General vertical response theorem

- **Status:** `PROVED`.
- **Claim:** For every \(n\ge2\), the canonical vertical response on the highest-spin component is
  \[
  A_n(S)=(-2)^{n-1}C_S\qquad(S\in S^n_0V).
  \]
  Therefore \(A_n\) is injective on \(S^n_0V\).
- **Evidence:** `notes/06-general-vertical-response-theorem.md`.
- **Caveat:** This theorem concerns one canonical vertical component, not the complete response profile at every depth.

### FN-VERT-002 — Verified low-length coefficients

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:**
  \[
  A_2=-2C,\qquad A_3=4C,\qquad A_4=-8C
  \]
  on the corresponding symmetric trace-free components.
- **Evidence:** Notes 03–06 and the exact length-four sign check cited in Note 06.

---

## E. Spin-depth multiplicity structure

### FN-SPIN-001 — Exact spin-depth tables for lengths two, three, and four

- **Status:** `EXACT-CHECK`, with analytic proofs for the stated lower-length components.
- **Claim:** The remaining-kernel multiplicities by probe depth are exactly those listed in Note 11 for \(n=2,3,4\).
- **Evidence:** `notes/11-spin-depth-filtration.md`; `certificates/note11_certificate.py`.

### FN-SPIN-002 — Top-spin last-survivor pattern at n = 2, 3, 4

- **Status:** `EXACT-CHECK` for \(n=2,3,4\); `CONJECTURE` as a full-profile all-\(n\) statement.
- **Claim verified at low length:**
  \[
  F_{n-2}^{(n)}=S^n_0V\qquad(n=2,3,4).
  \]
- **Evidence:** `notes/11-spin-depth-filtration.md`; `certificates/note11_certificate.py`.
- **Caveat:** The all-\(n\) theorem currently proved is only the canonical vertical response theorem, not this stronger full-profile equality.

### FN-SPIN-003 — Naive diagonal spin-depth rule

- **Status:** `REFUTED`.
- **Refuted claim:** “Spin \(s\) is always first detected at depth \(s-1\).”
- **Counterexample:** At \(n=4\), copies of the same spin split across different probe depths.
- **Evidence:** `notes/11-spin-depth-filtration.md`.

### FN-SPIN-004 — First multiplicity-depth splitting

- **Status:** `EXACT-CHECK`.
- **Claim:** At \(n=4\), the six \(V_2\) copies in \(K_4\) split as three detected at depth one and three surviving to depth two. The five \(V_1\) copies split as four at depth one and one at depth two.
- **Evidence:** `notes/11-spin-depth-filtration.md`; `certificates/note11_certificate.py`.

### FN-SPIN-OPEN-001 — General multiplicity-depth law

- **Status:** `OPEN`.
- **Problem:** Find a closed formula for the depth-graded multiplicity spaces
  \[
  \dim\,\mathrm{gr}_d\,\mathrm{Hom}_{SO(3)}(V_s,V^{\otimes n}).
  \]
- **Evidence:** `notes/11-spin-depth-filtration.md`.

---

## F. Admissible identity, transport, and confluence

### FN-ID-001 — Three-part admissible identity layer

- **Status:** `SPECIFICATION`.
- **Claim:** Global generated identity is controlled by three distinct conditions:
  - `BoundaryIso` for generated boundary identity;
  - `EqAdm` for admissible equivalence;
  - `ResidualPurity` for retained residual mismatch.
- **Evidence:** `notes/07-admissible-identity-layer.md`.
- **Caveat:** The prose specification is richer than the current Lean implementation.

### FN-ID-002 — Projected equality does not infer admissible identity

- **Status:** `SPECIFICATION` / inference prohibition.
- **Claim:** Equality after compression or external projection is not sufficient to infer `BoundaryIso`, `EqAdm`, or erasure of residual mismatch.
- **Evidence:** `notes/07-admissible-identity-layer.md`.

### FN-TRANSPORT-001 — Transport separation principle

- **Status:** `SPECIFICATION`.
- **Claim:** Transport is external to restricted `Red`. A transport is usable as preparation only after it is signature-visible, preserves the admissible identity layer and residual mismatch, and strictly decreases a separate well-founded transport cost \(\kappa_T\).
- **Evidence:** `notes/08-transport-policy.md`.
- **Caveat:** The note does not prove the existence of such transports or transport-inclusive confluence.

### FN-SPLIT-001 — Derivation splitting schema

- **Status:** `CONJECTURE` / proof obligation.
- **Proposed structure:**
  \[
  \mathrm{Derivation}/\!\sim_{\mathrm{admin}}
  \simeq
  \sum_{c:\mathrm{BoundaryCertificate}}\mathrm{ResidualTraceOver}(c).
  \]
- **Evidence:** `notes/09-derivation-splitting-certificate-confluence.md`.
- **Caveat:** The splitting is intentionally not claimed as proved. The residual trace is a dependency-aware trace monoid, not the full derivation log and not a bare multiset.

### FN-CONF-001 — Restricted certified weak confluence

- **Status:** `PROVED` in Note 12; not yet fully machine-checked as the complete structural theorem.
- **Claim:** Restricted `CertifiedRed` is weakly confluent up to `BoundaryIso` on boundary certificates when generated-boundary normalization is represented by one certified `GenDecision` rather than independent existing/fresh predicates.
- **Evidence:** `notes/12-certified-red-restricted-weak-confluence.md`.
- **Caveat:** No syntactic, trace-level, transport-inclusive, or unrestricted confluence is claimed.

### FN-CONF-002 — Finite certified generation decision

- **Status:** `PROVED` in the finite-data model + `LEAN` for the current structural skeleton.
- **Claim:** For a finite registry, a generated boundary can be classified as either an existing certified fold or fresh by finite search, provided the witness predicates are decidable finite checks.
- **Evidence:** Note 12; `lean/DecideGen.lean`.
- **Caveat:** Current `ResidualPurity` is the permissive placeholder `True`, and full provenance extraction is not implemented.

---

## G. Lean implementation ledger

### FN-LEAN-001 — Restricted raw-kernel termination

- **Status:** `LEAN`.
- **Claim checked:**
  ```lean
  Red X Y -> weight Y < weight X
  ```
  for
  ```lean
  weight X = openGenCount X + openGenCount X + termSize X.
  ```
- **Evidence:** `lean/Minimal.lean`.
- **Dependencies:** Lean `propext` plus the abstract relations `LocalMul`, `ExistingBoundary`, and `FreshBoundary` as documented in `RELEASE-NOTES_v0.2-pre.2.md`.
- **Caveat:** This is restricted generated normalization, not the full transport system.

### FN-LEAN-002 — CertifiedRed termination

- **Status:** `LEAN`.
- **Claim checked:** `CertifiedRed` driven by one `GenDecision` strictly decreases the same weight.
- **Evidence:** `lean/Certified.lean`.

### FN-LEAN-003 — Structural certificate reversal calculus

- **Status:** `LEAN`.
- **Claim checked:** Structural boundary-certificate isomorphism defined as equality up to one explicit reversal involution is reflexive, symmetric, transitive, and decidable.
- **Evidence:** `lean/BoundaryIsoStructural.lean`.
- **Caveat:** Structural tags are presently conservative placeholders when embedded from `Minimal.Boundary`; full provenance extraction is deferred.

### FN-LEAN-004 — Structural finite-registry decision

- **Status:** `LEAN`, partial implementation.
- **Claim checked:** `decideGenFromRegistry` searches a finite boundary registry using the current structural `BoundaryIso` relation and returns a `GenDecision`.
- **Evidence:** `lean/DecideGen.lean`.
- **Caveat:** Nontrivial `ResidualPurity` and the full intended `EqAdm` preservation checks are not yet implemented.

### FN-LEAN-005 — Equality-based certificate scaffold

- **Status:** `SUPERSEDED` as the active certified-kernel relation; retained as an earlier conservative scaffold.
- **Description:** `lean/BoundaryIso.lean` defines certificate isomorphism as literal equality.
- **Superseded by:** `lean/BoundaryIsoStructural.lean` and its connection through `lean/Certified.lean`.

---

## H. Superseded or rejected routes

### FN-HIST-001 — Single-compression residual as a complete carrier

- **Status:** `SUPERSEDED`.
- **Earlier route:** Treat a quotient or a single quaternionic compression as both residual detector and history carrier.
- **Reason for replacement:** A single observation cannot witness distinctions in its own kernel. The active route uses non-aligned insertion responses and retained boundary-word structure.
- **Evidence:** `notes/no-go-single-compression.md`; Note 01.

### FN-HIST-002 — Externally tagged residual carriers

- **Status:** `REJECTED` as foundations.
- **Routes tested:** hand-added tags, \(\varepsilon\mathbb H\), Rees variables, bare free-magma distinctions, and undecorated reduction logs.
- **Reason:** They either add the residual by hand, enlarge the carrier without deriving the structure, or retain process information without a quaternion-specific canonical witness.
- **Evidence:** Note 01 and the no-go note.

### FN-HIST-003 — Simple spin-depth diagonal

- **Status:** `REFUTED`.
- **Replacement:** Probe depth filters multiplicity spaces inside a fixed spin, beginning visibly at length four.
- **Evidence:** Note 11.

---

## I. Independent appendix model

### FN-APP-001 — Last-percent delay model

- **Status:** `INDEPENDENT`; analytic derivations are `PROVED` conditional on the model equation.
- **Model:**
  \[
  \frac{dE}{dt}=-\frac{kE}{1+(\alpha/E)^n}.
  \]
- **Derived result:**
  \[
  t(E)=\frac1k\left[\log\frac{E_0}{E}+\frac{\alpha^n}{n}(E^{-n}-E_0^{-n})\right].
  \]
- **Evidence:** `appendix/last-percent-delay-hypothesis-v0.2.1.md`.
- **Caveat:** This is explicitly not a Free Numbers theorem and is not used in the Free Numbers theorem chain.

### FN-APP-002 — Physical existence of a terminal tail

- **Status:** `CONJECTURE` / empirical question.
- **Claim not made:** No real battery, organism, reserve, or physical system is claimed to obey the terminal-tail equation without measurement.
- **Evidence:** `appendix/last-percent-delay-hypothesis-v0.2.1.md`.

---

## J. Global non-claims

The current repository does **not** claim:

1. a completed theory of meaning, cognition, time, or physical reality;
2. full trace-level confluence;
3. transport-inclusive confluence;
4. global syntactic normal-form uniqueness;
5. decidability of semantic equality under every future context;
6. a complete classification of all residual components for every length;
7. a closed all-\(n\) multiplicity-depth formula;
8. a completed Lean implementation of full provenance, nontrivial `ResidualPurity`, or the full intended `EqAdm` checks;
9. that the project’s core claims are individually unprecedented in the literature.

---

## K. Immediate audit tasks

1. Audit the proof and literature status of `FN-ARCH-001` directly against `paper/free_numbers.tex`.
2. Add stable theorem anchors or labels to Notes 01–12 so ledger entries can cite exact theorem identifiers rather than file names alone.
3. Update Note 12’s “Current Lean implementation status,” which predates the structural `BoundaryIso` connection.
4. Decide whether the superseded equality-only `lean/BoundaryIso.lean` remains in the active build path or moves to an archival directory.
5. Replace `ResidualPurity := True` with a first nontrivial finite predicate before claiming a complete certified normalization engine.
6. Add a machine-readable companion, such as `claims-ledger.json`, after the human ledger stabilizes.
