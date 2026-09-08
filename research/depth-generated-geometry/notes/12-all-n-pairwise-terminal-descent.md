# Note 12 — All-\(n\) Pairwise Terminal Descent

## local quaternion slides make every compatible response boundary globally fillable

**Status:** theorem for every finite \(n\ge2\); fixed local identities and exact rational checks through the \(n=6\) local model, with an auxiliary two-prime stress check at the \(n=7\) local model

**Depends on:** Notes 02, 07, and 09–11

**Claim boundary:** this note proves that pairwise common-shadow compatibility is sufficient to glue every terminal boundary, at every length. It also gives the universal first syzygy character. It does not construct a local higher differential resolving that syzygy module, give a short closed formula for the canonical Casimir filler, or identify any response residual with curvature.

---

## 0. Main theorem

Put

\[
\mathcal R_q
:=
\operatorname{Hom}_{\mathbb R}(V^{\otimes q},\mathbb H),
\qquad
\dim\mathcal R_q=4\cdot3^q.
\]

At length \(n\), let

\[
B_{n,r}:V^{\otimes n}\longrightarrow\mathcal R_{n-2},
\qquad 1\le r\le n-1,
\]

be the terminal face obtained by probing every internal gap except \(r\), and
write

\[
\mathbf B_n:=\bigoplus_{r=1}^{n-1}B_{n,r}.
\]

For every pair \(r<s\), the two faces have a common shadow in
\(\mathcal R_{n-3}\). The decoder-collapse construction gives unique
restriction maps

\[
\rho_r^{rs},\rho_s^{rs}:
\mathcal R_{n-2}\longrightarrow\mathcal R_{n-3}
\]

such that both compositions with the corresponding terminal face equal the
same two-gap collapse. Define

\[
\boxed{
\partial_n:
\mathcal R_{n-2}^{\oplus(n-1)}
\longrightarrow
\mathcal R_{n-3}^{\oplus\binom{n-1}{2}}
}
\tag{0.1}
\]

by

\[
(\partial_nF)_{rs}
=
\rho_r^{rs}F_r-\rho_s^{rs}F_s.
\tag{0.2}
\]

The identity

\[
\partial_n\mathbf B_n=0
\tag{0.3}
\]

is automatic. The question left by Notes 10 and 11 was whether these
pairwise equations are all the gluing equations.

### Theorem 0.1 — all-\(n\) pairwise terminal descent

For every \(n\ge3\),

\[
\boxed{
\ker\partial_n=\operatorname{im}\mathbf B_n.
}
\tag{0.4}
\]

For \(n=2\), the same statement holds with the empty matching operator:
the single terminal face \(B_{2,1}:V^{\otimes2}\to\mathbb H\) is onto.

Combining (0.4) with the all-length boundary-kernel theorem of Note 09 gives
the exact sequence

\[
\boxed{
0\longrightarrow S^n_0V
\longrightarrow V^{\otimes n}
\xrightarrow{\ \mathbf B_n\ }
\mathcal R_{n-2}^{\oplus(n-1)}
\xrightarrow{\ \partial_n\ }
\mathcal R_{n-3}^{\oplus\binom{n-1}{2}}
\longrightarrow\mathfrak S_n
\longrightarrow0,
}
\tag{0.5}
\]

where

\[
\mathfrak S_n:=\operatorname{coker}\partial_n.
\]

Thus the terminal boundary has an intrinsic generators-and-relations
presentation for every finite length:

\[
\boxed{
\mathcal P_{n,n-2}
=
\operatorname{im}\mathbf B_n
=
\ker\partial_n.
}
\tag{0.6}
\]

---

## 1. Reduce the induction to one null-boundary face

Write

\[
m:=n-2.
\]

Suppose

\[
(F_1,\ldots,F_{m+1})\in\ker\partial_n
\]

is a compatible family of terminal faces. Temporarily discard the last face
\(F_{m+1}\).

For \(r\le m\), the face \(F_r\) still probes the outermost gap \(m+1=n-1\).
Apply the left local decoder of Note 07 in that probe variable. There are
unique responses

\[
F_{r,a}\in\mathcal R_{m-1},
\qquad a=1,2,3,
\]

such that

\[
F_r(x_1,\ldots,x_m)
=
\sum_{a=1}^3
e_a x_m F_{r,a}(x_1,\ldots,x_{m-1}).
\tag{1.1}
\]

