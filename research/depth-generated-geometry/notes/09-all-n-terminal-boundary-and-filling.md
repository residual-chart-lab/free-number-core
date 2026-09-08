# Note 09 — All-\(n\) Terminal Boundary and Canonical Filling

## adjacent-pair kernel が最高スピンだけを terminal birth として残す

**Status:** theorem for every finite \(n\ge2\); exact rational checks through \(n=5\)  
**Depends on:** Notes 01–03 and 08; the left and right local decoders of Note 07; Free Numbers Core v1, Notes 06 and 11  
**Claim boundary:** this note proves the all-length terminal transition. It does not classify the intermediate-depth multiplicity filtration or identify the terminal interior with curvature. The intrinsic compatibility equations left open here are supplied by Note 12.

---

## 0. Main result

Let the internal gaps of a length-\(n\) word be

\[
\{1,\ldots,n-1\}.
\]

For each \(r\), let

\[
B_{n,r}:
V^{\otimes n}
\longrightarrow
\operatorname{Hom}(V^{\otimes(n-2)},\mathbb H)
\]

be the exact-depth-\((n-2)\) response obtained by probing every internal gap
except \(r\). Collect the \(n-1\) codimension-one faces:

\[
\boxed{
\mathbf B_n
:=
\bigoplus_{r=1}^{n-1}B_{n,r}.
}
\tag{0.1}
\]

Then, for every \(n\ge2\),

\[
\boxed{
\ker\mathbf B_n=S^n_0V\cong V_n.
}
\tag{0.2}
\]

Thus exact-depth-\((n-2)\) boundary data alone sees every state direction
except the highest-spin symmetric trace-free component.

Consequently,

\[
\boxed{
\operatorname{rank}\mathbf B_n
=
3^n-(2n+1).
}
\tag{0.3}
\]

The full probe-depth filtration therefore satisfies the all-length
last-survivor equality

\[
\boxed{
F_{n-2}^{(n)}
:=
\ker D_n^{\le n-2}
=
S^n_0V.
}
\tag{0.4}
\]

On the intrinsic response side,

\[
\boxed{
\widehat F_{n-2}^{(n)}
=
A_n(S^n_0V)
=:
\mathfrak H_n.
}
\tag{0.5}
\]

At terminal depth \(n-1\), this entire remaining space is detected by

\[
\boxed{
A_n(S)=(-2)^{n-1}C_S.
}
\tag{0.6}
\]

Hence the terminal birth has the universal dimension and principal symbol

\[
\boxed{
h_n(n-1)=2n+1,
\qquad
\sigma_{n-1}^{\mathrm{depth}}=(-2)^{n-1}C.
}
\tag{0.7}
\]

This closes the all-length last-survivor conjecture.

---

## 1. The codimension-one terminal faces

Write a pure word as

\[
T=a_1|\cdots|a_n.
\]

The terminal all-gap response is

\[
A_n(T)(x_1,\ldots,x_{n-1})
=
a_nx_{n-1}a_{n-1}\cdots x_1a_1.
\]

Fix a gap \(r\). Probe every gap except \(r\). The resulting face is

\[
\boxed{
\begin{aligned}
B_{n,r}(T)
\bigl((x_s)_{s\ne r}\bigr)
={}&
a_nx_{n-1}a_{n-1}\cdots
a_{r+2}x_{r+1}\\
&\cdot
(a_{r+1}a_r)
\cdot
x_{r-1}a_{r-1}\cdots x_1a_1.
\end{aligned}
}
\tag{1.1}
\]

At the omitted gap, the two adjacent \(V\)-factors meet directly through
reversed quaternion multiplication.

For \(n=2\), there is one omitted gap and no probes. Then

\[
B_{2,1}=m_2,
\]

so the theorem begins with the established identity

\[
\ker m_2=S^2_0V.
\]

---

## 2. Adjacent collapse followed by an invertible encoder

Define the reversed pair product

\[
\mu:V\otimes V\longrightarrow\mathbb H,
\qquad
\mu(u\otimes v):=vu.
\tag{2.1}
\]

At gap \(r\), define the adjacent collapse

\[
\boxed{
c_{n,r}
:=
\operatorname{id}^{\otimes(r-1)}
\otimes\mu
\otimes
\operatorname{id}^{\otimes(n-r-1)}.
}
\tag{2.2}
\]

