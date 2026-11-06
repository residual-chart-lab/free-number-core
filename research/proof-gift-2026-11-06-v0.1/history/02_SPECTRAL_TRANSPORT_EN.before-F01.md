# Spectral transport: arbitrary residual shape, uniqueness, and boundaries

All matrices here are real. [X,Y]=XY-YX; the Frobenius inner product is tr(X^T Y). General n-dimensional lemmas are explicitly distinguished from the actual Core dimension three.

## T07. Orthogonal decomposition and the minimum generator for any symmetric S

Let S,D be symmetric n-by-n matrices, n>=2. Write the spectral decomposition into **distinct** eigenvalues as `S=sum_alpha lambda_alpha P_alpha`. Define

```
E = sum_alpha P_alpha D P_alpha,
Omega_* = sum_(alpha!=beta) P_alpha D P_beta/(lambda_beta-lambda_alpha). (6)
```

Then Omega_* is skew, E commutes with S, and

```
D=[Omega_*,S]+E.                                      (7)
```

The decomposition of D into an orbit tangent `[Omega,S]` and a symmetric commuting part E is unique. Every skew generator of that tangent is `Omega_*+K`, `[K,S]=0`, and

```
||Omega_*+K||_F^2=||Omega_*||_F^2+||K||_F^2.           (8)
```

Hence Omega_* uniquely minimizes the norm among those generators.

**Proof.** In a basis diagonalizing S, symmetric D splits orthogonally into its diagonal spectral blocks and its cross-block entries. For a skew Omega, `[Omega,S]_ij=(lambda_j-lambda_i)Omega_ij`. The cross-block entries uniquely give (6); swapping indices proves skewness. Its within-block entries are zero. The kernel is precisely the within-block skew matrices. The two supports are Frobenius orthogonal, proving (7), uniqueness of E and the tangent, and (8). This proof works in any dimension and includes repeated eigenvalues and S=scalar*I. ∎

**Response-only construction.** On skew matrices define `L_A(K)=[[K,A],A]` with A=-2S, and let L_A^+ denote its Moore–Penrose inverse with the zero action on its kernel. Its eigenvalues in a spectral block are `(a_beta-a_alpha)^2`, so it is positive semidefinite. Since `[D_A,A]` has no diagonal spectral blocks, with D_A=-2D,

```
Omega_* = L_A^+([D_A,A]).                             (9)
```

Thus the fixed Core response A2 can generate this canonical minimum rotational component for arbitrary symmetric trace-free S, not only a uniaxial family. A rational S,D permits an exact rational linear solve for (9) without computing eigenvectors or square roots. This is a construction from operator compositions, not a new product on Core representatives.

**Spectral evolution.** Suppose S(t) is C1 on an interval, its number of distinct eigenvalues and their multiplicities are constant, and its spectral projectors are C1 (local nonzero gaps ensure this). Then D=Sdot satisfies

```
E=sum_alpha lambda_dot_alpha P_alpha,
[Omega_*,P_alpha]=Pdot_alpha,
Omega_*=(1/2)sum_alpha [Pdot_alpha,P_alpha].            (10)
```

Differentiate `SP_alpha=lambda_alpha P_alpha`, take cross-blocks, and substitute (6). Differentiating the resolution of identity verifies the last equality block by block. Conversely all projector-tracking skew generators differ from Omega_* by a commuting K. The amplitude/eigenvalue drift E is retained separately; a rotation does not create it.

For continuous Omega_*, the linear ODE `Rdot=Omega_*R, R(t0)=I` has a unique solution on every compact subinterval. Differentiating R^T R and det R shows R in SO(n). Differentiating R^T P_alpha R using (10) shows it is constant. ODE uniqueness gives concatenation, inverse transport for the reversed path, and reparameterization covariance along the same ordered path. These statements concern the supplied path, not endpoint-only path reconstruction.

## T08. In three dimensions, first-jet equivariance selects that generator

