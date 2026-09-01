# Note 11 — \(n=6\) Terminal Response 4-Simplex

## five-face pairwise descent and the 176-dimensional compatibility syzygy

**Status:** response-side middle exactness proved by a deterministic exact modular rank certificate; rational conclusion obtained by a modular-minor lift

**Depends on:** Notes 09 and 10

**Claim boundary:** this note proves intrinsic pairwise terminal gluing at \(n=6\). Note 12 later proves pairwise descent for every length. The next local differential after the 176-dimensional cokernel and any curvature interpretation remain open.

---

## 0. Main result

Write

\[
\mathcal R_q
:=
\operatorname{Hom}_{\mathbb R}(V^{\otimes q},\mathbb H),
\qquad
\dim\mathcal R_q=4\cdot3^q.
\]

At length six there are five exact-depth-four terminal faces

\[
F_1,\ldots,F_5\in\mathcal R_4
\]

and ten pairwise exact-depth-three common shadows in \(\mathcal R_3\).
The decoder-collapse construction of Note 10 gives twenty oriented
restriction maps

\[
\rho_r^{rs},\rho_s^{rs}:
\mathcal R_4\longrightarrow\mathcal R_3,
\qquad
1\le r<s\le5.
\]

Define

\[
\boxed{
\partial_6:
\mathcal R_4^{\oplus5}
\longrightarrow
\mathcal R_3^{\oplus10}
}
\]

by

\[
\boxed{
(\partial_6F)_{rs}
=
\rho_r^{rs}F_r-\rho_s^{rs}F_s.
}
\tag{0.1}
\]

Then, over \(\mathbb Q\),

\[
\boxed{
\operatorname{rank}\partial_6=904,
\qquad
\dim\ker\partial_6=716,
\qquad
\dim\operatorname{coker}\partial_6=176.
}
\tag{0.2}
\]

Let

\[
\mathbf B_6:
V^{\otimes6}\longrightarrow\mathcal R_4^{\oplus5}
\]

be the joint terminal-boundary map. Then

\[
\boxed{
\operatorname{im}\mathbf B_6
=
\ker\partial_6.
}
\tag{0.3}
\]

Thus

\[
\boxed{
\mathcal P_{6,4}
:=
\ker\partial_6
}
\tag{0.4}
\]

is an intrinsic response-side presentation of the 716-dimensional terminal
boundary.

Define

\[
\mathfrak S_6:=\operatorname{coker}\partial_6.
\]

There is an exact sequence

\[
\boxed{
0\longrightarrow S^6_0V
\longrightarrow V^{\otimes6}
\xrightarrow{\ \mathbf B_6\ }
\mathcal R_4^{\oplus5}
\xrightarrow{\ \partial_6\ }
\mathcal R_3^{\oplus10}
\longrightarrow\mathfrak S_6
\longrightarrow0.
}
\tag{0.5}
\]

The compatibility-syzygy module has type

\[
\boxed{
\mathfrak S_6
\cong
10V_0\oplus21V_1\oplus15V_2\oplus4V_3,
\qquad
\dim\mathfrak S_6=176.
}
\tag{0.6}
\]

---

## 1. The terminal response 4-simplex

Length six has five internal-gap omissions. Every individual terminal face is
an arbitrary element of

\[
\mathcal R_4,
\qquad
\dim\mathcal R_4=4\cdot3^4=324.
\]

Hence the unconstrained five-face space is

\[
C_6^0
:=
\mathcal R_4^{\oplus5},
\qquad
\dim C_6^0=5\cdot324=1620.
\tag{1.1}
\]

Every pair of omitted gaps leaves three probe variables, so its common shadow
lies in

\[
\mathcal R_3,
\qquad
\dim\mathcal R_3=4\cdot3^3=108.
\]

There are \(\binom52=10\) pairs. The equation space is therefore

