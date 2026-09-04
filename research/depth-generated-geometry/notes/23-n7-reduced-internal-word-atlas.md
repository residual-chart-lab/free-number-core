# Note 23 — The Reduced \(n=7\) Internal-Word Atlas

## all five generic two-spectator quotients admit exact anchored coordinates over \(\mathbb Q\)

**Status:** theorem over \(\mathbb Q\), with exact integer identities,
two-prime reconstruction, and certified Casimir edge profiles

**Depends on:** Notes 15, 20, 21, and 22

**Claim boundary:** this note closes the characteristic-zero classification
of all six reduced two-spectator words at \(n=7\). For each of the five
generic words it constructs a 144-dimensional quotient coordinate by
transporting one valid \(n=6\) edge anchor and completing it uniquely through
the local matching relations. Together with Note 21 it gives an exact atlas
for every reduced word, and Note 22 then gives every \(n=7\) placement. The
coordinate attached to a generic word is canonical relative to the stated
anchor; independence of all admissible anchors, transition maps between such
coordinates, and an all-word theorem for arbitrary spectator number are not
claimed here.

---

## 0. Result in one line

Let

\[
Q=\{q_1<q_2<q_3<q_4\}\subset G_7,
\qquad G_7=\{1,\ldots,6\},
\tag{0.1}
\]

be **reduced**, meaning

\[
q_1=1,
\qquad q_4=6.
\tag{0.2}
\]

Its internal spacing word is

\[
\lambda(Q)
=
(q_2-q_1,q_3-q_2,q_4-q_3).
\tag{0.3}
\]

There are exactly six possibilities:

\[
113,\quad122,\quad131,\quad212,\quad221,\quad311.
\tag{0.4}
\]

In right-decoder coordinates put

\[
E_Q
:=
\bigoplus_{e\in\binom Q2}
(\mathbb H\otimes V^{\otimes4})_e,
\qquad
\dim E_Q=6\cdot324=1944,
\tag{0.5}
\]

and let

\[
\widehat\partial_{7,Q}:
\mathcal R_5^{\oplus4}\longrightarrow E_Q
\tag{0.6}
\]

be the decoded local matching map. Write

\[
T_7
:=
(\mathbb H\otimes\mathbb H)\otimes V^{\otimes2},
\qquad
\dim T_7=144.
\tag{0.7}
\]

For each generic word

\[
\lambda\in\{113,122,131,221,311\}
\tag{0.8}
\]

there is an explicitly anchored, surjective, \(SO(3)\)-equivariant map

\[
\boxed{
C_\lambda:E_{Q_\lambda}\longrightarrow T_7
}
\tag{0.9}
\]

such that

\[
\boxed{
\mathcal R_5^{\oplus4}
\xrightarrow{\ \widehat\partial_{7,Q_\lambda}\ }
E_{Q_\lambda}
\xrightarrow{\ C_\lambda\ }
T_7
\longrightarrow0
}
\tag{0.10}
\]

is exact over \(\mathbb Q\). Consequently

\[
\boxed{Y_{7,Q_\lambda}\cong T_7}
\qquad(\lambda\ne212).
\tag{0.11}
\]

Note 21 supplies the remaining word:

\[
\boxed{
Y_{7,Q_{212}}
\cong T_7\oplus\mathbb H.
}
\tag{0.12}
\]

Thus

\[
\boxed{
Y_{7,Q_\lambda}
\cong
\begin{cases}
T_7,&\lambda\ne212,\\[1mm]
T_7\oplus\mathbb H,&\lambda=212.
\end{cases}}
\tag{0.13}
\]

The extra quaternion is not a generic ambiguity in constructing the
144-dimensional core. It is a genuine additional quotient direction
confined to the interlaced word \(212\).

---

## 1. Why six words are the whole reduced problem

If a spectator lies strictly to the left or right of the support interval,
Note 22 removes it by an inverse exterior suspension without changing the
internal spacing word. Repeating this operation leaves a unique reduced
support with first vertex \(1\) and last vertex \(n-1\).

At \(n=7\), a reduced word \(\lambda=(a,b,c)\) satisfies

\[
a+b+c=5,
\qquad a,b,c\ge1.
\tag{1.1}
\]

