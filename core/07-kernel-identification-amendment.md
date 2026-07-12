# Core 07 Kernel-Identification Amendment

**Status:** proof clarification for `core/07-length-four-cross-boundary-propagation.md`  
**Date:** 2026-07-12  
**Target claim:**

\[
\ker(D_{13}|_{RR})=V_4=S^4_0V.
\]

## 1. Why this amendment exists

Core 07 correctly computes

\[
\operatorname{rank}(D_{13}|_{RR})=16
\]

on the \(25\)-dimensional sector

\[
RR=S^2_0V\otimes S^2_0V.
\]

Hence the kernel has dimension nine. The original prose then invokes the multiplicity-free decomposition

\[
RR\cong V_0\oplus V_1\oplus V_2\oplus V_3\oplus V_4
\]

to identify that kernel with \(V_4\).

Dimension nine and multiplicity-freeness alone do not make that identification: the direct sum

\[
V_0\oplus V_1\oplus V_2
\]

also has dimension \(1+3+5=9\). The conclusion is nevertheless correct, because a stronger independently checked subspace statement is available.

## 2. Exact argument

Let \(D_4^{\le2}\) denote compression together with every depth-one and depth-two distinct-gap response, and let

\[
F_2^{(4)}:=\ker D_4^{\le2}.
\]

The exact length-four spin-depth certificate proves the subspace equality

\[
F_2^{(4)}=S^4_0V=V_4.
\]

The sector analysis in Core 07 proves that on \(RR\):

1. compression vanishes identically;
2. every depth-one response vanishes identically;
3. among depth-two responses, the only potentially nonzero component is \(D_{13}\).

Therefore

\[
F_2^{(4)}\cap RR
=\ker(D_{13}|_{RR}).
\]

Since

\[
S^4_0V\subset RR,
\]

the checked global equality gives

\[
F_2^{(4)}\cap RR
=S^4_0V.
\]

Consequently,

\[
\ker(D_{13}|_{RR})=S^4_0V=V_4.
\]

The rank computation supplies a consistency check:

\[
\dim\ker(D_{13}|_{RR})=25-16=9=\dim V_4.
\]

It is not the sole identification argument.

## 3. No decomposable residual pair survives

For nonzero \(S,T\in S^2_0V\), Core 07 proves

\[
D_{13}(S|T)(d_1,d_2)=4T(d_2)S(d_1).
\]

Choose \(d_1,d_2\) so that \(S(d_1)\ne0\) and \(T(d_2)\ne0\). Because \(\mathbb H\) is a division algebra,

\[
T(d_2)S(d_1)\ne0.
\]

Thus

\[
D_{13}(S|T)\ne0.
\]

Hence the surviving \(V_4\) sector contains no nonzero decomposable tensor \(S\otimes T\). Its elements are necessarily coherent linear combinations whose individual depth-two responses cancel.

## 4. Replacement paragraph

Replace the kernel-identification paragraph in Core 07 with:

> The exact certificate gives \(\operatorname{rank}(D_{13}|_{RR})=16\), hence a nine-dimensional kernel. More importantly, compression and every depth-one response vanish on \(RR\), and \(D_{13}\) is the only depth-two component that may remain. Therefore \(\ker(D_{13}|_{RR})=F_2^{(4)}\cap RR\). The independently verified length-four subspace equality \(F_2^{(4)}=S^4_0V\), together with \(S^4_0V\subset RR\), yields \(\ker(D_{13}|_{RR})=S^4_0V=V_4\). The rank count \(25-16=9\) is a consistency check, not the sole identification argument.

## 5. Dependencies

- `notes/11-spin-depth-filtration.md`
- `certificates/note11_certificate.py`
- `certificates/core07_cross_boundary_certificate.py`
- `core/07-length-four-cross-boundary-propagation.md`
