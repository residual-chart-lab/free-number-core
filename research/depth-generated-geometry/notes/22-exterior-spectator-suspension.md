# Note 22 — Exterior Spectator Suspension and Flatness

## adding probes outside a tetrahedral support tensorizes the complete decorated quotient

**Status:** theorem over \(\mathbb Q\) (and hence over \(\mathbb R\)) for
every \(n\ge5\), with an exact finite certificate of the defining identities

**Depends on:** Notes 12–15, 19, and 21

**Claim boundary:** this note proves a functorial transport law for
spectators inserted strictly to the left or right of an existing ordered
gap system. It transports the quotient and every labelled edge image, and
the left/right exterior insertions commute exactly. It does not describe an
insertion between two vertices of the tetrahedral support, classify all
internal spectator placements, or identify any residual with curvature.

---

## 0. Result in one line

Let

\[
G_n=\{1,\ldots,n-1\},
\qquad
Q=\{q_1<q_2<q_3<q_4\}\subset G_n.
\tag{0.1}
\]

There are two exterior suspensions.

- A new leftmost gap sends

  \[
  Q\longmapsto Q^-:=Q+1
  =\{q_1+1,\ldots,q_4+1\}\subset G_{n+1}.
  \tag{0.2}
  \]

- A new rightmost gap sends

  \[
  Q\longmapsto Q^+:=Q
  \subset G_{n+1}.
  \tag{0.3}
  \]

In both cases the new gap is a spectator: it is probed in every face and
every edge response of the local tetrahedral complex.

The full decorated quotients satisfy canonical decoder-normalized
isomorphisms

\[
\boxed{
\mathscr Y_{n+1,Q^-}
\cong
\mathscr Y_{n,Q}\otimes V,
}
\tag{0.4}
\]

and

\[
\boxed{
\mathscr Y_{n+1,Q^+}
\cong
V\otimes\mathscr Y_{n,Q}.
}
\tag{0.5}
\]

Here an isomorphism of decorated quotients means not only
\(Y_{n+1,Q^\pm}\cong Y_{n,Q}\otimes V\), but also

\[
\boxed{
E_{ab}^{(n+1,Q^-)}
\cong E_{ab}^{(n,Q)}\otimes V,
\qquad
E_{ab}^{(n+1,Q^+)}
\cong V\otimes E_{ab}^{(n,Q)}
}
\tag{0.6}
\]

for all six labelled edges.

Moreover, one left and one right suspension commute exactly. Consequently,
if \(a,b\ge0\), then

\[
\boxed{
\mathscr Y_{n+a+b,Q+a}
\cong
V^{\otimes b}\otimes
\mathscr Y_{n,Q}\otimes
V^{\otimes a},
}
\tag{0.7}
\]

where the \(a\) new gaps lie to the left of the old system and the \(b\)
new gaps lie to its right.

Thus exterior spectators do not create a twist. They propagate every
existing core, residual, sum, and intersection by ordinary tensor product.

---

## 1. The two one-step suspension maps

Write

\[
\mathcal R_m:=\operatorname{Hom}_{\mathbb R}
(V^{\otimes m},\mathbb H).
\tag{1.1}
\]

The right local decoder of Notes 07 and 12 gives an isomorphism

\[
J_m^R:
\mathbb H\otimes V^{\otimes m}
\xrightarrow{\sim}
\mathcal R_m
\tag{1.2}
\]

with

\[
J_m^R(h;v_1,\ldots,v_m)(x_1,\ldots,x_m)
=
h\,x_m v_m\cdots x_1v_1.
\tag{1.3}
\]

For \(F\in\mathcal R_m\), \(w\in V\), and a new leftmost probe \(z\in V\),
define

\[
\boxed{
\Sigma_m^-(F\otimes w)(z,x_1,\ldots,x_m)
:=
F(x_1,\ldots,x_m)\,z\,w.
}
\tag{1.4}
\]

Pointwise in the old variables, this is the right one-variable encoder

\[
\Theta_R:
\mathbb H\otimes V\longrightarrow\operatorname{Hom}(V,\mathbb H),
\qquad
\Theta_R(h\otimes w)(z)=hzw.
\tag{1.5}
\]

It is invertible, so

\[
\boxed{
\Sigma_m^-:
\mathcal R_m\otimes V\xrightarrow{\sim}\mathcal R_{m+1}.
}
\tag{1.6}
\]

Equivalently,

\[
\Sigma_m^-\!\left(
J_m^R(h;v_1,\ldots,v_m)\otimes w
\right)
=
J_{m+1}^R(h;w,v_1,\ldots,v_m).
\tag{1.7}
\]

There is a left-handed mirror. The local encoder

