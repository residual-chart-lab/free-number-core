# Adjacent-literature audit — pass 1

Status: active working document, not a novelty certificate.

This audit compares Free Numbers Core v1 against nearby mathematical frameworks by structure rather than vocabulary. A shared word such as *realization*, *observability*, *tomography*, or *compression* does not imply equivalence. Conversely, unfamiliar terminology does not establish novelty.

The object under audit is the combined package

\[
\bigl(m_n, A_n, \Theta^{-1}, F_d^{(n)}, \star\bigr),
\]

where:

- \(m_n:B_n\to\mathbb H\) is deliberately many-to-one reversed quaternionic compression;
- \(A_n\) records all-gap insertion responses;
- one explicit local inverse \(\Theta^{-1}\) is reused recursively at every finite grade;
- \(F_d^{(n)}\) records first contextual-detection depth;
- exact-response coordinates compose by a unital associative graded product.

The audit question is not whether any one ingredient has precedent. The question is whether an equivalent closed architecture has already been established.

## 1. Comparison axes

Every neighboring source is compared against the same eight axes.

| Axis | Core v1 datum |
|---|---|
| State | a finite boundary tensor \(x\in V^{\otimes n}\) |
| Coarse output | reversed quaternionic product \(m_n(x)\) |
| Non-injectivity | intentional and nontrivial |
| Probe | imaginary-quaternion insertion into selected internal gaps |
| Exact decoder | explicit, finite, recursive, grade-independent local gate |
| Visibility | first-detection filtration ending by depth \(n-1\) |
| Composition | bridge product on exact-response coordinates |
| Efficiency claim | none yet; exactness is proved, compression rate is not |

## 2. Noncommutative rational realization

### 2.1 Kaliuzhnyi-Verbovetskyi and Vinnikov

**Noncommutative rational functions, their difference-differential calculus and realizations**  
arXiv:1003.0695

The paper surveys noncommutative rational functions, their realization theory, and a difference-differential calculus. It confirms that finite linear descriptions of noncommutative functions are an established subject and that realization language is not new.

**Overlap with Core v1**

- noncommutative multiplication is structural rather than cosmetic;
- a complicated object is represented through finite linear data;
- local algebraic operations can control global evaluation behavior.

**Difference currently visible**

- the realized object is a noncommutative rational function, not a fixed tensor state hidden by a deliberately many-to-one quaternionic value map;
- the inputs are matrix tuples or formal variables, not canonical probes inserted into every internal gap of one boundary word;
- no equivalent of the Core first-detection filtration has been located;
- no source-level match to the recursive \(\Theta\)-peeling formula has been located.

**Audit status:** close in language and general philosophy; no equivalence found in pass 1.

### 2.2 Volčič

**Matrix coefficient realization theory of noncommutative rational functions**  
arXiv:1505.07472

Volčič develops realizations of arbitrary noncommutative rational functions, minimality, obstruction modules, matrix evaluations, complexity invariants, and local-global linear-dependence bounds. The paper explicitly connects noncommutative realization to systems, control, automata, and free analysis.

**Overlap with Core v1**

- finite realization of noncommutative data;
- local-global reasoning;
- obstructions to minimal or faithful representation;
- exact identity testing in a noncommutative setting.

**Difference currently visible**

- Core reconstructs a graded tensor representative from an enlarged response profile; it does not minimize a realization of a rational function;
- Volčič's obstruction modules concern reduction and minimality, whereas \(F_d^{(n)}\) measures delayed contextual visibility of a retained state;
- the Core decoder is one fixed twelve-dimensional quaternionic gate reused at every grade;
- the exact-response product is induced by concatenation of boundary tensors, not by composition of rational realizations.

**Main unresolved question:** can the full family \((A_n)_n\) be repackaged as one recognizable generalized series or Sylvester realization? If yes, the paper must say so. Even then, the depth filtration may remain additional structure.

**Audit status:** strongest algebraic neighbor found so far; no direct identification found.

### 2.3 Alpay and Kalyuzhnyi-Verbovetzkii

**Matrix-J-unitary non-commutative rational formal power series**  
arXiv:math/0407387

