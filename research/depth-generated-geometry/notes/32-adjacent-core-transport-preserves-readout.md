# Note 32 — Adjacent core transport preserves the readout law

**Base:** Notes 25–31; commit `08d7ea8306c33a171ec52ca53fb8594a85f6a952`.

**Question.** Does Note 31's recovered-core identification survive the
first adjacent placement, when transport is fixed by the stationary outer
edge before comparing readouts?

**Result.** Yes, for the specified right-edge ladder

\[
(122,132,142)\longrightarrow(212,222,232).
\]

The common right outer edges define equivariant core isomorphisms of
dimensions 144, 432, and 1296. The middle transport carries the entire
1152-dimensional readout ambiguity onto its counterpart. The induced
144-dimensional quotient transport commutes with both the recovered-core
identification and the endpoint term of the readout law.

Thus this adjacent comparison requires **zero additional dimensions** to
transport the determined core. The full readout on either side still has
its 1152-dimensional ambiguity when only source and endpoint sum are known.

## 1. Fix the adjacent placements and the operations

Slide the second support vertex from gap 3 to gap 2 in the original
\(212\) placement. This is the \(212\leftrightarrow122\) adjacency of
Note 25. Keep the two insertions and the later coefficient readout at the
same actual gaps as in Notes 30–31.

| Stage | Original support / word | Neighbor support / word | Shared right edge |
|---|---|---|---|
| Before insertion | \((1,3,4,6)\), 212 | \((1,2,4,6)\), 122 | \((4,6)\) |
| After one insertion | \((1,3,5,7)\), 222 | \((1,2,5,7)\), 132 | \((5,7)\) |
| After two insertions | \((1,3,6,8)\), 232 | \((1,2,6,8)\), 142 | \((6,8)\) |

For each column, the two final raw paths are

\[
P_{ab}(G\otimes a\otimes b)=Gz_aaz_bb,
\qquad
P_{ba}(G\otimes a\otimes b)=Gz_bbz_aa,
\]

where the final probes \(z_a,z_b\) are at gaps 4 and 5. The input order is
always old input, \(a\), \(b\). The same local right-coefficient decoder
reads final gap 5 on both sides. Each side uses its own matching quotient
for the displayed support.

The exact quotient dimensions are

| Stage | Original full quotient | Original core | Neighbor full quotient = core |
|---|---:|---:|---:|
| \(n=7\) | 148 | 144 | 144 |
| \(n=8\) | 444 | 432 | 432 |
| \(n=9\) | 1332 | 1296 | 1296 |

The certificate reconstructs all six matching quotients from literal
quaternionic responses.

## 2. The stationary edge fixes the core transports

Let \(q_o,q_n\) denote the original and neighboring quotient coordinates
at one stage, and restrict them to the common right edge. The two
restrictions have the same kernel and ranks 144, 432, or 1296, respectively.
The common response space and its probe ordering are identical on this
edge; no change of response values is inserted.

Consequently there are unique maps satisfying the shared-edge identities:

\[
\begin{aligned}
J_0 &: Y_{122}\xrightarrow{\sim}T_{212},\\
J_1 &: Y_{132}\xrightarrow{\sim}T_{222},\\
J_2 &: Y_{142}\xrightarrow{\sim}T_{232},
\end{aligned}
\qquad
J_k\,q_n|_{\mathrm{edge}}=q_o|_{\mathrm{edge}}.
\tag{2.1}
\]

The original residual maps vanish on these outer edges. Their edge images
have the full known core dimensions, so the images in (2.1) are precisely
the original cores. Each neighboring edge restriction is onto its whole
quotient. The exact matrix identities establish existence; that
surjectivity establishes uniqueness. Equivariance follows from the
equivariance of the response maps and uniqueness.

The original residuals, of dimensions 4, 12, and 36, lie outside these
edge-defined core transports. Their transport would require additional
data beyond (2.1).

## 3. The neighboring determined quotient

For either side \(u\in\{o,n\}\), write

\[
T_+^u=F_{ab}^u+F_{ba}^u,\qquad
H_+^u=(S^u,T_+^u),\qquad
N^u=R_b^uP_{ba}^u.
\]

The readout targets are

\[
\mathcal B_o=Y_{222}\otimes V_b,
\qquad \mathcal B_n=Y_{132}\otimes V_b.
\]

Set \(W_u=N^u(\ker H_+^u)\). The exact ranks are

| Quantity | Original | Neighbor |
|---|---:|---:|
| \(\operatorname{rank}H_+\) | 2628 | 2592 |
| \(\operatorname{rank}N\) | 1332 | 1296 |
| \(\operatorname{rank}(H_+,N)\) | 3780 | 3744 |
| \(\dim W\) | 1152 | 1152 |
| \(\dim(\mathcal B/W)\) | 180 | 144 |
| Determined core dimension | 144 | 144 |

On the original side, the determined core is
\(\mathcal C_o=(T_{222}\otimes V_b)/W_o\). On the neighbor side the
entire determined quotient is core:
\(\mathcal C_n=\mathcal B_n/W_n\).

The neighboring \(H_+\) is onto the full direct sum of its two codomains,
because their dimensions add to 2592. Thus every source observation and
endpoint sum can be realized together.