\[
\Theta_L:
V\otimes\mathbb H\longrightarrow\operatorname{Hom}(V,\mathbb H),
\qquad
\Theta_L(w\otimes h)(z)=wzh
\tag{1.8}
\]

is also an isomorphism. Define

\[
\boxed{
\Sigma_m^+(w\otimes F)(x_1,\ldots,x_m,z)
:=
w\,z\,F(x_1,\ldots,x_m).
}
\tag{1.9}
\]

Then

\[
\boxed{
\Sigma_m^+:
V\otimes\mathcal R_m\xrightarrow{\sim}\mathcal R_{m+1}.
}
\tag{1.10}
\]

No quotient basis or finite-rank calculation enters these definitions.
They are iterated forms of the two local quaternionic decoders already used
by the response theory.

---

## 2. Exterior suspension commutes with every old restriction

Let

\[
A_{n,S}:V^{\otimes n}\longrightarrow
\mathcal R_{n-1-|S|}
\tag{2.1}
\]

be the exact response with the gaps in \(S\subseteq G_n\) omitted. For a
face \(S=\{r\}\) and an edge \(S=\{r,s\}\), the intrinsic restriction

\[
\rho_{r\to rs}:
\mathcal R_{n-2}\longrightarrow\mathcal R_{n-3}
\tag{2.2}
\]

is characterized by

\[
\rho_{r\to rs}A_{n,\{r\}}=A_{n,\{r,s\}}.
\tag{2.3}
\]

The face response is onto, so (2.3) determines the restriction uniquely.

Take a pure state

\[
T=v_1\otimes\cdots\otimes v_n.
\tag{2.4}
\]

Prepend \(w\in V\). Every old gap moves one step to the right, and the new
leftmost probe-coefficient pair is the final factor \(zw\) in the reversed
quaternion product. Hence

\[
\boxed{
A_{n+1,S+1}(w\otimes T)
=
\Sigma_{n-1-|S|}^-
\left(A_{n,S}(T)\otimes w\right).
}
\tag{2.5}
\]

Apply (2.5) first to a face and then to its edge shadow. Equation (2.3)
and surjectivity give

\[
\boxed{
\rho_{r+1\to(r+1)(s+1)}\Sigma_{n-2}^-
=
\Sigma_{n-3}^-
\left(\rho_{r\to rs}\otimes\operatorname{id}_V\right).
}
\tag{2.6}
\]

Appending \(w\) places the new rightmost pair \(wz\) at the beginning of
the reversed product:

\[
\boxed{
A_{n+1,S}(T\otimes w)
=
\Sigma_{n-1-|S|}^+
\left(w\otimes A_{n,S}(T)\right).
}
\tag{2.7}
\]

Therefore

\[
\boxed{
\rho_{r\to rs}\Sigma_{n-2}^+
=
\Sigma_{n-3}^+
\left(\operatorname{id}_V\otimes\rho_{r\to rs}\right).
}
\tag{2.8}
\]

Equations (2.6) and (2.8) are the whole mechanism. An exterior insertion
adds the same local decoder to every face and every edge, so it cannot
change their matching pattern.

---

## 3. Tensorization of the local complex

Recall

\[
C^0_{n,Q}=\mathcal R_{n-2}^{\oplus4},
\qquad
C^1_{n,Q}=\mathcal R_{n-3}^{\oplus6}.
\tag{3.1}
\]

The local matching map is assembled from the restrictions (2.2) with
ordered incidence signs. Since \(q\mapsto q+1\) preserves vertex order,
(2.6) gives

\[
\begin{array}{ccc}
C^0_{n,Q}\otimes V
&\xrightarrow{\ \partial_{n,Q}\otimes\operatorname{id}_V\ }&
C^1_{n,Q}\otimes V\\[2mm]
\Big\downarrow{\scriptstyle\oplus\,\Sigma_{n-2}^-}
&&
\Big\downarrow{\scriptstyle\oplus\,\Sigma_{n-3}^-}\\[2mm]
C^0_{n+1,Q^-}
&\xrightarrow{\ \partial_{n+1,Q^-}\ }&
C^1_{n+1,Q^-}.
\end{array}
\tag{3.2}
\]

The right-handed diagram obtained from (2.8) is

\[
\begin{array}{ccc}
V\otimes C^0_{n,Q}
&\xrightarrow{\ \operatorname{id}_V\otimes\partial_{n,Q}\ }&
V\otimes C^1_{n,Q}\\[2mm]
\Big\downarrow{\scriptstyle\oplus\,\Sigma_{n-2}^+}
&&
\Big\downarrow{\scriptstyle\oplus\,\Sigma_{n-3}^+}\\[2mm]
C^0_{n+1,Q^+}
&\xrightarrow{\ \partial_{n+1,Q^+}\ }&
C^1_{n+1,Q^+}.
\end{array}
\tag{3.3}
\]