This work develops finite-dimensional realizations, minimal factorizations, structured Hermitian equations, and uniqueness properties for noncommutative rational formal power series.

**Overlap**

- finite-dimensional noncommutative realization;
- structured inner-product or metric data;
- uniqueness of suitable realizations.

**Difference currently visible**

- no deliberately non-injective quaternionic value projection paired with exact contextual recovery;
- no all-gap probe family;
- no first-detection-depth filtration;
- no recursive outer-letter decoder identified.

**Audit status:** relevant background, not an equivalent architecture in pass 1.

## 3. Weighted automata and Hankel realization

### 3.1 Balle, Panangaden, and Precup

**A Canonical Form for Weighted Automata and Applications to Approximate Minimization**  
arXiv:1501.06841

Weighted finite automata represent rational series. Infinite Hankel matrices govern minimal realizations, canonical forms, and approximate minimization.

**Overlap with Core v1**

- observable behavior can determine a finite hidden representation;
- finite algebraic data support exact or approximate reconstruction;
- a family of contextual extensions distinguishes hidden states;
- minimal realization dimension is an information-bearing invariant.

This is conceptually important: the idea that two prefixes are distinct when some continuation distinguishes them is a genuine precedent for contextual distinguishability.

**Difference currently visible**

- the Core state is not an automaton state or a rational series coefficient;
- the contextual operation is insertion into internal gaps, not continuation at one end of a word;
- the output semiring model does not by itself reproduce reversed quaternionic compression;
- the Core filtration records the minimum number or pattern of internal probes needed for detection, not ordinary Hankel rank;
- no coding or storage advantage follows merely from the Core dimension identity \(\dim B_n=\dim\mathfrak A_n=3^n\).

**Main unresolved question:** is there a two-sided or multi-context Hankel object whose rows and columns reproduce the all-gap response map? This is a serious route and must be tested before the final novelty paragraph.

**Audit status:** strong conceptual neighbor; not yet a formula-level match.

## 4. Classical observability and realization

### 4.1 Davis, Gravagne, Jackson, and Marks

**Controllability, Observability, Realizability, and Stability of Dynamic Linear Systems**  
arXiv:0901.3764

This source develops observability and controllability through Gramians and rank conditions in linear dynamical systems.

**Overlap**

- hidden state is recoverable from a family of outputs;
- kernels of partial observation maps define unobservable subspaces;
- finite rank conditions can certify complete observability.

**Difference currently visible**

- Core has no time evolution in the reconstruction theorem;
- probe depth is combinatorial insertion depth, not elapsed time or successive output time;
- the state space changes with tensor grade;
- noncommutative multiplication and internal insertion order are essential.

**Provisional terminology ruling:** *observability filtration* is defensible as an analogy, but the paper must define it internally and must not imply that Core is merely a standard linear control system in disguise.

## 5. Tensor-state and process tomography

### 5.1 Landon-Cardinal, Liu, and Poulin

**Efficient Direct Tomography for Matrix Product States**  
arXiv:1002.4632

The paper reconstructs matrix product states using efficiently implementable measurements and exploits structured state representations.

**Overlap with Core v1**

- exact or certified recovery of a structured tensor object from a prescribed measurement family;
- local operations can reveal global tensor data;
- reconstruction can be recursive or layerwise.

**Difference currently visible**

- MPS tomography assumes low-bond-dimension structure and studies measurement efficiency;
- Core works on the full finite tensor grade \(V^{\otimes n}\), without low-rank assumptions;
- Core responses are deterministic algebraic evaluations, not sampled physical measurements;
- Core proves exact injectivity but no noise stability or sample-complexity bound.

**Audit status:** useful analogy for reconstruction, not an equivalent theorem.

### 5.2 Teo et al.

**Objective Compressive Quantum Process Tomography**  
arXiv:1911.06122

This work reconstructs rank-deficient quantum processes using adaptive or randomized measurements and certifies informational completeness.

**Overlap**

- active queries rather than one passive output;
- certification that accumulated observations uniquely determine the hidden object;
- a possible distinction between cheap coarse information and expensive exact recovery.

**Difference currently visible**

