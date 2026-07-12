# Free Numbers Claims Ledger

**Snapshot date:** 2026-07-12  
**Repository state audited:** `main` at `a06856a` plus the 25 commits on `core-reconstruction`  
**Purpose:** separate proved results, exact computations, Lean-checked statements, specifications, proof schemas, conjectures, superseded routes, and open problems.

This ledger is a status record. It does **not** claim that every listed result is new in the literature. Priority, novelty, and comparison with prior work require a separate review.

## Status vocabulary

| Status | Meaning |
|---|---|
| `PROVED` | A complete mathematical proof is present in the cited source and survived the present internal audit. |
| `PROVED-CONDITIONAL` | Correct under explicit construction assumptions or hypotheses that must remain visible. |
| `EXACT-CHECK` | Verified by exact integer or rational computation with a reproducible certificate. |
| `LEAN` | Typechecked in the current Lean kernel, subject to the stated axioms, representations, and placeholders. |
| `SPECIFICATION` | A definition, design constraint, or policy; not an existence theorem. |
| `PROOF-SCHEMA` | The intended argument is visible, but additional definitions or hypotheses are required before it is a theorem. |
| `SCOPE-VERDICT` | A declared stopping or packaging boundary, not a universal mathematical theorem. |
| `CONJECTURE` | Proposed but not proved. |
| `REFUTED` | A previously tempting claim is shown false. |
| `SUPERSEDED` | Retained for history but replaced by a later formulation. |
| `OPEN` | Explicitly unresolved. |
| `INDEPENDENT` | A detachable result not used in the Free Numbers theorem chain. |

## Layer map

The repository currently contains distinct layers that must not be silently identified.

1. **Local closure / Residual Chart OS:** local quaternionic charts, admissible identity, generated boundaries, transport policy, and normalization.
2. **Quaternionic response theory:** boundary words, compression kernels, insertion response, spin-depth filtration, and vertical response.
3. **Free Numbers Core v1:** the standalone quaternionic exact-response realization on the tensor algebra.
4. **Lean normalization skeleton:** restricted reduction, structural certificate reversal, and finite-registry decision.
5. **Independent appendix:** the last-percent delay model.

Core v1 does not prove the full Residual Chart OS. Conversely, the chart-normalization layer is not needed for the Core v1 reconstruction theorem.

---

## A. Local closure and architecture

### FN-ARCH-001 — Local quaternionic closure

- **Status:** `PROVED-CONDITIONAL` as a presentation theorem.
- **Claim:** A four-dimensional unital associative real algebra with basis \(e_0,I,J,K\) and quaternion relations
  \[
  I^2=J^2=K^2=-e_0,\qquad IJ=K,\quad JK=I,\quad KI=J
  \]
  is isomorphic to \(\mathbb H\).
- **Evidence:** `paper/free_numbers.tex`, proposition “Local quaternionic form.”
- **Audit note:** The statement is standard and correct. The current paper effectively installs the quaternion relations and then identifies the resulting algebra. It does not yet derive associativity, linear independence, or the full multiplication law from a more primitive fold-plane construction alone. The source should define \(F_1\) explicitly as the corresponding associative presented algebra or Clifford algebra.

### FN-ARCH-002 — Global chart identity is not compressed-value equality

- **Status:** `SPECIFICATION`.
- **Claim:** In the Residual Chart OS, generated charts are not automatically identified merely because their local quaternionic values agree.
- **Evidence:** `paper/free_numbers.tex`; `notes/07-admissible-identity-layer.md`.
- **Caveat:** This is an identity policy for the chart system, not a theorem excluding every alternative global quotient.

### FN-ARCH-003 — Boundary-word compression model

- **Status:** `SPECIFICATION`.
- **Claim:** For \(V=\operatorname{Im}\mathbb H\),
  \[
  B_n=V^{\otimes n},\qquad
  m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
  \]
- **Evidence:** Notes 01–06 and Core v1.

### FN-ARCH-004 — Core v1 and the Residual Chart OS are distinct layers

- **Status:** `SPECIFICATION` / scope separation.
- **Claim:** Core v1 is the associative exact-response realization on \(T(V)\). Registries, generated-chart provenance, `BoundaryIso`, `EqAdm`, `ResidualPurity`, transport, and normalization remain outside Core v1.
- **Evidence:** `core/09-core-closure-theorem.md`, §12.
- **Caveat:** Associativity of Core v1 does not establish global associativity for the separate generated-chart system.