Its target is

\[
W_{n,r}
:=
V^{\otimes(r-1)}
\otimes\mathbb H
\otimes
V^{\otimes(n-r-1)},
\]

whose dimension is

\[
\dim W_{n,r}=4\cdot3^{n-2}.
\]

Define

\[
\mathcal E_{n,r}:
W_{n,r}
\longrightarrow
\operatorname{Hom}(V^{\otimes(n-2)},\mathbb H)
\]

on pure tensors by inserting the \(n-2\) probe variables between all
remaining factors, with the central quaternion occupying the omitted pair.
Equation (1.1) says exactly

\[
\boxed{
B_{n,r}=\mathcal E_{n,r}\circ c_{n,r}.
}
\tag{2.3}
\]

### Lemma 2.1 — two-sided encoder isomorphism

For every \(n\ge2\) and every \(1\le r\le n-1\),

\[
\boxed{
\mathcal E_{n,r}:
W_{n,r}
\xrightarrow{\ \cong\ }
\operatorname{Hom}(V^{\otimes(n-2)},\mathbb H)
}
\tag{2.4}
\]

is an isomorphism.

### Proof

Use the two local isomorphisms of Note 07:

\[
\Theta_R:
\mathbb H\otimes V
\longrightarrow
\operatorname{Hom}(V,\mathbb H),
\qquad
\Theta_R(h\otimes v)(x)=hxv,
\]

and

\[
\Theta_L:
V\otimes\mathbb H
\longrightarrow
\operatorname{Hom}(V,\mathbb H),
\qquad
\Theta_L(v\otimes h)(x)=vxh.
\]

Apply their inverses pointwise in the other probe variables.

If a \(V\)-factor remains to the right of the central \(\mathbb H\), regard
the response as a function of the rightmost probe variable and apply
\(\Theta_R^{-1}\). This peels off one right factor. Repeat until the central
\(\mathbb H\) reaches the right boundary.

Then regard the response as a function of the leftmost remaining probe and
apply \(\Theta_L^{-1}\). This peels off one left factor. Repeat until only the
central quaternion remains.

The finite decoder sequence recovers every tensor in \(W_{n,r}\) uniquely.
Thus \(\mathcal E_{n,r}\) is invertible. ∎

### Corollary 2.2

Every individual terminal boundary face is onto:

\[
\boxed{
\operatorname{rank}B_{n,r}
=
4\cdot3^{n-2}.
}
\tag{2.5}
\]

Moreover,

\[
\boxed{
\ker B_{n,r}=\ker c_{n,r}.
}
\tag{2.6}
\]

The response wrapper changes coordinates but does not change the adjacent
collapse kernel.

---

## 3. The local pair kernel

For \(u,v\in V=\operatorname{Im}\mathbb H\),

\[
vu=-\langle v,u\rangle+v\times u.
\tag{3.1}
\]

The scalar part records the trace component, while the imaginary part records
the antisymmetric component. Since

\[
\Lambda^2V\xrightarrow{\ \times\ }V
\]

is an isomorphism in dimension three, Note 01 gives

\[
\boxed{
\ker\mu=S^2_0V.
}
\tag{3.2}
\]

Therefore

\[
\boxed{
\ker B_{n,r}
=
V^{\otimes(r-1)}
\otimes S^2_0V
\otimes V^{\otimes(n-r-1)}.
}
\tag{3.3}
\]

An exact-depth-\((n-2)\) face misses precisely the component in which its one
unprobed adjacent pair is symmetric and trace-free.

---

## 4. The adjacent-pair intersection theorem

### Theorem 4.1

For every \(n\ge2\),

\[
\boxed{
\bigcap_{r=1}^{n-1}
\left(
V^{\otimes(r-1)}
\otimes S^2_0V
\otimes V^{\otimes(n-r-1)}
\right)
=
S^n_0V.
}
\tag{4.1}
\]

### Proof

Let \(T\) lie in the intersection on the left.

For every adjacent pair \((r,r+1)\), membership in \(S^2_0V\) says two things:

1. \(T\) is invariant under the adjacent transposition \(\tau_r\);
2. the contraction of slots \(r,r+1\) vanishes.

The adjacent transpositions

\[
\tau_1,\ldots,\tau_{n-1}
\]

generate the full symmetric group \(S_n\). Hence \(T\) is invariant under
every permutation of its tensor slots:

\[
T\in S^nV.
\]

Because \(T\) is fully symmetric, the trace of any pair of slots is a
permutation of an adjacent trace. Every adjacent trace is zero, so every
pairwise trace is zero. Thus

\[
T\in S^n_0V.
\]

Conversely, a symmetric trace-free tensor is symmetric and trace-free on each
adjacent pair, so it belongs to every factor on the left of (4.1). ∎

Combining (2.6), (3.3), and Theorem 4.1 gives

\[
\ker\mathbf B_n
=
\bigcap_{r=1}^{n-1}\ker B_{n,r}
=
S^n_0V,
\]

which proves (0.2).

---

## 5. The all-length last-survivor theorem

The full depth-\((n-2)\) profile contains every component of \(\mathbf B_n\).
Therefore

\[
F_{n-2}^{(n)}
=
\ker D_n^{\le n-2}
\subseteq
\ker\mathbf B_n
=
S^n_0V.
\tag{5.1}
\]

On the other hand, every response target at depth \(d\le n-2\) has highest
possible spin \(V_{d+1}\), hence at most \(V_{n-1}\). The response maps are
\(SO(3)\)-equivariant, so the source top spin \(V_n=S^n_0V\) maps to zero:

\[
S^n_0V\subseteq F_{n-2}^{(n)}.
\tag{5.2}
\]

Equations (5.1) and (5.2) prove:

### Theorem 5.1 — all-\(n\) last survivor

\[
\boxed{
F_{n-2}^{(n)}=S^n_0V
\qquad(n\ge2).
}
\tag{5.3}
\]

Transporting through the terminal representation theorem gives

\[
\boxed{
\widehat F_{n-2}^{(n)}
=
A_n(S^n_0V)
=
\mathfrak H_n.
}
\tag{5.4}
\]

Thus the highest spin is not merely one subspace contained in the terminal
birth. It is the entire last-surviving subspace for every finite length.

---

## 6. Exact-depth boundary already determines the penultimate space

Define the terminal boundary image

\[
\boxed{
\mathcal P_{n,n-2}
:=
\operatorname{im}\mathbf B_n.
}
\tag{6.1}
\]

Since

\[
\dim S^n_0V=2n+1,
\]

Theorem 5.1 gives

\[
\boxed{
\dim\mathcal P_{n,n-2}
=
3^n-(2n+1).
}
\tag{6.2}
\]

Projection of the full depth-\((n-2)\) profile onto its exact-depth faces
induces

\[
\mathcal Q_{n,n-2}\longrightarrow\mathcal P_{n,n-2}.
\]

Both spaces are images of \(V^{\otimes n}\), and both defining maps have the
same kernel \(S^n_0V\). Hence:

### Corollary 6.1 — penultimate boundary sufficiency

\[
\boxed{
\mathcal Q_{n,n-2}
\xrightarrow{\ \cong\ }
\mathcal P_{n,n-2}.
}
\tag{6.3}
\]

Thus all shallower information is determined by the collection of
codimension-one terminal faces, even before explicit all-\(n\) boundary
formulas are written down.

This is a separation and reconstruction statement. It is not yet an intrinsic
generators-and-relations presentation of \(\mathcal P_{n,n-2}\).

---

## 7. Universal terminal dimension law

The penultimate visible dimension and the final birth dimension are now known
for every length:

\[
\boxed{
N_n(n-2)=3^n-(2n+1),
}
\tag{7.1}
\]

\[
\boxed{
N_n(n-1)=3^n,
}
\tag{7.2}
\]

\[
\boxed{
h_n(n-1)=2n+1.
}
\tag{7.3}
\]

The first four rungs are

| \(n\) | penultimate depth | \(N_n(n-2)\) | terminal birth | terminal total |
|---:|---:|---:|---:|---:|
| 2 | 0 | 4 | 5 | 9 |
| 3 | 1 | 20 | 7 | 27 |
| 4 | 2 | 72 | 9 | 81 |
| 5 | 3 | 232 | 11 | 243 |

The \(n=5\) line is the first new exact rung beyond the previous certificates.
Its terminal coefficient is

\[
\boxed{
A_5(S)=16C_S
\qquad(S\in S^5_0V).
}
\tag{7.4}
\]

---

## 8. All-\(n\) canonical terminal filling

The terminal boundary map gives the exact sequence

