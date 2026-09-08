# DGG Research Snapshot 2026-09-07 audit1 — Claims ledger

The status in column 3 is the mathematical status asserted by the source.
The last column separately records verification performed while preparing
this snapshot. A carried-forward theorem is not represented as a freshly
rerun computation. Finite-field checks are not promoted to rational theorems.

| ID | Claim and scope | Status | Source | Snapshot verification |
|---|---|---|---|---|
| F01 | Local quaternionic decoders are invertible; terminal faces are onto; pairwise restrictions factor the literal responses | Established local algebra | Core v1; Note 12 | Literal state/probe factorizations independently checked exhaustively for 122,212,221,222; full n=6 and n=7 historical reconstructions also rerun |
| S01 | At n=5, the closed operator omega_5 identifies the 16-dimensional tetrahedral cokernel with H tensor H | Rational theorem | Note 14 | Original seed certificate passed during initial preparation; unchanged source retained with that provenance |
| S02 | The seed has an intrinsic orthogonal 12+4 split, with Frobenius coordinate nu | Rational theorem | Note 18 | Full original canonical-seed certificate rerun and passed in audit |
| A01 | The five n=6 placements have 48-dimensional quotients with the stated two-chart cover and anchor classification | Rational finite theorem | Note 20 | Full original five-placement atlas certificate rerun and passed in audit |
| A02 | The central transition is id_H tensor theta with minimal polynomial (t-1)^2(t+1) | Rational finite theorem | Note 20 | Full chart reconstruction and closed minimal-polynomial checks rerun and passed |
| A03 | The n=6 cap residual is chart-independent; the direct seed K4 tensor V lies in its kernel | Rational finite theorem | Notes 17, 19, 20 | Full seed-to-cap bridge and atlas certificates rerun and passed; manuscript now distinguishes response and decoded domains |
| E01 | Exterior left/right suspension tensorizes the local complex and every labelled edge image; left/right operations commute | All-length theorem, for exterior insertions | Note 22 | Symbolic all-length proof reviewed; original finite suspension certificate rerun and passed |
| W01 | The six reduced n=7 quotient dimensions are 144,144,144,148,144,144 | Rational finite theorem | Notes 21, 23 | All six reconstructed in fresh historical runs; 122,212,221 also checked independently over 1019 and against all literal state/probe products |
| W02 | All transported direct-anchor histories at n=7 have the stated three pair-local generators | Rational finite theorem | Note 24 | Full exhaustive anchor census, transition identities, commutator ranks and polynomial certificate rerun and passed |
| W03 | Six stationary-edge core maps give identity holonomy on the sole independent n=7 word loop | Rational finite theorem | Note 25 | Full original spacing-word transport reconstruction rerun; exact identity holonomy and full face-trace ranks passed |
| W04 | Kappa_212 vanishes on both incident outer hinges; the selected projection-defined full maps forget its four-dimensional summand | Rational finite theorem | Notes 21, 25 | Full exceptional and spacing-word certificates rerun; manuscript explicitly states that residual forgetting selects the zero extension |
| N01 | At 222 the matching rank is 5388 and quotient dimension is 444; all six edge ranks are as tabulated | Rational finite theorem | Note 26 | Corrected certificate rerun from a fresh cache; exact upper bounds and matching lower bounds rechecked; independent arithmetic over 1019 agrees |
| N02 | The common 432-dimensional outer-edge image is exactly the kernel of kappa_222 on Y; the residual quotient has dimension 12 | Rational finite theorem | Note 26 | Full exact verification and independent third-prime check passed |
| N03 | The 122 and 221 exterior edge comparisons descend to isomorphisms onto T_222 | Rational finite theorem | Note 26 | Both exact kernel comparisons passed; third-prime ranks also agree |
| N04 | A specified central-slot RIGHT decoder induces D_212 tensor V isomorphic to D_222 | Rational theorem with a specified comparison operator | Note 26 | Exact residual square and fixed-unit readout passed; operator choice remains explicit |
| N05 | That same suspension does not descend to Y_222; its obstruction image is all of T_222 | Rational theorem for that specified operator | Note 26 | Exact upper bound, lower bounds over three primes, and integer obstruction witness agree |
| X01 | The tetrahedral second complex is middle-exact at n=6,7 in the stated prime fields | Finite-field exact check only | Notes 13, 15 | Historical evidence archived; not a rational or all-length claim in the main manuscript |
| X02 | The complete three-spectator atlas, full interior-word transport, nonzero holonomy or curvature | Open | Source scope boundaries | Not claimed |
| X03 | A local state update F, condition update Psi, time generation, physical space generation | Open / interpretation outside this snapshot | Continuity boundary | Not claimed |

## Interpretation rules

- D_222 is a quotient. No canonical complementary 12-dimensional subspace
  inside Y_222 is selected in this snapshot.
- K_212 in the anchored decomposition and D_212 in the intrinsic residual
  quotient are related by the already specified residual coordinate; they
  are not silently substituted for one another.
- The central suspension puts an argument at gap 4 but multiplies its value
  on the right. It is not declared to be literal state-word insertion.
- A rank or a dimension match alone is not a transport theorem. The package
  supplies factorization identities, kernel comparisons and the obstruction.
- The hinge equation alone allows nonzero extensions on the invisible residual; the selected full maps use the zero extension.
- Flat core holonomy, nontrivial chart shear and a local residual are distinct
  statements. The snapshot does not call the residual core curvature.
- No priority or literature-wide novelty claim is certified by this archive.

## Review boundary

This audit1 candidate incorporates the corrections in AUDIT_REPORT.md.
The full logs distinguish fresh historical reruns, independent checks of
literal matrix meaning and rank arithmetic, and initial preparation checks
retained with unchanged source. This is an internal audit, not an external
referee report or a rerun of every exploratory note. The residual extension
choice and the exceptional face projection kernel are now explicit.
