# Note 28 — Decoder continuations detect the discarded core

**Base:** Note 27, commit `3e479034f1834542eb8679cca6638eeee7d82e0c`.

**Question.** Does the 432-dimensional kernel of the Note 27 update affect
any subsequent response operation, and what must be carried forward?

**Answer for an explicit operation family.** Central-probe evaluation and
the existing right local decoder give three coefficient readouts. Together
they detect every direction of that kernel. Retaining one, two, or three
independent coefficient directions requires respectively 144, 288, or 432
additional linear dimensions at the child. The corresponding minimal child
states have dimensions 588, 732, and 876. Refining both ends for the full
decoder makes the specified encode/decode transport an isomorphism.

The readout family is fixed by the right decoder already used in Notes 22
and 26; it is not selected by solving for a desired obstruction rank. These
are readouts of the retained response data. They are not operations on the
old 444-dimensional child quotient: this failure of descent is exactly what
is measured below. Ordinary operations already well-defined on that coarse
quotient cannot detect a difference it has erased.

## 1. Data retained from Notes 26–27

Let

\[
E_s=E_{212}\otimes V,\quad L_s=\operatorname{im}\partial_{212}\otimes V,
\quad Q=Y_{212}\otimes V,
\]
\[
E_t=E_{222},\quad L_t=\operatorname{im}\partial_{222},\quad Y=Y_{222},
\]

with quotient maps q_s and q_t. Fix the same central-slot right operation
Sigma=Sigma_4^R:E_s -> E_t. It is an isomorphism of raw response spaces.
Set F=q_t Sigma. Note 27 constructs

\[
\widetilde Q=E_s/(L_s\cap\Sigma^{-1}L_t)
\cong Q\times_DY,
\quad\dim\widetilde Q=876,
\]

where D=D_222 has dimension 12. Its maps p and u are the parent and child
projections. Write T_s=T_212 tensor V and T_t=T_222; both have dimension 432.
The residual maps alpha:Q -> D and beta:Y -> D are onto and

\[
\ker\alpha=T_s,\quad\ker\beta=T_t,\qquad
\ker u=\{(a,0):a\in T_s\}.
\tag{1.1}
\]

In particular, p restricted to ker u is an isomorphism onto T_s.

## 2. Specify the continuations before inspecting their ranks

For f:V -> H, the right encoder is

\[
f(z)=c_i z i+c_j z j+c_k z k.
\]

Its inverse has the explicit local formula

\[
\boxed{
c_i=\tfrac12(f(j)k-f(k)j),\quad
c_j=\tfrac12(f(k)i-f(i)k),\quad
c_k=\tfrac12(f(i)j-f(j)i).
}
\tag{2.1}
\]

**Proof.** Substitute f(z)=h z w for each w=i,j,k and use the quaternion
multiplication table. The selected coefficient is h when w agrees with the
readout index and zero for the other two indices. Linearity proves the
formula on all H tensor V; the twelve basis responses span Hom(V,H).

For a child edge response G, keep its four other probe variables open and
apply (2.1) to the variable at actual gap 4. This gives three parent edge
responses C_i G, C_j G, C_k G. Restore the parent gap labels as in Note 26.
Applying this edgewise and retaining the coefficient index gives

\[
C:E_t\longrightarrow E_{212}\otimes V,
\qquad C=\Sigma^{-1}.
\tag{2.2}
\]

This equality follows from the literal formula G(...,z,...)=F(...)zw.
It does not require an inverse of a quotient transport. In particular these
readouts can be constructed directly from probe evaluations and quaternion
products, before any quotient-rank computation.

The quotient-valued readout is

\[
R=q_s C:E_t\longrightarrow Q,\qquad
R_a=\pi_{212} C_a:E_t\longrightarrow Y_{212}.
\tag{2.3}
\]

R packages all three R_a in the order (parent coefficient, vector index).
It is available on retained raw response data, not on Y alone.

## 3. Exactly the lost 432 dimensions are readable

On the source refinement, the continuation satisfies

\[
R\Sigma=q_s,\qquad\widetilde R:\widetilde Q\to Q,\quad
\widetilde R=p.
\tag{3.1}
\]

This is well-defined because the relations retained in tilde Q lie in L_s.
By (1.1),

\[
\boxed{\widetilde R|_{\ker u}:\ker u\xrightarrow{\sim}T_{212}\otimes V.}
\tag{3.2}
\]

Every nonzero difference lost by u therefore affects at least one of the
three decoder continuations. One coefficient readout has rank 144 on that
kernel, and all three jointly have rank 432. This is an exact isomorphism
claim, not an inference from equal dimensions alone.

Equivalently, at the raw child,

\[
\boxed{R(L_t)=T_s.}
\tag{3.3}
\]

To prove (3.3), the residual square gives alpha R=beta q_t, so R(L_t) subset
T_s. Conversely for a in T_s, the compatible pair (a,0) is realized by some
x in E_s by Note 27. Then y=Sigma x lies in L_t and R y=a.

Consequently R cannot be reconstructed as a map on the old child quotient.
If h:Y -> Q satisfied h q_t=R, it would annihilate L_t, contradicting (3.3).