Removing an inner probe commutes with this outer decoder. Equivalently, the
restriction squares commute because they agree after precomposition with the
onto face maps. Hence, for each fixed \(a\),

\[
(F_{1,a},\ldots,F_{m,a})
\]

is a compatible length-\((n-1)\) boundary.

Assume Theorem 0.1 at length \(n-1\). Choose

\[
T_a\in V^{\otimes(n-1)}
\]

filling this decoded boundary and put

\[
T:=\sum_{a=1}^3T_a|e_a\in V^{\otimes n}.
\tag{1.2}
\]

Then

\[
B_{n,r}(T)=F_r,
\qquad 1\le r\le m.
\tag{1.3}
\]

Only the last face may be wrong. Its residual is

\[
G:=F_{m+1}-B_{n,m+1}(T)\in\mathcal R_m.
\tag{1.4}
\]

Compatibility and (1.3) imply that every common-shadow restriction of \(G\)
vanishes. Define the last-face null-boundary space

\[
\boxed{
Z_m
:=
\bigcap_{j=1}^{m}\ker\delta_{m,j}
\subseteq\mathcal R_m,
}
\tag{1.5}
\]

where \(\delta_{m,j}\) deletes the \(j\)-th remaining probe of the last face.
Then

\[
G\in Z_m.
\tag{1.6}
\]

The all-length gluing problem is therefore reduced to identifying \(Z_m\)
and showing that it is exactly the range of corrections that preserve the
first \(m\) faces.

---

## 2. Right response coordinates

Define the iterated right encoder

\[
\boxed{
J_m:
\mathbb H\otimes V^{\otimes m}
\xrightarrow{\ \cong\ }
\mathcal R_m
}
\tag{2.1}
\]

on pure tensors by

\[
J_m(h\otimes v_1\otimes\cdots\otimes v_m)
(x_1,\ldots,x_m)
=
h x_m v_m\cdots x_1v_1.
\tag{2.2}
\]

This is an isomorphism because it is an iteration of

\[
\Theta_R:
\mathbb H\otimes V\xrightarrow{\ \cong\ }
\operatorname{Hom}(V,\mathbb H),
\qquad
\Theta_R(h\otimes v)(x)=hxv.
\]

In these coordinates define the simple slot contractions

\[
\boxed{
M_{m,j}:
\mathbb H\otimes V^{\otimes m}
\longrightarrow
\mathbb H\otimes V^{\otimes(m-1)}
}
\tag{2.3}
\]

by

\[
M_{m,j}
(h\otimes v_1\otimes\cdots\otimes v_m)
=
(hv_j)\otimes
v_1\otimes\cdots\widehat{v_j}\cdots\otimes v_m.
\tag{2.4}
\]

These are not individually equal to the actual deletion maps. An inner
deletion produces an internal product \(v_{j+1}v_j\), whereas \(M_{m,j}\)
moves \(v_j\) directly into the quaternion coefficient. The crucial fact is
that the two full families have the same common kernel.

---

## 3. The local quaternion slide

For \(h\in\mathbb H\) and \(u,v,x\in V\), the quaternion anticommutator gives

\[
xv+vx=-2\langle x,v\rangle.
\]

Associativity therefore gives the fixed identity

\[
\boxed{
h x(vu)+(hv)xu
=
-2\langle x,v\rangle hu.
}
\tag{3.1}
\]

Define an automorphism \(\Psi:\mathcal R_1\to\mathcal R_1\) as follows. If

\[
\Theta_R^{-1}(H)=\sum_a c_a\otimes w_a,
\]

put

\[
\boxed{
(\Psi H)(x)
=
-2\sum_a\langle x,w_a\rangle c_a.
}
\tag{3.2}
\]

The metric identifies \(V\cong V^*\), so (3.2) is an isomorphism. More
explicitly, a basis calculation gives

\[
\boxed{
\Psi^2+\Psi-2\operatorname{id}=0,
\qquad
\Psi^{-1}=\frac12(\Psi+\operatorname{id}),
\qquad
\det\Psi=16.
}
\tag{3.2a}
\]

At two slots, set

\[
\begin{aligned}
D_1(h,u,v)(x)&:=hx(vu),\\
D_2(h,u,v)(x)&:=(hv)xu,\\
S_1(h,u,v)(x)&:=(hu)xv,\\
S_2(h,u,v)(x)&:=(hv)xu.
\end{aligned}
\]

