# Draft Introduction and Related Work

## 1. Introduction

Compression is usually treated as a map from a larger state space to a smaller visible value space. When that map is non-injective, distinct states collide. The ordinary conclusion is that the distinction has been lost. This paper studies a different possibility: the visible value may be deliberately coarse while the discarded distinction remains exactly recoverable from structured contextual responses.

Let

\[
V=\operatorname{Im}\mathbb H,
\qquad
B_n=V^{\otimes n},
\]

and define reversed quaternionic compression by

\[
m_n(a_1|\cdots|a_n)=a_n\cdots a_1.
\]

The maps \(m_n:B_n\to\mathbb H\) are strongly non-injective for \(n\ge2\). Equality of compressed values therefore does not imply equality of boundary tensors. Rather than quotienting by these collisions, we retain the tensor state and probe it by inserting imaginary quaternions into its internal gaps. The resulting all-gap response is

\[
A_n(a_1|\cdots|a_n)(d_1,\ldots,d_{n-1})
=
 a_n d_{n-1}a_{n-1}\cdots d_1a_1.
\]

Our main theorem states that \(A_n\) is injective for every finite grade. Thus a many-to-one noncommutative value map can coexist with exact state recovery once contextual response data are retained.

The reconstruction is controlled by one local gate,

\[
\Theta:V\otimes\mathbb H\longrightarrow\operatorname{Hom}(V,\mathbb H),
\qquad
\Theta\!\left(\sum_{a=1}^3 e_a\otimes h_a\right)(d)
=
\sum_{a=1}^3e_a d h_a.
\]

This map is an isomorphism. In the standard basis its determinant is \(256\), and its inverse is explicit. Applying \(\Theta^{-1}\) to the final-variable slice of an all-gap response recovers the three lower-grade response functions associated with the outer boundary letter. Repeating the same local step reconstructs the entire tensor in finitely many stages. No separate global inverse is introduced at each grade.

This exact decoder leads to a second structure. Let \(D_n^{\le d}\) denote the response profile obtained from probes of depth at most \(d\), and define

\[
F_d^{(n)}=\ker D_n^{\le d}.
\]

Then

\[
F_0^{(n)}\supseteq F_1^{(n)}\supseteq\cdots\supseteq F_{n-1}^{(n)}=0.
\]

Every nonzero finite state therefore has a first detection depth

\[
\delta(x)=\min\{d:D_n^{\le d}(x)\neq0\}
\le n-1.
\]

The filtration is not a cosmetic restatement of injectivity. At length four, equal representation types can split across different first-detection depths according to factor origin. Moreover, coherent superpositions can remain invisible after every decomposable residual pair has already become visible. Probe depth therefore records structure that is erased both by ordinary compression and by a representation label alone.

Finally, exact-response coordinates compose. If \(F=A_m(x)\) and \(G=A_n(y)\), define

\[
(F\star G)(\mathbf d,\delta,\mathbf e)
=
G(\mathbf e)\,\delta\,F(\mathbf d).
\]

Then

\[
A_m(x)\star A_n(y)=A_{m+n}(x\Vert y),
\]

so the exact-response space is a unital associative graded algebra. This matters because contextual recovery is not merely a collection of isolated measurements: it is compatible with composition of the underlying boundary states.

The contribution is not another decoder for an injective encoding. The visible quaternionic value is genuinely many-to-one. Exactness appears only after retaining structured contextual responses. The combined result is a closed finite model with five simultaneous features:

1. deliberately coarse noncommutative compression;
2. canonical internal contextual probes;
3. one explicit recursive local decoder;
4. finite first-detection depth;
5. composition of exact-response coordinates.

We do not claim that each ingredient is new in isolation. We claim that this explicit combination closes.

## 1.1 Why this formulation matters

The construction separates three notions that are often conflated:

- visible value;
- retained state;
- recoverability under intervention.

The value map \(m_n\) is allowed to forget. The state is not identified with that value. Exact recovery is delegated to a controlled family of queries. In this sense, compression is not equated with erasure.