---

## B. Observation kernels and insertion response

### FN-OBS-001 — Same-eye observation no-go

- **Status:** `PROVED`.
- **Claim:** If \(\Omega\in\ker\Phi\), then every observation factoring through \(\Phi\) also kills \(\Omega\). One observation cannot both erase and witness the same distinction.
- **Evidence:** `notes/01-non-aligned-compression-kernels.md`; `notes/no-go-single-compression.md`.
- **Caveat:** A second observation detects \(\Omega\) only if it is genuinely non-aligned.

### FN-OBS-002 — Canonical insertion-response profile

- **Status:** `SPECIFICATION`, with a proved exterior-vanishing lemma.
- **Claim:** Probe insertion followed by compression defines
  \[
  \mathcal R_n^{(r)}(x)(c)=m_{n+1}(I_c^{(r)}x).
  \]
  If \(x\in\ker m_n\), both exterior insertion responses vanish.
- **Evidence:** `notes/02-insertion-response-witness.md`.

### FN-OBS-003 — First non-aligned residual witness

- **Status:** `PROVED`.
- **Claim:** For
  \[
  \sigma=i|j+j|i,
  \]
  one has \(\sigma\in\ker m_2\), but
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
  one has \(\tau_k\in\ker m_3\), while
  \[
  \mathcal R_3^{(1)}(\tau_k)(pi+qj+rk)=-2pi+2qj.
  \]
- **Evidence:** `notes/02-insertion-response-witness.md`.
- **Caveat:** These examples alone do not prove an infinite residual ladder.

---

## C. Residual structure at lengths two and three

### FN-L2-001 — Length-two kernel decomposition

- **Status:** `PROVED`.
- **Claim:**
  \[
  V\otimes V=\mathbb Rg\oplus\Lambda^2V\oplus S^2_0V,
  \qquad
  \ker m_2=S^2_0V.
  \]
- **Evidence:** `notes/03-length-2-and-3-residual-filtration.md`.

### FN-L2-002 — Length-two response recovery

- **Status:** `PROVED`.
- **Claim:**
  \[
  \mathcal R_2^{(1)}|_{S^2_0V}=-2\,\mathrm{id},
  \qquad
  K_2^{\mathrm{null}}=0.
  \]
- **Evidence:** `notes/03-length-2-and-3-residual-filtration.md`.

### FN-L3-001 — Length-three next-null residual

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:**
  \[
  K_3^{\mathrm{null}}=S^3_0V\cong V_3.
  \]
- **Evidence:** Representation-theoretic containment and exact rank \(20\) in `notes/03-length-2-and-3-residual-filtration.md`.

### FN-L3-002 — Length-three depth-two recovery

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:**
  \[
  A_3(S)=4C_S\qquad(S\in S^3_0V).
  \]
- **Evidence:** `notes/04-length-3-depth-2-response.md`.

### FN-L3-003 — Complete length-three spin-depth profile

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:**
  \[
  K_3\cong2V_1\oplus2V_2\oplus V_3.
  \]
  Depth one detects \(2V_1\oplus2V_2\), and depth two detects \(V_3\).
- **Evidence:** `notes/10-depth-one-detection-in-length-three.md`; `certificates/depth_one_detection_certificate.py`.

---

## D. General probe depth and vertical response

### FN-DEPTH-001 — Probe-depth filtration

- **Status:** `SPECIFICATION`.
- **Claim:**
  \[
  K_n=F_0^{(n)}\supseteq F_1^{(n)}\supseteq F_2^{(n)}\supseteq\cdots,
  \]
  where \(F_{d-1}^{(n)}/F_d^{(n)}\) is first detected at depth \(d\).
- **Evidence:** `notes/05-general-probe-depth-profile.md`; `notes/11-spin-depth-filtration.md`.

### FN-DEPTH-002 — Top-spin visibility lower bound

- **Status:** `PROVED`.
- **Claim:** The depth-\(d\) target contains no \(V_n\) when \(d<n-1\), so \(S^n_0V\cong V_n\) cannot be detected before depth \(n-1\).
- **Evidence:** `notes/05-general-probe-depth-profile.md`.
- **Dependency:** Equivariance of the response maps under the standard \(SO(3)\) action.

