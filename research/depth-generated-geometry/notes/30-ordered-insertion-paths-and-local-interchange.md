# Note 30 — Ordered insertion paths and local interchange

**Base:** Notes 27–29, commit `be89eec9b5cc6a2ed3c558d5b0ccd62565127f4a`.

**Question.** Starting with the same raw input, do the two orders of central
right insertion give the same state at the same final placement? Can the
preceding retained state support the comparison, and which later readout
distinguishes the paths?

**Result.** With final labels fixed, the two endpoint maps differ
by a rank-1320 operator. Their raw difference is exactly the prescribed
local quaternionic ordering difference. The corresponding local comparison
map fails to descend to the 1332-dimensional endpoint quotient: its descent
obstruction fills the 1296-dimensional outer core. Keeping both paths'
intermediate and final states requires a minimal 6516-dimensional common
refinement of the fixed raw source.

More sharply, paths with exactly the same coarse endpoint can differ under
the same subsequent gap-5 coefficient readout. The image of this hidden
path difference has dimension 1296: it fills the readout target's core.
Preserving both retained paths and this readout on both endpoints requires
7668 dimensions, an additional 1152 beyond the five-component state.

The equality obtained after applying the additional local comparison is
recorded separately from equality of the two original paths. The comparison
mixes response coordinates; the final labels have already been identified.

## 1. Two paths with the input order and final labels fixed

Take

\[
\Omega=E_{212}\otimes V_a\otimes V_b,\qquad \dim\Omega=17496.
\]

The initial support is (1,3,4,6). Both paths end at support (1,3,6,8), word
232. In the final placement, z_a is the probe at actual gap 4 and z_b is
the probe at actual gap 5. The input tensor order is always (old input,a,b).

| Path | First insertion | Second insertion | Final edge response |
|---|---|---|---|
| ab | a at gap 4 | b at gap 5 | G z_a a z_b b |
| ba | b at gap 4 | a at gap 4, moving b to gap 5 | G z_b b z_a a |

Each insertion is exactly the right operation from Notes 26 and 29. Old
edge and probe labels are transported by the indicated order-preserving
gap insertion. Let the resulting raw isomorphisms be

\[
P_{ab},P_{ba}:\Omega\xrightarrow{\sim}E_{232}.
\]

With q=pi_232, define the endpoint maps

\[
F_{ab}=qP_{ab},\qquad F_{ba}=qP_{ba},\qquad
\Delta=F_{ab}-F_{ba}.
\tag{1.1}
\]

These maps have the same domain and codomain. Thus Delta tests literal
endpoint agreement after the final labels have been fixed.

## 2. Fix the local comparison before inspecting the quotient

On two probe slots define the right encoders

\[
\Theta_{ab}(h\otimes a\otimes b)(z_a,z_b)=h z_a a z_b b,
\]
\[
\Theta_{ba}(h\otimes a\otimes b)(z_a,z_b)=h z_b b z_a a.
\]

Both are isomorphisms from H tensor V tensor V to R_2, by applying the
one-variable right decoder twice. Fix

\[
\tau=\Theta_{ba}\Theta_{ab}^{-1}:\mathcal R_2\to\mathcal R_2.
\tag{2.1}
\]

Apply tau to the two central probe variables, keeping the other four probes
open, on each edge. This gives an explicitly determined raw map

\[
C:E_{232}\xrightarrow{\sim}E_{232}.
\]

The certificate constructs tau from its 36 basis responses before any
quotient computation. C is then built pointwise from that local formula.
It checks the two exact identities

\[
\boxed{CP_{ab}=P_{ba},\qquad
\kappa_{232}C=\tau\kappa_{232}.}
\tag{2.2}
\]

The first follows pointwise from (2.1), taking h to be the value of the old
four-probe response. The second follows because the paired contractions
defining kappa leave both central probes open.

Hence the raw defect P_ba-C P_ab is identically zero. The original path
difference is still

\[
(P_{ab}-P_{ba})(G\otimes a\otimes b)
=G\bigl(z_a a z_b b-z_b b z_a a\bigr).
\tag{2.3}
\]

The local matrix tau has rows with multiple nonzero entries. Applying it
changes response values and constitutes an additional operation. In
particular (2.2) by itself does not establish equality of F_ab and F_ba.

## 3. The endpoint difference has rank 1320

Let k= kappa_212 and let D_0=H tensor V_a tensor V_b, of dimension 36.
The residual squares are

\[
\kappa_{232}P_{ab}=\Theta_{ab}(k\otimes\operatorname{id}_{V_a\otimes V_b}),
\]
\[
\kappa_{232}P_{ba}=\Theta_{ba}(k\otimes\operatorname{id}_{V_a\otimes V_b}).
\tag{3.1}
\]

