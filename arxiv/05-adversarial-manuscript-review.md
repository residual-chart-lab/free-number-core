# Adversarial manuscript review — pass 1

Status: internal review of `arxiv/manuscript/main.tex`; not an external referee report.

## Verdict

The manuscript has crossed from a positioning document into a coherent mathematical preprint. The main reconstruction argument, the equivariant local decoder, the partial-response factorization, and the depth-additivity theorem form one readable chain. No new research gate is required before the next revision.

The draft is not yet submission-ready. The remaining work is tightening, proof packaging, and submission metadata rather than extending the theory.

## Results that survive the first hostile pass

1. The paper does not claim that the many-to-one map `m_n` is invertible. It correctly distinguishes `m_n` from the injective enriched response `A_n`.
2. The explicit formula for `Theta^{-1}` proves more than a dimension count.
3. The `SO(3)` decomposition explains the determinant structurally and identifies which part is standard representation theory and which part is multiplication-specific.
4. The all-grade reconstruction theorem follows by a clean last-letter induction.
5. Partial responses factor under concatenation, and the division-algebra property of `H` gives the exact depth-additivity theorem on nonzero decomposable states.
6. The grade-four survivor is presented as algebraic coherence delay, with an explicit warning that no quantum-coherence claim is made.
7. The memory/coding language is bounded by explicit non-claims: no rate, noise, sample-complexity, or practical-storage theorem.

## Revisions required before submission

### R1. Zero-state convention

`delta` is initially defined only for nonzero states, while the shifted filtration is written as a set containing zero. Add the convention

`delta(0)=+infinity`.

This correction has already been applied to the locally compiled PDF and must be synchronized to the repository source.

### R2. Grade-two notation

Define

`g = sum_a e_a | e_a`,

identify `S^2_0 V` with symmetric trace-free endomorphisms using the Euclidean metric, and state explicitly

`A_2(S)(d) = -2 S(d)`.

Without this, the later formula `D_13(S||T)=4 T(d_2)S(d_1)` introduces `S(d)` and `T(d)` too abruptly. This correction has also been applied to the locally compiled PDF.

### R3. Determinant basis statement

The number `256` is correct in the standard pure-tensor/evaluation bases. The manuscript should name those bases explicitly, then say that the equivariant coordinates factor the same determinant. This prevents a referee from objecting that a change-of-basis determinant was silently normalized away.

### R4. Decoder-complexity wording

The recursive decoder reuses one *type* of local inverse at every node. It is not literally one matrix application per grade for the whole state. Replace any wording that suggests `O(n)` total work by:

> the same local inverse is reused at every recursive node, with recursion depth `n-1`.

No complexity theorem should be stated until arithmetic operation counts and representation format are fixed.

### R5. Grade-four proof packaging

The exact integer certificate `scripts/verify_depth4.py` verifies the rank and sector-kernel tables. The paper should promote the grade-four table to a proposition and make the proof split explicit:

- exact integer rank computation for the tables;
- equivariant inclusion `S^4_0 V subset S^2_0 V tensor S^2_0 V`;
- identification of the nine-dimensional final kernel with `V_4`;
- Clebsch–Gordan bookkeeping for the layer decomposition.

The rank count alone must not be presented as the sole identification argument.

### R6. Bibliographic refinement

The current arXiv references are sufficient for an internal draft. Before submission, normalize author diacritics, add journal/book publication data where available, and confirm that every Related Work sentence is supported by the cited source rather than by search-result summaries.

### R7. Submission metadata

Still unresolved and deliberately not guessed:

- individual author identity versus project/lab label;
- manuscript license;
- primary arXiv category and optional cross-list;
- account endorsement status;
- final relationship to the Zenodo Core v1 artifact.

These are submission blockers but not mathematical blockers.

## Build verification

The local manuscript compiles under TeX Live 2025 to a 13-page A4 PDF. Cross-references and citations resolve; the final build log has no warnings. The PDF was rendered page by page and visually checked for clipping, overlap, and broken glyphs.

## Next action

Revise the manuscript once against R1–R6, rebuild and visually verify it, then perform a second hostile pass focused only on theorem statements and proof gaps. Do not open Gate C or add the Time Engine.
