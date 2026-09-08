#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
pandoc ordered-quaternionic-response-quotients.md --from markdown+tex_math_single_backslash --standalone --lua-filter=table-layout.lua --top-level-division=section -V colorlinks=true -V documentclass=article -V fontsize=11pt -V geometry:margin=25mm -V papersize=a4 --include-in-header preamble.tex -o ordered-quaternionic-response-quotients.tex
pdflatex -interaction=nonstopmode -halt-on-error ordered-quaternionic-response-quotients.tex
pdflatex -interaction=nonstopmode -halt-on-error ordered-quaternionic-response-quotients.tex