\[
C_6^1
:=
\mathcal R_3^{\oplus10},
\qquad
\dim C_6^1=10\cdot108=1080.
\tag{1.2}
\]

The five faces and ten pairwise shadows form the first two levels of a
response 4-simplex:

\[
\boxed{
C_6^0
\xrightarrow{\ \partial_6\ }
C_6^1.
}
\tag{1.3}
\]

---

## 2. Intrinsic common-shadow restrictions

Fix \(r<s\). Let

\[
D_{rs}:V^{\otimes6}\longrightarrow\mathcal R_3
\]

probe every gap except \(r,s\).

Note 09 gives the single-face encoder isomorphism

\[
\mathcal E_{6,r}:
W_{6,r}
\xrightarrow{\ \cong\ }
\mathcal R_4,
\]

where

\[
W_{6,r}
=
V^{\otimes(r-1)}
\otimes\mathbb H
\otimes V^{\otimes(5-r)}.
\]

Decode a face by \(\mathcal E_{6,r}^{-1}\), multiply across the second omitted
gap, and re-encode the three remaining probes. This defines

\[
\boxed{
\rho_r^{rs}:
\mathcal R_4\longrightarrow\mathcal R_3
}
\tag{2.1}
\]

without choosing a state representative.

For every actual state,

\[
\boxed{
\rho_r^{rs}B_{6,r}
=D_{rs}
=\rho_s^{rs}B_{6,s}.
}
\tag{2.2}
\]

All twenty oriented restrictions are onto:

\[
\boxed{
\operatorname{rank}\rho_r^{rs}
=108.
}
\tag{2.3}
\]

Equation (2.2) gives

\[
\boxed{
\partial_6\mathbf B_6=0,
}
\tag{2.4}
\]

and hence

\[
\operatorname{im}\mathbf B_6
\subseteq
\ker\partial_6.
\tag{2.5}
\]

---

## 3. The rational rank upper bound

The all-length terminal theorem gives

\[
\ker\mathbf B_6
=
S^6_0V
\cong V_6,
\qquad
\dim V_6=13.
\]

Therefore

\[
\boxed{
\operatorname{rank}\mathbf B_6
=
3^6-13
=716.
}
\tag{3.1}
\]

By (2.5),

\[
\dim\ker\partial_6\ge716.
\]

Since the source of \(\partial_6\) has dimension 1620,

\[
\boxed{
\operatorname{rank}_{\mathbb Q}\partial_6
\le
1620-716
=904.
}
\tag{3.2}
\]

Thus only the opposite inequality is required.

---

## 4. Exact modular rank lift

The local decoders \(\Theta_L^{-1}\) and \(\Theta_R^{-1}\) have coefficients
in \(\mathbb Z[1/2]\). Every iterated restriction map therefore has entries
whose denominators are powers of two.

Let \(p\) be an odd prime. Reduction modulo \(p\) is well defined. If the
reduced terminal-face map remains onto, the reduced factor map

\[
\overline\rho_r^{rs}
\]

is unique because it satisfies

\[
\overline\rho_r^{rs}\,\overline B_{6,r}
=
\overline D_{rs}.
\]

Consequently, the restriction obtained by exact finite-field factorization is
the reduction of the rational response-side restriction.

### Lemma 4.1 — modular lower bound

Let \(M\) be a rational matrix whose denominators are prime to \(p\). Then

\[
\operatorname{rank}_{\mathbb Q}M
\ge
\operatorname{rank}_{\mathbb F_p}\overline M.
\tag{4.1}
\]

Indeed, a nonzero \(r\times r\) minor modulo \(p\) has a determinant whose
rational numerator is nonzero, so the same minor is nonzero over
\(\mathbb Q\).

The exact certificate computes

\[
\boxed{
\operatorname{rank}_{\mathbb F_{1009}}
\overline{\partial}_6
=904
}
\tag{4.2}
\]

and independently

\[
\boxed{
\operatorname{rank}_{\mathbb F_{1013}}
\overline{\partial}_6
=904.
}
\tag{4.3}
\]