The six words and supports are

\[
\begin{array}{c|c|c}
\lambda&Q_\lambda&G_7\setminus Q_\lambda\\ \hline
113&(1,2,3,6)&(4,5)\\
122&(1,2,4,6)&(3,5)\\
131&(1,2,5,6)&(3,4)\\
212&(1,3,4,6)&(2,5)\\
221&(1,3,5,6)&(2,4)\\
311&(1,4,5,6)&(2,3).
\end{array}
\tag{1.2}
\]

Every one of the other nine four-element subsets of \(G_7\) has at least
one exterior spectator. It therefore descends by Note 22 to either the
exact \(n=5\) seed or the exact \(n=6\) one-spectator atlas. Hence (1.2) is
the only new characteristic-zero calculation required to upgrade the full
\(n=7\) placement classification.

---

## 2. The five transported anchors

The construction does not tensorize an entire \(n=6\) chart blindly. It
transports one full-rank edge block through a spectator which is exterior
**relative to that edge response**, then asks local compatibility to recover
the other five blocks.

For each generic word, delete the spectator listed as new, compress the
remaining ordered gaps to the \(n=6\) system, and let \(s\) be the position
of the other spectator. Use the left or right chart \(\Omega_s^L\) or
\(\Omega_s^R\) from Note 20. The following choices all have rank 144:

\[
\begin{array}{c|c|c|c|c|c}
\lambda&\text{new}&\text{old}&s&\text{parent chart}&
\text{anchored actual edge}\\ \hline
113&5&4&4&\Omega_4^R&(1,6)\\
122&3&5&4&\Omega_4^R&(1,2)\\
131&3&4&3&\Omega_3^L&(1,2)\\
221&2&4&3&\Omega_3^L&(1,3)\\
311&2&3&2&\Omega_2^L&(1,4).
\end{array}
\tag{2.1}
\]

For the first row, the new spectator is rightmost among the four probe
variables remaining on the anchored edge, so \(\Sigma^+\) carries the block.
In the other four rows it is leftmost, so \(\Sigma^-\) carries the block.
Denote the result by

\[
A_\lambda:
\mathbb H\otimes V^{\otimes4}\longrightarrow T_7.
\tag{2.2}
\]

The parent chart, its chosen block, and the one-step decoder are already
exact over \(\mathbb Q\). Thus \(A_\lambda\) is a transported structural
datum, not a fitted quotient basis.

The exceptional word \(212\) admits an analogous transported anchor on
\((1,6)\), but its local quotient has dimension 148. Note 21 proves that
the anchor still completes uniquely to a 144-dimensional core, while the
transverse square coordinate \(\kappa_{212}\) supplies the remaining
\(\mathbb H\).

---

## 3. Unique compatible completion

Let

\[
L_\lambda
:=
\left\{
\ell\in E_{Q_\lambda}^*:
\ell\widehat\partial_{7,Q_\lambda}=0
\right\}
\tag{3.1}
\]

be the left annihilator of the generic matching image. Exact rank gives

\[
\operatorname{rank}\widehat\partial_{7,Q_\lambda}=1800,
\qquad
\dim L_\lambda=1944-1800=144.
\tag{3.2}
\]

For the anchored edge \(e_\lambda\) in (2.1), restriction is injective:

\[
\boxed{
L_\lambda\longrightarrow
(\mathbb H\otimes V^{\otimes4})_{e_\lambda}^*
\quad\text{has rank }144.
}
\tag{3.3}
\]

The 144 rows of \(A_\lambda\) lie in its image and therefore possess unique
lifts to \(L_\lambda\). Lifting them simultaneously defines \(C_\lambda\),
characterized by

\[
\boxed{
C_\lambda\widehat\partial_{7,Q_\lambda}=0,
\qquad
(C_\lambda)_{e_\lambda}=A_\lambda.
}
\tag{3.4}
\]

Because \(A_\lambda\) is onto, \(C_\lambda\) has rank 144. Equations (3.2)
and (3.4) imply

\[
\ker C_\lambda
=
\operatorname{im}\widehat\partial_{7,Q_\lambda},
\tag{3.5}
\]

which proves (0.10).

