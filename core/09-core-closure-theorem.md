# Free Numbers Core v1 — Closure Theorem

**Status:** closure declaration for the first standalone Free Numbers core  
**Version:** `Free Numbers Core v1`  
**Branch:** `core-reconstruction`  
**Depends on:** `core/00-capability-ledger.md` through `core/08-all-grade-response-reconstruction.md`  
**Realization:** quaternionic exact-response core

## 0. Closure verdict

The first standalone Free Numbers core is closed.

The object being closed is not a universal classification of every possible Free Numbers model. It is the first complete, exact, compositional realization:

\[
\boxed{
\text{Free Numbers Core v1}
=
\text{Quaternionic Exact-Response Core}.
}
\]

It consists of:

- a graded carrier;
- a non-injective quaternionic compression;
- admissible contextual responses with finite detection depth;
- a canonical exact response coordinate in every finite grade;
- an explicit recursive decoder;
- a uniform associative composition law;
- a standalone composition-compatible equality;
- and a strict separation from the Residual Chart OS and originating interpretation.

The residual-depth spectrum remains open. The reconstruction and composition problem does not.

---

## 1. Underlying graded representatives

Let

\[
V=\operatorname{Im}\mathbb H
\]

with its Euclidean metric and quaternionic orientation.

For every \(n\ge1\), define

\[
B_n=V^{\otimes n}.
\]

Introduce the grade-zero sector

\[
B_0=\mathbb R\mathbf 1,
\]

where \(\mathbf 1\) is the empty boundary word.

The full representative carrier is the tensor algebra

\[
T(V)
=
\bigoplus_{n\ge0}B_n.
\]

Composition is concatenation:

\[
\Vert:B_m\times B_n\longrightarrow B_{m+n}.
\]

It is strictly associative and has unit \(\mathbf 1\in B_0\).

The grade is additive:

\[
\deg(x\Vert y)=\deg x+\deg y.
\]

No deletion or grade-reducing operation belongs to Core v1.

---

## 2. Compression and contextual response

For \(n\ge1\), reversed quaternionic compression is

\[
\boxed{
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
}
\]

At grade zero, set

\[
m_0(\lambda\mathbf1)=\lambda.
\]

Compression is not equality. In particular, for \(n\ge2\), its kernel contains nonzero states.

For a pure word, the canonical all-gap response is

\[
\boxed{
A_n(a_1|\cdots|a_n)(d_1,\ldots,d_{n-1})
=
a_nd_{n-1}a_{n-1}\cdots d_1a_1.
}
\]

Set

\[
A_0(\lambda\mathbf1)=\lambda,
\qquad
A_1(a)=a.
\]

The maps \(A_n\) are admissible finite-depth observations: \(A_n\) inserts one probe in every original internal gap and compresses.

---

## 3. Exact response coordinate spaces

For every \(n\ge1\), define

\[
\mathfrak A_n:=\operatorname{im}A_n
\subseteq
\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H),
\]

and set

\[
\mathfrak A_0:=\mathbb R.
\]

The All-Grade Reconstruction Theorem proves

\[
\boxed{
A_n:B_n\xrightarrow{\cong}\mathfrak A_n
}
\]

for every finite \(n\ge0\).

Hence

\[
\dim\mathfrak A_n=3^n
\qquad(n\ge0).
\]

Define the full exact-response carrier

\[
\boxed{
\mathfrak A
=
\bigoplus_{n\ge0}\mathfrak A_n.
}
\]

A finite Free Number may be represented without loss either by

\[
x\in B_n
\]

or by its exact response coordinate

\[
F=A_n(x)\in\mathfrak A_n.
\]

---

## 4. The local decoder and all-grade reconstruction

The local decoding map is

\[
\Theta:V\otimes\mathbb H
\longrightarrow
\operatorname{Hom}(V,\mathbb H),
\]

\[
\Theta\!\left(\sum_{a=1}^3e_a\otimes h_a\right)(d)
=
\sum_{a=1}^3e_adh_a.
\]