This separation suggests an architectural interface for systems in which inexpensive summaries are insufficient to identify internal states, but ambiguity can be resolved by finite contextual queries. Potential interfaces include active sensing, structured hidden-state recovery, provenance-preserving summaries, and query-addressable memory. No efficiency theorem is asserted here. Since

\[
\dim B_n=\dim\operatorname{im}A_n=3^n,
\]

Core v1 does not by itself reduce worst-case storage dimension. Practical savings would require additional hypotheses such as sparsity, shallow typical detection depth, selective recovery, generated rather than stored responses, or a distributional model.

## 1.2 Main results

The paper proves the following.

**Local decoder.** The multiplication-defined map

\[
\Theta:V\otimes\mathbb H\to\operatorname{Hom}(V,\mathbb H)
\]

is an isomorphism with explicit inverse. In the standard basis, \(\det\Theta=256\).

**All-grade reconstruction.** For every finite \(n\),

\[
A_n:B_n\xrightarrow{\cong}\mathfrak A_n:=\operatorname{im}A_n.
\]

Equivalently, \(A_n(x)=A_n(y)\) if and only if \(x=y\).

**Finite visibility.** Every nonzero \(x\in B_n\) is detected by depth at most \(n-1\).

**Delayed contextual visibility.** Nonzero states may have zero compressed value and remain invisible at several lower probe depths before reappearing.

**Depth splitting.** At length four, first-detection depth distinguishes factor origins inside equal spin types, and a nine-dimensional coherent survivor appears only at maximal depth.

**Exact-response algebra.** The graded response space carries an explicit bridge product for which

\[
A:T(V)\xrightarrow{\cong}\mathfrak A
\]

is a graded algebra isomorphism.

## 2. Related work

### 2.1 Noncommutative realization theory

Finite realizations of noncommutative rational functions and formal power series are well established. Kaliuzhnyi-Verbovetskyi and Vinnikov develop realization theory and difference-differential calculus for noncommutative rational functions (arXiv:1003.0695). Alpay and Kalyuzhnyi-Verbovetzkii study finite-dimensional realizations, minimality, and structured factorizations for matrix-\(J\)-unitary noncommutative rational formal power series (arXiv:math/0407387). Volčič develops matrix-coefficient realizations of arbitrary noncommutative rational functions, including minimality, obstruction modules, complexity measures, and local-global linear-dependence results (arXiv:1505.07472).

These works establish that finite linear realization of noncommutative data is not new. Our object and direction of reconstruction are different. We begin with a fixed tensor state and a deliberately non-injective quaternionic value map. The enlarged response profile is formed by internal probe insertion, and one multiplication-defined local inverse recursively recovers the original tensor. We do not currently identify the family \((A_n)_n\) with a standard realization of a single noncommutative rational function. Determining whether such a reformulation exists is an open comparison problem.

### 2.2 Weighted automata and Hankel methods

Weighted automata represent rational series, and Hankel matrices govern minimal realization. Balle, Panangaden, and Precup use the singular structure of infinite Hankel matrices to obtain canonical forms and approximate minimizations of weighted automata (arXiv:1501.06841).

The important conceptual precedent is contextual distinguishability: hidden states can be separated by their behavior under extensions. Core v1 also defines state identity through response to context. The difference is geometric. Automata contexts are ordinarily concatenated prefixes or suffixes, whereas our probes are inserted into all internal gaps of a fixed tensor word. The residual-depth filtration measures how many internal contextual layers are required before a state becomes visible. Whether \(A_n\) admits a natural multi-context Hankel formulation is left open.

### 2.3 Observability

Classical systems theory reconstructs hidden states from output families and characterizes unobservable subspaces by rank conditions or Gramians. Davis, Gravagne, Jackson, and Marks provide a unified treatment of controllability, observability, realizability, and stability for linear dynamic systems on general time domains (arXiv:0901.3764).

Our terminology *observability depth* is deliberately analogous, but the present model is not a time-evolving control system. Probe depth counts internal insertions, the state space is graded by tensor length, and noncommutative multiplication order is essential. The kernels \(F_d^{(n)}\) are therefore defined directly from the response family rather than imported from a dynamical realization.