Equation (3.1) is exactly

\[
\boxed{
D_1=\Psi S_1-S_2,
\qquad
D_2=S_2.
}
\tag{3.3}
\]

This is the elementary triangular move.

### Lemma 3.1 — deletion-contraction triangularization

For every \(m\ge1\), order the actual deletions from the outermost probe to
the innermost probe. Repeated use of (3.3), with all other tensor factors and
probe variables held as spectators, gives an invertible block-triangular
change of target coordinates between

\[
(\delta_{m,1}J_m,\ldots,\delta_{m,m}J_m)
\]

and

\[
(J_{m-1}M_{m,1},\ldots,J_{m-1}M_{m,m}).
\]

More strongly, for every suffix \(k\le j\le m\), the two suffix stacks have
the same row space.

### Proof

The outermost deletion is already the outermost simple contraction. Suppose
the deletions outside slot \(j\) have been triangularized. At the first factor
outside \(j\), apply (3.3) pointwise in all spectator variables. Its leading
term slides \(v_j\) one position toward the quaternion coefficient and is
multiplied by a conjugate of \(\Psi\). Its correction contracts a strictly
outer factor. Factors already crossed by \(v_j\) may appear in a different
order afterward, but this is only a permutation of the *remaining target
slots* after contraction. It is therefore an invertible target coordinate
change applied to \(M_{m,k}\) for some \(k>j\), not a permutation of the
source tensor. Thus the correction already lies in the row space of the
outer suffix stack. Continue until \(v_j\) reaches the coefficient.

The diagonal block is a composition of conjugates of \(\Psi\) by spectator
encoders, hence is invertible. Downward induction on \(j\) gives a block
triangular operator with invertible diagonal. The same induction beginning at
any \(k\) proves the suffix statement. ∎

Equivalently, if

\[
D_{m,j}:=\delta_{m,j}J_m,
\qquad
S_{m,j}:=J_{m-1}M_{m,j},
\]

then the proof constructs an invertible block-triangular target operator
\(\mathcal U_m\) such that

\[
\boxed{
\begin{bmatrix}
D_{m,1}\\ \vdots\\ D_{m,m}
\end{bmatrix}
=
\mathcal U_m
\begin{bmatrix}
S_{m,1}\\ \vdots\\ S_{m,m}
\end{bmatrix}.
}
\tag{3.3a}
\]

Its off-diagonal blocks include the target permutations described above;
its diagonal blocks are compositions of decoder conjugates and are
invertible by (3.2a).

Consequently,

\[
\boxed{
J_m^{-1}(Z_m)
=
K_m
:=
\bigcap_{j=1}^{m}\ker M_{m,j}.
}
\tag{3.4}
\]

The response-specific deletion problem has been reduced to a tensor kernel
with one elementary contraction per slot.

---

## 4. The simple contraction kernel

### Theorem 4.1 — Cartan kernel decomposition

For every \(m\ge0\),

\[
\boxed{
K_m
\cong
S^m_0V\oplus S^{m+1}_0V
\cong
V_m\oplus V_{m+1}.
}
\tag{4.1}
\]

In particular,

\[
\boxed{
\dim K_m=4(m+1).
}
\tag{4.2}
\]

For \(m=0\), this is the quaternion decomposition

\[
\mathbb H\cong V_0\oplus V_1.
\]

The proof for \(m\ge1\) is constructive.

### 4.1 Input symmetry

The space \(K_m\) is invariant under permutations of the \(m\) input slots.
Take the antisymmetric part of \(T\in K_m\) in two slots and freeze every
other slot. Write its two-slot coefficient as

\[
T_{pq}=-T_{qp}=\sum_a\varepsilon_{pqa}c_a,
\qquad c_a\in\mathbb H.
\]

One simple contraction becomes the fixed map

\[
\boxed{
\kappa:
\mathbb H\otimes V\longrightarrow\mathbb H\otimes V,
\qquad
(\kappa c)_q
=
\sum_{p,a}\varepsilon_{pqa}c_a e_p.
}
\tag{4.3}
\]

Direct expansion in the basis \(1,e_1,e_2,e_3\) gives the stronger identity

