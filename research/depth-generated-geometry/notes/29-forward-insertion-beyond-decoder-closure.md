# Note 29 — Forward insertion beyond decoder closure

**Base:** Notes 27–28, commit `cb23eb4258396bb1d248972c2f86da084d200f67`.

**Result.** Fix the next central right insertion, at new actual gap 5,
from spacing word 222 to 232. The 876-dimensional retained state of Note 28,
tensored with the new vector input, has dimension 2628. This state is
insufficient for the prescribed full output. The missing information has
dimension 1296 and maps onto the entire outer core of the new quotient.
The coarsest linear refinement preserving the retained state and this
output has dimension **3924**.

A concrete failure already occurs when the new vector is fixed to i.
The dimension 3924 concerns the full tensor-extended operation with input
ranging over V. It is the exact cost for this specified continuation.

## 1. Fix the state and the next operation

Write V=Im H. Keep Note 28's quotient map

\[
r:E_{222}\longrightarrow Z,
\qquad
Z=E_{222}/K_{222},\qquad \dim Z=876,
\]
\[
K_{222}=L_{222}\cap\Sigma_4^R(L_{212}\otimes V),
\qquad L_{abc}=\operatorname{im}\partial_{abc}.
\tag{1.1}
\]

Equivalently, Z retains the two compatible readouts

\[
Z\cong Y_{222}\times_{D_{222}}(Y_{212}\otimes V).
\tag{1.2}
\]

At n=8 the support is (1,3,5,7). Insert a new probe at actual gap 5,
shifting the old gaps 5,6,7 to 6,7,8. The new support is (1,3,6,8), with
spacing word 232 and spectator gaps (2,4,5,7). Edge labels are transported
by this order-preserving relabelling.

On each edge use the same right insertion rule as Note 26:

\[
J(F\otimes w)(\text{old probes},z)=F(\text{old probes})\,z\,w,
\qquad w\in V.
\tag{1.3}
\]

Here z occupies actual gap 5 in the ordered argument list, while its
quaternionic product is appended on the right as displayed. This fixes
the operation completely. The one-variable right decoder makes J an
isomorphism of raw response spaces.

Set

\[
\Omega=E_{222}\otimes V,\quad A=Z\otimes V,\quad H=r\otimes\operatorname{id}_V,
\]
\[
F=\pi_{232}J:\Omega\longrightarrow Y_{232}.
\tag{1.4}
\]

Then dim Omega=17496, dim A=2628, and dim ker H=14868. The descent question
is whether F vanishes on ker H, or equivalently whether the same full
output can be determined from H alone.

## 2. The new quotient and its 36-dimensional residual

For this support the matching presentation is

\[
\mathcal R_7^{\oplus4}\xrightarrow{\partial_{232}}
E_{232}=\mathcal R_6^{\oplus6}\longrightarrow Y_{232}\longrightarrow0,
\qquad \mathcal R_m=\operatorname{Hom}(V^{\otimes m},\mathbb H).
\]

The exact ranks are

\[
\operatorname{rank}\partial_{232}=16164,\qquad
\boxed{\dim Y_{232}=17496-16164=1332.}
\tag{2.1}
\]

Define the paired contraction

\[
\epsilon_6(G)(z_4,z_5)
=\sum_{a,b=1}^{3}G(e_a,e_a,z_4,z_5,e_b,e_b)
\]

and the cross-edge residual

\[
\kappa_{232}(G)
=\epsilon_6(G_{16})-\epsilon_6(G_{18})
-\epsilon_6(G_{36})+\epsilon_6(G_{38}).
\tag{2.2}
\]

It annihilates the matching relations. Indeed, the identity
sum_a e_a v e_a=v for imaginary v collapses both paired probes. On literal
state responses, each cross edge reduces to

\[
v_9v_8v_7v_6\,z_5\,v_5\,z_4\,v_4v_3v_2v_1.
\]

The two restrictions from each face occur with opposite signs. Surjectivity
of the natural terminal-face parametrization extends this cancellation to
the entire matching space. Thus kappa factors through a quotient map

\[
\beta:Y_{232}\longrightarrow D_{232}=\mathcal R_2.
\]

The paired evaluations for distinct (z_4,z_5) basis inputs are disjoint,
so the residual is onto and dim D_232=36. The sum T_232 of the outer-edge
images (edges 13 and 68) has exact dimension 1296. Both outer blocks of
kappa are zero. Comparing dimensions gives

\[
\boxed{T_{232}=\ker\beta,\qquad \dim T_{232}=1296.}
\tag{2.3}
\]

The computational certificate proves (2.1) and the outer-image rank by
exact integer identities and matching modular lower bounds. It reconstructs
all twelve face-to-edge restrictions from literal quaternion products.

## 3. Residual transport survives the next insertion

Let

\[
B:\mathcal R_1\otimes V\xrightarrow{\sim}\mathcal R_2,
\qquad B(k\otimes w)(z_4,z_5)=k(z_4)z_5w.
\]

Since the newly inserted probe is kept open in the paired contraction,

\[
\kappa_{232}J=B(\kappa_{222}\otimes\operatorname{id}_V).
\tag{3.1}
\]

The retained state Z includes its Y_222 projection, so the right side
factors through H. This defines an onto map gamma:A -> D_232 with

\[
\boxed{\beta F=\gamma H.}
\tag{3.2}
\]

In particular F(ker H) lies in T_232. Thus the 36-dimensional residual
already agrees whenever the retained inputs agree. The possible failure
of descent is located within the new outer core.

## 4. The full outer core is still missing

The certificate determines the three joint ranks:

\[
\operatorname{rank}H=2628,\qquad
\operatorname{rank}F=1332,\qquad
\boxed{\operatorname{rank}(H,F)=3924.}
\tag{4.1}
\]