### FN-VERT-001 — General vertical response theorem

- **Status:** `PROVED`.
- **Claim:**
  \[
  A_n(S)=(-2)^{n-1}C_S
  \qquad(S\in S^n_0V,\ n\ge2).
  \]
- **Evidence:** `notes/06-general-vertical-response-theorem.md`.
- **Caveat:** This concerns the canonical all-gap component on the highest-spin summand, not the entire lower-depth profile.

### FN-VERT-002 — Verified low-length coefficients

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:**
  \[
  A_2=-2C,\qquad A_3=4C,\qquad A_4=-8C.
  \]
- **Evidence:** Notes 03–06.

---

## E. Spin-depth multiplicity structure

### FN-SPIN-001 — Exact tables for \(n=2,3,4\)

- **Status:** `EXACT-CHECK`.
- **Claim:** The depth-filtered spin multiplicities are exactly those listed in Note 11.
- **Evidence:** `notes/11-spin-depth-filtration.md`; `certificates/note11_certificate.py`.

### FN-SPIN-002 — Top-spin last-survivor equality at low length

- **Status:** `EXACT-CHECK` for \(n=2,3,4\); `CONJECTURE` as a full-profile all-\(n\) statement.
- **Claim verified at low length:**
  \[
  F_{n-2}^{(n)}=S^n_0V\qquad(n=2,3,4).
  \]
- **Caveat:** The proved all-\(n\) result is the injectivity of the all-gap response and the vertical-response theorem, not this stronger lower-depth equality.

### FN-SPIN-003 — Naive diagonal rule

- **Status:** `REFUTED`.
- **Refuted claim:** “Spin \(s\) is always first detected at depth \(s-1\).”
- **Counterexample:** At \(n=4\), copies of the same spin split across different depths.
- **Evidence:** Note 11.

### FN-SPIN-004 — First multiplicity-depth splitting

- **Status:** `EXACT-CHECK`.
- **Claim:** At \(n=4\), the six \(V_2\) copies split \(3+3\) across depths one and two; the five \(V_1\) copies split \(4+1\).
- **Evidence:** Note 11 and its certificate.

### FN-SPIN-OPEN-001 — General multiplicity-depth law

- **Status:** `OPEN`.
- **Problem:**
  \[
  \dim\,\mathrm{gr}_d\,\operatorname{Hom}_{SO(3)}(V_s,V^{\otimes n})
  \]
  as a closed function of \(n,s,d\), refined where necessary by factor origin.
- **Evidence:** Note 11; Core v1.

---

## F. Free Numbers Core v1 — Quaternionic exact-response core

### FN-CORE1-001 — Local decoder

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:** The map
  \[
  \Theta:V\otimes\mathbb H\to\operatorname{Hom}(V,\mathbb H),
  \qquad
  \Theta\!\left(\sum_a e_a\otimes h_a\right)(d)=\sum_a e_adh_a
  \]
  is an isomorphism, with
  \[
  h_a=\frac12\sum_{b,c}\varepsilon_{abc}e_bF(e_c),
  \qquad
  \det\Theta=256.
  \]
- **Evidence:** `core/08-all-grade-response-reconstruction.md`; `certificates/core08_all_grade_response_certificate.py`.
- **Audit:** The inverse formula and determinant were independently recomputed during this ledger audit.

### FN-CORE1-002 — All-grade reconstruction

- **Status:** `PROVED` + `EXACT-CHECK`.
- **Claim:** For every finite \(n\ge0\),
  \[
  A_n:B_n\xrightarrow{\cong}\mathfrak A_n=\operatorname{im}A_n,
  \qquad
  A_n(x)=A_n(y)\iff x=y.
  \]
- **Evidence:** `core/08-all-grade-response-reconstruction.md`.
- **Certificate scope:** Exact full-column-rank checks for \(n=1,\ldots,5\), plus recursive and composition identities.
- **Audit:** The induction is valid once the local decoder is established.

### FN-CORE1-003 — Finite visibility bound

- **Status:** `PROVED`.
- **Claim:** Admitting the all-gap response gives
  \[
  F_{n-1}^{(n)}=0,
  \qquad
  \delta(x)\le n-1
  \quad(x\ne0).
  \]
- **Evidence:** All-grade reconstruction theorem.
- **Caveat:** Finite grades only; no claim about infinite words or completions.