\[
\boxed{
\kappa^2-\kappa-2\operatorname{id}=0,
\qquad
\kappa^{-1}=\frac12(\kappa-\operatorname{id}),
\qquad
\det\kappa=16.
}
\tag{4.4}
\]

Thus \(\kappa\) is invertible, so every two-slot antisymmetric part vanishes.
Hence every \(T\in K_m\) is symmetric in its input slots.

### 4.2 Input traces

Compose two distinct contractions. Since the input coefficient is symmetric,
only the symmetric quaternion product contributes:

\[
e_pe_q+e_qe_p=-2\delta_{pq}.
\]

The composite equation is therefore the negative of the corresponding input
trace. It vanishes because each \(M_{m,j}T\) vanishes. Hence every input trace
of \(T\) is zero and

\[
\boxed{
K_m\subseteq\mathbb H\otimes S^m_0V.
}
\tag{4.5}
\]

### 4.3 Scalar projection and its kernel

Use

\[
\mathbb H=\mathbb R1\oplus V
\]

and write

\[
T=1\otimes A+\sum_{p=1}^3e_p\otimes B_p.
\tag{4.6}
\]

By (4.5), \(A\in S^m_0V\). Let

\[
\pi:K_m\longrightarrow S^m_0V,
\qquad
\pi(T)=A.
\tag{4.7}
\]

If \(A=0\), the scalar part of \(M_{m,j}T=0\) says that the output-input
trace of \(B\) vanishes. Its vector part says that the antisymmetric
output-input component vanishes. This holds for every input slot, so

\[
\boxed{
\ker\pi=S^{m+1}_0V.
}
\tag{4.8}
\]

The embedding in (4.8) simply regards one tensor slot as the imaginary
quaternion coefficient.

### 4.4 An explicit section

For \(A\in S^m_0V\), define

\[
\boxed{
B(A)_{p;i_1\ldots i_m}
=
-\frac1{m+1}
\sum_{j=1}^m\sum_{q=1}^3
\varepsilon_{p i_j q}
A_{i_1\ldots i_{j-1}q i_{j+1}\ldots i_m}.
}
\tag{4.9}
\]

Set

\[
\boxed{
\iota_m(A)
:=
1\otimes A+\sum_pe_p\otimes B(A)_p.
}
\tag{4.10}
\]

The scalar part of every \(M_{m,j}\iota_m(A)\) vanishes by symmetry. For the
vector part use

\[
\sum_{p,q}\varepsilon_{pqr}\varepsilon_{pqt}
=2\delta_{rt}.
\tag{4.11}
\]

The summand \(j\) in (4.9) contributes twice, each of the other \(m-1\)
summands contributes once by symmetry, and trace terms vanish because \(A\)
is trace-free. Thus

\[
\sum_{p,q}\varepsilon_{pqr}
B(A)_{p;i_1\ldots q\ldots i_m}
=-A_{i_1\ldots r\ldots i_m}.
\tag{4.12}
\]

This cancels the vector contribution of \(1\otimes A\), so

\[
M_{m,j}\iota_m(A)=0
\]

for every \(j\). Moreover,

\[
\pi\iota_m=\operatorname{id}_{S^m_0V}.
\]

Therefore

\[
0\longrightarrow S^{m+1}_0V
\longrightarrow K_m
\xrightarrow{\ \pi\ }
S^m_0V
\longrightarrow0
\tag{4.13}
\]

has the explicit equivariant section (4.10), proving (4.1). ∎

---

## 5. The last-face null-boundary lemma

Combining Lemma 3.1 and Theorem 4.1 gives:

### Lemma 5.1

For every \(m\ge0\),

\[
\boxed{
Z_m
=
J_m(K_m)
\cong
V_m\oplus V_{m+1},
\qquad
\dim Z_m=4(m+1).
}
\tag{5.1}
\]

Return to length \(n=m+2\). Corrections that leave the first \(m=n-2\)
terminal faces unchanged form

\[
\begin{aligned}
C_n
&:=
\bigcap_{r=1}^{n-2}\ker B_{n,r}\\
&=
S^{n-1}_0V\otimes V.
\end{aligned}
\tag{5.2}
\]

The equality is the adjacent-pair intersection theorem of Note 09 applied to
the first \(n-1\) tensor slots.