Either prime alone is sufficient. Lemma 4.1 gives

\[
\operatorname{rank}_{\mathbb Q}\partial_6\ge904.
\]

Combining with (3.2),

\[
\boxed{
\operatorname{rank}_{\mathbb Q}\partial_6=904.
}
\tag{4.4}
\]

This is an exact proof, not a numerical approximation. NumPy is used by the
certificate only to vectorize integer row operations modulo the two primes;
no floating-point operation occurs.

---

## 5. Pairwise-gluing theorem at \(n=6\)

From (4.4),

\[
\dim\ker\partial_6
=1620-904
=716.
\]

But (3.1) and (2.5) give a 716-dimensional subspace

\[
\operatorname{im}\mathbf B_6
\subseteq
\ker\partial_6.
\]

Hence:

### Theorem 5.1 — terminal response 4-simplex gluing

A five-tuple

\[
(F_1,\ldots,F_5)\in\mathcal R_4^{\oplus5}
\]

is the terminal boundary of a length-six state if and only if all ten
pairwise common shadows agree:

\[
\boxed{
\rho_r^{rs}F_r
=
\rho_s^{rs}F_s
\qquad
(1\le r<s\le5).
}
\tag{5.1}
\]

Equivalently,

\[
\boxed{
\mathcal P_{6,4}
=
\ker\partial_6
=
\operatorname{im}\mathbf B_6.
}
\tag{5.2}
\]

The final presentation is response-first: five arbitrary local faces are
global exactly when their ten common shadows match.

---

## 6. The 176-dimensional compatibility syzygy

The equation target has dimension 1080. Since \(\partial_6\) has rank 904,

\[
\boxed{
\dim\mathfrak S_6
=
\dim\operatorname{coker}\partial_6
=1080-904
=176.
}
\tag{6.1}
\]

Equivalently, after invariant inner products are chosen, the 1080 scalar
matching coordinates obey a 176-dimensional space of row relations.

The increase

\[
0\quad(n=4),
\qquad
16\quad(n=5),
\qquad
176\quad(n=6)
\]

shows that higher compatibility is not a small correction. Pairwise descent
continues to be complete, while relations among the pairwise equations grow
rapidly.

---

## 7. \(SO(3)\)-type of \(\mathfrak S_6\)

The relevant response modules are

\[
\mathcal R_3
\cong
4V_0\oplus9V_1\oplus8V_2\oplus4V_3\oplus V_4,
\tag{7.1}
\]

and

\[
\mathcal R_4
\cong
9V_0\oplus21V_1\oplus21V_2
\oplus13V_3\oplus5V_4\oplus V_5.
\tag{7.2}
\]

Repeated Clebsch-Gordan decomposition gives

\[
V^{\otimes6}
\cong
15V_0\oplus36V_1\oplus40V_2\oplus29V_3
\oplus15V_4\oplus5V_5\oplus V_6.
\tag{7.3}
\]

Removing the unique terminal kernel \(V_6\) gives

\[
\mathcal P_{6,4}
\cong
15V_0\oplus36V_1\oplus40V_2\oplus29V_3
\oplus15V_4\oplus5V_5.
\tag{7.4}
\]

The exact sequence yields

\[
[\mathfrak S_6]
=
10[\mathcal R_3]
-5[\mathcal R_4]
+[\mathcal P_{6,4}].
\tag{7.5}
\]

Substitution gives

\[
\boxed{
\mathfrak S_6
\cong
10V_0\oplus21V_1\oplus15V_2\oplus4V_3.
}
\tag{7.6}
\]

The dimension check is

\[
10+21\cdot3+15\cdot5+4\cdot7
=176.
\]

All spins \(V_4,V_5,V_6\) cancel. As at \(n=5\), the compatibility syzygy
occupies lower spins and is distinct from the terminal top-spin interior.

---

## 8. The emerging response-simplex sequence