### FN-CORE1-004 — Exact-response graded algebra

- **Status:** `PROVED`.
- **Claim:** With
  \[
  (F\star G)(\mathbf d,\delta,\mathbf e)
  =G(\mathbf e)\,\delta\,F(\mathbf d),
  \]
  the direct sum
  \[
  \mathfrak A=\bigoplus_{n\ge0}\mathfrak A_n
  \]
  is a unital associative graded real algebra, and
  \[
  A:T(V)\xrightarrow{\cong}\mathfrak A
  \]
  is a graded algebra isomorphism.
- **Evidence:** `core/08-all-grade-response-reconstruction.md`; `core/09-core-closure-theorem.md`.
- **Audit note:** As an algebraic carrier, Core v1 is isomorphic to the familiar tensor algebra. Its additional structure is the distinguished compression, probe family, zero fibers, and depth filtration.

### FN-CORE1-005 — Lower observations factor through the exact coordinate

- **Status:** `PROVED`.
- **Claim:** Every linear observation \(O:B_n\to W\) factors uniquely on \(\mathfrak A_n\) as
  \[
  O=(O\circ A_n^{-1})\circ A_n.
  \]
- **Evidence:** Core 08.
- **Caveat:** This is a transport-of-structure statement; it does not provide a minimal closed formula for every transported observation.

### FN-CORE1-006 — Active zero states

- **Status:** `PROVED`.
- **Claim:** The transported compression
  \[
  \mu_n=m_n\circ A_n^{-1}
  \]
  has nonzero kernel for \(n\ge2\). In particular,
  \[
  Z_2=\ker\mu_2\cong S^2_0V.
  \]
- **Evidence:** Core 09 and the length-two theorem.

### FN-CORE1-007 — Pure residual collision at grade four

- **Status:** `PROVED`.
- **Claim:** For nonzero \(S,T\in S^2_0V\),
  \[
  m_4(S|T)=0,
  \]
  all depth-one responses vanish, but
  \[
  D_{13}(S|T)(d_1,d_2)=4T(d_2)S(d_1)
  \]
  is not the zero map. Hence \(\delta(S|T)=2\).
- **Evidence:** `core/07-length-four-cross-boundary-propagation.md`.
- **Audit:** Nonvanishing follows from the division-algebra property of \(\mathbb H\).

### FN-CORE1-008 — Length-four factor-origin filtration

- **Status:** `EXACT-CHECK`.
- **Claim:** Under
  \[
  B_4=VV\oplus VR\oplus RV\oplus RR,
  \]
  the sectorwise remaining-kernel dimensions are
  \[
  \begin{array}{c|rrrr}
  &F_0&F_1&F_2&F_3\\\hline
  VV&12&0&0&0\\
  VR&20&12&0&0\\
  RV&20&12&0&0\\
  RR&25&25&9&0
  \end{array}
  \]
  and the full kernel dimensions are \(77,49,9,0\).
- **Evidence:** `certificates/core07_cross_boundary_certificate.py`.
- **Audit:** These ranks were independently recomputed.

### FN-CORE1-009 — Higher coherent residual sector

- **Status:** `EXACT-CHECK` + `PROVED` identification using the prior \(n=4\) top-spin equality.
- **Claim:**
  \[
  \ker(D_{13}|_{RR})=V_4=S^4_0V,
  \]
  and no nonzero decomposable \(S\otimes T\) lies in this kernel.
- **Evidence:** Core 07; Note 11; both certificates.
- **Audit note:** Rank \(16\) on the \(25\)-dimensional \(RR\) sector gives a nine-dimensional kernel, but dimension and multiplicity-freeness alone do not identify it as \(V_4\). The identification also uses the independently checked equality \(F_2^{(4)}=S^4_0V\). The Core 07 prose should cite that step explicitly.

### FN-CORE1-010 — Core v1 closure declaration

- **Status:** `SCOPE-VERDICT`.
- **Declaration:** The package
  \[
  \mathfrak F_{\mathrm{v1}}
  =
  \left(
  \mathfrak A,\star,1,\deg,(\mu_n),\mathcal P,(F_d^{(n)})
  \right)
  \]
  is closed as the first standalone quaternionic exact-response realization.
