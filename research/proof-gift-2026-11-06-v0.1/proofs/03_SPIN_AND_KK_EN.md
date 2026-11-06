# General identities underlying the spin, rotor, units and KK studies

These are mathematical consequences of the explicitly chosen model equations. They provide general hypotheses and proofs for relationships previously checked on selected inputs. They do not calibrate a material or impose field equations on a prescribed background.

## T13. Quadratic residual response in every irreducible spin

Set hbar=1. Let Jx,Jy,Jz be the standard irreducible spin-j Hermitian generators, j a nonnegative integer or half-integer, `[Ja,Jb]=i epsilon_abc Jc` and `sum Ja^2=j(j+1)I`. For a real symmetric trace-free 3-by-3 S define

```
Q_j(S)=sum_ab S_ab (JaJb+JbJa)/2.                     (13)
```

The map is covariant under simultaneous spatial rotation and the corresponding unitary spin representation. It is zero for j=0 and j=1/2, and injective for every j>=1. More precisely,

```
tr(Q_j(S)Q_j(T))=c_j tr(ST),
c_j=(2j+1)j(j+1)(4j(j+1)-3)/30.                      (14)
```

In the Cartesian spin-1 convention of the original model, `Q_1(S)=-S=A2(S)/2`.

**Proof.** A unitary spin rotation sends the vector of generators by the same orthogonal rotation, proving covariance. For spin zero the generators vanish. For spin 1/2, `{Ja,Jb}/2=delta_ab I/4`; trace-free S therefore gives zero.

Let |n,j> be the highest-weight state along a unit vector n, obtained by rotation of |z,j>. The highest-weight relations give `<Jz^2>=j^2`, `<Jx^2>=<Jy^2>=j/2`, and zero symmetrized cross moments at z. Rotating this identity gives

```
<n,j|{Ja,Jb}/2|n,j>=(j/2)delta_ab+j(j-1/2)n_a n_b.
```

Thus `<n,j|Q_j(S)|n,j>=j(j-1/2)n^T S n`. For j>=1, if the operator is zero then this quadratic form vanishes for every n. Polarization gives S=0, proving injectivity.

For the coefficient in (14), the rotation-invariant bilinear form on Sym_0(R3) is a scalar multiple of tr(ST). One elementary justification is that sign-flips kill cross terms between diagonal and distinct off-diagonal coordinates, coordinate permutations identify the off-diagonal coefficients, and a 45-degree coordinate-plane rotation identifies them with the diagonal coefficient; the trace constraint leaves one scalar. Take `S0=diag(-1/3,-1/3,2/3)`, with tr(S0^2)=2/3. Then `Q_j(S0)=Jz^2-j(j+1)I/3`. Sum over m=-j,...,j using

```
sum m^2=(2j+1)j(j+1)/3,
sum m^4=(2j+1)j(j+1)(3j(j+1)-1)/15.
```

Expansion gives `tr Q_j(S0)^2=(2j+1)j(j+1)(4j(j+1)-3)/45`, which divided by 2/3 yields c_j. The sums are finite arithmetic-polynomial sums and hold also on half-integer grids. Polarization gives (14). Finally Cartesian `Ja_bc=-i epsilon_abc` gives `Q_1(S)=tr(S)I-S=-S`, directly by contracting the two epsilon tensors. ∎

This proves that the selected quadratic coupling's loss at spin 1/2 is general, not a numerical accident, and that its residual detectability extends beyond spin 1. It is not a theorem about every possible spin-1/2 interaction.

## T14. Quantum state/classical rotor balances for arbitrary smooth coupling

Let I>0, H(theta,t) a C1 finite-dimensional Hermitian matrix (with enough local smoothness for classical ODE existence), and psi a normalized state. Consider the chosen Ehrenfest equations

```
psi_dot=-i H(theta,t)psi,
theta_dot=L/I,
L_dot=-<psi,H_theta psi>.
```

Along every solution,

```
d||psi||^2/dt=0,
d[L^2/(2I)+<H>]/dt=<H_t>.                            (15)
```

Thus autonomous H conserves energy, while a specified control contributes its explicitly computed work integral. These identities also hold for a density matrix with `rho_dot=-i[H,rho]` and expectations `tr(rho X)`.

If `H=V(theta,t)+Z(t)` and

```
V(theta,t)=exp(-i theta Jz) V0(t) exp(i theta Jz),
```

then

```
d(L+<Jz>)/dt=i<[Z,Jz]>.                              (16)
```

For `Z=-gamma B(t) dot J`, the right side is `gamma(<J> cross B)_z`. This accounts for arbitrary external field directions, rather than assuming the external torque is zero.

**Proof.** Hermiticity cancels the two terms in the norm derivative. For any observable X, direct differentiation of the Schrödinger equation gives `d<X>/dt=<X_t>+theta_dot<X_theta>+i<[H,X]>`. For X=H the commutator vanishes. The theta term cancels `(L/I)L_dot`, proving (15). Conjugation gives `V_theta=i[V,Jz]`; insert this in the mechanical torque and in `d<Jz>/dt=i<[H,Jz]>` to obtain (16). The spin commutation relations give the displayed cross product. Cyclicity of trace proves the density-matrix version by the same steps. ∎