The first three cases now read:

| length | response simplex | face space | matching rank | compatible boundary | syzygy |
|---:|---|---:|---:|---:|---:|
| \(n=4\) | triangle | 108 | 36 | 72 | 0 |
| \(n=5\) | tetrahedron | 432 | 200 | 232 | 16 |
| \(n=6\) | 4-simplex | 1620 | 904 | 716 | 176 |

For general \(n\ge4\), let

\[
C_n^0
=
\mathcal R_{n-2}^{\oplus(n-1)},
\qquad
C_n^1
=
\mathcal R_{n-3}^{\oplus\binom{n-1}{2}}.
\]

The all-length terminal descent statement, conjectural at the time of this
calculation and proved subsequently in Note 12, is

\[
\boxed{
0\longrightarrow S^n_0V
\longrightarrow V^{\otimes n}
\xrightarrow{\ \mathbf B_n\ }
C_n^0
\xrightarrow{\ \partial_n\ }
C_n^1
\quad\text{is exact at }V^{\otimes n}\text{ and }C_n^0.
}
\tag{8.1}
\]

This note proved it for \(n=4,5,6\); Note 12 proves it for every \(n\).
Consequently the syzygy character is

\[
\boxed{
[\mathfrak S_n]
=
\binom{n-1}{2}[\mathcal R_{n-3}]
-(n-1)[\mathcal R_{n-2}]
+[V^{\otimes n}]-[V_n].
}
\tag{8.2}
\]

Its dimension is

\[
\boxed{
\dim\mathfrak S_n
=
(2n^2-18n+43)3^{n-3}-(2n+1).
}
\tag{8.3}
\]

Formula (8.3) gives \(0,16,176\) at \(n=4,5,6\).

---

## 9. Curvature status

The 176-dimensional cokernel is a higher compatibility module, not curvature.
It records dependencies among pairwise matching defects. No path transport or
path comparison has yet been introduced.

The new result does, however, sharpen the future curvature problem. A
transport theory on the response simplex must respect not only the pairwise
matching operator but also its rapidly growing syzygy module. Any Bianchi-type
identity will have to land in, or factor through, this next compatibility
layer.

---

## 10. Exact certificate

Run

```bash
python3 certificates/n6_response_4simplex_modular_certificate.py
```

from `research/depth-generated-geometry/`.

The script builds the signed integer response matrices directly from
quaternion basis multiplication and performs deterministic row reduction over
\(\mathbb F_{1009}\) and \(\mathbb F_{1013}\). NumPy is required only for
vectorized integer storage and row operations.

It verifies:

- all five terminal faces have shape \(324\times729\) and remain onto;
- all ten common shadows have shape \(108\times729\);
- all twenty oriented restriction maps are onto;
- \(\partial_6\mathbf B_6=0\);
- the joint terminal boundary has rank 716 modulo both primes;
- the matching operator has rank 904 modulo both primes;
- the compatible kernel and compatibility cokernel have dimensions 716 and
  176;
- the modular rank lifts to the rational equality
  \(\operatorname{rank}_{\mathbb Q}\partial_6=904\);
- \(\mathfrak S_6\cong10V_0\oplus21V_1\oplus15V_2\oplus4V_3\).

Expected final line:

```text
ALL CHECKS PASSED
```

---

## 11. Next obstruction

The computational question is no longer whether \(n=6\) works. It does, and
Note 12 proves that the same pairwise descent is exact for every \(n\).
Consequently (8.2) is a universal compatibility-syzygy law and
\(\ker\partial_n/\mathcal P_{n,n-2}\) vanishes at all lengths.

The next obstruction lies one level later: construct a local higher
differential whose kernel or image realizes \(\operatorname{coker}\partial_n\).
The 16-dimensional \(n=5\) and 176-dimensional \(n=6\) modules are now the
first two finite models of that universal problem, not evidence awaiting a
larger isolated rank test.