- **Evidence:** `core/09-core-closure-theorem.md`; `core/free_numbers_core_v1.tex`.
- **Meaning:** Reconstruction, exact equality, and composition are complete for this finite-grade realization.
- **Not implied:** universality, novelty, completion of the Residual Chart OS, or classification of the depth spectrum.

---

## G. Admissible identity, transport, and derivation splitting

### FN-ID-001 — Three-part admissible identity layer

- **Status:** `SPECIFICATION`.
- **Claim:** The chart system distinguishes `BoundaryIso`, `EqAdm`, and `ResidualPurity`.
- **Evidence:** Note 07.
- **Caveat:** The prose layer is richer than the current Lean implementation.

### FN-ID-002 — Projected equality does not infer chart identity

- **Status:** `SPECIFICATION` / inference prohibition.
- **Claim:** Compression equality or external projected equality is not sufficient to infer `BoundaryIso`, `EqAdm`, or erasure of residual mismatch.
- **Evidence:** Note 07.

### FN-TRANSPORT-001 — Transport separation principle

- **Status:** `SPECIFICATION`.
- **Claim:** Transport remains external to restricted `Red` and is admitted as preparation only after signature visibility, identity preservation, residual preservation, and decrease of a separate cost.
- **Evidence:** Note 08.
- **Caveat:** Existence of such transports and transport-inclusive confluence are not proved.

### FN-SPLIT-001 — Derivation splitting schema

- **Status:** `CONJECTURE` / proof obligation.
- **Proposed structure:**
  \[
  \mathrm{Derivation}/\!\sim_{\mathrm{admin}}
  \simeq
  \sum_{c:\mathrm{BoundaryCertificate}}
  \mathrm{ResidualTraceOver}(c).
  \]
- **Evidence:** Note 09.

---

## H. Certified rewriting and confluence audit

### FN-CONF-001 — Restricted certified weak confluence

- **Status:** `PROOF-SCHEMA`; **not yet established for the current formal definitions**.
- **Intended claim:** A suitably defined contextual `CertifiedRed` is weakly confluent up to `BoundaryIso` when generated-boundary normalization is controlled by one `GenDecision`.
- **Evidence:** Note 12.
- **Blocking gaps found in this audit:**
  1. `LocalMul` is an arbitrary relation in `Minimal.lean`; the same input pair may reduce to different atoms. Functionality or local confluence of `LocalMul` is not assumed.
  2. The Lean `CertifiedRed` is root-only. The “inner G1 / outer generated-boundary decision” critical pair discussed in Note 12 is not represented by the current term relation.
  3. Newman-style reasoning modulo `BoundaryIso` requires a precise reduction-compatible equivalence framework, not only an informal local join statement.
  4. The full structural `EqAdm` and nontrivial `ResidualPurity` used by the prose theorem are not implemented.
- **Repair target:** State the missing hypotheses explicitly, define contextual closure, and machine-check the modulo-equivalence Newman argument.

### FN-CONF-002 — Finite certified generation decision

- **Status:** `PROVED-CONDITIONAL` in the abstract finite-data model + `LEAN` for the current structural skeleton.
- **Claim:** A finite registry can be searched for an existing witness, with the negative result yielding the fresh branch, provided the witness predicate is decidable.
- **Evidence:** Note 12; `lean/DecideGen.lean`.
- **Caveat:** The current implementation searches the present structural `BoundaryIso`; `ResidualPurity` is still `True`, and the full intended `EqAdm` checks are absent.

---

## I. Lean implementation ledger

### FN-LEAN-001 — Restricted raw-kernel termination

- **Status:** `LEAN`.
- **Checked statement:**
  ```lean
  Red X Y -> weight Y < weight X
  ```
- **Evidence:** `lean/Minimal.lean`.
- **Dependencies:** `propext`, `LocalMul`, `ExistingBoundary`, and `FreshBoundary`.
- **Caveat:** This is not full transport termination or confluence.

### FN-LEAN-002 — CertifiedRed termination

- **Status:** `LEAN`.
- **Checked statement:** `CertifiedRed` driven by one `GenDecision` strictly decreases the same weight.
- **Evidence:** `lean/Certified.lean`.

### FN-LEAN-003 — Structural certificate reversal calculus