Consider the union of admissible C1 **constant-multiplicity spectral first jets** of real symmetric 3-by-3 S(t). A rule F(S,Sdot) returning a skew matrix is required to depend only on that first jet, track every spectral projector, and be equivariant under every time-independent common G in SO(3). Then F=Omega_* from T07, without assuming linearity, continuity, or minimum norm.

**Proof by the three multiplicity types.**

1. **Three distinct eigenvalues.** Any difference K of two tracking generators commutes with S. In an eigenbasis K is skew and diagonal, hence zero. Tracking alone is enough.
2. **One simple and one double eigenvalue.** Write `S=lambda_2 I+aP`, a!=0, with rank-one unoriented P. An admissible jet is `D=lambda_dot_2 I+adot P+aPdot`. Write `P=nn^T`, `Pdot=nv^T+vn^T`, n dot v=0. Then Omega_*=[Pdot,P]. Every alternative is Omega_*+k hat(n). If v!=0, the proper half-turn about n cross v changes n,v to -n,-v and leaves S,D unchanged, while conjugating hat(n) to -hat(n). Equivariance forces k=0. If v=0, use a half-turn about any perpendicular axis. Eigenvalue rates are scalars and do not break this argument.
3. **Triple eigenvalue.** On the constant-multiplicity stratum S=lambda I and D=lambda_dot I. All of SO(3) fixes the input; a skew output fixed by all conjugations must vanish. This also follows by the three coordinate half-turns. Omega_*=0.

These cases exhaust real symmetric 3-by-3 matrices. ∎

The same proof allows any additional rotation-invariant scalar parameters: the stabilizer fixes them too. Scalars such as an external time do not by themselves permit an axial twist. Directional extra data are different. For rational uniaxial data the amplitude also has the rational formula `a=3 tr(S^3)/tr(S^2)`; the square root used in the old first-jet checker is therefore exact on every valid rational input. More generally T07's rational minimum linear solve avoids a finite-step square root altogether.

**Why the assumptions matter.**

- A stored additional tensor M or second derivative can break the input's symmetry and allow extra commuting K. The earlier explicit `Q[M,Pdot]Q` and `Q[Pddot,Pdot]Q`, Q=I-P, remain valid examples.
- For a uniaxial S with an arbitrary D that splits the double eigenspace, the jet is not on that stratum. At P=diag(1,0,0), choose `D=E_xy+E_yz`. Then `Q[D,DPD]Q=Jx` is a nonzero, covariant, commuting skew term formed from this enlarged first-jet domain. It vanishes for stable uniaxial jets. Thus the stable-multiplicity condition is substantial.
- The uniqueness is dimension-specific. In oriented R4 take rank-one P, D=Pdot, and Omega0=[D,P]. The Hodge dual `star(Omega0)` of its 2-form acts on the complementary two-plane, commutes with P, and transforms equivariantly under SO(4). Thus `Omega0+k star(Omega0)` gives distinct first-jet equivariant tracking rules. At P=diag(1,0,0,0), D=E12, Omega0=J12 and star(Omega0)=J34!=0. No such conclusion is being asserted for all dimensions.

## T09. The finite shortest line step, over the reals

Let P=nn^T,Q=mm^T be rank-one projections in R3, and `c=sqrt(tr(QP))>0`. Align the otherwise auxiliary signs so n dot m=c. Put

```
C=[Q,P], B=C/c, R_(Q<-P)=I+B+B^2/(1+c).               (11)
```

Write R=R_(Q<-P). Then R in SO(3), RPR^T=Q, and R is the unique rotation of minimum rotation angle among rotations taking the unoriented line P to Q. When P=Q this is I. The construction is common-SO(3)-equivariant and `R_(P<-Q)=R_(Q<-P)^-1`.