All spaces are over a field, so tensor product is exact. Taking cokernels
proves (0.4) and (0.5). In decoder-normalized coordinates, the whole local
presentation is transported:

\[
\boxed{
\partial_{n+1,Q^-}
\sim
\partial_{n,Q}\otimes\operatorname{id}_V,
\qquad
\partial_{n+1,Q^+}
\sim
\operatorname{id}_V\otimes\partial_{n,Q}.
}
\tag{3.4}
\]

This is stronger than a dimension recurrence.

---

## 4. The decorated quotient is preserved

Let

\[
\iota_{ab}:\mathcal R_{n-3}\longrightarrow C^1_{n,Q}
\tag{4.1}
\]

be the inclusion of the edge \(ab\). The vertical maps in (3.2) and (3.3)
are block diagonal and use the same suspension on every edge block. They
therefore intertwine every \(\iota_{ab}\), proving (0.6).

More generally, let \(\mathcal L_I\) be any subspace obtained from labelled
edge images by sums and intersections. Then

\[
\mathcal L_I^{(n+1,Q^-)}
\cong
\mathcal L_I^{(n,Q)}\otimes V,
\qquad
\mathcal L_I^{(n+1,Q^+)}
\cong
V\otimes\mathcal L_I^{(n,Q)}.
\tag{4.2}
\]

Thus the complete incidence lattice, not only six individual ranks, is
propagated. In particular,

\[
\boxed{
\dim Y_{n+1,Q^\pm}=3\dim Y_{n,Q},
\qquad
\dim E_{ab}^{(n+1,Q^\pm)}
=3\dim E_{ab}^{(n,Q)}.
}
\tag{4.3}
\]

The \(SO(3)\)-character is multiplied by the vector character \([V_1]\).
Exterior suspension preserves placement memory while adding one ordinary
vector factor.

---

## 5. Exterior left and right insertions are strictly flat

Take \(u,w,z_+,z_-\in V\) and \(F\in\mathcal R_m\). Suspending first on
the left and then on the right gives

\[
u z_+\,F(x_1,\ldots,x_m)\,z_-w.
\tag{5.1}
\]

Suspending in the opposite order gives the same expression. Therefore

\[
\boxed{
\Sigma_{m+1}^+
\bigl(
u\otimes\Sigma_m^-(F\otimes w)
\bigr)
=
\Sigma_{m+1}^-
\bigl(
\Sigma_m^+(u\otimes F)\otimes w
\bigr).
}
\tag{5.2}
\]

This is equality, not equality up to a transition automorphism. Hence every
rectangle formed solely by left and right exterior insertions commutes on
face spaces, edge spaces, and local quotients.

The word **flat** here has only this precise algebraic meaning: the
displayed exterior transport squares commute. It does not assert a metric,
a connection on all placements, or vanishing of a future curvature outside
this restricted subcategory.

The contrast with Note 20 is sharp:

\[
\boxed{
\text{exterior insertion: strict tensor suspension},
\qquad
\text{interior insertion: order-sensitive transition may appear}.
}
\tag{5.3}
\]

Thus the central shear \(\theta\) cannot be blamed on spectator number
alone. It is caused by moving a spectator through the ordered support.

---

## 6. Three infinite exact towers

### 6.1 The seed tower

At \(n=5\), Note 14 proves

\[
Y_{5,G_5}\cong\mathbb H\otimes\mathbb H
\tag{6.1}
\]

and the six edge ranks are

\[
(16,12,16,4,12,16).
\tag{6.2}
\]

After \(a\) left and \(b\) right exterior insertions, put \(r=a+b\). Then

\[
\boxed{
Y_{5+r,\{a+1,a+2,a+3,a+4\}}
\cong
V^{\otimes b}\otimes
(\mathbb H\otimes\mathbb H)
\otimes V^{\otimes a},
}
\tag{6.3}
\]

and its edge ranks are

\[
\boxed{
3^r(16,12,16,4,12,16).
}
\tag{6.4}
\]

### 6.2 The central-cap tower

Note 19 proves at

\[
n=6,
\qquad
Q_{\mathrm{cap}}=(1,2,4,5),
\tag{6.5}
\]

that the long-edge defect is

\[
Y_{6,Q_{\mathrm{cap}}}/E_{14}\cong\mathbb H.
\tag{6.6}
\]

Exterior suspension gives, for every \(a,b\ge0\),

\[
\boxed{
\frac{
Y_{6+a+b,\,(a+1,a+2,a+4,a+5)}
}{
E_{14}
}
\cong
V^{\otimes b}\otimes\mathbb H\otimes V^{\otimes a}.
}
\tag{6.7}
\]

The four-dimensional cap defect therefore propagates to an exact
\(4\cdot3^{a+b}\)-dimensional exterior tower.