### 2.4 Tensor tomography and active reconstruction

Tensor-network and quantum-state tomography reconstruct structured high-dimensional states from prescribed measurements. Landon-Cardinal, Liu, and Poulin give efficient direct tomography for matrix product states using local operations and structured recovery (arXiv:1002.4632). Teo et al. develop compressive quantum process tomography with adaptive or randomized measurements and informational-completeness certification (arXiv:1911.06122).

These methods are close in reconstruction philosophy but differ in assumptions and goals. They exploit low-rank, low-bond-dimension, positivity, or statistical structure and study measurement complexity or stability. Core v1 works on the full finite tensor grade, gives an exact algebraic inverse, and makes no noise or sample-complexity claim.

### 2.5 Process tensors and intervention slots

Xiang et al. reconstruct a restricted process tensor using a complete family of intervening projections and a final measurement, thereby retaining history-dependent information in a non-Markovian quantum process (arXiv:2105.03333).

This is the closest operational analogy we have found. In both settings, distinctions invisible to a coarse output become observable under controlled interventions inserted at internal stages. The mathematical objects remain different. A process tensor is a physical multi-time quantum map subject to positivity and probabilistic constraints. Our construction is a static quaternionic tensor algebra with an explicit grade-independent local decoder and a first-detection filtration.

### 2.6 Quaternionic multilinear algebra

Flamant, Luciani, Miron, and Zniyed develop a multilinear framework for quaternion arrays and quaternion Tucker and canonical polyadic decompositions (arXiv:2412.05409). Their work confirms that noncommutativity materially changes tensor analysis and uniqueness questions.

Our tensors are real tensors over \(V=\operatorname{Im}\mathbb H\), and quaternion multiplication appears in the response map rather than as scalar multiplication on a quaternion array. We have not found an all-gap response map, a recursive \(\Theta\)-decoder, or an observability-depth filtration in that framework.

### 2.7 Coding-theoretic interface

State-space descriptions and minimal encoders are standard in convolutional coding. Relevant examples include Gluesing-Luerssen and Schneider, *State Space Realizations and Monomial Equivalence for Convolutional Codes* (arXiv:cs/0603049), and Holub, *State spaces of convolutional codes, codings and encoders* (arXiv:1712.01914).

Core v1 is not yet an error-correcting code. It has no channel model, distance, rate, redundancy, error pattern, or noisy decoding theorem. Its coding-theoretic relevance is architectural: equality of visible outputs does not identify hidden states, while structured contextual queries preserve exact distinguishability.

## 2.8 Contribution boundary

We do not claim that every ingredient above is individually novel. In particular:

- finite noncommutative realization is established;
- contextual distinguishability is established in automata and systems;
- active reconstruction is established in tomography;
- intervention slots are established in process-tensor theory;
- quaternionic tensor analysis is established;
- the existence of some vector-space isomorphism between two 12-dimensional spaces is not itself a novelty claim.

What is established here is the explicit closure of the following package in one finite model:

\[
\text{many-to-one quaternionic value}
+
\text{all-gap responses}
+
\text{one recursive local inverse}
+
\text{finite detection depth}
+
\text{exact-response composition}.
\]

Our current literature audit has not located an equivalent construction combining all five features. This is a documented search result, not an absolute priority claim over all mathematical literature.

## 2.9 Open comparison problems

The strongest remaining literature and structural questions are:

1. Can \((A_n)_n\) be represented by a two-sided or multi-context Hankel object?
2. Is \(\Theta\) a standard equivariant isomorphism whose multiplication-defined form has a known name?
3. Does \(F_d^{(n)}\) coincide with an observability-index, Loewy, coradical, or operadic filtration after reformulation?
4. Is there a process-tensor or quantum-comb inversion theorem formally equivalent to all-gap peeling?
5. What is the minimal probe family required for exact reconstruction?
6. Under what structural assumptions can exact contextual recoverability yield a genuine rate or memory-efficiency theorem?