It is a real-linear isomorphism with

\[
\boxed{
\det\Theta=256.
}
\]

Its inverse is explicit:

\[
\boxed{
h_a
=
\frac12\sum_{b,c=1}^3
\varepsilon_{abc}\,e_bF(e_c).
}
\]

If

\[
x=\sum_{a=1}^3x_a|e_a\in B_n,
\]

then

\[
A_n(x)(\mathbf d,d)
=
\sum_{a=1}^3e_adA_{n-1}(x_a)(\mathbf d).
\]

Applying \(\Theta^{-1}\) to the final-variable slice recovers all three functions

\[
A_{n-1}(x_a).
\]

Repeating the same local inverse recursively recovers every boundary letter and therefore the whole representative.

### Theorem 4.1 — Finite all-grade reconstruction

For every finite \(n\ge0\),

\[
\boxed{
A_n(x)=A_n(y)
\iff
x=y.
}
\]

Consequently,

\[
\boxed{
A_n(x)=0
\Longrightarrow
x=0.
}
\]

There are no absolutely invisible nonzero finite representatives once the all-gap response is admitted.

Every nonzero state of grade \(n\) is detected by depth at most

\[
n-1.
\]

---

## 5. Exact response product and unit

For positive grades, let

\[
F\in\mathfrak A_m,
\qquad
G\in\mathfrak A_n.
\]

Define

\[
\boxed{
(F\star G)(\mathbf d,\delta,\mathbf e)
=
G(\mathbf e)\,\delta\,F(\mathbf d).
}
\]

The ordered bridge variable \(\delta\in V\) occupies the new gap between the two factors.

For the grade-zero sector, define

\[
\lambda\star F=\lambda F,
\qquad
F\star\lambda=\lambda F
\qquad(\lambda\in\mathbb R).
\]

Then

\[
1\in\mathfrak A_0
\]

is a two-sided unit.

The uniform factorization theorem gives

\[
\boxed{
A_{m+n}(x\Vert y)
=
A_m(x)\star A_n(y).
}
\]

The product is bilinear, grade-preserving, and strictly associative:

\[
(F\star G)\star H
=
F\star(G\star H).
\]

Therefore:

### Theorem 5.1 — Exact-response algebra

\[
\boxed{
(\mathfrak A,\star,1)
}
\]

is a unital associative graded real algebra, and

\[
\boxed{
A:T(V)\xrightarrow{\cong}\mathfrak A
}
\]

is a graded algebra isomorphism.

This isomorphism does not exhaust the Free Numbers structure. Core v1 also retains the distinguished compression maps, probe family, zero fibers, and depth filtration.

---

## 6. Transported observations

Every observation on representatives transports uniquely to exact response coordinates.

For compression, define

\[
\boxed{
\mu_n
:=
m_n\circ A_n^{-1}:
\mathfrak A_n\longrightarrow\mathbb H.
}
\]

For any admissible linear observation

\[
O:B_n\to W,
\]

define

\[
\widehat O
:=
O\circ A_n^{-1}:
\mathfrak A_n\to W.
\]

Then

\[
O=\widehat O\circ A_n.
\]

Thus the exact coordinate contains:

- compressed quaternionic value;
- every lower-depth response;
- every residual distinction erased by compression;
- and the full representative itself.

The exact coordinate is complete, while the lower-depth profile remains useful for measuring when each component first becomes visible.

---

## 7. Standalone equality

Define equality in Core v1 by literal equality inside each exact response space:

\[
F=G
\qquad(F,G\in\mathfrak A_n).
\]

Equivalently, on representatives,

\[
x\equiv_{\mathrm{v1}}y
\iff
A_n(x)=A_n(y).
\]

By injectivity,

\[
\boxed{
x\equiv_{\mathrm{v1}}y
\iff
x=y.
}
\]

Because the all-gap response is admissible, full finite observational equivalence also collapses to the same relation:

\[
\boxed{
x\equiv_{\mathrm{obs}}y
\iff
A_n(x)=A_n(y)
\iff
x=y.
}
\]

This equality is compatible with:

- grade;
- addition;
- compression;
- every admitted probe;
- and composition.

In particular,

\[
F=F',\quad G=G'
\Longrightarrow
F\star G=F'\star G'.
\]

No quotient by compressed value is admitted.

---

## 8. Zero fibers and active zero states

Define the grade-\(n\) zero fiber by

\[
\boxed{
Z_n:=\ker\mu_n
\subseteq\mathfrak A_n.
}
\]

The additive zero is the zero element of \(\mathfrak A_n\).

An active zero state is any

\[
F\in Z_n\setminus\{0\}.
\]

At grade two,

\[
Z_2\cong S^2_0V,
\]

and the canonical internal response is nonzero on every nonzero element:

\[
A_2(S)=-2C_S.
\]

At grade four, nonzero pure residual pairs satisfy

\[
\mu_4(A_4(S|T))=0,
\]

all depth-one responses vanish, and the cross-boundary depth-two response is

\[
D_{13}(S|T)(d_1,d_2)=4T(d_2)S(d_1)\ne0.
\]

Thus zero compressed value is not zero state, and residual composition can generate new detection depth without changing the compressed value.

The notation

\[
0[\lambda]
\]

is not part of Core v1 unless a separate construction

\[
\lambda\mapsto z_\lambda
\]

is supplied. Active zero states are proved; arbitrary external condition labels are not.

---

## 9. Residual-depth filtration

Let

\[
D_n^{\le d}
\]

denote the combined response profile through probe depth \(d\), and define

\[
F_d^{(n)}:=\ker D_n^{\le d}.
\]

Then

\[
F_0^{(n)}
\supseteq
F_1^{(n)}
\supseteq
\cdots
\supseteq
F_{n-1}^{(n)}=0.
\]

The first-detection depth of a nonzero state is

\[
\delta(x)
=
\min\{d:D_n^{\le d}(x)\ne0\}.
\]

Core v1 contains this filtration as part of its structure.

What is closed:

\[
\boxed{
\delta(x)\le n-1
\qquad(x\in B_n\setminus\{0\}).
}
\]

What remains open is the classification of the intermediate quotients

\[
F_{d-1}^{(n)}/F_d^{(n)}
\]

by spin, multiplicity, factor origin, and probe depth.

The depth spectrum is a research program inside the closed core, not a missing axiom of the core.

---

## 10. Capability Ledger audit

### C1. Result-conditioned history distinction — PASS

States with the same compressed value may have different exact responses. Grade-two active zero states and grade-four residual collisions are explicit witnesses.

### C2. Non-collapsing compression — PASS

The fibers of \(\mu_n\) remain inside \(\mathfrak A_n\). Compression never defines equality.

### C3. Contextual re-observability — PASS

Every nonzero finite state is recovered by an admissible all-gap context. Explicit lower-depth resurrection is already proved at grades two through four.

### C4. Residual depth — PASS

The descending filtration \(F_d^{(n)}\) and first-detection depth \(\delta\) are defined. Termination by depth \(n-1\) is proved.

### C5. Compositional propagation — PASS

Exact coordinates compose by the uniform bridge product \(\star\).

### C6. Closure with remainder — PASS

The compressed value \(\mu_n(F)\) and everything omitted by it coexist inside the exact coordinate \(F\).

### C7. Reinterpretation without deletion — PASS

Grade is retained and additive. No operation in Core v1 erases structural length. Later observation does not delete the representative that produced it.

### C8. Standalone equality — PASS

Exact response equality is finite, composition-compatible, and stronger than quaternionic value equality.

### C9. Finite observability where possible — PASS

Every finite grade has the complete finite certificate \(A_n\), with explicit recursive decoding.

### C10. Quaternionic recovery without quaternionic confinement — PASS