Every quaternion grading block contributes the same ranks:

| Map | Rank per grade | Total rank |
|---|---:|---:|
| H: retained input | 657 | 2628 |
| F: new full output | 333 | 1332 |
| (H,F): joint information | 981 | 3924 |

The grading split is checked on the matrices. For each block, two modular
left kernels are lifted to integer annihilators and checked by exact
multiplication. Their independence supplies the upper rank bound; the
prime-field ranks supply the equal lower bound. Hence (4.1) holds over Q
and over R.

For any pair of linear maps,

\[
\operatorname{rank}(F|_{\ker H})
=\operatorname{rank}(H,F)-\operatorname{rank}H.
\]

This follows by projecting im(H,F) onto im H: its kernel consists of
(0,Fx) for x in ker H. Applying (4.1) gives

\[
\operatorname{rank}(F|_{\ker H})=3924-2628=1296.
\]

Together with (3.2) and (2.3), this proves

\[
\boxed{F(\ker H)=T_{232}.}
\tag{4.2}
\]

Thus keeping the preceding decoder readouts does not yet determine the
next specified internal insertion. All 1296 new core directions can vary
while the preceding retained state stays fixed.

## 5. A concrete witness with the new vector fixed to i

Use zero-based standard right-decoder coordinates on E_222. The edge order
is (13,15,17,35,37,57); within each 972-dimensional edge block, h runs over
(1,i,j,k), followed by five vector coefficients in lexicographic order on
(i,j,k). Let e_j denote the corresponding raw basis vector. Define

\[
\begin{aligned}
d={}&e_0+e_4+e_8-3e_{258}+3e_{264}+3e_{288}-3e_{306}\\
   &+e_{972}+e_{976}+e_{980}+3e_{1944}.
\end{aligned}
\tag{5.1}
\]

The exact certificate verifies

\[
\boxed{r(d)=0,\qquad F(d\otimes i)\ne0.}
\tag{5.2}
\]

In its explicitly constructed quotient coordinates, output coordinate 10
is -24 (integer numerator -48, common denominator 2). Therefore zero and
d have the same retained state, yet give different next outputs for the
same new input i. This witness is independent of any dimension inference
about varying the new vector.

## 6. Minimal refinement and its compatible-triple description

Keep both the retained input H and the prescribed output F. Note 27's
general theorem gives the coarsest linear refinement

\[
\widehat A=\Omega/(\ker H\cap\ker F).
\]

Using (4.2),

\[
\boxed{\dim\widehat A=2628+1296=3924,}
\qquad
\dim(\ker H\cap\ker F)=13572.
\tag{6.1}
\]

There is a canonical realization

\[
\boxed{\widehat A\cong A\times_{D_{232}}Y_{232},\qquad
[x]\mapsto(Hx,Fx).}
\tag{6.2}
\]

To prove surjectivity, take a compatible pair (a,c), choose x with Hx=a,
and observe c-Fx in ker beta. Equation (4.2) gives k in ker H with
Fk=c-Fx. Then x+k realizes the pair. Its kernel is the defining relation
of widehat A. This also proves sufficiency, while the intersection of
kernels proves minimality among linear quotient refinements preserving
the two fixed maps.

Expanding A using (1.2) yields three components:

\[
Y_{212}\otimes V\otimes V,\qquad
Y_{222}\otimes V,\qquad Y_{232}.
\]

Each has dimension 1332. Their residuals are identified with D_232 by the
specified right-decoder bridges, and all three must agree there. Thus

\[
\boxed{\dim\widehat A=3\cdot1332-2\cdot36=3924.}
\tag{6.3}
\]

The rank calculation proves that every such compatible triple is realized
by raw input; (6.3) is not merely a count of formally available coordinates.
The three core contributions can vary independently once the common
36-dimensional residual is fixed.

The projection widehat A -> A has kernel T_232 of dimension 1296. The
coarse output projection widehat A -> Y_232 has kernel dimension
3924-1332=2592. To carry all the joint information through this operation,
the target can be refined as

\[
\widehat Y_{232}
=E_{232}/\bigl(L_{232}\cap J(\ker H)\bigr).
\tag{6.4}
\]

Since J is invertible on raw responses, it induces an isomorphism
widehat A -> widehat Y_232; both dimensions are 3924. The relation in (6.4)
is the coarsest one preserving both the child quotient and the transported
retained input.

## 7. Reproduction and scope of the next question

Requirements: Python 3, NumPy, SciPy, python-flint, and g++ for the imported
Note 26 backend. The recorded run used python-flint 0.9.0. Assertions must
remain enabled. From the repository root:

```bash
OPENBLAS_NUM_THREADS=1 python3 research/depth-generated-geometry/certificates/n9_232_continuation_certificate.py --output /tmp/n9_232_continuation_result.json
```

The new n=9 matching maps are rebuilt on every run. Recursive local
decoding is checked against the literal response encoder. The certificate
reconstructs the quotient, outer core, retained state, and fixed insertion;
checks the exact residual square; proves the ranks; and verifies (5.2).
Stored result JSONs are not proof inputs. The recorded
[result](../certificates/n9_232_continuation_result.json) includes source
hashes, environment versions, rank profiles, and the sparse witness.

Note 28 closed the specified insertion/decoder pair. Adding the forward
gap-5 operation makes that relation family strictly smaller, by 1296
dimensions on the tensor-extended source. This is a concrete instance of
Note 27's allowed-path refinement criterion.

The next closure question concerns further specified operations on the
3924-dimensional retained state. The compatible-triple result provides an
exact two-insertion baseline. Whether a larger operation family stabilizes,
and whether other insertion orders produce additional differences, each
requires its own operation comparison.