\[
\boxed{
0\longrightarrow S^n_0V
\longrightarrow V^{\otimes n}
\xrightarrow{\ \mathbf B_n\ }
\mathcal P_{n,n-2}
\longrightarrow0.
}
\tag{8.1}
\]

Let \(\Omega\) be the Casimir with convention

\[
\Omega|_{V_j}=-j(j+1)\operatorname{id}.
\]

The unique top-spin \(V_n=S^n_0V\) has spectral projector

\[
\boxed{
P_n
=
\frac{(-1)^n}{(2n)!}
\prod_{j=0}^{n-1}
\bigl(\Omega+j(j+1)\operatorname{id}\bigr).
}
\tag{8.2}
\]

Indeed, on \(V_n\) the product in the numerator is

\[
\prod_{j=0}^{n-1}
\bigl(j(j+1)-n(n+1)\bigr)
=
(-1)^n(2n)!,
\]

while on every lower spin it vanishes.

Define

\[
W_{<n}:=\ker P_n=\operatorname{im}(1-P_n).
\]

Then

\[
V^{\otimes n}=W_{<n}\oplus S^n_0V.
\]

Since \(\ker\mathbf B_n=S^n_0V\), restriction gives an isomorphism

\[
\boxed{
\mathbf B_n|_{W_{<n}}:
W_{<n}
\xrightarrow{\ \cong\ }
\mathcal P_{n,n-2}.
}
\tag{8.3}
\]

### Theorem 8.1 — all-\(n\) canonical terminal filling

For every \(n\ge2\), the terminal boundary map has the canonical section

\[
\boxed{
s_{n,\mathrm{tf}}
:=
\left(\mathbf B_n|_{W_{<n}}\right)^{-1}.
}
\tag{8.4}
\]

It is the unique \(SO(3)\)-equivariant section of \(\mathbf B_n\).

### Proof of uniqueness

The quotient \(\mathcal P_{n,n-2}\) contains no \(V_n\), while

\[
\ker\mathbf B_n\cong V_n.
\]

The difference of two equivariant sections would belong to

\[
\operatorname{Hom}_{SO(3)}
(\mathcal P_{n,n-2},V_n)=0.
\]

Hence the sections coincide. ∎

For any terminal boundary \(p\), every filler has the unique state-side form

\[
\boxed{
T=s_{n,\mathrm{tf}}(p)+S,
\qquad
S\in S^n_0V.
}
\tag{8.5}
\]

---

## 9. Intrinsic response-side normal form

Let

\[
A_n:V^{\otimes n}\xrightarrow{\ \cong\ }\mathfrak Q_n,
\qquad
\Psi_n=A_n^{-1}.
\]

Define

\[
\Phi_n:=\mathbf B_n\Psi_n:
\mathfrak Q_n\longrightarrow\mathcal P_{n,n-2}
\]

and

\[
\widehat P_n:=A_nP_n\Psi_n.
\]

Equivalently, if \(\widehat\Omega_n\) is the Casimir of the natural \(SO(3)\)
action on \(\mathfrak Q_n\), then

\[
\boxed{
\widehat P_n
=
\frac{(-1)^n}{(2n)!}
\prod_{j=0}^{n-1}
\bigl(
\widehat\Omega_n+j(j+1)\operatorname{id}
\bigr).
}
\]

Thus the top-spin removal is intrinsic to the terminal response
representation and does not require an arbitrary state-space complement.

Then

\[
\boxed{
\mathfrak Q_n
=
\ker\widehat P_n
\oplus
\mathfrak H_n,
}
\tag{9.1}
\]

and

\[
\boxed{
\Phi_n|_{\ker\widehat P_n}:
\ker\widehat P_n
\xrightarrow{\ \cong\ }
\mathcal P_{n,n-2}.
}
\tag{9.2}
\]

The unique equivariant response-side filler is

\[
\boxed{
s_{n,\mathrm{tf}}^{\mathrm{resp}}
:=
A_ns_{n,\mathrm{tf}}
=
\left(
\Phi_n|_{\ker\widehat P_n}
\right)^{-1}.
}
\tag{9.3}
\]

Using the vertical-response theorem, every terminal response has the unique
normal form

\[
\boxed{
F
=
s_{n,\mathrm{tf}}^{\mathrm{resp}}(p)
+
(-2)^{n-1}C_S,
\qquad
S\in S^n_0V.
}
\tag{9.4}
\]