The last face maps \(C_n\) into \(Z_{n-2}\). Indeed, for \(U\in C_n\), every
last-face common shadow equals the corresponding restriction of the zero
face \(B_{n,r}(U)\).

The kernel of this restricted map is

\[
\begin{aligned}
\ker(B_{n,n-1}|_{C_n})
&=
\bigcap_{r=1}^{n-1}\ker B_{n,r}\\
&=
S^n_0V
\end{aligned}
\tag{5.3}
\]

by Note 09. Therefore

\[
\begin{aligned}
\dim B_{n,n-1}(C_n)
&=
3\dim S^{n-1}_0V-\dim S^n_0V\\
&=
3(2n-1)-(2n+1)\\
&=
4n-4.
\end{aligned}
\tag{5.4}
\]

But Lemma 5.1 gives

\[
\dim Z_{n-2}=4n-4.
\]

Hence inclusion plus dimension equality gives the correction-surjectivity
statement

\[
\boxed{
B_{n,n-1}(C_n)=Z_{n-2}.
}
\tag{5.5}
\]

Representation-theoretically, (5.5) is the quotient

\[
\boxed{
\frac{V_{n-1}\otimes V_1}{V_n}
\cong
V_{n-2}\oplus V_{n-1},
}
\tag{5.6}
\]

which agrees with (5.1) for \(m=n-2\).

---

## 6. Completion of the induction

The base \(n=2\) is the onto reversed quaternion product

\[
B_{2,1}:V\otimes V\twoheadrightarrow\mathbb H.
\]

Assume pairwise descent at length \(n-1\) and take a compatible length-\(n\)
boundary. Section 1 constructs \(T\in V^{\otimes n}\) filling its first
\(n-2\) faces and leaves a last-face residual

\[
G\in Z_{n-2}.
\]

By (5.5), choose

\[
U\in C_n
\]

with

\[
B_{n,n-1}(U)=G.
\]

Since \(U\in C_n\), adding \(U\) changes none of the first \(n-2\) faces.
By the definition of \(G\), it corrects the last face exactly. Thus

\[
\mathbf B_n(T+U)=(F_1,\ldots,F_{n-1}).
\]

Every pairwise-compatible boundary is globally fillable, so

\[
\ker\partial_n\subseteq\operatorname{im}\mathbf B_n.
\]

The reverse inclusion is (0.3). This proves Theorem 0.1 for every finite
\(n\). ∎

---

## 7. Universal ranks and the first syzygy law

Theorem 0.1 and Note 09 give

\[
\boxed{
\dim\ker\partial_n
=
3^n-(2n+1).
}
\tag{7.1}
\]

Since

\[
\dim\mathcal R_{n-2}^{\oplus(n-1)}
=
4(n-1)3^{n-2},
\]

the matching rank is

\[
\boxed{
\operatorname{rank}\partial_n
=
4(n-1)3^{n-2}-3^n+(2n+1)
=
(4n-13)3^{n-2}+(2n+1).
}
\tag{7.2}
\]

For \(n\ge3\), the target dimension is

\[
4\binom{n-1}{2}3^{n-3}.
\]

Therefore

\[
\boxed{
\dim\mathfrak S_n
=
(2n^2-18n+43)3^{n-3}-(2n+1).
}
\tag{7.3}
\]

At the level of \(SO(3)\)-characters,

\[
\boxed{
[\mathfrak S_n]
=
\binom{n-1}{2}[\mathcal R_{n-3}]
-(n-1)[\mathcal R_{n-2}]
+[V^{\otimes n}]-[V_n].
}
\tag{7.4}
\]

This is now a theorem, not a character predicted under an exactness
assumption.

The first cases are:

| \(n\) | simplex | \(\dim C_n^0\) | \(\operatorname{rank}\partial_n\) | compatible boundary | \(\dim\mathfrak S_n\) |
|---:|---|---:|---:|---:|---:|
| 3 | edge | 24 | 4 | 20 | 0 |
| 4 | triangle | 108 | 36 | 72 | 0 |
| 5 | tetrahedron | 432 | 200 | 232 | 16 |
| 6 | 4-simplex | 1620 | 904 | 716 | 176 |
| 7 | 5-simplex | 5832 | 3660 | 2172 | 1200 |

For \(n=7\), (7.4) gives

\[
\boxed{
\mathfrak S_7
\cong
45V_0\oplus100V_1\oplus90V_2
\oplus45V_3\oplus10V_4.
}
\tag{7.5}
\]

