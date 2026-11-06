# Algebra, response completeness, and paths

FN-GENERAL-PROOFS-001 v0.1. All tensor products are over the real numbers. The metric, orientation and Hamilton multiplication of H are fixed. Write V=Im H, <a,b>=Re(conjugate(a)b), and e=(1,i,j,k). These are concrete tensor spaces, before imposing any additional quotient or observational equivalence.

## T01. Exact length-two coordinates and full insertion

For T in V tensor V, use the coefficient convention

```
m(T)=sum T_ab e_b e_a = q0+w,
rho(T)=(T+T^T)/2-tr(T)I/3,
sigma(q0+w)=-q0 I/3+hat(w)/2,
hat(w)x=w cross x.
```

Then `T=sigma(m(T))+rho(T)` uniquely. For S=rho(T) and any real t and c in V,

```
L_T(t+c):=sum T_ab e_b (t+c) e_a
         =t(q0+w)+<w,c> - (q0/3)c-2Sc.                 (1)
```

Consequently the compressed quaternion and the residual response operator `A2(S)=-2S` determine every T exactly.

**Proof.** Hamilton multiplication of pure imaginary vectors gives `uv=-<u,v>+u cross v`. Thus the scalar part of m is -tr(T), and its vector part is twice the axial vector of the antisymmetric part of T. The symmetric trace-free part is killed. Orthogonal decomposition into scalar, skew and symmetric trace-free matrices gives the displayed sigma and rho, and their uniqueness. For a pure imaginary probe,

```
vector(e_b c e_a)=delta_ab c-c_b e_a-c_a e_b.
```

Contraction yields `tr(T)c-(T+T^T)c=-q0 c/3-2Sc`. The scalar contraction of the skew sector is `<w,c>`; the symmetric sector has zero scalar contraction. The real probe t contributes t m(T). This proves (1). In particular S=-A2(S)/2, giving the inverse. ∎

**Provenance.** The splitting, kernel classification and complete signature were already proved in fixed Core note 04. They are inherited results, not new discoveries here. Equation (1) records the full insertion convention needed below. This statement defines no final multiplication on the coordinate pair.

## T02. Exactly five fixed scalar samples suffice for a residual

For S in Sym_0(R^3), the five samples `w^T A2(S)c` at `(w,c)=(ex,ex),(ey,ey),(ex,ey),(ex,ez),(ey,ez)` determine S. No collection of fewer than five **fixed scalar linear** samples can distinguish every S.

**Proof.** Divide the samples by -2 to recover Sxx,Syy,Sxy,Sxz,Syz, and use Szz=-Sxx-Syy. Conversely the space has dimension five. A linear map to R^r, r<5, has a nonzero kernel by rank-nullity. Such a kernel element and zero have the same samples. ∎

This is not a lower bound for arbitrary encoded real numbers, nonlinear measurements, or unconstrained adaptive procedures. The full operator is not a single scalar observation.

## T03. Every finite quaternion tensor has a complete all-gap response

For every integer m>=1, put W_m=H^{tensor m}. On a pure tensor define

```
F_m(a0 tensor ... tensor a_(m-1))(c1,...,c_(m-1))
   =a_(m-1)c_(m-1) ... a1 c1 a0,
```

and extend linearly. The target is the space of real multilinear maps `H^(m-1) -> H`, equipped with the Hilbert-Schmidt inner product obtained by evaluating every argument on the orthonormal basis e. For m=1 the target is H.

For all T,U in W_m,

```
<F_m(T),F_m(U)>_HS = 4^(m-1)<T,U>.                    (2)
```

Hence F_m is a vector-space isomorphism. If b_alpha is a tensor basis word, its coefficient is explicitly

```
T_alpha = 4^(1-m) sum_(beta1,...,beta_(m-1))
    <F_m(T)(e_beta1,...), F_m(b_alpha)(e_beta1,...)>.   (3)
```

Restriction to B_m=V^{tensor m} is injective with the same norm identity. All these statements are for arbitrary finite m, not just the lengths executed by the checker.

**Proof of the basic identity.** For any a,b,c,d in H,

```
sum_(r=0)^3 <a e_r b, c e_r d> = 4<a,c><b,d>.        (4)
```

Indeed cyclicity of the real part rewrites the summand as `Re(conjugate(e_r) conjugate(a)c e_r d conjugate(b))`. The identity `sum conjugate(e_r)x e_r=4 Re(x)` follows by expanding x in 1,i,j,k. Summing gives (4).

**Induction.** For two basis tensor words, fix all probes except c1 and apply (4). The result is `4 delta_(a0,b0)` times the inner product of the two shorter response words. Repeating removes one gap at a time, giving `4^(m-1)` times the product of Kronecker deltas. Bilinearity proves (2). The dimensions of domain and target are both 4^m; (2) gives injectivity and therefore surjectivity. Taking the inner product with each basis response proves (3). Restriction preserves injectivity. ∎

