# Gate B — intervention observability and residual depth

Status: proved working note for the arXiv manuscript.

## 1. Partial insertion responses

Let

\[
B_n=V^{\otimes n},\qquad V=\operatorname{Im}\mathbb H.
\]

For a subset of internal gaps

\[
S\subseteq\{1,\ldots,n-1\},
\]

let

\[
D_S:B_n\longrightarrow \operatorname{Hom}(V^{\otimes |S|},\mathbb H)
\]

be the response obtained by inserting probe variables exactly in the gaps indexed by \(S\), while leaving all other gaps unprobed. The empty response is ordinary reversed quaternionic compression:

\[
D_\varnothing=m_n.
\]

Collect all responses up to probe depth \(d\):

\[
D_n^{\le d}=\bigoplus_{|S|\le d}D_S,
\qquad
F_d^{(n)}=\ker D_n^{\le d}.
\]

Then

\[
F_0^{(n)}\supseteq F_1^{(n)}\supseteq\cdots\supseteq F_{n-1}^{(n)}=0.
\]

For nonzero \(x\in B_n\), define

\[
\delta(x)=\min\{d:D_n^{\le d}(x)\ne0\}.
\]

Thus

\[
x\in F_{d-1}^{(n)}\setminus F_d^{(n)}
\quad\Longleftrightarrow\quad
\delta(x)=d,
\]

with the convention \(F_{-1}^{(n)}=B_n\).

## 2. Relation to standard observability

For a discrete linear system \((C,A)\), the finite unobservable chain has the form

\[
\mathcal N_d=\bigcap_{k=0}^{d}\ker(CA^k).
\]

Multivariable and noncommutative systems replace powers \(A^k\) by operator words. In this broad sense, \(F_d^{(n)}\) is an observability filtration: it is the joint kernel of a growing, canonically indexed family of output maps.

The native Core construction is nevertheless not a classical single-transition system:

1. there is no distinguished time-evolution endomorphism \(A:B_n\to B_n\);
2. the index set is the subset lattice of internal positions in one fixed boundary tensor, not successive time powers;
3. each response is multilinear in freely chosen quaternionic probes;
4. the response family factorizes under boundary concatenation;
5. the filtration is \(SO(3)\)-equivariant and records factor origin as well as representation type.

Any finite descending filtration can be encoded artificially as the unobservable chain of some enlarged linear system. Therefore the defensible claim is not absolute non-representability by control theory. The distinctive content is that the filtration arises canonically from internal insertion geometry and obeys the factorization and coherence laws below.

The closest general observability language located in the first literature pass is the free-semigroup or noncommutative observability-operator framework, for example Ball--Bolotnikov--Fang, *Multivariable backward-shift-invariant subspaces and observability operators*, arXiv:math/0610634. Word-indexed observability is therefore known. Internal-gap indexing, the quaternionic factorization law, and the depth behavior proved here remain model-specific.

## 3. Concatenation factorization

Let \(x\in B_m\) and \(y\in B_n\). For a selected-gap set

\[
S\subseteq\{1,\ldots,m+n-1\},
\]

split \(S\) into

- internal gaps \(S_x\subseteq\{1,\ldots,m-1\}\) of \(x\);
- the bridge gap \(m\), either selected or unselected;
- internal gaps \(S_y\subseteq\{1,\ldots,n-1\}\) of \(y\), after shifting indices by \(m\).

Then the partial response of the concatenation factors as

\[
D_S(x\Vert y)
=
D_{S_y}(y)\,\eta\,D_{S_x}(x),
\]

where \(\eta=1\) when the bridge is unprobed and \(\eta=d_*\in V\) when the bridge probe is present. Probe arguments on the two factors are independent.

This is the partial-response analogue of the exact bridge product.

## 4. Additivity of first-detection depth on decomposable states

### Theorem

For nonzero \(x\in B_m\) and nonzero \(y\in B_n\),

\[
\boxed{\delta(x\Vert y)=\delta(x)+\delta(y).}
\]

### Proof

Set

\[
p=\delta(x),\qquad q=\delta(y).
\]

Choose internal-gap sets \(S_x,S_y\) of sizes \(p,q\) for which the corresponding response maps are nonzero. Leaving the bridge unprobed gives

\[
D_{S_x\cup(m+S_y)}(x\Vert y)
=
D_{S_y}(y)D_{S_x}(x).
\]

The probe variables on the two factors can be chosen independently so that both quaternionic outputs are nonzero. Since \(\mathbb H\) has no zero divisors, their product is nonzero. Hence

\[
\delta(x\Vert y)\le p+q.
\]

Conversely, consider any response of total depth less than \(p+q\). If it uses \(r\) internal probes in \(x\), \(s\) internal probes in \(y\), and possibly one bridge probe, then at least one of

\[
r<p,\qquad s<q
\]

must hold. The corresponding factor response is identically zero, so the concatenated response vanishes. Therefore

\[
\delta(x\Vert y)\ge p+q.
\]

Combining the inequalities proves the theorem.

## 5. Multiplicative filtration law

Define the shifted depth filtration

\[
G_d^{(n)}=\{x\in B_n:\delta(x)\ge d\},
\]

so that

\[
G_0^{(n)}=B_n,
\qquad
G_d^{(n)}=F_{d-1}^{(n)}\quad(d\ge1).
\]