- efficiency depends on rank deficiency and probabilistic measurement design;
- the target is a completely positive process;
- no quaternionic all-gap product or exact-response algebra appears;
- Core has no compressive-sensing theorem.

**Audit status:** application-side neighbor only.

### 5.3 Xiang et al.

**Quantify the Non-Markovian Process with Intervening Projections in a Superconducting Processor**  
arXiv:2105.03333

A complete set of intervening projections plus final measurement determines a restricted process tensor that retains history-dependent information.

This is the closest operational analogy found in pass 1.

**Overlap with Core v1**

- history invisible to a coarse current-state description can be revealed by controlled interventions;
- intervention slots are internal to a multi-stage process;
- a complete intervention family supports reconstruction;
- hidden memory is operationally defined through response to context.

**Difference currently visible**

- process tensors are physical multi-time quantum maps with positivity and statistical structure;
- Core is a static finite-grade algebraic construction;
- Core probes are imaginary quaternions and the response is reversed multiplication;
- Core proves a grade-independent local decoder and a finite first-detection bound;
- no exact-response bridge algebra has been identified in the process-tensor source.

**Audit status:** very important for terminology and positioning; not an algebraic equivalence.

## 6. Quaternionic tensor analysis

### 6.1 Flamant, Luciani, Miron, and Zniyed

**Multilinear analysis of quaternion arrays: theory and computation**  
arXiv:2412.05409

This paper develops a rigorous multilinear framework for quaternion arrays, including quaternion Tucker and canonical polyadic decompositions and uniqueness questions under noncommutativity.

**Overlap with Core v1**

- quaternionic noncommutativity changes tensor algebra materially;
- multilinearity must be stated carefully over real and quaternionic scalars;
- uniqueness and reconstruction of quaternion-valued tensor structure are central.

**Difference currently visible**

- Core tensors are real tensors over the imaginary quaternion module, not quaternion arrays reconstructed by low-rank decomposition;
- Core uses ordered internal probe insertion and reversed multiplication;
- no all-gap response map, local \(\Theta\) decoder, or visibility-depth filtration has been located.

**Audit status:** establishes that quaternion tensor analysis is an active neighboring field; no duplicate construction found.

## 7. Coding theory

The initial map includes state-space realizations of convolutional codes, including:

- Gluesing-Luerssen and Schneider, **State Space Realizations and Monomial Equivalence for Convolutional Codes**, arXiv:cs/0603049;
- Holub, **State spaces of convolutional codes, codings and encoders**, arXiv:1712.01914.

These sources are relevant because they formalize encoders, state spaces, and equivalence. However, Core v1 currently has:

- no channel model;
- no minimum distance;
- no error pattern;
- no redundancy or rate theorem;
- no noisy decoding theorem.

Therefore Core v1 is **not yet an error-correcting code**. The coding-theory interface is architectural: a deliberately coarse visible value coexists with a richer queryable state.

The strongest defensible application sentence is:

> The construction suggests coding-like architectures in which equality of coarse outputs does not identify internal states, while structured contextual queries retain exact distinguishability.

It must not say that such an architecture is memory-efficient until a rate, sparsity, selective-recovery, or average-depth theorem is proved.

## 8. Formula-level risk audit

The literature search did not expose an equivalent package, but several components may be more standard than their current presentation suggests.

### 8.1 The local decoder may be a natural representation-theoretic isomorphism

The fact that

\[
\Theta:V\otimes\mathbb H\to\operatorname{Hom}(V,\mathbb H)
\]

is an isomorphism is dimensionally plausible and may be expressible as a standard \(SO(3)\)- or \(SU(2)\)-equivariant identification. Its explicit inverse and determinant remain useful, but the manuscript should not sell the mere existence of a 12-dimensional vector-space isomorphism as novelty.

What is stronger is that this particular multiplication-defined map is invertible and recursively peels the exact-response tensor.

### 8.2 The exact-response product is partly transported structure

Once \(A=\bigoplus A_n\) is injective and the product is defined so that

\[
A_m(x)\star A_n(y)=A_{m+n}(x\Vert y),
\]