**Controls as corollaries.** A scalar shift f(t)I only changes the quantum state's global phase and the recorded energy/work by f(t); it leaves all mechanical forces and spin expectations unchanged. A theta-independent isotropic term, including `k(t)sum Ja^2`, has zero mechanical torque. For a quadratic trace-free coupling, T13 explains the spin-1/2 zero control. These are conditional identities for these couplings, not prohibitions on other mechanisms.

**Existence.** Locally Lipschitz right-hand sides give the usual local ODE solution. For an autonomous smooth theta-periodic H, bounded H and conserved (15) bound L; norm conservation bounds psi. Thus no finite-time escape in these variables occurs and solutions extend on all finite time intervals. This argument assumes the smooth model and I>0, not an arbitrary singular control or I=0. Numerical conservation tolerances and the quantum/classical approximation remain separate questions.

## T15. Exact change from SI units to the dimensionless rotor

Let hbar>0 and E0>0. Put

```
tau=E0 t/hbar,  L_phys=hbar ell,  H_phys=E0 h,
I_dim=I_phys E0/hbar^2,  W_phys=E0 w.
```

The physical equations `i hbar psi_dot=H_phys psi`, `theta_dot=L_phys/I_phys`, `L_phys_dot=-<partial_theta H_phys>` become precisely

```
i psi_prime=h psi, theta_prime=ell/I_dim,
ell_prime=-<h_theta>, w_prime=<h_tau>.
```

**Proof.** Substitute `d/dt=(E0/hbar)d/dtau` into each equation and cancel the nonzero constants. The work and energy equations rescale by the same E0. The inverse substitution is defined for every stated positive scale, so the correspondence is bijective. ∎

This proves the parameter conversion for all such scales. Selecting E0, a material's spin content, an effective inertia and anisotropy coefficients is still an empirical modeling input.

## T16. KK reduction for an arbitrary prescribed smooth base geometry

Let (M,g) be a smooth nondegenerate pseudo-Riemannian base, A a smooth 1-form, phi a smooth nonzero real function, and kappa a constant. All are independent of the additional coordinate y. In a local coordinate patch define

```
ds^2=g_mu_nu dx^mu dx^nu+phi^2(dy+kappa A_mu dx^mu)^2,
L5=(1/2)g(v,v)+(1/2)phi^2(ydot+kappa A(v))^2.
```

For affinely parametrized geodesics,

```
p=phi^2(ydot+kappa A(v))                              (17)
```

is constant. The projection solves

```
nabla_v v = kappa p F^sharp(v)+p^2 phi^(-3) grad_g(phi),
F_mu_nu=partial_mu A_nu-partial_nu A_mu.               (18)
```

Conversely, every local solution of (18) for a fixed p lifts to a geodesic, uniquely after fixing y at one time, by integrating `ydot=p/phi^2-kappa A(v)`.

**Proof.** The y Euler–Lagrange equation is conservation of (17). At fixed p the Routhian, not simple substitution in L5, is

```
R=L5-p ydot=(1/2)g(v,v)+kappa p A(v)-p^2/(2phi^2).
```

Its x Euler–Lagrange equation is (18): the kinetic term supplies the Levi-Civita connection, the antisymmetrized A derivative supplies kappa p F, and differentiating the last term gives `p^2 phi^-3 dphi`. Raising the free index uses g. More explicitly, if w=ydot is eliminated by its momentum equation, then at fixed p `partial_x R=partial_x L5+(partial_w L5-p)partial_x w=partial_x L5`, and similarly `partial_v R=partial_v L5`. Thus the reduced Euler–Lagrange equations are exactly the full x equations restricted to p. The reconstructed y satisfies the remaining Euler–Lagrange equation, proving the converse. ∎

Under `A'=A+dchi`, `y'=y-kappa chi(x)`, the one-form `dy+kappa A` and the metric are unchanged. p is unchanged, while R changes by the total derivative `kappa p dchi/dlambda`; (18) is invariant. This proves gauge equivalence for arbitrary smooth chi, not just the two vector potentials executed in KK-001.

For a timelike normalization `G(v5,v5)=-1` and a Lorentzian base, `g(v,v)=-1-p^2/phi^2`. On intervals where four-dimensional proper time is used, `dtau/dlambda=sqrt(1+p^2/phi^2)`. If phi is constant, the proper-time Lorentz coefficient is `kappa p/sqrt(1+p^2/phi^2)`; if phi varies, parameter conversion has extra derivative terms and this constant-coefficient conclusion is not applied.

The theorem proves the general reduction and lift for the stipulated metric. It assumes neither flat g nor constant fields, but it does not prove that this background solves a vacuum or matter field equation. No spin or material coupling is supplied by this point-particle identity.