If two compatible maps had the same anchor, every row of their difference
would lie in \(L_\lambda\) and vanish on \(e_\lambda\). Injectivity in (3.3)
forces the difference to vanish. Hence the completion is unique relative to
the selected transported anchor.

The matching map and anchor are \(SO(3)\)-equivariant. Acting on (3.4)
produces another completion of the same anchor, so uniqueness forces
equivariance. The certificate also verifies all three infinitesimal
intertwining identities directly over \(\mathbb Z\).

---

## 4. Exact decorated edge atlas

Let \(P_j\) be a nonzero scalar multiple of the Casimir projector onto the
spin-\(j\) isotypic part of \(T_7\). For an edge image \(E\subset T_7\)
write

\[
\sigma(E)
=
(\dim P_0E,\ldots,\dim P_4E).
\tag{4.1}
\]

The full target has

\[
\boxed{
\sigma(T_7)=(6,39,55,35,9),
}
\tag{4.2}
\]

equivalently

\[
T_7
\cong
6V_0\oplus13V_1\oplus11V_2\oplus5V_3\oplus V_4.
\tag{4.3}
\]

The five generic words fall into exactly two edge-profile classes.

### 4.1 Standard words \(113\) and \(311\)

\[
\begin{array}{c|c|c}
ab&\dim E_{ab}&\sigma(E_{ab})\\ \hline
12,14,34&144&(6,39,55,35,9)\\
13,24&108&(4,27,40,28,9)\\
23&36&(2,12,15,7,0).
\end{array}
\tag{4.4}
\]

### 4.2 Central-gap words \(122,131,221\)

Every edge except the long edge \(14\) has the standard profile. The long
edge is

\[
\boxed{
\dim E_{14}=132,
\qquad
\sigma(E_{14})=(5,33,50,35,9).
}
\tag{4.5}
\]

Its missing part has profile

\[
(6,39,55,35,9)-(5,33,50,35,9)
=(1,6,5,0,0),
\tag{4.6}
\]

the 12-dimensional type

\[
V_0\oplus2V_1\oplus V_2
\cong
\mathbb H\otimes V.
\tag{4.7}
\]

The condition distinguishing the two generic classes is exactly

\[
\lambda_2=q_3-q_2>1.
\tag{4.8}
\]

Thus the total module remains \(T_7\), but the labelled incidence data
remembers whether a spectator lies in the central interval.

### 4.3 Exceptional word \(212\)

For comparison, Note 21 gives

\[
Y_{7,Q_{212}}\cong T_7\oplus\mathbb H
\tag{4.9}
\]

with core edge ranks

\[
(144,108,144,36,108,144)
\tag{4.10}
\]

and full edge ranks

\[
\boxed{(144,112,148,40,112,144).}
\tag{4.11}
\]

The same four-dimensional square coordinate is added on exactly the four
cross edges. Therefore the six-word atlas separates three phenomena:

\[
\boxed{
\begin{array}{rcl}
113,311&:&\text{standard core incidence},\\
122,131,221&:&\text{central }\mathbb H\otimes V\text{ long-edge defect},\\
212&:&\text{transverse cross-edge }\mathbb H\text{ birth}.
\end{array}}
\tag{4.12}
\]

---

## 5. How the rational theorem is certified

For each of the five generic supports, the decoded matching matrix is
reconstructed independently over

\[
\mathbb F_{1009}
\qquad\text{and}\qquad
\mathbb F_{1013}.
\tag{5.1}
\]

Multiplication by 16 followed by centered lifting gives the same integral
matrix

\[
M_{16,\lambda}
=16\widehat\partial_{7,Q_\lambda}
\tag{5.2}
\]

from both fields, with coefficient alphabet contained in

\[
\{-2,-1,0,1,2\}.
\tag{5.3}
\]

Every possible coefficient in the integer face-to-shadow factorization
error is bounded by

\[
324\cdot972\cdot2+16=629872,
\tag{5.4}
\]

while

\[
629872<1009\cdot1013=1022117.
\tag{5.5}
\]

The error vanishes modulo both primes and is smaller in absolute value than
their product, so it vanishes over \(\mathbb Z\). Thus
\(M_{16,\lambda}/16\) is the exact rational matching map, not a guessed
lift.

