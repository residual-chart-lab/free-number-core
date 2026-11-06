# Free Numbers — another gift, 6 November 2026

**Frozen Core. A new proof companion. Two working applications.**

This MIT research gift accompanies [Free Numbers Core v1.0.0](https://github.com/residual-chart-lab/free-number-core/releases/tag/core-v1.0.0). The Core stays unchanged. Aki initiated the research; Ronnie assembled the models and written proofs; Astra independently reviewed the mathematical claims and supplied separate checks.

## Start with your question

| Your question | Start here | What you can try |
|---|---|---|
| Can equal compressed results respond differently to an inserted operation? | `examples/connection-holonomy/README_JA.md`, T01–T06 | Compare the two equal-endpoint paths and their intermediate responses. |
| Can residual changes determine a transport rule? | `examples/generated-transport/README_JA.md`, T07–T12 | Follow forward and reverse input paths; inspect the explicit extra choices and rejection conditions. Read `INPUT_CONTRACT_JA.md` before changing inputs. |
| Which statements extend beyond finite examples? | `proofs/01_ALGEBRA_AND_PATHS_EN.md` through `05_LINE_DIMENSION_CLASSIFICATION_EN.md` | Inspect each hypothesis, proof and obstruction; run the checks separately. |
| How was an error handled? | `proofs/review/initial/REPORT_JA.md`, `proofs/review/correction/REPORT_JA.md`, `history/` | Compare the obsolete amplitude paragraph, the counterexample and its verified correction. |

Read [CORE_RELATIONSHIP.md](CORE_RELATIONSHIP.md) for attribution: all-grade reconstruction already belongs to frozen Core. The new companion includes rederivations, normalization/bounds, transport characterizations, spin and KK connections. The 16 claim IDs and two supplements are not a novelty count.

## Run it

Python 3.12 or newer; the verification commands use only the standard library. No package installation, network or credentials are required. Unzip into an ordinary writable folder, open a terminal there, then run:

```text
python -I -B verify_manifest.py
python -I -B run_checks.py --out fresh-checks
```

Use a new output folder on each run. `fresh-checks/SUMMARY.json` records the commands, results and comparisons. The run includes 29 main checks, both supplements, the centered-amplitude correction, 35 + 18 proof-audit and 81 application-audit independent checks and the two application runs (36 + 65). Exact certificates are compared to saved evidence; platform/version fields remain visible. Optional plot regeneration in the example folders requires matplotlib and is outside this standard-library run.

## Read the evidence

- **Written mathematics:** T01–T16 under stated hypotheses, plus imaginary-gap and all-dimensional rank-one supplements. Astra's combined verdict is `PASS_UNDER_STATED_HYPOTHESES`, after correction F01. Finite checks support implementation; they do not replace the written arguments. No proof-assistant certification is claimed.
- **Correction history:** the original uncentered amplitude quotient fails for `diag(2,1,1)` (5 instead of 1). The final text centers the matrix and treats isotropy separately. Old and corrected text and the audit diff are included.
- **Applications:** a prescribed non-Abelian graph connection transports residuals; a second model generates minimum-twist transport from changing residual responses under explicit hypotheses. The exact-rational implementation has a narrower arithmetic input domain than the real geometric formula.
- **Physical interpretation:** these are mathematical constructions, with a general Routh reduction on prescribed KK backgrounds. A physical background solving field equations, material calibration and a measured needle displacement are further research questions.

`PUBLICATION_MAP.json` binds the public files to the original source hashes. Proof texts and calculation sources remain byte-identical. Some audit/metadata copies replace internal storage locations with neutral labels; original hash fields in those historical records refer to original artifacts. The new public `MANIFEST.json` is authoritative for this package. The independent mathematical verdict does not by itself certify the new packaging.

The fixed Core is linked at its original tag and DOI, rather than rebuilt inside this companion. It is usable independently of this gift.

日本語の入口: [README_JA.md](README_JA.md).

Application-audit launcher note: `audit/applications/independent_checks.py` changes only three input-path literals for the public folder layout. The original independent checker is also included as `original_independent_checks.py`; all calculation statements are identical. This packaging adaptation is not attributed to the independent reviewer.