**Contrast with quotient-safe continuations.** A raw J:E_t -> E' that obeys
J(L_t) subset L' induces a map on Y. It sends every y in L_t to zero in
E'/L'. A chain of such operations has the same property. Note 22's exterior
suspensions obey precisely this descent condition (with their tensor input).
They cannot, by themselves, redetect this discarded child relation.

Thus the answer depends on the specified continuation family. Decoder
readout exposes the missing information; a family restricted to existing
coarse-quotient operations does not. The original raw data or its sufficient
refinement must be retained before the coarse projection is performed.

## 4. Minimal information for the chosen readouts

Fix a subspace W of V, of dimension r, and let P_W:V -> W be the orthogonal
projection for the standard imaginary-quaternion inner product. The
required readout is

\[
R_W=(\operatorname{id}_{Y_{212}}\otimes P_W)R.
\tag{4.1}
\]

For W spanned by a subset of i,j,k, this simply selects those coefficient
channels. From (3.3),

\[
R_W(L_t)=T_{212}\otimes W,\qquad\operatorname{rank}(R_W|_{L_t})=144r.
\]

Applying Note 27's minimal-refinement theorem at the child gives

\[
\boxed{Y_W=E_t/(L_t\cap\ker R_W),\qquad\dim Y_W=444+144r.}
\tag{4.2}
\]

| Required independent coefficient directions | Additional dimensions | Minimal child dimension |
|---|---:|---:|
| none | 0 | 444 |
| one | 144 | 588 |
| two | 288 | 732 |
| three | 432 | 876 |

Minimality is among linear quotient refinements preserving the original
child state and the indicated readouts. The full three-channel result is
SO(3)-equivariant; a particular proper W is additional readout data.

More precisely let alpha_W=(pi_D212 tensor id_W) on Y_212 tensor W, and
beta_W=(id_D212 tensor P_W) beta_R^{-1} beta on Y. Then

\[
Y_W\cong
Y\times_{D_{212}\otimes W}(Y_{212}\otimes W).
\tag{4.3}
\]

The map is y -> (q_t y,R_W y). Its kernel is the relation in (4.2).
Compatibility follows from the residual square. Any compatible pair is
realized: choose a representative of its first component and correct the
readout using L_t, whose image is exactly T_212 tensor W. This proves
surjectivity. Dimensions also agree: 444+148r-4r=444+144r.

## 5. Full retention closes this encode/decode pair

For W=V set tilde Y=Y_V. Since C=Sigma^{-1},

\[
L_t\cap\ker R=L_t\cap\Sigma L_s
=\Sigma(L_s\cap\Sigma^{-1}L_t).
\]

Hence the unchanged raw operation and its decoder induce inverse maps

\[
\boxed{\widetilde\Sigma:\widetilde Q\xrightarrow{\sim}\widetilde Y,
\qquad\widetilde C=\widetilde\Sigma^{-1}.}
\tag{5.1}
\]

In compatible-pair coordinates these are (a,b) -> (b,a) and its inverse.
The coarse update u is the composite of tilde Sigma with the projection
tilde Y -> Y. The entire 432-dimensional loss is in that last projection.

The information required for all three readouts is exactly the information
already present in Note 27's refined source: both dimensions are 876. A
canonical implementation can store a compatible pair with 888 coordinates
subject to twelve residual constraints. Choosing only 432 independent
supplemental numerical coordinates requires an explicit coordinate choice;
no canonical complement is presumed.

For the two-node operation graph consisting of Sigma and C, these relation
spaces are the greatest invariant family contained in (L_s,L_t). Indeed
invariance requires H_s subset L_s intersect Sigma^{-1}L_t and H_t subset
L_t intersect Sigma L_s, and this pair itself is invariant. All alternating
encode/decode paths are therefore well-defined on the refined states.
Their inverse loops are identity, as their definitions require.

This closes this specified operation pair. A forward-only internal-insertion
atlas with further spectators has additional operations and still needs its
own closure calculation. The readouts here reduce response arity; they are
not a construction of that larger atlas.

## 6. Certificate and remaining target

Run from the repository root:

```bash
python3 research/depth-generated-geometry/certificates/n8_222_decoder_continuation_certificate.py --output /tmp/n8_222_decoder_continuation_result.json
```

The certificate builds the caps directly from (2.1) using child probe
evaluations. Only afterwards does it check that they invert the specified
suspension. It reconstructs the parent/child matching spaces, verifies the
exact residual square for the readout, and checks obstruction ranks and
the minimal dimensions for all subsets of the three coefficient channels.
It records a child matching relation with zero coarse child state and a
nonzero decoder readout. Integer identities and certified rational ranks
are used throughout; stored result JSONs are not inputs.

The output [result](../certificates/n8_222_decoder_continuation_result.json)
includes hashes, environment, dimensions, and the witness.

The next mathematical target is to select the forward internal operations
for the next spectator layer and test whether this 876-dimensional retained
state suffices for them. If it does not, the intersection-of-kernels
construction measures the extra information they require. The readout
result supplies a concrete baseline: the full 432-dimensional loss already
matters for an existing local decoder family.
