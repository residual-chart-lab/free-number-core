# Claims Ledger Addendum — 2026-07-12

This addendum records repairs completed after the initial audited `CLAIMS_LEDGER.md`. It is authoritative for the three claim entries below until the amendments are integrated into their parent documents and the main ledger is regenerated.

## 1. FN-ARCH-001 — Local quaternionic closure

**Updated status:** `PROVED` for the explicit quotient construction.

Define

\[
F_1=T(U)/(u^2+1,\ v^2+1,\ uv+vu).
\]

Then every word reduces to a linear combination of \(1,u,v,uv\), while the map \(u\mapsto i\), \(v\mapsto j\) surjects onto \(\mathbb H\). Hence \(\dim F_1=4\), and

\[
F_1\cong_{\mathbb R\mathrm{-alg}}\mathbb H.
\]

**Source:** `paper/LOCAL_CLOSURE_PRESENTATION_AMENDMENT.md`.

**Integration remaining:** replace the implicit construction in `paper/free_numbers.tex`.

## 2. FN-CONF-001 — Certified confluence

This entry is split into two claims.

### FN-CONF-001A — Current root-only local confluence

**Status:** `PROVED-CONDITIONAL`.

For fixed registry and `decideGen`, if `LocalMul` is functional, current root-only `CertifiedRed` is one-step deterministic and therefore locally confluent by equality. Its strict termination measure remains Lean-checked.

**Source:** `notes/12a-certified-red-confluence-repair.md`.

### FN-CONF-001B — Contextual confluence modulo BoundaryIso

**Status:** `PROOF-SCHEMA` / `OPEN`.

The intended theorem requires an explicit contextual reduction, local-algebra hypotheses, certificate preservation, decision stability, reduction-compatible `BoundaryIso`, contextual termination, and a precise Newman theorem modulo equivalence.

The single `GenDecision` removes the independent existing/fresh ambiguity, but does not discharge these other obligations.

## 3. FN-CORE1-009 — Higher coherent residual sector

**Status unchanged:** `PROVED` + `EXACT-CHECK`.

The proof dependency is now explicit:

\[
\ker(D_{13}|_{RR})
=F_2^{(4)}\cap RR
=S^4_0V
=V_4.
\]

The equality uses the checked global subspace result \(F_2^{(4)}=S^4_0V\), not merely the nine-dimensional kernel count.

**Source:** `core/07-kernel-identification-amendment.md`.

## Repair state

| Repair | Mathematical status | Parent-file integration |
|---|---|---|
| Explicit \(F_1\) quotient presentation | complete | pending |
| Note 12 theorem split | complete | pending |
| Core 07 kernel argument | complete | pending |

No claim in this addendum concerns novelty or priority in the literature.
