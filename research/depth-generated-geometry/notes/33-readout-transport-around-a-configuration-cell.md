# Note 33 — Readout transport around a configuration cell

**Base:** Notes 25 and 31–32; commit `4c6aa068e9844be940a676eaa9da661af42397d7`.

**Question.** When both interior support vertices can move by one gap,
does their order of movement affect the transported core or its determined
readout law?

**Result.** Both routes agree exactly at all three stages, with core
holonomies \(I_{144},I_{432},I_{1296}\). On every one of the four adjacent
ladders, the transported readout quotient and endpoint term commute with
the source-core transport. The 1152-dimensional ambiguity spaces are
preserved, and the determined 144-dimensional core requires zero extra
retention across this cell.

The comparison uses four placements at each of three stages. Every edge
transport is fixed independently by the stationary outer edge. The two
right insertions and the later coefficient readout keep their actual gap
positions throughout.

## 1. The three configuration cells

Name the four placement ladders A, B, C, and D by their initial words.

| Ladder | Before insertion, n=7 | After one insertion, n=8 | After two insertions, n=9 |
|---|---|---|---|
| A | 122: (1,2,4,6) | 132: (1,2,5,7) | 142: (1,2,6,8) |
| B | 131: (1,2,5,6) | 141: (1,2,6,7) | 151: (1,2,7,8) |
| C | 221: (1,3,5,6) | 231: (1,3,6,7) | 241: (1,3,7,8) |
| D | 212: (1,3,4,6) | 222: (1,3,5,7) | 232: (1,3,6,8) |

At every stage, compare the two routes

\[
A\longrightarrow B\longrightarrow C,
\qquad
A\longrightarrow D\longrightarrow C.
\tag{1.1}
\]

The moves A→B and D→C shift the third support vertex one gap to the
right. Their stationary anchors are the left outer edges. The moves
A→D and B→C shift the second support vertex one gap to the right; their
anchors are the right outer edges.

The resulting loops are

\[
\begin{aligned}
122&\to131\to221\to212\to122,\\
132&\to141\to231\to222\to132,\\
142&\to151\to241\to232\to142.
\end{aligned}
\tag{1.2}
\]

The first is the loop of Note 25. Note 32 supplied the A→D ladder.
Here all four edges at all three stages are reconstructed from their own
anchors, including those two previously studied cases.

For each ladder, use the input order old input, a, b. The final literal
paths are

\[
P_{ab}(G,a,b)=Gz_aaz_bb,
\qquad P_{ba}(G,a,b)=Gz_bbz_aa.
\]

The final probe gaps are 4 and 5. The same right-coefficient decoder
reads gap 5 on the second path. Both gaps lie outside all four final
supports. Put

\[
S=\text{source observation},\qquad
T_+=F_{ab}+F_{ba},\qquad H_+=(S,T_+),\qquad N=R_bP_{ba}.
\tag{1.3}
\]

Each ladder has its own matching quotient and its own operators (1.3),
constructed from the literal responses at that support.

## 2. Fixing the core coordinates and edge transports

Write \(T_{u,n}\) for the outer core of ladder u at stage n. To work
with rectangular full-quotient coordinates, choose a coordinate map on
the image of the right outer edge. Concretely, select independent rows
of that edge block and factor the entire block through them. This gives
an injective core embedding

\[
C_{u,n}:\mathbb Q^{d_n}\hookrightarrow Y_{u,n},
\qquad (d_7,d_8,d_9)=(144,432,1296).
\]

The certificate also checks that the left outer edge has this same image
and full rank. Thus both types of stationary anchor describe the same
core at each vertex.

For each of the four directed edges \(u\to v\), let \(h\) be its
stationary outer edge. The transport \(g_{uv}^{(n)}\) is the unique map
whose full-coordinate form satisfies

\[
C_{v,n}g_{uv}^{(n)}q_{u,n}^{\mathrm{core}}|_h
=q_{v,n}|_h.
\tag{2.1}
\]