The exact ranks are

\[
\operatorname{rank}F_{ab}=\operatorname{rank}F_{ba}=1332,
\qquad \boxed{\operatorname{rank}\Delta=1320.}
\tag{3.2}
\]

The local difference Theta_ab-Theta_ba has rank 24. As k tensor id is onto,
the projection of Delta to the 36-dimensional residual has rank 24.
Consequently

\[
\dim\bigl(\operatorname{im}\Delta\cap T_{232}\bigr)=1320-24=1296,
\]

so im Delta contains the entire outer core T_232. The calculation locates
the path difference both in the residual and in the core.

All four quaternion grading blocks give rank 330 for Delta. The certificate
verifies the grading split, reconstructs exact left annihilators, checks
their integer products, and matches their bounds with ranks modulo 1009 and
1013. These are characteristic-zero rank statements.

## 4. The local comparison fails on the coarse endpoint state

Set L_232=ker q. The matrix calculation gives

\[
\operatorname{rank}(q,qC)=2628.
\tag{4.1}
\]

The elementary joint-rank identity therefore yields

\[
\dim qC(L_{232})=2628-1332=1296.
\]

Equation (2.2) shows qC(L_232) lies in ker beta=T_232, where beta is the
residual quotient of Note 29. Thus

\[
\boxed{qC(L_{232})=T_{232}.}
\tag{4.2}
\]

In particular no map c on Y_232 satisfies c q=q C: a zero coarse state can
have a nonzero coarse image after the specified raw comparison.

The least linear state preserving q and qC is

\[
E_{232}/(L_{232}\cap C^{-1}L_{232}),\qquad \dim=2628.
\tag{4.3}
\]

Its paired coordinates (u,v) satisfy beta(v)=tau beta(u). Surjectivity onto
this compatible-pair space follows from (4.2), by correcting a representative
with a relation in L_232. This measures precisely what the extra comparison
operation requires.

Thus three statements have distinct meanings here: the original paths
differ; the added local comparison exactly accounts for the raw difference;
and implementing that comparison requires more information than the coarse
endpoint state contains.

## 5. Minimal information for both retained paths

Let S=q_212 tensor id_(V_a tensor V_b). Let M_a be the intermediate Y_222
state after inserting a, tensored with the still-open input b. Let M_b be
the analogous intermediate state after inserting b, tensored with a. In
M_b the inputs are permuted back to the fixed source order (old,a,b).

The two three-stage observation maps are

\[
H_{ab}=(S,M_a,F_{ab}),\qquad H_{ba}=(S,M_b,F_{ba}).
\tag{5.1}
\]

Each has rank 3924, recovering Note 29 for both orders. The exact joint ranks
are as follows; every component S, M_a, M_b, F_ab, F_ba has dimension 1332.

| Information preserved | Minimal linear state dimension |
|---|---:|
| Either endpoint alone | 1332 |
| Both endpoints | 2628 |
| Either complete three-stage path | 3924 |
| H_ab and the other endpoint F_ba | 5220 |
| Both complete paths: S, M_a, M_b, F_ab, F_ba | 6516 |

All residual maps can be pulled back to D_0 using the specified, invertible
right-decoder bridges. The five components have the same residual in these
coordinates. Their compatible five-component space has dimension

\[
5\cdot1332-4\cdot36=6516.
\tag{5.2}
\]

The exact joint rank attains this bound. Hence every compatible five-tuple
is realized by an input in Omega. This proves the compatible-tuple
description, rather than assuming independence of the core components.

By Note 27's theorem, the coarsest linear refinement supporting all five
observations is Omega modulo the intersection of their kernels. Relative
to H_ab alone, the additional cost is 6516-3924=2592. If only the other
endpoint is additionally requested, its cost is 5220-3924=1296.

These minima preserve the specified observations on this fixed source.
They make the dependence on the chosen operation family explicit.

## 6. The same later readout on both endpoints

Fix the full coefficient readout at final gap 5. At each edge, keep the
other five probe variables open and use

\[
c_i=\tfrac12(f(j)k-f(k)j),\quad
c_j=\tfrac12(f(k)i-f(i)k),\quad
c_k=\tfrac12(f(i)j-f(j)i).
\]

After removing that probe and restoring the n=8 gap labels, project each
coefficient response to Y_222. The combined map is

\[
R_b:E_{232}\longrightarrow Y_{222}\otimes V_b.
\tag{6.1}
\]

This is one fixed raw readout applied to both paths. It obeys

\[
R_bP_{ab}=M_a.
\]

The certificate also constructs R_b P_ba and compares