Thus the \(n=4\) formula

\[
F=F_{\mathrm{tf}}(p)-8C_S
\]

is one rung of a universal terminal filling law.

---

## 10. The all-length fourfold identification

For every finite \(n\ge2\), the following four descriptions are canonically
identified:

\[
\boxed{
\begin{aligned}
S^n_0V\cong V_n
&\quad\text{(highest spin)},\\
\ker\mathbf B_n
&\quad\text{(codimension-one boundary kernel)},\\
K_{n,n-1}^{\mathrm{birth}}
&\quad\text{(terminal birth)},\\
\mathfrak H_n=A_n(S^n_0V)
&\quad\text{(pure terminal interior response)}.
\end{aligned}
}
\tag{10.1}
\]

In abbreviated form,

\[
\boxed{
\text{highest spin}
\simeq
\text{terminal boundary kernel}
\simeq
\text{next birth}
\simeq
\text{pure terminal interior}.
}
\tag{10.2}
\]

The equality first isolated at \(n=4\) is therefore not a low-length
coincidence.

---

## 11. What this theorem changes

Before this note, the all-\(n\) statement was:

\[
S^n_0V
\hookrightarrow
K_{n,n-1}^{\mathrm{birth}},
\]

with equality exact-checked only for \(n=2,3,4\).

The adjacent-pair theorem upgrades the inclusion to

\[
\boxed{
S^n_0V
=
K_{n,n-1}^{\mathrm{birth}}
\qquad\text{for every }n\ge2.
}
\]

Consequently, the conditional all-length filling result of Note 08 is now
unconditional.

The remaining all-length difficulty has moved one level earlier. It is no
longer the terminal transition, but the intermediate filtration

\[
\text{spin}\times\text{multiplicity}\times\text{probe depth}
\]

for \(d<n-2\).

### 11.1 Why the argument stops exactly here

The terminal boundary is special. At exact depth \(n-2\), precisely one gap
is unprobed. Hence there is precisely one length-two quaternion block, while
every other surviving factor remains a singleton \(V\). The collapsed
coordinate space has dimension

\[
4\cdot3^{n-2},
\]

exactly equal to the response target, and the two-sided local encoder is
invertible.

At a shallower depth, several gaps are unprobed. They may form several blocks
or longer blocks. Replacing those blocks by quaternion products produces
multiple \(\mathbb H\)-factors, and the resulting block encoder is generally
no longer injective. The simple adjacent-pair intersection argument therefore
does not classify the intermediate layers.

This identifies the next obstruction precisely: it lies in syzygies among
multiple block compressions and in their \(SO(3)\) multiplicity spaces, not in
the terminal highest-spin sector.

---

## 12. Exact certificate

Run

    python3 certificates/all_n_terminal_boundary_certificate.py

from the research/depth-generated-geometry directory.

The certificate uses only Python's standard library and exact
fractions.Fraction arithmetic. It verifies for \(n=2,3,4,5\):

- surjectivity and rank \(4\cdot3^{n-2}\) of every individual terminal face;
- equality of each face kernel with its adjacent quaternion-collapse kernel;
- joint rank \(3^n-(2n+1)\);
- equality of the common face kernel with \(S^n_0V\) as an exact subspace;
- the new \(n=5\) terminal dimension \(11\);
- injectivity of \(C\) on \(S^5_0V\);
- the signed coefficient \(A_5=16C\).

Expected final line:

    ALL CHECKS PASSED

---

## 13. Remaining problems

This theorem closes:

- the all-\(n\) terminal last-survivor equality;
- the universal penultimate dimension formula;
- canonical \(SO(3)\)-equivariant terminal filling;
- the all-length fourfold identification.

Note 12 subsequently closes the intrinsic generators-and-relations problem
for \(\mathcal P_{n,n-2}\) at every length by proving
\(\mathcal P_{n,n-2}=\ker\partial_n\).

The remaining open problems are:

- short local formulas for the canonical filler itself;
- a local higher differential generating the universal compatibility
  syzygy after \(\partial_n\);
- the full intermediate multiplicity-depth filtration;
- transport, path nonconfluence, holonomy, and curvature.

In particular, the terminal interior sector is now canonical at every finite
length, but it is still not a curvature sector without an additional
path-comparison theorem.