Here \(q_{u,n}^{\mathrm{core}}|_h\) is the source anchor in its chosen
core coordinates. The response space on h, including its probe order,
is identical on the two sides. Exact factorization proves (2.1), and
full anchor rank gives uniqueness and invertibility. The maps are
equivariant because the response maps are equivariant and (2.1) has a
unique solution.

All twelve arrows are fixed by (2.1) before any route comparison. The
cell defect is

\[
\Delta_n=g_{BC}^{(n)}g_{AB}^{(n)}
          -g_{DC}^{(n)}g_{AD}^{(n)}.
\tag{2.2}
\]

Multiplying by the inverse of the second route converts (2.2) to
holonomy minus the identity. Its rank therefore also measures the
closed-loop defect, independently of the core-coordinate choices.

The exact results are

| Stage | Core dimension | Rank of \(\Delta_n\) | Loop holonomy |
|---|---:|---:|---|
| n=7 | 144 | 0 | \(I_{144}\) |
| n=8 | 432 | 0 | \(I_{432}\) |
| n=9 | 1296 | 0 | \(I_{1296}\) |

Since every constituent arrow is invertible, these are exact identities
on the full indicated cores. The twelve arrow matrices are integral in
the selected coordinates.

## 3. Readout coordinates for the four ladders

Let \(\mathcal B_u=Y_{u,8}\otimes V_b\) and
\(W_u=N_u(\ker H_{+,u})\). A full-row-rank quotient matrix K is obtained
by projecting the exact relations of \((H_+,N)\) onto the N rows.
Its kernel is W, and the certificate constructs a factorization

\[
K_uN_u=A_uS_u+B_uT_{+,u}.
\tag{3.1}
\]

The ranks are

| Ladder | rank H+ | rank N | rank (H+,N) | dim W | dim (B/W) | Determined core |
|---|---:|---:|---:|---:|---:|---:|
| A: 122/132/142 | 2592 | 1296 | 3744 | 1152 | 144 | 144 |
| B: 131/141/151 | 2592 | 1296 | 3744 | 1152 | 144 | 144 |
| C: 221/231/241 | 2592 | 1296 | 3744 | 1152 | 144 | 144 |
| D: 212/222/232 | 2628 | 1332 | 3780 | 1152 | 180 | 144 |

For A, B and C, H+ is onto its full 2592-dimensional codomain. D retains
the 36-dimensional determined residual of Note 31, alongside its
144-dimensional determined core.

The scalar coevaluation \(\eta=\frac13\sum_r e_r\otimes e_r\)
defines the recovered-core map as in Notes 31–32:

\[
\Psi_u(c)=[N_ux],\qquad
S_ux=C_{u,7}c\otimes\eta,\quad T_{+,u}x=0.
\tag{3.2}
\]

For the generic ladders, surjectivity of H+ supplies the required input.
For D, the compatible-pair statement of Note 31 supplies it for every
source-core vector. Changing the chosen input adds an element of W.

To compare the laws in source-core coordinates, define

\[
\begin{aligned}
\mathcal D_u&=\Psi_u^{-1}K_u(C_{u,8}\otimes I_{V_b}),\\
\Lambda_u&=\Psi_u^{-1}B_uC_{u,9}.
\end{aligned}
\tag{3.3}
\]

Here K and B use the actual rational scales in (3.1). Each inverse in
(3.3) is taken on the image of the injective map \(\Psi_u\); exact
linear solves check that the entire displayed image lies there.
The kernel of \(\mathcal D_u\) is the readout ambiguity expressed in
core coordinates.

Indeed, the restriction of K to the 1296-dimensional readout core has
rank 144. Its kernel there has dimension 1152, equal to the full W
dimension in the table. Hence W lies in that core, and this restricted
kernel is exactly W. Each \(\Psi_u\), \(\mathcal D_u\), and
\(\Lambda_u\) has rank 144.