### 6.3 The exceptional \(2\!-\!1\!-\!2\) tower

Note 21 proves

\[
Y_{7,(1,3,4,6)}
\cong
\left((\mathbb H\otimes\mathbb H)\otimes V^{\otimes2}\right)
\oplus\mathbb H.
\tag{6.8}
\]

For \(a,b\ge0\), set \(r=a+b\) and

\[
Q_{a,b}
:=
(a+1,a+3,a+4,a+6)
\subset G_{7+r}.
\tag{6.9}
\]

Then

\[
\boxed{
Y_{7+r,Q_{a,b}}
\cong
V^{\otimes b}\otimes
\left[
\left((\mathbb H\otimes\mathbb H)\otimes V^{\otimes2}\right)
\oplus\mathbb H
\right]
\otimes V^{\otimes a}.
}
\tag{6.10}
\]

Equivalently,

\[
\boxed{
148\cdot3^r
=
144\cdot3^r+4\cdot3^r.
}
\tag{6.11}
\]

The core edge ranks are

\[
\boxed{
3^r(144,108,144,36,108,144),
}
\tag{6.12}
\]

and the full exceptional edge ranks are

\[
\boxed{
3^r(144,112,148,40,112,144).
}
\tag{6.13}
\]

The residual generates the exact exterior family

\[
\boxed{
V^{\otimes b}\otimes\mathbb H\otimes V^{\otimes a}.
}
\tag{6.14}
\]

---

## 7. What this changes in the generalization problem

The local classification now separates into two operations.

1. **Exterior suspension.** It is solved by (0.4)–(0.7). It is exact,
   functorial, preserves the full decorated quotient, and has commuting
   left/right squares.

2. **Interior passage.** A spectator crosses a support vertex or lies
   between support vertices. This is where Note 20's nilpotent shear and
   Notes 16–17's square/cap residuals occur.

An arbitrary-placement theorem no longer needs to discover all transport at
once. Exterior spectators may be stripped off canonically. The irreducible
classification problem is the finite ordered word inside the support
interval.

For \(Q=(q_1,q_2,q_3,q_4)\), define its internal spacing word

\[
\lambda(Q)
=
(q_2-q_1,\ q_3-q_2,\ q_4-q_3).
\tag{7.1}
\]

Exterior suspension leaves \(\lambda(Q)\) unchanged. Thus every decorated
local quotient belongs to an exterior tower indexed by one internal word.
The \(2\!-\!1\!-\!2\) anomaly is the minimal member of the tower

\[
\lambda=(2,1,2).
\tag{7.2}
\]

The finite calculations through \(n=7\) reduce to:

| internal spectators | reduced words | established result |
|---:|---|---|
| \(0\) | \((1,1,1)\) | exact seed quotient \(\mathbb H\otimes\mathbb H\) |
| \(1\) | \((2,1,1),(1,2,1),(1,1,2)\) | exact 48-dimensional quotients; the middle word has the cap defect and central shear |
| \(2\) | \((3,1,1),(2,2,1),(2,1,2),(1,3,1),(1,2,2),(1,1,3)\) | Note 23 closes all five generic words over \(\mathbb Q\); \((2,1,2)\) has the exact \(144+4\) decomposition of Note 21 |

All placements obtained by adding exterior spectators are theorems over the
same base field as their reduced row. Note 23 therefore upgrades the full
two-internal-spectator row, and hence all fifteen \(n=7\) supports, to
characteristic zero. No generic reduced word remains to be lifted.

The next finite target is the transition graph among the multiple admissible
anchored coordinates on these six exact reduced words. Beyond that lies the
three-internal-spectator row and the general elementary passage produced when
one letter is increased.

---

## 8. What remains open

This note does **not** prove:

- a transport formula for inserting a spectator inside \([q_1,q_4]\);
- that every internal spacing word decomposes into a generic core plus
  square/cap residuals;
- path independence when interior insertions are allowed;
- all-\(n\) middle exactness of the tetrahedral second complex;
- a curvature or holonomy theorem.

It does prove that exterior directions are not the source of the observed
twist. Any nontrivial closed-path residual must use at least one interior
passage.

---

## 9. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/exterior_spectator_suspension_certificate.py
~~~

The certificate checks:

- invertibility of the left and right one-variable encoders;
- the prepend identity (2.5) and append identity (2.7) on every basis state,
  probe word, face, and edge through \(n=5\);
- the strict interchange identity (5.2);
- the seed, cap, and exceptional dimension/rank recurrences.

These finite checks witness the primitive quaternion identities. The all-\(n\)
theorem is the symbolic argument in Sections 2–5, not an extrapolation from
the checked lengths.

Expected final line:

~~~text
ALL CHECKS PASSED
~~~