**Proof.** For c<1 write m=c n+s u, s=sqrt(1-c^2)>0, u perpendicular to n. Then `B=s(u n^T-n u^T)`. On span(n,u), (11) is the 2D rotation matrix with cosine c and sine s, and it fixes the orthogonal complement. This proves orthogonality, determinant and tracking. Any rotation taking n to m or -m has angle at least the spherical angle between these vectors: for a rotation of angle alpha around k, `n dot Rn=cos(alpha)+(1-cos(alpha))(k dot n)^2>=cos(alpha)`. The smaller lower bound is arccos(c)<pi/2; equality requires k perpendicular to both n,m and fixes the sign of the rotation. Therefore the stated R is unique. For c=1 the only zero-angle rotation is I. Formula (11) is invariant under the auxiliary simultaneous sign change, conjugates under a common frame, and transposes when P,Q swap. ∎

If c=0, rotations by +/-pi/2 about n cross m tie. In fact no SO(3)-equivariant selector into SO(3) tracking **all** orthogonal line pairs exists: the common stabilizer of Px,Py contains the three coordinate half-turns. Equivariance would force the selected R to commute with all of them, hence be diagonal, which cannot map Px to Py. A path refinement or extra information is required.

The real formula's domain and an exact Fraction implementation's domain are different. A valid rational pair with overlap squared 1/2 needs sqrt(1/2), which the old Fraction finite-step implementation cannot represent. This is an arithmetic limitation, not nonuniqueness of (11).

For a C1 path, (11) has `R_(P(t+h)<-P(t))=I+h[Pdot,P]+o(h)`. An O(h^2) remainder requires, for example, a bounded second derivative. Thus the infinitesimal generator agrees with T07 on the rank-one stratum. Exact equality of finite endpoint steps with a true intervening path is asserted only when that path is the specified short line geodesic.

## T10. Reference-assisted transport is equivariant

Let a reference B0 in SO(3) carry the source frame into the target frame. When Q and `B0 P B0^T` are nonorthogonal define `F(P,Q;B0)=R_(Q<-B0PB0^T) B0`. For independent Gs,Gt in SO(3), transform P,Q and B0 by conjugation at their vertices and `B0'=Gt B0 Gs^T`. Then `F'=Gt F Gs^T`.

**Proof.** The source projector transported by B0' is `Gt(B0 P B0^T)Gt^T`. T09's common-frame equivariance conjugates the correction by Gt. Multiplication by B0' cancels the inner Gt^T Gt. ∎

## T11. Stabilizers obstruct endpoint-only local-frame covariance

Suppose target endpoint data y admit a nonidentity frame stabilizer H, so Hy=y. A proposed single-valued invertible F(x,y) is required to transform as `F(gx,hy)=h F(x,y)g^-1` under independent endpoint frames. No such F can exist on that pair: take the source frame g=I and target frame h=H.

**Proof.** The input remains the same while covariance demands `F=HF`. Right-multiplication by F^-1 gives H=I, a contradiction. ∎

Every symmetric 3-by-3 target has a nontrivial SO(3) stabilizer: diagonalize it and conjugate diag(-1,-1,1) back. Thus removing eigenvalue degeneracy does not remove this endpoint-only obstruction. The theorem's output is a chosen invertible frame map; a coset, multivalued object, or extra reference data has different requirements.

For time-dependent common frames, an actual connection transforms as `Omega'=G Omega G^T+Gdot G^T`. A constant line P can remain unchanged under a rotating frame about that line, even though the last term is nonzero. Residual-only first-jet covariance of T08 is therefore not full time-dependent gauge covariance.

## T12. A gap bound, and failure of unrestricted continuity at collisions

For T07 let delta be the smallest nonzero eigenvalue gap. Then

```
||Omega_*||_F <= ||D-E||_F/delta <= ||D||_F/delta.      (12)
```

**Proof.** Sum the squared entries in (6); every denominator has magnitude at least delta. E and D-E are orthogonal. ∎

No rule agreeing with T08 on every stable spectral stratum extends continuously over their entire union of admissible jets. For r>0 take

```
S_r=diag(r^2,-r^2,0), D_r=r E_xy.
```

These are realizable stable simple-spectrum jets via rotation at angular speed 1/(2r). T07 gives `Omega_r=Jz/(2r)`. The input jets tend to `(0,0)`, an admissible isotropic stationary jet, while Omega_r diverges. Thus additional bounds or boundary conventions are needed at collisions. ∎