- **Status:** `LEAN`.
- **Checked statement:** Equality up to one explicit reversal involution is reflexive, symmetric, transitive, and decidable.
- **Evidence:** `lean/BoundaryIsoStructural.lean`.
- **Caveat:** Tags embedded from `Minimal.Boundary` are currently conservative defaults.

### FN-LEAN-004 — Structural finite-registry decision

- **Status:** `LEAN`, partial implementation.
- **Checked statement:** `decideGenFromRegistry` returns a `GenDecision` using the current structural `BoundaryIso`.
- **Evidence:** `lean/DecideGen.lean`.
- **Caveat:** Nontrivial `ResidualPurity`, full provenance, and full `EqAdm` checks are deferred.

### FN-LEAN-005 — Equality-only certificate scaffold

- **Status:** `SUPERSEDED` as the active relation.
- **Description:** `lean/BoundaryIso.lean` uses literal certificate equality.
- **Superseded by:** `lean/BoundaryIsoStructural.lean` connected through `lean/Certified.lean`.

---

## J. Superseded, rejected, or refuted routes

### FN-HIST-001 — Single compression as complete residual carrier

- **Status:** `SUPERSEDED`.
- **Reason:** A map cannot witness distinctions in its own kernel. The active mathematics uses non-aligned response maps and exact-response coordinates.
- **Evidence:** No-go note and Note 01.

### FN-HIST-002 — Externally tagged residual foundations

- **Status:** `SUPERSEDED` / rejected as foundations.
- **Routes:** hand-added tags, \(\varepsilon\mathbb H\), Rees variables, bare free-magma distinctions, and undecorated reduction logs.
- **Reason:** They either add the distinction by hand or retain process data without the canonical quaternionic response mechanism.
- **Evidence:** Note 01 and the no-go note.

### FN-HIST-003 — Simple spin-depth diagonal

- **Status:** `REFUTED`.
- **Replacement:** Probe depth filters multiplicity and factor-origin spaces inside a fixed spin.
- **Evidence:** Note 11 and Core 07.

---

## K. Independent appendix model

### FN-APP-001 — Last-percent delay model

- **Status:** `INDEPENDENT`; analytic derivations are `PROVED` conditional on the model equation.
- **Model:**
  \[
  \frac{dE}{dt}=-\frac{kE}{1+(\alpha/E)^n}.
  \]
- **Derived law:**
  \[
  t(E)=\frac1k\left[
  \log\frac{E_0}{E}
  +\frac{\alpha^n}{n}(E^{-n}-E_0^{-n})
  \right].
  \]
- **Evidence:** `appendix/last-percent-delay-hypothesis-v0.2.1.md`.
- **Caveat:** Not used in the Free Numbers theorem chain.

### FN-APP-002 — Physical terminal-tail existence

- **Status:** `OPEN` empirical question.
- **Non-claim:** No real battery, organism, or physical reserve is asserted to obey the equation without measurement.

---

## L. Global non-claims

The audited repository does **not** currently establish:

1. novelty or priority relative to all existing literature;
2. a universal characterization of all Free Numbers models;
3. completion of the Residual Chart OS by Core v1;
4. the current Note 12 weak-confluence claim under the existing Lean definitions;
5. full trace-level or transport-inclusive confluence;
6. a nontrivial implemented `ResidualPurity`;
7. the full intended `EqAdm` and provenance extraction;
8. a closed all-\(n\) spin-multiplicity-factor-origin-depth formula;
9. infinite-word, completion, or limiting response theorems;
10. Time Engine, cognition, consciousness, or physical claims.

---

## M. Immediate repair and packaging tasks

1. Rewrite the local \(F_1\) section as an explicit associative presentation or Clifford-algebra construction.
2. Correct Note 12: add `LocalMul` determinism/local confluence, define contextual reduction, and state the exact modulo-equivalence Newman hypotheses.
3. Update Note 12’s Lean-status section to reflect the structural reversal connection.
4. In Core 07, replace the dimension-only wording around \(\ker(D_{13}|_{RR})=V_4\) with an explicit citation to the checked \(F_2^{(4)}=S^4_0V\) subspace equality.
5. Decide whether the equality-only `lean/BoundaryIso.lean` remains active or moves to an archive.
6. Replace `ResidualPurity := True` before claiming a complete certified normalization engine.
7. Add stable theorem labels and a machine-readable `claims-ledger.json`.
8. Perform a separate prior-art and novelty audit before arXiv submission.
