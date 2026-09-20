# Free Numbers

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21328470.svg)](https://doi.org/10.5281/zenodo.21328470)

**Frozen release:** Core v1.0.0  
**Version DOI:** [10.5281/zenodo.21328471](https://doi.org/10.5281/zenodo.21328471)  
**Concept DOI:** [10.5281/zenodo.21328470](https://doi.org/10.5281/zenodo.21328470)  
**Frozen tag:** `core-v1.0.0`  
**Frozen commit:** `9efc241d38e5ca2cd07f425b747bfb5d67ea0235`  
**License:** MIT

> Compression is not disappearance.

Free Numbers Core v1.0.0 is a quaternionic exact-response framework for finite boundary words. It studies information that is lost under ordinary quaternionic compression but remains recoverable through canonical probe insertion.

## Core v1.0.0

For \(V=\operatorname{Im}\mathbb H\), let

\[
B_n=V^{\otimes n},
\qquad
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
\]

The frozen Core v1.0.0 release establishes an exact-response realization in which finite boundary states can be reconstructed from their all-gap probe responses.

The audited core includes:

- an explicit associative presentation of the local quaternionic closure;
- the local decoder
  \[
  \Theta:V\otimes\mathbb H\longrightarrow\operatorname{Hom}(V,\mathbb H),
  \]
  with explicit inverse and exact determinant `256`;
- all-grade reconstruction for every finite tensor length;
- finite visibility: every nonzero finite state is detected by depth at most `n-1`;
- an associative bridge product on exact-response coordinates;
- the vertical-response law on the highest-spin component;
- exact low-length spin-depth calculations and reproducible certificates;
- a claims ledger separating proofs, exact checks, specifications, conjectures, and open problems.

## Scope

Core v1.0.0 is deliberately narrower than the full Free Numbers research program.

It does **not** claim:

- completion of the full Residual Chart OS;
- contextual confluence modulo `BoundaryIso`;
- a complete all-length multiplicity-depth classification;
- universality or novelty relative to all prior literature;
- physical, temporal, cognitive, or consciousness applications.

The current root-only certified reduction is deterministic and locally confluent under functional `LocalMul`. The stronger contextual confluence problem remains open under explicit hypotheses.

## Frozen release

- [GitHub Release: `core-v1.0.0`](https://github.com/residual-chart-lab/free-number-core/releases/tag/core-v1.0.0)
- [Zenodo record for v1.0.0](https://doi.org/10.5281/zenodo.21328471)
- [Concept DOI for all versions](https://doi.org/10.5281/zenodo.21328470)
- [Audited reconstruction branch](https://github.com/residual-chart-lab/free-number-core/tree/core-reconstruction)

The release bundle contains the PDF and LaTeX sources, the claims ledger, supporting notes, exact computational certificates, a release manifest, and SHA-256 checksums.

## Depth-Generated Geometry research snapshot

A separate [DGG Research Snapshot 2026-09-07](research/depth-generated-geometry/releases/research-2026-09-07/README.md)
consolidates the ordered quaternionic quotient atlas through Note 26, with a
standalone manuscript, claim ledger and reproducibility records. The audited
snapshot was published on Zenodo on September 7, 2026 as an independent preprint.

- **Version:** `research-2026-09-07-audit1`
- **Version DOI:** [10.5281/zenodo.22646591](https://doi.org/10.5281/zenodo.22646591)
- **All DGG versions:** [10.5281/zenodo.22646590](https://doi.org/10.5281/zenodo.22646590)
- **Archived source:** [audited source tree](https://github.com/residual-chart-lab/free-number-core/tree/110113dd763da371bb6e02c6c5083b40dd12aecc)

## Research navigation for readers and AI agents

This work develops a quaternionic exact-response framework for finite ordered
words in the Free Numbers Program.

**[Note 25](research/depth-generated-geometry/notes/25-n7-spacing-word-flat-core-and-quaternionic-defect.md)** establishes a flat, 144-dimensional stationary-edge core
connection on the reduced two-spectator spacing-word graph, with identity
holonomy \(I_{144}\).

**[Note 26](research/depth-generated-geometry/notes/26-n8-222-residual-redetection.md)** studies the three-internal-spectator word \(222\). Its quotient
has dimension 444, with a 432-dimensional outer-edge core and a 12-dimensional
residual quotient. A specified central-slot right decoder induces an
isomorphism of residual quotients, while its full descent obstruction has
image equal to the entire 432-dimensional core.

For exact rational verification, run from the repository root:

```bash
python3 research/depth-generated-geometry/certificates/n8_222_redetection_certificate.py --certificate
```

From the extracted DGG snapshot directory, use:

```bash
python3 certificates/n8_222_redetection_certificate.py --certificate
```

See the DGG [claims ledger](research/depth-generated-geometry/releases/research-2026-09-07/CLAIMS_LEDGER.md)
for theorem scope and [reproducibility guide](research/depth-generated-geometry/releases/research-2026-09-07/REPRODUCIBILITY.md)
for dependencies and verification records.

**Post-snapshot Note 27:** [minimal state refinement for the central update](research/depth-generated-geometry/notes/27-minimal-state-refinement-for-central-update.md)
keeps Note 26's specified operation and full target fixed. Its coarsest linear
source refinement has dimension 876, retaining 432 additional dimensions.
The full output is then well-defined, but the update still has a
432-dimensional kernel. The proof and exact certificate are separate from
the frozen Core release and published DGG snapshot.

**Post-snapshot Note 28:** [decoder continuations and retained core](research/depth-generated-geometry/notes/28-decoder-continuations-and-retained-core.md)
shows that the existing central-probe coefficient readouts jointly detect
all 432 directions lost by that update. Supporting one, two, or three
independent coefficient directions requires a minimal child refinement of
dimension 588, 732, or 876. With full retention, the specified encoding and
decoding induce inverse maps between the two 876-dimensional refinements.

**Post-snapshot Note 29:** [forward insertion beyond decoder closure](research/depth-generated-geometry/notes/29-forward-insertion-beyond-decoder-closure.md)
tests the next fixed internal insertion, from 222 to 232. The retained
state tensored with the new vector has dimension 2628; preserving its
information and the new full output requires a minimal refinement of
dimension 3924. The extra 1296 dimensions map onto the entire new outer
core. The certificate includes a counterexample with the new vector fixed
to i and a compatible-triple description over the 36-dimensional residual.

**Post-snapshot Note 30:** [ordered insertion paths and local interchange](research/depth-generated-geometry/notes/30-ordered-insertion-paths-and-local-interchange.md)
compares two insertion orders with the same input and final labels. Their
endpoint difference has rank 1320. A fixed local quaternionic comparison
accounts for the raw ordering difference, and its descent obstruction on
the endpoint quotient has dimension 1296. Retaining both paths' intermediate
and final states requires a minimal common state of dimension 6516.
Even equal nonzero endpoints can differ under the same later gap-5
coefficient readout; the hidden difference has rank 1296. Supporting that
readout on both retained paths raises the minimum to 7668.

**Post-snapshot Note 31:** [symmetric endpoint law and recovered core](research/depth-generated-geometry/notes/31-symmetric-endpoint-law-and-recovered-core.md)
identifies the determined 144-dimensional readout-core quotient with the
original core T212 through an explicit equivariant isomorphism. The common
source and the sum of the two endpoints already determine this quotient.
On the source core, the two new vectors contribute through their inner
product; the endpoint sum contributes through a rank-144 map.

**[Retention and path-readout checkpoint, Notes 27–31](research/depth-generated-geometry/synthesis/retention-and-path-readout-checkpoint.md)**
collects the theorem chain, the conditions attached to each dimension,
the recovered-core law, and the remaining research branches.

## Repository map

| Path | Contents |
|---|---|
| `core/` | Core v1 theorem chain, TeX source, and frozen PDF |
| `paper/` | Broader paper source and local-closure presentation |
| `certificates/` | Exact computational certificates |
| `notes/` | Technical development notes and open branches |
| `lean/` | Lean normalization and certified-reduction skeletons |
| `CLAIMS_LEDGER.md` | Audited status of repository claims |
| `CLAIMS_LEDGER_ADDENDUM_2026-07-12.md` | Parent-document integration record |

## Citation

```text
Residual Chart Lab. (2026). Free Numbers Core v1.0.0 (Version 1.0.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.21328471
```

Machine-readable citation metadata is provided in [`CITATION.cff`](CITATION.cff).

For the DGG results and their computational certificates, cite the independent
research snapshot:

```text
Residual Chart Lab. (2026). Depth-Generated Geometry: Ordered Quaternionic Response Quotients, Flat Cores, and Residual Descent (research-2026-09-07-audit1) [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.22646591
```

DGG citation metadata is provided in its
[`CITATION.cff`](research/depth-generated-geometry/releases/research-2026-09-07/CITATION.cff).

## License

Released under the MIT License.

Copyright (c) 2026 Free Number Authors.
