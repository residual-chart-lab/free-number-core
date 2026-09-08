# Note 26 — The 222 residual and its connection to 212

**Base:** `09b77f329d0c825c794443a0cd98cde89d8f1d73` (Notes 12, 21–25).

**Status:** exact theorem over Q, and hence over R, with an executable
certificate. The certificate reconstructs rational operators independently
modulo 1009 and 1013 and verifies their defining identities over the integers.

**Claim boundary.** The word 222 has a 444-dimensional quotient, a canonical
432-dimensional outer-edge subspace, and an intrinsic 12-dimensional residual
quotient. An explicitly specified central-slot **right decoder suspension**
induces an isomorphism from the 212 residual tensored with V to this residual
quotient. The same suspension does **not** descend to the full local
quotients. It has an obstruction whose image is the entire 432-dimensional
outer-edge subspace. No full state update, residual-to-core evolution,
choice-independent interior insertion, curvature, or time-generation law is
claimed.

## 1. The spaces and the three parents

Let V = Im H, with basis i,j,k, and let

\[
\mathcal R_m=\operatorname{Hom}(V^{\otimes m},\mathbb H),\qquad
J_m(h;v_1,\ldots,v_m)(x_1,\ldots,x_m)
=h x_m v_m\cdots x_1v_1.
\]

At n=8 take

\[
Q_{222}=(1,3,5,7),\qquad G_8\setminus Q_{222}=(2,4,6).
\]

The local matching presentation is

\[
C^0=\mathcal R_6^{\oplus4}
\xrightarrow{\partial_{222}}
E_{222}=\mathcal R_5^{\oplus6}
\xrightarrow{\pi_{222}}Y_{222}\longrightarrow0.
\]

Thus dim C^0 = 11664 and dim E = 5832. The matching map uses exactly the
face-to-edge restrictions of Note 12; no new matching relation is imposed.

Removing one spectator and compressing the remaining gap labels gives:

| Removed gap | Parent word | Parent support | Parent dimension |
|---|---|---|---:|
| 2 | 122 | (1,2,4,6) | 144 |
| 4 | 212 | (1,3,4,6) | 148 |
| 6 | 221 | (1,3,5,6) | 144 |

This combinatorial parent relation by itself does not define a map of
quotients. Maps are specified below.

## 2. An intrinsic residual with the central probe left open

For a cross edge e in {15,17,35,37}, the probed gap 4 is the third of its
five ordered probe slots. Define

\[
\epsilon_5(F)(z)=\sum_{a,b=1}^3 F(e_a,e_a,z,e_b,e_b),
\qquad \epsilon_5:\mathcal R_5\to\mathcal R_1.
\]

For an arbitrary six-edge tuple F set

\[
\boxed{\kappa_{222}(F)=
\epsilon_5(F_{15})-\epsilon_5(F_{17})
-\epsilon_5(F_{35})+\epsilon_5(F_{37}).}
\tag{2.1}
\]

The blocks on 13 and 57 are zero.

The elementary quaternion identity

\[
\sum_{a=1}^3 e_a v e_a=v\quad(v\in V)
\tag{2.2}
\]

proves compatibility. On a literal cross-edge response, each repeated
probe pair encloses one imaginary state coefficient, so (2.2) removes the
pair. All four cross edges reduce to the same one-probe response with only
gap 4 probed:

\[
v_8v_7v_6v_5\;z\;v_4v_3v_2v_1.
\]

Surjectivity of each terminal face then identifies the corresponding
compositions with its two cross-edge restrictions. Their opposite incidence
signs cancel. Consequently

\[
\boxed{\kappa_{222}\partial_{222}=0.}
\tag{2.3}
\]

This is the same paired-collapse mechanism used by kappa_212, but with the
central probe left open. It is not a claim that changing n leaves the
underlying state unchanged.

The operator epsilon_5 is onto R_1: its three sets of sampled coordinates
are independent for the three choices of z. Thus kappa_222 has rank 12.
In right-decoder coordinates its cross-edge block has the useful formula

\[
\epsilon_5 J_5(h;v_1,\ldots,v_5)(z)
=h v_5v_4\;z\;v_3v_2v_1.
\tag{2.4}
\]

In particular, merely taking the old collapsed quaternion and carrying the
middle coefficient without changing its position in the quaternion product
is not justified.

