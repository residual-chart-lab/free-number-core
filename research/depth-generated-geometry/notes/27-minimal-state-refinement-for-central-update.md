# Note 27 — Minimal state refinement for the central update

**Base:** `bf26e5f2681096b0a15549f0edebdcc452128705`, in particular Note 26.

**Status:** a linear-algebra theorem over Q (and R), conditional on the exact
Note 26 identities and ranks. An accompanying certificate reconstructs and
checks the required operators. The general quotient/fiber-product arguments
below are proofs, not extrapolations from a finite test.

**Question.** With the central-slot right decoder of Note 26 held fixed, what
is the least refinement of the parent state that makes its full child output
well-defined?

**Answer.** There is a canonical refinement relative to that specified
operation. It has dimension 876, retains 432 additional linear coordinates,
and is a fiber product of the 444-dimensional tensor-extended parent and
444-dimensional child over their common 12-dimensional residual. Its update
is surjective, but has a 432-dimensional kernel. Well-defined update is not
lossless update.

This is an extension of the finite response-quotient research branch. It does
not change frozen Core v1.0.0 or the published September 7 snapshot. Standard
linear-algebra constructions are used here; no novelty claim is made for the
abstract refinement theorem.

## 1. Fix the operation and both original state spaces

Use the notation and **exact same** operation of Note 26:

\[
E=E_{212}\otimes V,\quad
L=\operatorname{im}(\partial_{212}\otimes\operatorname{id}_V),\quad
Q=E/L=Y_{212}\otimes V,
\]
\[
\Sigma=\Sigma_4^R:E\xrightarrow{\sim}E_{222},\qquad
F=\pi_{222}\Sigma:E\longrightarrow Y_{222}=:Y.
\]

Write q:E -> Q for the original quotient. This is the tensor-extended
operation with the new vector ranging over V, including linear combinations;
it is not a dimension claim about a fixed-vector slice.

Note 26 establishes

\[
\dim E=5832,\quad\dim L=5388,\quad\dim Q=444,\quad\dim Y=444,
\]
\[
F(L)=T_{222}=:T,\qquad\dim T=432.
\tag{1.1}
\]

In particular F does not factor through q. No choice of a representative is
silently inserted into F. Also F is onto: Sigma is an isomorphism and pi is
onto.

Let D=D_222=Y/T, and let beta:Y -> D be the residual quotient. The exact
residual square of Note 26 induces the onto map

\[
\alpha:Q\longrightarrow D,\qquad
\alpha=\beta_R\circ(\pi_{D_{212}}\otimes\operatorname{id}_V),
\]
\[
\beta F=\alpha q,\quad\dim D=12,\quad
\ker\alpha=T_{212}\otimes V,\quad\dim\ker\alpha=432.
\tag{1.2}
\]

Here beta_R is Note 26's specified residual isomorphism. No complement of T
or T_212 is chosen.

## 2. General minimal-refinement theorem

Let E and Y be vector spaces over a field, L a subspace of E, q:E -> E/L
the quotient, and F:E -> Y linear. Define

\[
L_{\mathrm{safe}}=L\cap\ker F,\qquad
\widetilde Q=E/L_{\mathrm{safe}},\qquad r:E\to\widetilde Q.
\tag{2.1}
\]

There are unique linear maps

\[
p:\widetilde Q\to E/L,\quad p([x])=q(x),\qquad
u:\widetilde Q\to Y,\quad u([x])=F(x).
\tag{2.2}
\]

**Proof.** Differences in L_safe vanish under both q and F. Conversely, two
representatives have the same original state and the same prescribed output
if and only if their difference belongs to L_safe. Thus

\[
\widetilde Q\cong\operatorname{im}(q,F)\subset(E/L)\oplus Y.
\tag{2.3}
\]

**Minimality.** A linear quotient E/K that both refines the original state
and admits the same output F must have K subset L and K subset ker F.
Consequently K subset L_safe, and it admits the unique quotient map

\[
E/K\longrightarrow\widetilde Q,\qquad[x]_K\mapsto[x]_{L_{\mathrm{safe}}},
\]

