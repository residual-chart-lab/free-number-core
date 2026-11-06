# T08 supplement: classify first-jet line transport in all dimensions

This is about a rank-one line projector on an underlying Euclidean R^n. It is not an identification of that n with spacetime dimension or the dimension of the residual tensor space. For the fixed quaternion Core the underlying n is three.

Let n>=2, P a rank-one orthogonal projector, and D a symmetric tangent to its manifold, `PD+DP=D`. A skew generator depends only on this first jet (and, optionally, additional rotation-invariant scalars), tracks P by `[Omega,P]=D`, and is equivariant under common time-independent rotations. No linearity, continuity or minimum norm is assumed.

## Classification

- Under **O(n)** equivariance, `Omega0=[D,P]` is the only rule for every n>=2.
- Under **SO(n)** equivariance it is the only rule for n=2, n=3 and every n>=5.
- For **SO(4)** and D!=0, all rules have the form `Omega0+kappa *Omega0`, where kappa is any rotation-invariant scalar function of the permitted inputs. At D=0 the output is forced to zero. The star is the four-dimensional Hodge operator on two-forms in the fixed orientation.

The prior three-dimensional theorem covers **all spectral multiplicity types** in that dimension. The present all-dimensional theorem concerns the **rank-one projector** family, not every higher-dimensional multiplicity pattern.

## Proof

Write `P=uu^T`, `D=uv^T+vu^T`, |u|=1, u dot v=0. As before, Omega0=vu^T-uv^T tracks P. The difference K of any other tracking solution commutes with P, so K annihilates u and is an arbitrary skew operator on u-perp.

First take v!=0 and write `u-perp=span(v) direct_sum W`, dim W=n-2. The proper half-turn that changes u,v to -u,-v and fixes W preserves the input. Equivariance forces K's components between v and W to be zero. Thus only a skew K_W supported on W can remain.

Every rotation in SO(W), extended by the identity on u,v, also preserves the input. Therefore K_W must be fixed by conjugation by SO(W).

- For dim W=0 or 1, there is no nonzero skew operator.
- For dim W=2, so(W) is one-dimensional and commutes with SO(W), so one component survives.
- For dim W>=3, every entry K_ij is killed by a proper coordinate half-turn that flips i and a third axis l distinct from i,j. It preserves SO(W) and changes the sign of that entry. All entries are zero.

This proves uniqueness except in n=4. In n=4 the surviving complementary-plane skew line is spanned by *Omega0. Equivariance of a rule implies its coefficient relative to that canonical nonzero vector is constant along each input orbit, hence is a rotation-invariant scalar; conversely any such coefficient yields an equivariant tracking rule.

If O(n) equivariance is required, a reflection in a coordinate of W is also allowed. In the exceptional two-dimensional W it reverses its skew generator, so that component vanishes as well. The other dimensions have already vanished.

Finally take v=0. Every orthogonal transformation g on u-perp can be embedded into SO(n) by acting on u with the sign det(g). The input is unchanged. K must therefore be fixed under all O(u-perp), and an individual coordinate reflection kills each possible skew entry. Hence K=0 already under SO(n). ∎

No choices of eigenvector signs have been given to the rule; the auxiliary simultaneous change (u,v)->(-u,-v) is built into the proof. The invariant coefficient in SO(4) may be noncontinuous if no regularity is required; its value at D=0 is still forced by that point's larger stabilizer.

The extra O(n) requirement and the SO(n) exception are mathematical distinctions about allowed changes of description. This does not assert that physical laws must adopt one of them.