## 3. Exact dimensions and the canonical outer-edge subspace

The exact certificate gives

\[
\operatorname{rank}_{\mathbb Q}\partial_{222}=5388,
\qquad\boxed{\dim Y_{222}=444.}
\tag{3.1}
\]

Write E_e^Y = im(pi_222 iota_e) for the image of a single decoded edge.
Their dimensions, in lexicographic edge order, are:

| Edge | 13 | 15 | 17 | 35 | 37 | 57 |
|---|---:|---:|---:|---:|---:|---:|
| Dimension of its image in Y_222 | 432 | 336 | 408 | 120 | 336 | 432 |

The joint image of the two outer edges also has dimension 432. Since
kappa_222 vanishes on either outer edge and is onto a 12-dimensional target,

\[
\boxed{T_{222}:=E_{13}^Y=E_{57}^Y=\ker\bar\kappa_{222}.}
\tag{3.2}
\]

Here bar-kappa is the map induced on Y. There is an intrinsic exact sequence

\[
\boxed{
0\longrightarrow T_{222}\longrightarrow Y_{222}
\xrightarrow{\bar\kappa_{222}}\mathcal R_1\longrightarrow0,
\qquad 432\longrightarrow444\longrightarrow12.
}
\tag{3.3}
\]

The residual is, intrinsically, the **quotient**

\[
D_{222}:=Y_{222}/T_{222}\cong\mathcal R_1\cong\mathbb H\otimes V.
\]

Writing 444 = 432 + 12 does not choose a canonical complementary subspace
inside Y_222. No such choice is needed here.

For the parent 212, the same outer-edge characterization gives

\[
T_{212}=E_{13}^Y=E_{46}^Y=\ker\bar\kappa_{212},\quad
\dim T_{212}=144,\quad D_{212}:=Y_{212}/T_{212}\cong\mathbb H.
\tag{3.4}
\]

Note 21's anchored residual summand K_212 maps isomorphically onto D_212.
This distinguishes the intrinsic residual quotient from its anchored
realization as a summand.

## 4. The two generic parents transport onto the core

For parent 122, carry the new gap 2 through the common left outer edge,
which is 12 before compression and 13 in the child. The new argument is
leftmost among the edge's remaining probes, so use Note 22's right
suspension F z w.

For parent 221, carry the new gap 6 through the common right outer edge,
which is 56 in the parent and 57 in the child. The new argument is rightmost,
so use the left suspension w z F.

On either edge, the carried parent quotient block and the child quotient
block have rank 432 and the same kernel. Equality is certified by exact
rational row reduction, not inferred from equal dimensions. Therefore the
edge equations uniquely descend to isomorphisms

\[
\boxed{
Y_{122}\otimes V\xrightarrow{\sim}T_{222},\qquad
Y_{221}\otimes V\xrightarrow{\sim}T_{222}.
}
\tag{4.1}
\]

For the second map we use the standard tensor flip to keep the source order
(parent, new vector). These maps construct the common 432-dimensional
subspace; they do not specify a projection of all of Y_222 onto it.

## 5. Specify the central-slot comparison operation

There is no exterior new argument for the central parent 212. To make a
precise comparison, choose the following right-handed decoder operation.
On every edge, relabel the old gaps into the child and put the new variable
z at actual gap 4 in the list of arguments. Define

\[
\boxed{
(\Sigma_4^R(F\otimes w))(x_1,\ldots,z,\ldots,x_5)
:=F(x_1,\ldots,\widehat z,\ldots,x_5)\;z\;w.
}
\tag{5.1}
\]

The position of z as an argument is the physical gap label 4; its
multiplication at the right of F is the stated **choice of decoder**. This
must not be confused with inserting a vector into a literal state word.
The local encoder makes (5.1) an isomorphism E_212 tensor V -> E_222. It is
SO(3)-equivariant. It is not assumed to be a chain map.

On the cross edges z is the middle argument, so paired collapse gives the
exact identity

\[
\boxed{
\kappa_{222}\Sigma_4^R
=\Theta_R(\kappa_{212}\otimes\operatorname{id}_V),
\quad
\Theta_R(k\otimes w)(z)=kzw.
}
\tag{5.2}
\]