Quaternionic value is recovered by \(\mu_n\), but the full grade-\(n\) space has dimension \(3^n\) and is not identified with \(\mathbb H\).

Therefore:

### Theorem 10.1 — Capability closure

\[
\boxed{
\text{Free Numbers Core v1 satisfies C1--C10.}
}
\]

---

## 11. Standalone independence

Every primitive and theorem of Core v1 is stated using only:

- real vector spaces;
- the quaternion algebra;
- tensor powers;
- multilinear response maps;
- graded composition;
- compression;
- contextual probes;
- and exact equality.

No theorem depends on:

- the Time Engine;
- a future endpoint;
- consciousness;
- ethics;
- ASI;
- Y-axis terminology;
- a chart registry;
- or normalization machinery.

The originating interpretation explains why these capabilities were sought. It does not define or prove them.

Thus the closure criterion of the Capability Ledger is satisfied by this concrete standalone theory:

\[
\boxed{
\text{the required capabilities are definable, computable, and provable without the originating interpretation.}
}
\]

---

## 12. Boundary of Core v1

The following belong to Core v1:

1. the graded exact-response algebra \((\mathfrak A,\star,1)\);
2. reversed quaternionic compression \(\mu_n\);
3. admissible insertion and response profiles;
4. the residual-depth filtration;
5. active zero fibers;
6. the local decoder \(\Theta^{-1}\);
7. all-grade reconstruction;
8. exact composition and equality.

The following do not belong to Core v1:

1. a universal or initial characterization among all possible Free Numbers models;
2. a closed formula for the full spin-multiplicity-depth spectrum;
3. infinite words, completions, or limiting response objects;
4. a canonical external condition assignment \(\lambda\mapsto z_\lambda\);
5. Residual Chart OS registries, provenance, normalization, or certified rewriting;
6. Time Engine, Y-axis, causal, conscious, ethical, or physical interpretation;
7. claims that every future realization must be quaternionic.

These exclusions do not prevent closure. They define the next research programs.

---

## 13. Core Closure Theorem

### Theorem 13.1 — Free Numbers Core v1

Let

\[
\mathfrak F_{\mathrm{v1}}
=
\left(
\mathfrak A,
\star,
1,
\deg,
(\mu_n)_{n\ge0},
\mathcal P,
(F_d^{(n)})
\right)
\]

be the quaternionic exact-response package defined above.

Then:

1. \(\mathfrak A\) is a unital associative graded real algebra;
2. every finite representative has a unique exact response coordinate;
3. the coordinate is decoded recursively without information loss;
4. every finite nonzero state is visible at some depth at most \(n-1\);
5. compression is non-injective but does not destroy the retained state;
6. zero-valued nonzero states exist and compose nontrivially;
7. exact coordinates compose uniformly by \(\star\);
8. exact equality is a composition-compatible standalone equality;
9. quaternionic value is recovered without confining the full object to \(\mathbb H\);
10. C1--C10 are satisfied without dependence on the Residual Chart OS or originating interpretation.

Therefore:

\[
\boxed{
\mathfrak F_{\mathrm{v1}}
\text{ is a complete standalone Free Numbers core.}
}
\]

This closure is model-first rather than universal:

\[
\boxed{
\text{first complete core}
\ne
\text{final classification of all cores}.
}
\]

---

## 14. Stopping rule

The first reconstruction cycle stops here.

Further computation of

\[
n=5,6,\ldots
\]

spin-depth tables is not required to validate Core v1.

The closed question is:

\[
\boxed{
\text{Can every finite state be represented, reconstructed, compared, and composed without losing compression-hidden structure?}
}
\]

The answer is yes.

The open question is:

\[
\boxed{
\text{How is that structure distributed across the residual-depth spectrum?}
}
\]

That is the next research program.

---

## 15. Final declaration

\[
\boxed{
\textbf{Free Numbers Core v1 is closed.}
}
\]

The core is finite-grade complete, recursively decodable, compositionally closed, and standalone.

The mine remains open.

The foundation does not.