associativity follows from concatenation. This is mathematically valid, but reviewers may regard it as transport of structure rather than an independent surprise.

The paper should emphasize the explicit bridge formula and compatibility with compression, not oversell associativity alone.

### 8.3 The most distinctive object may be the depth filtration

The length-four calculations show that equal representation types can first appear at different probe depths according to factor origin, and that coherent superpositions can remain invisible after decomposable residual pairs are already detected.

This is more specific than generic observability and may be the sharpest novel-looking feature of the package.

### 8.4 Exactness is not compression efficiency

Because

\[
\dim B_n=\dim\mathfrak A_n=3^n,
\]

Core v1 does not prove that fewer real numbers store the same data. Any memory-efficiency claim requires additional structure such as:

- sparse response coordinates;
- shallow typical detection depth;
- on-demand generation of responses;
- selective rather than complete recovery;
- a distributional or average-case model;
- a noise and condition-number analysis.

## 9. Pass-1 comparison matrix

Legend: **Y** = explicit in source family; **A** = analogous but materially different; **N/F** = not found in pass 1.

| Framework | Deliberately many-to-one coarse value | Internal contextual probes | Fixed recursive local inverse | First-detection filtration | Exact-response composition |
|---|---:|---:|---:|---:|---:|
| NC rational realization | N/F | A | A | N/F | A |
| Weighted automata / Hankel | A | A, mainly end-contexts | N/F | A | A |
| Linear observability | A | A, controlled inputs/outputs | A | A | N/F |
| Tensor-state tomography | N/F | A | A | N/F | N/F |
| Process tensors | A | Y, intervention slots | N/F | A | A |
| Quaternion tensor decomposition | N/F | N/F | A | N/F | N/F |
| Core v1 | Y | Y | Y | Y | Y |

This table is a working comparison, not proof of novelty.

## 10. Current contribution boundary

### Established neighboring ideas

The following are known in broad form and must be credited:

- finite realization of noncommutative functions;
- observability through families of outputs;
- contextual distinguishability in automata and state-space models;
- reconstruction of structured tensor states from measurements;
- intervention-based recovery of history-dependent processes;
- quaternionic multilinear algebra and representation-theoretic decompositions.

### Established by Core v1

The manuscript can state without hesitation that it proves, for its explicit model:

1. reversed quaternionic compression is genuinely non-injective;
2. canonical all-gap insertion response is injective at every finite grade;
3. one explicit multiplication-defined local inverse recursively decodes every grade;
4. every nonzero state is visible by depth at most \(n-1\);
5. zero-valued nonzero states can have delayed contextual visibility;
6. representation types can split by first-detection depth and factor origin;
7. exact-response coordinates admit an explicit bridge product compatible with concatenation.

### Still historically unresolved

Pass 1 has not established:

- absolute priority;
- absence of an equivalent construction under different terminology;
- minimality of the all-gap probe family;
- novelty of the local \(\Theta\) isomorphism in isolation;
- an information-theoretic rate advantage;
- numerical stability or practical memory savings.

## 11. Provisional manuscript sentence

The following sentence is now supportable as a documented search result, provided the paper cites the neighboring areas above:

> We have not located in the reviewed noncommutative-realization, weighted-automata, observability, tomography, process-tensor, coding, or quaternionic-tensor literature an equivalent construction that combines a deliberately many-to-one reversed quaternionic value map, canonical all-gap insertion responses, one grade-independent recursive local decoder, a finite first-detection-depth filtration, and an explicit associative composition law on exact-response coordinates.

This is stronger and safer than “this is the first construction of its kind.”

## 12. Next audit pass

1. Recast \(A_n\) as a multi-context Hankel object and test recognizability.
2. Derive the representation-theoretic decomposition of \(\Theta\) to separate standard isomorphism from model-specific content.
3. Compare \(F_d^{(n)}\) with observability indices, Loewy filtrations, and coradical-type filtrations.
4. Search process-tensor and quantum-comb literature for exact finite intervention bases and recursive inversion formulas.
5. Search operad, planar algebra, and tensor-category literature for internal-slot insertion maps with transported composition.
6. Only after these checks, freeze the Related Work and novelty paragraph.