This equation follows directly by taking z w outside the sums over the two
paired variables. The certificate checks it on every edge over Q.

It follows that Sigma sends old matching relations into T_222 after taking
the child quotient. It therefore descends to

\[
Y_{212}\otimes V\longrightarrow D_{222},
\qquad\ker=T_{212}\otimes V.
\]

Factoring that kernel produces an isomorphism

\[
\boxed{
\beta_R:D_{212}\otimes V\xrightarrow{\sim}D_{222},
\qquad\operatorname{rank}\beta_R=12,
\qquad\ker\beta_R=0.
}
\tag{5.3}
\]

Equivalently, after using Note 21's specified K_212,

\[
K_{212}\otimes V\xrightarrow{\sim}D_{222}.
\]

For a fixed unit w in V, all four parent residual dimensions survive:

\[
\beta_{R,w}(k)(z)=kzw,\qquad
\operatorname{rank}\beta_{R,w}=4,\qquad\ker\beta_{R,w}=0,
\tag{5.4}
\]

with the explicit readout

\[
\boxed{k=-\beta_{R,w}(k)(w).}
\tag{5.5}
\]

For arbitrary nonzero w, divide the right side by its squared norm. Allowing
w to vary accounts for all 12 dimensions. Thus this is an explicit
residual-quotient redetection theorem, not merely a matching dimension count.

## 6. The full suspension fails, and the failure is exactly the core

The operator (5.1) does not descend to a map
Y_212 tensor V -> Y_222. Define its obstruction on old matching relations:

\[
\mathcal O:=\pi_{222}\Sigma_4^R
(\partial_{212}\otimes\operatorname{id}_V).
\]

Equation (5.2) proves im O is contained in T_222. The certificate finds a
nonzero 432-minor modulo both primes, using rational operators whose exact
identities have already been verified. Since dim T_222 = 432,

\[
\boxed{\operatorname{rank}_{\mathbb Q}\mathcal O=432,
\qquad\operatorname{im}\mathcal O=T_{222}.}
\tag{6.1}
\]

Changing an old representative by a matching relation can therefore change
the entire child core under this suspension. It cannot change the child
residual.

Consequently D_222 = Y_222/T_222 is precisely the **largest quotient of the
child** on which this chosen suspension descends from Y_212 tensor V.
The residual quotient was not selected just to hide a failed test: its
kernel is exactly the computed obstruction image.

This result also explains the limit of the redetection claim. A
representative-independent connection of residual quotients exists and is
injective on the full parent residual. The stronger connection into the
complete child state space fails for the specified operation. A later
residual-to-core update law must address this obstruction instead of silently
choosing representatives.

## 7. Proof certificate and stopping point

Run with Python 3, NumPy, SciPy, and a C++ compiler:

```bash
python3 certificates/n8_222_redetection_certificate.py --certificate --output result.json
```

The adjacent n8_222_exact_backend.cpp is compiled into a temporary cache. Set
FREE_NUMBER_222_CACHE to an absolute directory to choose another cache.
Delete that cache to force a clean reconstruction. No network is required.

The certificate:

1. checks the quaternion pairing identity and invertibility of Theta_R;
2. reconstructs the 212, 222, 122, and 221 local quotients over two primes;
3. verifies the reconstructed restrictions against literal natural-face
   quaternion products over the integers;
4. verifies full-rank rational annihilators and matching-rank lower bounds;
5. verifies every reported edge rank with exact rational row identities;
6. verifies the 12-dimensional residual and the two generic-parent core maps;
7. verifies the exact central residual square (5.2);
8. certifies the full obstruction rank 432 and all fixed-unit rank-4 readouts.

Natural face coordinates put h = v_(r+1)v_r at the missing gap r and retain
the other n-2 imaginary coefficients. They parametrize the entire terminal
face because successive left and right one-variable decoders are invertible.
Their use changes coordinates, not the matching presentation. On edge
spaces the right decoder J is exactly the one used in Notes 21–25.

The quaternion basis grading by the Klein four group splits the computations
into four blocks. This is an exact invariant decomposition, not a sampling
of states or a floating-point approximation.

The desired finite step is now closed: 222, all three parent comparisons,
and the precise redetection/kernel statements. Updating Lambda, constructing
F or Psi, traversing a word loop, and interpreting curvature remain outside
this note.