The scalar source identity is checked separately, so the resulting law is

\[
\Psi_u^{-1}([N_ux])
=\langle a,b\rangle c+\Lambda_u(t),
\quad
S_ux=C_{u,7}c\otimes a\otimes b,
\quad T_{+,u}x=C_{u,9}t.
\tag{3.4}
\]

## 4. What is measured on each adjacent edge

Set \(g^R_{uv}=g_{uv}^{(8)}\otimes I_{V_b}\). The two independently
computed defects are

\[
\begin{aligned}
\mathcal E^R_{uv}
&=\mathcal D_vg^R_{uv}-g_{uv}^{(7)}\mathcal D_u,\\
\mathcal E^+_{uv}
&=\Lambda_vg_{uv}^{(9)}-g_{uv}^{(7)}\Lambda_u.
\end{aligned}
\tag{4.1}
\]

The first tests the actual quotient of the transported readout. The
second tests the endpoint term. Their exact ranks are

| Edge | rank \(\mathcal E^R\) | rank \(\mathcal E^+\) |
|---|---:|---:|
| A→B: 122→131 | 0 | 0 |
| B→C: 131→221 | 0 | 0 |
| A→D: 122→212 | 0 | 0 |
| D→C: 212→221 | 0 | 0 |

Thus every edge preserves the ambiguity space, the recovered-core
identification, and the full determined-core law (3.4).

For example, the first equality implies

\[
g^R_{uv}(\ker\mathcal D_u)=\ker\mathcal D_v
\]

because both the source-core and readout-core transports are invertible.
It also implies that the two stacked observations
\((\mathcal D_u,\mathcal D_vg^R_{uv})\) have rank 144. Thus such an
edge requires no additional retention for the determined quotient.

Composing the first identity in (4.1) along either route gives

\[
\mathcal D_C\bigl((g_{BC}^{(8)}g_{AB}^{(8)})\otimes I\bigr)
=g_{BC}^{(7)}g_{AB}^{(7)}\mathcal D_A
=g_{DC}^{(7)}g_{AD}^{(7)}\mathcal D_A.
\tag{4.2}
\]

The endpoint identity composes in the same way. Together with Section 2,
this proves path independence of the determined readout law on this cell.
The readout-core holonomy is \(I_{432}\otimes I_3=I_{1296}\), so its
restriction to W and its induced map on the determined quotient are
identities as well.

## 5. Exact result and reproducibility

The [certificate](../certificates/n9_readout_transport_cell_certificate.py)
and its [result record](../certificates/n9_readout_transport_cell_result.json)
record a full reconstruction run: all checks passed in 897.841 seconds.

```bash
python research/depth-generated-geometry/certificates/n9_readout_transport_cell_certificate.py \
  --output research/depth-generated-geometry/certificates/n9_readout_transport_cell_result.json
```

The certificate reconstructs all twelve matching quotients, checks both
core anchors at every vertex, independently constructs the twelve edge
maps, and compares the two routes at each stage. It then rebuilds all
four literal path/readout systems, their quotient factorizations, scalar
source laws and core identifications, and evaluates (4.1) on every edge.

Ranks use modular lower bounds together with exact integer annihilators
or factorizations as upper bounds. Rational matrix products retain their
denominators. Saved matrices and result files are never inputs to the
certificate. The optional checkpoint directory receives output-only
intermediate matrices.

## 6. Scope and the next extension

This closes the specified three-stage configuration cell for the outer
cores and the fixed later readout. Both insertion orders remain the
literal operations of Notes 30–32; their separate endpoint difference
and retention requirements continue to apply.

The next question is whether the transport can be lifted to the minimal
retained states that support the updates themselves. Such a lift must
specify how the retained information moves and verify the update squares.
The dimension differences of the full quotients, including the residuals
at D, have to be accounted for in that construction. The present core
anchors give concrete maps against which to test it.