**Concatenation.** If x is a word tensor of length r, y one of length s, and d is the new junction probe, associativity gives

```
F_(r+s)(x tensor y)(internal probes of x,d,internal probes of y)
 =F_s(y)(... ) d F_r(x)(... ).                         (5)
```

Linearity extends this identity to all tensors. Thus the full response data are compositionally closed when their junction and all internal slots are retained.

**Operational boundary.** This is an external all-gap assay on the concrete tensor word model. It does not assert that every such probe has already been declared admissible in the current abstract Core, or that a quotient of W_m remains injective. The signature grows with m: 4^(m-1) quaternion evaluations suffice in this construction; dim(B_m)=3^m. A fixed number r of scalar linear coordinates cannot be complete on B_m when 3^m>r. In particular the length-two pair cannot silently stand for arbitrary internal slots of an unbounded history.

**Context.** The m=2 case is the familiar left/right action of the quaternion algebra on itself, related to `H tensor H^op ~= End_R(H)`. The proof above is explicit and does not require that theorem as an assumption. No priority claim is made.

## T04. Exact criterion for losing a future response under compression

Let pi:X->Y be any compression, and f:X->Z any specified response. A map g:pi(X)->Z with f=g composed pi exists **if and only if** f is constant on every fiber of pi.

**Proof.** Factorization implies equal pi-values give equal f-values. Conversely, define g(y) to be the common f-value of the nonempty fiber pi^-1(y); constancy makes this well-defined. ∎

For equal quaternion values at length two, T-U is a residual S. If S!=0 there are probes c,w with `w^T A2(S)c!=0`: choose c with Sc!=0 and w=Sc. The difference is then `-2||Sc||^2`. Thus value-only compression cannot preserve every internal response. A particular scalar probe can still miss S; universal completeness and a chosen single observation are different claims.

## T05. Response commutators span every infinitesimal rotation

For real n>=2, the linear span of `[S,T]` with S,T symmetric trace-free n-by-n matrices is so(n). Therefore in the Core dimension three, commutators of A2 responses span so(3).

**Proof.** A commutator of symmetric matrices is skew. For each p<q choose a trace-free diagonal D with Dpp!=Dqq, and E having ones at pq and qp. The commutator `[E,D]` has entries `(Dqq-Dpp)` at pq and its negative at qp, and zero elsewhere. These are the standard skew basis. Multiplying both S,T by -2 multiplies the commutator by four, without changing the span. ∎

The n-dimensional assertion is a matrix lemma. The actual fixed quaternionic Core still has n=3. A span of operator compositions is not a newly declared multiplication on B2.

## T06. Any finite graph path transports the complete length-two signature

On a graph choose a unit quaternion U_ts on every oriented edge, with U_st=U_ts^-1 when inverse edges are used. For a finite path p=(v0,...,vk), define `U(p)=U_(vk,vk-1)...U_(v1,v0)` and R(p)=Ad_(U(p)) on V. Transport T by `R(p)T R(p)^T`.

For every finite path, every T, every quaternion probe C, and every scalar analyzer w:

1. `m(RTR^T)=U m(T) U^-1`;
2. `rho(RTR^T)=R rho(T)R^T` and sigma intertwines too;
3. `L_(RTR^T)(UCU^-1)=U L_T(C) U^-1`;
4. transporting value and residual then reconstructing gives the same T as transporting it whole;
5. concatenation and reversal give `U(q*p)=U(q)U(p)`, `R(q*p)=R(q)R(p)`, and `U(p^-1)=U(p)^-1`;
6. under arbitrary vertex frames G_v, edge data `U'_ts=G_t U_ts G_s^-1` give `U'(p)=G_end U(p)G_start^-1`. Probes and analyzers transformed in the same frame preserve scalar readouts.

**Proof.** Quaternion conjugation preserves real scalars, inner product, orientation and multiplication. On a pure word, `(UvU^-1)(UuU^-1)=U(vu)U^-1`, and the same cancellation holds with an inserted probe. Extend linearly. Orthogonality preserves symmetrization and trace, proving rho-equivariance; the explicit sigma formula gives its equivariance. Each path statement follows by associativity; intermediate frames cancel in adjacent products. Induction on the finite path length includes the empty path and all concatenations. Readout invariance is `(Rw)^T(R A R^T)(Rc)=w^T A c`. ∎

This proves arbitrary path length and composition for **the given connection and the retained tensor**. It does not encode internal interventions inside an already compressed partial path. T03 specifies the larger data required when all such slots are to remain accessible.