compatible with both state and output. Hence tilde Q is the coarsest such
refinement, and in finite dimension it has the smallest dimension. This
comparison fixes E, q and F; it does not minimize over arbitrary nonlinear
encodings, changed operations, changed targets, or a restricted input set.

**Information cost.** The first isomorphism theorem applied to F restricted
to L gives a canonical isomorphism

\[
\ker p=L/(L\cap\ker F)\xrightarrow{\sim}F(L),\qquad[\ell]\mapsto F\ell.
\tag{2.4}
\]

Therefore

\[
0\to F(L)\to\widetilde Q\xrightarrow{p}E/L\to0,
\qquad
\dim\widetilde Q=\dim(E/L)+\operatorname{rank}(F|_L).
\tag{2.5}
\]

The first arrow is the inverse of (2.4) followed by inclusion; it uses no
chosen section. If the data are equivariant, the intersection, quotient, and
these maps are equivariant as well.

## 3. Apply the theorem: 876 is necessary and sufficient

By (1.1),

\[
\boxed{\dim L_{\mathrm{safe}}=5388-432=4956,}
\]
\[
\boxed{\dim\widetilde Q=5832-4956=876=444+432.}
\tag{3.1}
\]

The 432 added coordinates distinguish precisely those old matching
directions that the chosen operation makes visible in the child core.
They are not arbitrary generation-history labels. Old relation directions
annihilated by F remain identified. Note 26's obstruction is retained as
information rather than declared zero.

Any linear quotient refinement supporting the same q and F has dimension
at least 876. The quotient (2.1) attains this bound. In particular no
444-dimensional refinement preserving the original parent information can
support this operation on the full target.

This changes the parent state space explicitly; it does not claim that the
old parent state by itself now determines the child.

## 4. Intrinsic coordinates: a fiber product

Define the space of compatible pairs

\[
P=Q\times_DY
=\{(a,b)\in Q\oplus Y:\alpha(a)=\beta(b)\}.
\tag{4.1}
\]

Then

\[
\boxed{\Phi:\widetilde Q\xrightarrow{\sim}P,\qquad
\Phi([x])=(q(x),F(x)).}
\tag{4.2}
\]

**Proof.** Equation (1.2) gives containment in P. The kernel of (q,F) is
L_safe, giving injectivity after quotient. For any compatible (a,b), take
x with q(x)=a. Then beta(b-Fx)=0, so b-Fx belongs to T=F(L). Choose ell in L
with F ell=b-Fx. Now x+ell maps to (a,b). Different choices yield the same
class because their differences lie in L_safe. This proves surjectivity
without selecting a global section.

Equivalently P is the kernel of the onto map

\[
(\alpha,-\beta):Q\oplus Y\to D,
\]

so dim P=444+444-12=876. The update in these coordinates is simply

\[
\boxed{u(a,b)=b.}
\tag{4.3}
\]

This describes the amount of information an original representative carries
jointly into its parent and prescribed child states. It is not a method of
producing b from a alone, and b is not being assigned independently of x.
No future boundary condition has been introduced by the pair notation.

## 5. Two kernels: what is retained and what is still lost

The parent projection and the update have different kernels:

\[
\ker p=\{(0,b):b\in T\}\cong T_{222},
\tag{5.1}
\]
\[
\ker u=\{(a,0):a\in\ker\alpha\}
\cong T_{212}\otimes V.
\tag{5.2}
\]

Thus both have dimension 432 and both are onto. There are canonical exact
sequences

\[
0\to T_{222}\to\widetilde Q\xrightarrow{p}Y_{212}\otimes V\to0,
\]
\[
0\to T_{212}\otimes V\to\widetilde Q\xrightarrow{u}Y_{222}\to0.
\tag{5.3}
\]

Their kernels intersect only at zero. The joint map (p,u) is injective.
The 12-dimensional residual is preserved via alpha p=beta u and the
specified beta_R isomorphism. However, the child state alone cannot recover
all 876 refined coordinates. The second exact sequence explicitly locates
the information lost by this one-step update.

