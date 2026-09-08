# DGG internal audit — 2026-09-07

**Outcome:** the stated finite mathematics is retained after corrections to
scope, coordinate definitions and certificate validation. No contradictory
rank or operator identity was found in the audited theorem chain.
The corrected review candidate is **research-2026-09-07-audit1**.
This is an internal mathematical and computational audit, not an external
referee report or a novelty assessment.

The audited starting point was commit
74395434fe6441c272ccf4d345297fd9c427ea22, fixed by the earlier local tag
dgg-research-2026-09-07. The earlier source state remains recoverable.

## 1. Conclusions that survived the audit

| Object or comparison | Confirmed result |
|---|---|
| Seed tetrahedron | 16-dimensional quotient; intrinsic orthogonal \(12+4\) split |
| Five one-spectator placements | Dimension 48; stated direct-anchor cover and central transition |
| Central transition | \(m_\theta(t)=(t-1)^2(t+1)\) |
| Six reduced two-spectator words | \(144,144,144,148,144,144\) |
| Two-spectator stationary-edge connection | Six invertible core maps; identity holonomy on the independent loop |
| Child 222 matching | Rank 5388 in a target of dimension 5832 |
| Child 222 quotient | Dimension 444; common outer-edge subspace \(T_{222}\) of dimension 432 |
| Child 222 residual | Intrinsic quotient \(D_{222}=Y_{222}/T_{222}\), dimension 12 |
| Generic parents 122 and 221 | Specified exterior edge comparisons are isomorphisms onto \(T_{222}\) after tensoring with \(V\) |
| Central parent 212 | Specified right decoder gives \(D_{212}\otimes V\cong D_{222}\), rank 12 and zero kernel |
| Fixed unit-vector comparison | Rank 4, zero kernel; \(k=-f_k(w)\) |
| Full central suspension | Does not descend to the full quotients; obstruction image is exactly \(T_{222}\), rank 432 |

No dimension in this table was changed by the audit.

## 2. Corrections

### A1. Completeness of a cached cokernel certificate

The former cached path checked \(L\partial=0\) and full row rank of \(L\),
but inferred the matching lower bound from the number of rows returned by
the cached nullspace. These two identities alone do not establish that
the annihilator is complete: deleting one row preserves both.

The corrected certificate recomputes the matching rank over both primes,
even on a cache hit. It also checks off-incidence and off-grading blocks
are zero. A regression deliberately deletes one annihilator row: the old
two tests still pass, while the corrected completeness test rejects it.

This was a gap in validation of reused results. The original recorded
empty-cache calculation did compute the full nullspace; the fresh corrected
run and the independent third-prime check agree with its dimensions.

Caches now depend on hashes of both implementations. Optimized Python
execution is rejected because it removes assertions; invalid prime inputs
are also rejected. These safeguards protect the advertised verification
route and do not add mathematical hypotheses.

### A2. Residual forgetting is a specified extension

The shared hinges have zero \(\kappa_{212}\) block. This proves that the
residual is invisible on those hinges. It does not uniquely determine an
extension of the core map to the exceptional full quotient.

With the selected splitting, every linear extension has the form
\[
\rho_B(t,k)=g t+B k,\qquad B\in\operatorname{Hom}(K_{212},T_\mu).
\]
The existing defect-forgetting construction selects \(B=0\). Even
equivariance does not force that selection: after identifying \(K_{212}\)
with \(\mathbb H\),
\[
q\longmapsto q\otimes1\otimes\sum_{a=1}^3e_a\otimes e_a
\]
is a nonzero equivariant injection into the displayed \(T_7\) model.

The source note already recognized that additional extensions require data.
The manuscript now preserves this qualification explicitly. Core flatness
and the kernels of the selected maps are unchanged.

### A3. The exceptional common-face trace is not a graph over the hinge

A generic trace has dimension 144 and projects isomorphically to the
144-dimensional hinge row space. The full exceptional trace has dimension
148 and projects onto that same space with a four-dimensional kernel.
Calling both traces graphs of functions over the hinge was incorrect.
The manuscript and Note 25 now distinguish these cases. The claimed zero
intersection of the two face trace row spaces remains correct.

### A4. Coordinate domains and omitted definitions

The manuscript now defines the two cap contractions. It distinguishes
their action on response spaces from the decoded operators
\(\widehat\lambda_3^\bullet=\lambda_3^\bullet J_3\), so the identity with
the tensor-coordinate chart is explicitly well-typed. It also states the
chart identification used for the long-edge kernel, the inner product for
\(\iota^*\), the direct-anchor normalization, the reflection/shear operators,
and that the spin-profile entries are isotypic dimensions.

## 3. Verification evidence

The revised Note 26 certificate was rerun from a newly created cache. It
uses two prime fields, 1009 and 1013, to reconstruct operators and then
checks integer identities for the rational upper bounds.

The additional audit uses:

- expanded four-component Hamilton multiplication, independent of the
  production XOR grading and sign table;
- every state-basis tensor and every probe-basis tensor on all six edges
  of 122, 212, 221 and 222, comparing both incident face factorizations;
- NumPy forward elimination with reversed row/column ordering and Python
  modular inversion over the third prime 1019, independently of the
  production C++ Gauss–Jordan implementation.

There were **25,509,168 quaternion-valued comparisons**, counting the two
incident endpoints separately, with no mismatch. The four graded child
matching ranks were \(1347,1347,1347,1347\), summing to 5388. The child edge
ranks were \(432,336,408,120,336,432\); the obstruction rank was 432.

This independently checks the interpretation and rank arithmetic of the
production defining matrices. It is not described as an independent
reconstruction of the whole research program. Third-prime ranks supplement
the exact rational certificates; they do not replace their upper bounds.

Fresh runs also passed for the canonical seed coordinate, full \(n=6\)
atlas, seed-to-cap bridge, exceptional \(n=7\) decomposition, exterior
suspension identities, generic \(n=7\) atlas and spin profiles, exhaustive
anchor groupoid, and spacing-word transport. The seed tetrahedron and
targeted theta checks from the initial preparation are retained with their
actual execution provenance.

The exact scripts, full logs, results and source hashes are indexed by
verification/verification-record.json. The PDF has 16 pages; all were
rendered and visually inspected, with no overfull boxes in the final build.

## 4. Remaining claim boundary

The audited endpoint is one three-spectator word and its specified
comparison maps. There is no complete three-spectator atlas, canonical
interior insertion rule, nonzero core holonomy, state-update law, or
time-generation theorem here. The 12-dimensional residual remains a
quotient; no preferred complementary subspace is claimed.

The audit does not rerun every exploratory or historical certificate in
Notes 00–26. The finite-field-only historical middle-exactness observations
remain labelled as such. The all-length exterior theorem rests on its
symbolic argument, with finite computational checks of the identities.

The revised package is a concrete review candidate for a separate DGG
research record. This audit does not alter the frozen Core v1.0.0 artifact
or claim that a new Zenodo record has been published.
