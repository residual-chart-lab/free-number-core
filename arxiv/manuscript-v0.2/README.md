# Exact Reconstruction under Noncommutative Quaternionic Compression

Author: **Akihiko Kura**  
Affiliation: **Residual Chart Lab**

This is the final pre-submission source package prepared for arXiv. It includes the manuscript, editable bibliography metadata, and exact-arithmetic verification scripts.

Build with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the exact certificates with:

```bash
python verify_theta_decomposition.py
python verify_depth4.py
```

Primary arXiv category: `math.RA` (Rings and Algebras).

The clean arXiv upload archive contains only the TeX files required to compile the article. The full source package retains the certificate scripts and bibliography metadata.
