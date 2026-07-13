# arXiv manuscript build plan

Status: active plan for draft PR #9.

## Target manuscript

Working title:

**Exact Reconstruction under Noncommutative Quaternionic Compression**

Working subtitle:

**Finite-Grade Contextual Responses, Recursive Decoding, and Observability Depth**

Target length: approximately 16–22 pages including references and compact appendices.

Primary mathematical audience: noncommutative algebra and realization theory.

Secondary audience: information theory, coding, tomography, and structured memory.

## Section order

### 1. Introduction

- many-to-one compression versus recoverable distinction;
- exact statement of the model;
- one-paragraph theorem map;
- strong but bounded contribution claim;
- application signal without efficiency claim.

### 2. Relation to existing frameworks

- noncommutative rational realization;
- weighted automata and Hankel methods;
- observability;
- tensor/process tomography;
- quaternionic multilinear algebra;
- coding-theoretic interface;
- explicit contribution boundary.

### 3. Quaternionic boundary tensors

- \(V=\operatorname{Im}\mathbb H\);
- tensor grades \(B_n=V^{\otimes n}\);
- reversed compression \(m_n\);
- examples of collisions and active zero states.

### 4. Canonical contextual responses

- selected-gap insertion maps;
- all-gap response \(A_n\);
- response spaces \(\mathfrak A_n\);
- equivariance and basis conventions.

### 5. The local decoder

- definition of \(\Theta\);
- explicit inverse;
- determinant \(256\) in the standard basis;
- representation-theoretic decomposition of \(\Theta\);
- precise statement of what is basis-dependent and basis-independent.

### 6. All-grade exact reconstruction

- peeling identity;
- induction theorem;
- rank and dimension corollaries;
- finite reconstruction algorithm;
- operation-count upper bound if derivable without overselling complexity.

### 7. Observability-depth filtration

- partial response profiles \(D_n^{\le d}\);
- kernels \(F_d^{(n)}\);
- first detection depth \(\delta(x)\);
- termination by depth \(n-1\);
- distinction from ordinary observability indices.

### 8. Exact-response composition

- bridge product;
- compatibility with concatenation;
- unital associativity;
- compression map in exact-response coordinates;
- warning that associativity is partly transported structure.

### 9. Low-grade structure and delayed visibility

- grade two residual kernel;
- grade three highest-spin survivor;
- grade four factor-origin decomposition;
- exact table \(81\to77\to49\to9\to0\);
- depth splitting of equal spin types;
- coherent nine-dimensional depth-three survivor.

### 10. Discussion and open problems

- multi-context Hankel reformulation;
- minimal probe family;
- stability and condition number;
- other associative algebras;
- selective recovery and query-addressable memory;
- coding rate and noisy decoding as future problems;
- no Time Engine in this manuscript.

## Required figures and tables

1. **Peeling ladder:** one \(\Theta^{-1}\) step reused recursively.
2. **Compression versus response:** many-to-one \(m_n\), injective \(A_n\).
3. **Visibility filtration:** \(F_0^{(n)}\supseteq\cdots\supseteq0\).
4. **Length-four table:** sector dimensions and remaining kernels.
5. Optional: factor-origin diagram for \(VV\), \(VR\), \(RV\), \(RR\).

## Review gates

### Gate A — formula audit

- independently recompute \(\Theta\), its inverse, and determinant;
- decompose \(\Theta\) into irreducible \(SO(3)\) sectors;
- verify every sign and tensor-order convention;
- separate natural vector-space facts from model-specific facts.

### Gate B — theorem dependency audit

- every theorem lists exact hypotheses;
- no rank count is used as a sole subspace-identification argument;
- computational certificates are labelled as such;
- open classifications remain open.

### Gate C — literature audit

- each Related Work paragraph cites a primary source;
- no absolute firstness claim;
- multi-context Hankel, process tensor, operad, and quaternion tensor searches completed;
- novelty sentence matches documented findings.

### Gate D — hostile-reader audit

Three simulated reviewers:

1. noncommutative algebraist: “Is this transported tensor algebra with decorative language?”
2. realization theorist: “Is this a standard observable realization or Hankel representation?”
3. information theorist: “Where are rate, noise, redundancy, and complexity?”

The paper must answer all three without changing its scope.

### Gate E — release audit

- clean standalone LaTeX source;
- bibliography resolves;
- PDF builds without warnings that affect output;
- theorem numbering and hyperlinks verified;
- source package contains only submission files;
- author, category, abstract, and comments approved before any upload.

## Immediate build order

1. Complete formula-level decomposition of \(\Theta\).
2. Freeze Introduction and Related Work.
3. Construct the standalone LaTeX manuscript.
4. Port audited Core v1 proofs and low-grade certificates.
5. Run hostile-reader audit.
6. Build final PDF and submission source bundle.
7. Stop for explicit human approval before arXiv upload.