The same two computations reconstruct identical integer anchors and
identical integer matrices \(C_\lambda\). Their coefficients have absolute
value at most 12, and ordinary integer multiplication gives

\[
\boxed{C_\lambda M_{16,\lambda}=0.}
\tag{5.6}
\]

A rank-1800 minor modulo either prime gives

\[
\operatorname{rank}_{\mathbb Q}M_{16,\lambda}\ge1800.
\tag{5.7}
\]

On the other hand, \(C_\lambda\) has 144 independent rows and annihilates
the matching, so

\[
\operatorname{rank}_{\mathbb Q}M_{16,\lambda}
\le1944-144=1800.
\tag{5.8}
\]

This proves equality and hence exactness over \(\mathbb Q\). Finally, the
three \(SO(3)\) intertwining identities, all six edge ranks, and all thirty
Casimir-projected edge ranks are checked using exact integer or rational row
reduction.

---

## 6. What this resolves

Note 15 first detected the complete \(n=7\) table over two prime fields.
Before this note, only the exceptional \(212\) quotient had been lifted in
full coordinates to characteristic zero. The other five reduced words
could still have hidden a bad rational reconstruction or a modular-only
coincidence.

That possibility is now removed:

\[
\boxed{
\text{all six reduced }n=7\text{ words have explicit exact quotient maps
over }\mathbb Q.
}
\tag{6.1}
\]

Combining this with exterior suspension gives

\[
\boxed{
\text{every one of the fifteen }n=7\text{ tetrahedral supports is obtained
over }\mathbb Q.
}
\tag{6.2}
\]

The unique exceptional dimension jump has survived a construction in which
all five neighboring reduced words close onto the same 144-dimensional
target:

\[
\boxed{
144,144,144,\mathbf{148},144,144.
}
\tag{6.3}
\]

The placement residual is isolated against a complete exact background. It
is not an artifact of comparing one exceptional computation with an
unconstructed generic baseline.

---

## 7. What remains open

This note does **not** prove:

- that two different admissible anchors on the same generic word produce
  the same coordinate;
- a closed formula for the transition between two such anchored
  coordinates;
- that moving a spectator between adjacent internal intervals is generated
  by the \(n=6\) transition \(\theta\);
- that the exceptional square \(\kappa_{212}\) is the obstruction around a
  closed transport path;
- a classification of spacing words with three or more internal spectators;
- all-\(n\) middle exactness of the tetrahedral second complex;
- curvature, holonomy, topology, or a physical gauge field.

The next finite calculation is no longer another quotient dimension. Each
generic word admits more than one full-rank transported anchor. Their unique
completions should be compared on the common 144-dimensional target. This
produces an exact transition graph on the reduced words. Only after its
genuine closed loops are known is there a mathematically defined place to
ask whether a path residual lands in the \(212\) quaternion.

**Subsequent resolution.** Note 24 exhausts the transported direct-anchor
histories on every reduced word. Their same-word coordinate changes are
generated by three pair-local copies \(A,B,S\) of
\(\theta,\theta^{-1}\), while the exceptional full transition is
\(S\oplus I_{\mathbb H}\). The remaining graph problem is now specifically
the construction of transports **between different adjacent spacing
words**; same-word chart comparison is closed.

---

## 8. Certificate

Run from research/depth-generated-geometry:

~~~bash
python3 certificates/n7_internal_word_atlas_certificate.py
~~~

The script verifies:

- independent reconstruction of all five generic matchings over
  \(\mathbb F_{1009}\) and \(\mathbb F_{1013}\);
- equality of the centered integral lifts
  \(16\widehat\partial\);
- the CRT coefficient bound promoting every matching to \(\mathbb Q\);
- equality of transported anchors and quotient maps from both primes;
- exact integer cancellation
  \(C_\lambda(16\widehat\partial)=0\);
- matching rank 1800 and quotient-map rank 144;
- exact recovery of the specified anchor block;
- \(SO(3)\)-equivariance over \(\mathbb Z\);
- all six exact edge ranks and Casimir fingerprints for every word.

Expected final line:

~~~text
ALL CHECKS PASSED
~~~