Its dimension is \(1200\). No \(2187\)-column rank computation is required:
the value follows from the all-length descent theorem.

---

## 8. What has and has not generalized

Notes 07, 10, and 11 established pairwise terminal descent for a response
triangle, tetrahedron, and 4-simplex. Before this note there were two live
possibilities:

1. pairwise compatibility remains sufficient at every length;
2. a first higher gluing obstruction appears at some later \(n\).

Theorem 0.1 eliminates the second possibility at the first descent level:

\[
\boxed{
\frac{\ker\partial_n}{\operatorname{im}\mathbf B_n}=0
\qquad\text{for every }n.
}
\tag{8.1}
\]

The mechanism is not a lucky rank identity. It is the conjunction of three
length-independent local facts:

- the decoder slide (3.1);
- the Cartan kernel \(V_m\oplus V_{m+1}\);
- the adjacent-pair highest-spin kernel of Note 09.

The rapidly growing cokernel \(\mathfrak S_n\) remains. It measures linear
dependencies among pairwise matching defects, not a failure of pairwise
gluing. The next algebraic problem is to construct a local map

\[
\partial_n^{(2)}:C_n^1\longrightarrow C_n^2
\]

whose kernel or image realizes this universal syzygy module and begins a
higher response-simplex complex.

This note also does not turn \(\mathfrak S_n\), \(Z_m\), or the terminal
highest-spin sector into curvature. Curvature still requires transport,
path comparison, naturality under coordinate changes, and a nonconfluence
theorem. The present result supplies a rigid exact descent complex on which
such a construction can be tested.

---

## 9. Exact certificate

Run

```bash
python3 certificates/all_n_pairwise_terminal_descent_certificate.py
```

from `research/depth-generated-geometry/`.

The certificate uses only Python's standard library and exact
`fractions.Fraction` arithmetic. It verifies:

- the quaternion slide identity (3.1) on the full basis;
- \(\Psi^2+\Psi-2I=0\) and \(\det\Psi=16\);
- \(\kappa^2-\kappa-2I=0\) and \(\det\kappa=16\);
- equality of every actual-deletion and simple-contraction suffix row space
  for \(m=1,2,3,4\);
- \(\dim K_m=4(m+1)\) for \(m=1,2,3,4\);
- that the contraction equations force input STF symmetry;
- that the explicit formula (4.9) is a section landing in \(K_m\);
- that \(S^{m+1}_0V\) is the zero-scalar kernel.

The \(m=4\) line is the local model underlying the previously certified
\(n=6\) 4-simplex. The certificate checks fixed finite algebra used in the
proof; the all-\(m\) conclusion itself is the symbolic argument of Sections
3 and 4.

Expected final line:

```text
ALL CHECKS PASSED
```

An auxiliary first-unseen-rung stress check is available as

```bash
python3 certificates/n7_local_descent_modular_stress.py
```

It compares the full actual, simple, and joined row spaces at \(m=5\) over
\(\mathbb F_{1009}\) and \(\mathbb F_{1013}\). All three ranks are \(948\),
so the common kernel has dimension \(972-948=24=4(m+1)\). This modular check
is not used to prove the all-\(m\) theorem.

---

## 10. Next target

**Retrospective after Note 13.** The abstract second map requested below has
now been constructed from four-face local cokernels. It satisfies

\[
\partial_n^{(2)}\partial_n=0
\]

for every \(n\ge5\), and middle exactness is established at \(n=5\) over
\(\mathbb Q\) and checked at \(n=6,7\) over two prime fields. The remaining
target is no longer the existence of a second map, but its short local
quaternionic formula and the all-\(n\) exactness proof.

The all-length question is no longer whether a larger isolated simplex still
glues. It does.

The next structural target is the second response-simplex differential:

\[
C_n^0\xrightarrow{\partial_n}C_n^1
\xrightarrow{\partial_n^{(2)}}C_n^2,
\]

with a local formula explaining the modules \(\mathfrak S_n\) rather than
defining them only as cokernels. The \(16\)- and \(176\)-dimensional cases
then become the first two finite models of one higher compatibility law.

In parallel, the canonical Casimir section of Note 09 still lacks a short
response-side local expression. Only after these algebraic transports are
explicit should path nonconfluence and curvature be introduced.
