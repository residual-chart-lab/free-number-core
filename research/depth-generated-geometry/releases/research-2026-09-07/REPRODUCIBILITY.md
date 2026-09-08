# Reproducibility — audit revision 1

## Arithmetic and evidence

The certificates use integers, rational arithmetic, or exact prime fields.
No floating-point rank estimator is used. Note 26 reconstructs over 1009
and 1013 and verifies rational operator identities by integer multiplication.
Nonzero modular minors give lower bounds; exact annihilators and row
identities give upper bounds. The audit adds independent rank arithmetic
over 1019 and exhaustive expanded-component quaternion products.

AUDIT_REPORT.md describes the corrected claim boundaries.
verification/verification-record.json identifies each execution and log.
The audit is internal; it is not an external referee report or a rerun of
every exploratory certificate in the archive.

## Extracted layout and dependencies

The folders notes/, certificates/, synthesis/, manuscript/, and
verification/ are siblings. No full repository checkout is needed to run
the scientific certificates. Python certificates import helpers from the
same certificates/ folder.

Python 3, NumPy, SciPy and a C++ compiler callable as g++ are required for
the latest certificate. Several historical certificates also require NumPy;
the smaller standard-library scripts do not. The recorded versions are in
verification/environment.json. Run without Python -O or -OO: the latest
certificate explicitly rejects assertion-disabled execution.

## Latest exact certificate

From the extracted archive root:

    python3 certificates/n8_222_redetection_certificate.py --certificate --output result.json

Expected final line: ALL CHECKS PASSED.

The default cache root is the system temporary directory's
free-number-222-certificate-v2 folder. A subdirectory is keyed by the SHA-256
of the Python and C++ implementations. Set FREE_NUMBER_222_CACHE to an empty
directory to choose a fresh cache root. The recorded revised clean run used
a newly created source-hash subdirectory.

The full matching lower bound is rechecked even on a cache hit. Cached
annihilator row counts are never accepted as a substitute. Off-incidence
and off-grading zero blocks, literal defining identities and rational
upper bounds are also checked. verification/n8-222-result.json records the
implementation hash and confirms that the matching lower bound was rerun.

## Independent audit and guard regressions

    python3 verification/audit_independent.py --output audit-independent-result.json
    python3 verification/audit_guard_checks.py --output audit-guard-result.json

The first script uses the production defining matrices as inputs, then
compares all literal state/probe basis products with four-component Hamilton
multiplication and computes ranks with a different implementation over 1019.
It checks the three parent supports and 222. The production C++ elimination
and multiplication sign table are not used by those comparison checks.
It is an independent check of matrix interpretation and arithmetic, not a
separate construction of the entire theory.

The second deliberately presents an incomplete cached annihilator and
checks rejection. It also checks that optimized Python and invalid prime
inputs cannot produce a successful certificate.

Both scripts print ALL CHECKS PASSED. Their recorded logs and structured
results are included in verification/.

## Historical full certificates rerun during this audit

    python3 certificates/n5_central_channel_factorization_certificate.py
    python3 certificates/n6_spectator_chart_transition_certificate.py
    python3 certificates/n6_seed_cap_bridge_certificate.py
    python3 certificates/n7_exceptional_core_decomposition_certificate.py
    python3 certificates/exterior_spectator_suspension_certificate.py
    python3 certificates/n7_internal_word_atlas_certificate.py
    python3 certificates/n7_anchor_transition_groupoid_certificate.py
    python3 certificates/n7_spacing_word_transport_certificate.py

All eight original scripts were rerun and passed. The logs are indexed in
verification-record.json. The all-length exterior theorem also has the
symbolic proof in Note 22; its finite run alone is not an all-length proof.

These two checks passed during the initial preparation in the same work
session, before this audit; their unchanged scripts and actual logs are
retained with that provenance:

    python3 certificates/n5_quaternionic_second_differential_certificate.py
    python3 verification/verify_theta.py

The second is a targeted theta check. The audit separately reran the full
n=6 atlas reconstruction listed above.

## PDF and archive integrity

The published snapshot is available at https://doi.org/10.5281/zenodo.22646591.
The original archive records commit `b9ec03f3e9788b41ba1a560e299407b388db41e1`
and tag `dgg-research-2026-09-07-audit1`. On GitHub, check out commit
`110113dd763da371bb6e02c6c5083b40dd12aecc` to retrieve the same source files.
The two commits share the exact Git tree `24dd03c1f118752f5a08914076a7669055acbd9b`.
The GitHub transfer changed commit identity, not file content. Original history
and tags are retained in a recovery Git bundle; native tag synchronization is pending.
Later Git commits update publication metadata and navigation.
`ZENODO_METADATA.json` in the current release directory records the three uploaded
files and their checksums; it is not part of the historical ZIP.

Pandoc, pdfLaTeX and the included manuscript/preamble.tex produce the PDF.
Run manuscript/build.sh to rebuild from Markdown. The standalone generated
LaTeX source is also included. The revised 16-page PDF was rendered and
visually inspected; temporary images and compiler auxiliaries are excluded.

From the archive root, on a system with GNU coreutils:

    sha256sum -c SHA256SUMS

The checksum list covers every payload file except itself, not the
surrounding ZIP. MANIFEST.json records the committed source, byte lengths
and file hashes. The repository snapshot builder requires a clean committed
DGG source tree before recording its source commit.
The published ZIP is the reference for byte-level archive checks; a newly built
ZIP can have different timestamps even when its payload files are identical.
The builder records the current Git commit in MANIFEST.json, so a build from
the equivalent GitHub commit also has a different manifest from the original ZIP.
