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

## License

Released under the MIT License.

Copyright (c) 2026 Free Number Authors.