If retaining all refined information after the update is required, the target
must itself be enlarged or supplemented. This note does not hide the kernel
by calling the update lossless, nor does it prescribe an optimal target
extension or a time-evolution law.

## 6. More than one operation: the scope of the next step

For a prescribed family F_a:E -> Y_a, the same argument gives

\[
L_{\mathcal A}=L\cap\bigcap_{a\in\mathcal A}\ker F_a.
\tag{6.1}
\]

It is the largest relation subspace preserving the original state and every
specified output. For a finite family it is the kernel of the stacked map
(q,F_a)_a. This is a general theorem, not a computation of any further
spectator atlas.

For composable raw operations J_a:E_s -> E_t and original relations L_s,
one-step output visibility alone is not enough for arbitrary continuation.
Let the identity path and all allowed finite paths be included and define

\[
K_s=\bigcap_{w:s\to t}\ker(q_tJ_w).
\tag{6.2}
\]

Then K_s subset L_s and J_a K_s subset K_t: append any allowed continuation
to a. Conversely every family of subspaces H_s subset L_s invariant under
all J_a lies in K_s. Thus (K_s) is the greatest compatible relation family.
For a finite graph of finite-dimensional spaces it can be computed by

\[
K_s^{(0)}=L_s,\qquad
K_s^{(h+1)}=K_s^{(h)}\cap\bigcap_{a:s\to t}J_a^{-1}K_t^{(h)}.
\tag{6.3}
\]

The subspaces decrease; if a round changes the family its total dimension
strictly decreases. Hence there are at most sum_s dim L_s strict rounds.
The stationary family satisfies (6.2). No stabilization bound for an
unbounded collection of growing word spaces is claimed.

Equation (6.2) supplies a precise future research target: retain differences
that some allowed continuation can detect. It is an operation-based
equivalence criterion, not backward physical causation or a forecast of
which continuation occurs.

## 7. Certificate and claim ledger

Run from the repository root:

```bash
python3 research/depth-generated-geometry/certificates/n8_222_minimal_refinement_certificate.py --output /tmp/n8_222_minimal_refinement_result.json
```

Requirements and cache provenance are inherited from Note 26: Python 3,
NumPy, SciPy, and g++; exact integer identities with rational reconstruction
and nonzero minors modulo 1009 and 1013. Assertions must be enabled.

The certificate reconstructs the relevant parent and child quotients, checks
the literal right suspension and its invertibility, factors the residual
maps through the quotient coordinates, and checks the residual square.
It then verifies the obstruction rank, the compatible-pair constraint, and
the rank 876 of the joint state/output map. It records an explicit old
matching relation whose parent state is zero but whose child output is not.
No stored result JSON is used as a proof input.

The checked-in [result](../certificates/n8_222_minimal_refinement_result.json)
records a successful run, source hashes, and environment versions. The
pre-existing Note 26 certificate was also run from reconstructed operators;
its result matched the published result JSON exactly. The new certificate
additionally includes a three-dimensional continuation counterexample:
a difference invisible through one step can become visible at the second
step. This guards against treating one-step refinement as all-path closure.

| Statement | Basis and boundary |
|---|---|
| E/(L intersect ker F) is the coarsest linear refinement | General proof in Section 2 |
| Refinement dimension 876; extra information 432 | Note 26 ranks plus Section 3; reconstructed in the certificate |
| Canonical compatible-pair realization | Surjectivity proof in Section 4; exact constraint and rank checks |
| Parent and update kernels both dimension 432 | Section 5; exact ranks checked |
| Residual preservation | Note 26 residual square, checked again |
| Arbitrary allowed finite paths | General theorem under explicitly given composable linear operations, Section 6 |
| Canonical operator independent of decoder choice | Not claimed; Sigma_4^R is fixed |
| Full information preservation into Y_222 alone | False; ker u has dimension 432 |
| Physical time, experience, choice, backward causal force | Not established or modeled by this finite theorem |

The immediate remaining question is which further operations the retained
state must support. The operation family must be specified before testing
its closure; it must not be selected afterwards to make an obstruction vanish.
