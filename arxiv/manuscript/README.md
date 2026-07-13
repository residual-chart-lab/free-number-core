# arXiv manuscript working source

Working title: **Exact Reconstruction under Noncommutative Quaternionic Compression**

Build locally with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is embedded in `main.tex`; `references.bib` is retained as editable metadata for later refinement.

The manuscript is a separate arXiv-facing paper. It does not modify the frozen `core-v1.0.0` tag, GitHub Release, or Zenodo record.

Current status:

- full first manuscript assembled;
- Related Work and bounded novelty statement included;
- Gate A (equivariant local decoder) integrated;
- Gate B (depth additivity and algebraic coherence delay) integrated;
- local TeX build verified with TeX Live 2025;
- not submitted;
- author identity, final license, arXiv category, and endorsement status remain pending explicit approval and submission checks.