Let \(\eta=\frac13\sum_r e_r\otimes e_r\). Define

\[
\Psi_n(c)=[N^nx],\qquad
S^nx=c\otimes\eta,\quad T_+^nx=0.
\tag{3.1}
\]

Surjectivity supplies \(x\), and changing \(x\) changes its readout by
\(W_n\). The coefficient matrix in (3.1) has exact rank 144. Hence

\[
\Psi_n:Y_{122}\xrightarrow{\sim}\mathcal C_n.
\tag{3.2}
\]

Likewise define \(\Lambda_n:Y_{142}\to Y_{122}\) by taking source
observation zero and endpoint sum \(t\), then applying \(\Psi_n^{-1}\)
to the readout class. The certificate establishes its rank 144 and the
neighboring law

\[
\Psi_n^{-1}([N^nx])
=\langle a,b\rangle c+\Lambda_n(T_+^nx)
\quad\text{when }S^nx=c\otimes a\otimes b.
\tag{3.3}
\]

The same scalar-contraction identity holds for arbitrary sums by
linearity. This reconstructs the counterpart of Note 31 on the adjacent
placement using the fixed literal operations.

## 4. The ambiguity space is preserved exactly

The readout transport dictated by (2.1) is

\[
J_R=J_1\otimes\mathrm{id}_{V_b}:
\mathcal B_n\xrightarrow{\sim}T_{222}\otimes V_b.
\]

The main kernel statement is

\[
\boxed{J_R(W_n)=W_o.}
\tag{4.1}
\]

For a concrete proof, the certificate constructs onto quotient matrices
\(K_o:\mathcal B_o\to\mathbb Q^{180}\) and
\(K_n:\mathcal B_n\to\mathbb Q^{144}\), whose kernels are \(W_o,W_n\).
Using the core identifications, form the prescribed rank-144 comparison

\[
F=\Psi_oJ_0\Psi_n^{-1}:
\mathcal C_n\longrightarrow\mathcal C_o
\subset\mathcal B_o/W_o.
\]

In the corresponding quotient coordinates, the exact operator identity is

\[
\boxed{K_oJ_R=F K_n.}
\tag{4.2}
\]

Since \(F\) is injective, (4.2) gives equality of the two kernels on
\(\mathcal B_n\). Since \(J_R\) is an isomorphism onto the original
readout core, it gives (4.1). Thus the induced map

\[
\bar J_R:\mathcal C_n\xrightarrow{\sim}\mathcal C_o
\]

is the actual quotient transport and satisfies

\[
\boxed{\bar J_R\Psi_n=\Psi_oJ_0.}
\tag{4.3}
\]

Defining \(F\) alone would prescribe a candidate map. Identity (4.2)
verifies that the edge-fixed readout transport really induces that map.

The joint rank of \((K_n,K_oJ_R)\) is 144. Therefore the existing
144-dimensional neighboring quotient already supports both observations:
the additional retention cost for this comparison is zero.

## 5. The endpoint term commutes as well

Let \(B_o,B_n\) be the endpoint-sum coefficients in the exact laws

\[
K_uN^u=A_uS^u+B_uT_+^u.
\]

On the original endpoint core, \(B_o=\Psi_o\Lambda_o\); on the
neighbor, \(B_n=\Psi_n\Lambda_n\). The certificate independently checks

\[
B_oJ_2=F B_n.
\tag{5.1}
\]

Substituting the definition of \(F\) and using injectivity of \(\Psi_o\)
gives

\[
\boxed{\Lambda_oJ_2=J_0\Lambda_n.}
\tag{5.2}
\]

Together, (4.3), (5.2), and the scalar source law show that transporting
the compatible core observations first, or evaluating their determined
readout first, gives the same answer. The source observation is transported
by \(J_0\otimes\mathrm{id}_{V_a\otimes V_b}\), the endpoint sum by
\(J_2\), and the resulting readout class by \(\bar J_R\).

The exact defects tested in (4.2) and (5.1) both have rank zero. This is a
naturality statement for the specified core readout law across one
adjacent ladder. Its domains and transports are fixed by Sections 1–2.

## 6. Reproducible certificate and next boundary

Run from the repository root:

```bash
python research/depth-generated-geometry/certificates/n9_adjacent_core_transport_certificate.py \
  --output research/depth-generated-geometry/certificates/n9_adjacent_core_transport_result.json
```

The certificate rebuilds all six quotients and all literal paths and
readouts. For each quaternion grade, a modular matching rank gives a
lower bound. A lifted, full-row-rank annihilator is checked on the complete
integer matching map and gives the matching upper bound. Thus even a lift
using one prime proves the rational rank. If its small-denominator lift
fails, the implementation uses a second prime and verifies the resulting
integer identity. The remaining rank checks also use exact annihilators
and modular lower bounds.

It then verifies the shared-edge transports, both quotient factorizations,
both scalar source laws, the recovered-core maps, and the two commuting
squares. The result file records source hashes, rank certificates,
denominators and execution details.

This gives the first adjacent extension of Note 31. The next test is to
compare it with an independently fixed transport on another adjacent
edge, and then compare two routes around an actual configuration cell.
That will test compatibility of the readout law across a network and
supply a closed-loop question with all constituent maps specified.
