# F01: preserve the error as well as the correction

`02_SPECTRAL_TRANSPORT_EN.before-F01.md` is the obsolete initial text, SHA-256 `4b77cf1cb037a9b1dc04521c431a0dc37b828e3bd650954c1f2179b90e13ff0f`. Use `proofs/02_SPECTRAL_TRANSPORT_EN.md` for the final text.

The original general-uniaxial amplitude quotient was wrong outside the trace-free domain. Astra found the counterexample diag(2,1,1); the old expression gives 5 rather than 1. Centering S first resolves that auxiliary paragraph. The written principal proofs and main checker did not change. See `../proofs/review/F01_CORRECTION.json` and `../proofs/review/correction/VERIFIED_DIFF.patch`.