\[
\Delta_R=R_bP_{ab}-R_bP_{ba}
\]

on the kernel of Delta. This directly tests whether paths with equal
coarse endpoints can still be distinguished by this same later readout.

The exact ranks are

\[
\operatorname{rank}\Delta_R=1320,\qquad
\operatorname{rank}(\Delta,\Delta_R)=2616.
\]

Therefore

\[
\boxed{\operatorname{rank}(\Delta_R|_{\ker\Delta})=2616-1320=1296.}
\tag{6.2}
\]

There are inputs x for which

\[
\boxed{qP_{ab}x=qP_{ba}x,\qquad R_bP_{ab}x\ne R_bP_{ba}x.}
\tag{6.3}
\]

This uses the same R_b on both endpoint responses, with the same gap labels
and coefficient channels. The witness in the result file verifies both
equalities/inequalities over the integers after clearing denominators.
Its common endpoint is nonzero. The difference in readout coordinate 345,
the i coefficient of quotient coordinate 115, is exactly 768/64=12.
The sparse source vector is recorded in
`witnesses.equal_endpoints_different_readouts.input_coordinates`. Indices
are zero-based in the source order (edge, h, v1,v2,v3,v4, a,b), using the
lexicographic edges of (1,3,4,6), quaternion basis (1,i,j,k), and vector
basis (i,j,k). It is an element of the full tensor-extended input space.
The generic witness flag `retained_zero` here refers to Delta x=0;
`common_endpoint_nonzero` separately records the actual endpoint value.

Let eta:Y_222 tensor V_b -> D_232 be the residual bridge of Note 29.
The one-step residual square and the inverse cap identity give

\[
\eta R_b=\kappa_{232},\qquad \eta\Delta_R=\beta\Delta.
\]

Thus Delta_R(ker Delta) lies in ker eta=T_222 tensor V_b, which has dimension
1296. Equation (6.2) proves equality with that entire core. The coarse
endpoint identifies these path differences; the fixed later coefficient
readout requires that they be retained.

## 7. Holding both paths still leaves a readout ambiguity

Write

\[
H_5=(S,M_a,M_b,F_{ab},F_{ba}),\qquad N=R_bP_{ba}.
\]

The ab readout is already M_a. Adding the same readout after ba gives

\[
\boxed{\operatorname{rank}(H_5,N)=7668,\qquad
\operatorname{rank}(N|_{\ker H_5})=7668-6516=1152.}
\tag{7.1}
\]

Thus the least linear state supporting all five observations and the same
gap-5 readout on both endpoints is

\[
\Omega/(\ker H_5\cap\ker N),\qquad\dim=7668.
\tag{7.2}
\]

The 1296 in (6.2) and the 1152 in (7.1) concern different conditions.
Equation (6.2) requires only equality of the two endpoints. Equation (7.1)
fixes all five observations, including their intermediate states. Those
extra observations constrain part of the later readout.

More precisely let T_R=T_222 tensor V_b be the readout core. Since H_5
contains the ba endpoint, the residual square implies

\[
W=N(\ker H_5)\subset T_R,\qquad \dim W=1152,
\qquad \dim(T_R/W)=144.
\tag{7.3}
\]

The N output modulo W factors through H_5. Its residual part has dimension
36, and T_R/W describes a further 144-dimensional core quotient determined
by the five observations. Identifying this quotient intrinsically is a
concrete next question. No identification with a previously named
144-dimensional core is used in this dimension argument.

## 8. Reproduction and interpretation

Run from the repository root with the Note 29 dependencies (Python 3,
NumPy, SciPy, python-flint, and g++):

```bash
OPENBLAS_NUM_THREADS=1 python3 research/depth-generated-geometry/certificates/n9_232_path_comparison_certificate.py --output /tmp/n9_232_path_comparison_result.json
```

The certificate rebuilds the n=9 matching maps, fixes the local comparison
from the primitive quaternionic encoder, and constructs both raw paths
directly. It also checks each path against a composition of the existing
one-step insertions. Exact residual squares and ranks determine the
endpoint difference, failure of descent, and common retention costs.
The gap-5 readout is built directly from its local coefficient formulas.
The [result](../certificates/n9_232_path_comparison_result.json) records
source hashes, environment versions, rank profiles, and explicit witnesses.

For these two paths the raw ordering difference is fully accounted for by
the fixed local quaternionic operation. Its adjusted raw defect is zero.
At the coarse quotient that local comparison has a full-core descent
obstruction. These facts identify which equality is available and what
information it requires. A curvature claim would additionally require
specified transports on a common state family and a closed-loop comparison;
the open-path discrepancy alone does not supply that claim.