The depth theorem implies

\[
\boxed{
G_p^{(m)}\otimes G_q^{(n)}
\subseteq
G_{p+q}^{(m+n)}.
}
\]

Equality of depths holds on every nonzero decomposable tensor. Linear combinations may lie deeper because their first nonzero response can cancel.

Thus residual depth behaves like a valuation on decomposable concatenations and like a superadditive filtration on their linear span.

In the original \(F\)-indexing this gives

\[
F_p^{(m)}\otimes F_q^{(n)}
\subseteq
F_{p+q+1}^{(m+n)}.
\]

## 6. Algebraic coherence delay

At grade two,

\[
B_2=P\oplus R,
\]

where

\[
P=\mathbb Rg\oplus\Lambda^2V\cong V_0\oplus V_1,
\qquad
R=S_0^2V\cong V_2.
\]

The residual sector is exactly

\[
R=F_0^{(2)},
\]

and every nonzero \(S\in R\) has

\[
\delta(S)=1.
\]

Therefore every nonzero decomposable residual pair satisfies

\[
\delta(S\Vert T)=2.
\]

At grade four, however,

\[
F_2^{(4)}\cap(R\otimes R)=S_0^4V\cong V_4,
\qquad
\dim S_0^4V=9.
\]

Since \(F_3^{(4)}=0\), every nonzero element of this nine-dimensional subspace has depth three.

Hence no nonzero pure tensor \(S\Vert T\) belongs to \(F_2^{(4)}\), but suitable linear combinations of such depth-two tensors do. Their depth is raised by cancellation of every response through depth two.

We call this **algebraic coherence delay**:

> a non-decomposable linear superposition becomes visible strictly later than every nonzero decomposable residual pair from which it is assembled.

This is an algebraic statement. It does not assert quantum coherence.

## 7. Exact grade-four filtration

The exact dimensions are

\[
\dim B_4=81,
\]

and

\[
\begin{array}{c|cccc}
d&0&1&2&3\\
\hline
\operatorname{rank}D_4^{\le d}&4&32&72&81\\
\dim F_d^{(4)}&77&49&9&0.
\end{array}
\]

Split \(B_4\) by the two grade-two factors:

\[
B_4=(P\otimes P)\oplus(P\otimes R)\oplus(R\otimes P)\oplus(R\otimes R).
\]

The invisible dimensions in each sector are

\[
\begin{array}{c|rrrr|r}
& P\otimes P&P\otimes R&R\otimes P&R\otimes R&\text{total}\\
\hline
F_0^{(4)}&12&20&20&25&77\\
F_1^{(4)}&0&12&12&25&49\\
F_2^{(4)}&0&0&0&9&9\\
F_3^{(4)}&0&0&0&0&0.
\end{array}
\]

The associated first-detection layers

\[
L_d^{(4)}=F_{d-1}^{(4)}/F_d^{(4)}
\]

have dimensions

\[
4,\ 28,\ 40,\ 9
\]

at depths \(0,1,2,3\), respectively.

## 8. Equivariant depth decomposition

Using Clebsch--Gordan decomposition and sector invariance, the first-detection layers are

\[
\boxed{
\begin{aligned}
L_0^{(4)}&\cong V_0\oplus V_1,\\
L_1^{(4)}&\cong V_0\oplus4V_1\oplus3V_2,\\
L_2^{(4)}&\cong V_0\oplus V_1\oplus3V_2\oplus3V_3,\\
L_3^{(4)}&\cong V_4.
\end{aligned}
}
\]

The dimension check is

\[
4+28+40+9=81.
\]

This proves that representation type alone does not determine visibility depth. In particular, copies of \(V_0\), \(V_1\), and \(V_2\) occur at more than one detection depth.

The factor-sector decomposition makes the split more precise:

- \(P\otimes P\) contributes at depths zero and one;
- each mixed sector \(P\otimes R\) and \(R\otimes P\) contributes at depths one and two;
- \(R\otimes R\) contributes at depths two and three;
- the unique depth-three survivor is the spin-four sector \(S_0^4V\).

Thus equal-spin copies can be separated by factor origin and first detection depth.

## 9. What is standard and what is model-specific

### Standard in broad form

- a descending joint-kernel observability filtration;
- word-indexed outputs in multivariable and noncommutative systems;
- decomposition into observable and unobservable sectors;
- cancellation that can hide a linear combination from a measurement family.

### Established here for the explicit Core model

- canonical indexing by subsets of internal boundary gaps;
- factorization of every partial response under concatenation;
- exact additivity of first-detection depth on nonzero decomposable states;
- a multiplicative shifted filtration across tensor grades;
- a nine-dimensional algebraic coherence delay at grade four;
- equivariant splitting of equal representation types by factor origin and depth;
- finite termination by depth \(n-1\) from the all-grade decoder.

## 10. Manuscript claim boundary

The paper should not claim that residual depth cannot be represented by any classical or noncommutative control system. Such a claim would be false without a restrictive notion of equivalence.

The strong defensible statement is:

> The residual-depth chain is an observability filtration in the broad joint-kernel sense, but its native structure is an internal-intervention filtration rather than an iterate-of-dynamics filtration. Its model-specific content is the quaternionic slot factorization, additive depth on decomposable concatenations, coherence-induced depth delay, and equivariant separation of equal representation types by factor origin.

This closes Gate B.