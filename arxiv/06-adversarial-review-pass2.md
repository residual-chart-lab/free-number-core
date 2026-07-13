# Adversarial manuscript review — pass 2

Status: internal type-and-proof audit of the arXiv-facing manuscript. This is not an external referee report.

## Verdict

No fatal error was found in the central theorem chain:

1. the local map \(\Theta\) has the stated explicit inverse;
2. the inverse recursively peels the all-gap response and proves injectivity of \(A_n\) at every finite grade;
3. partial responses factor under concatenation;
4. the division-algebra property of \(\mathbb H\) gives exact additivity of first-detection depth on nonzero decomposable states;
5. the grade-four nine-dimensional survivor is identified as the spin-four Cartan-product sector by equivariance, target-spin bounds, and exact integer rank, rather than by dimension count alone.

The second pass did not open a new research gate. It repaired type declarations, quantifiers, and proof packaging.

## Repairs made in v0.2

### 1. Determinant statement

The manuscript now separates:

- the numerical determinant \(256\) in explicitly named standard domain and evaluation bases;
- the invariant representation-theoretic statement that every irreducible block of \(\Theta\) is nonzero and invertible.

This removes an implicit basis-normalization ambiguity.

### 2. Partial responses

Every map \(D_S\) is now defined by an explicit formula, with the quaternionic unit inserted at unprobed gaps. The ordering of probe variables is fixed.

An equivariance lemma was added, proving that all residual-depth kernels are \(SO(3)\)-submodules.

### 3. Positive-grade quantifiers and bridge variables

The factorization law, bridge product, and depth-additivity theorem now state \(m,n\ge1\) explicitly. The selected-gap sets on the left and right factors, the bridge index, and the order of multilinear variables are specified.

### 4. Multiplicative filtration

The shifted-filtration inclusion

\[
G_p^{(m)}\otimes G_q^{(n)}\subseteq G_{p+q}^{(m+n)}
\]

now has a proof: decomposable tensors satisfy exact depth additivity, such tensors span the tensor product, and the target filtration piece is linear.

### 5. Grade-four survivor

The proof now uses three ingredients explicitly:

- \(S_0^4V\cong V_4\) is the Cartan-product summand of \(V_2\otimes V_2\);
- a depth-\(r\) response has target spin at most \(r+1\), so all responses through depth two kill \(V_4\);
- the exact integer response matrix gives \(\dim F_2^{(4)}=9\).

Together these identify \(F_2^{(4)}=S_0^4V\), without treating rank count as the sole argument.

The manuscript also explains why the other two depth-two gap choices vanish on \(R\otimes R\), leaving the \(\{1,3\}\) channel as the only potentially nonzero one.

### 6. Equivariant depth layers

The sectorwise first-detection layers are now stated as a corollary and justified by Clebsch--Gordan decompositions, target-spin bounds, and the exact sector-kernel dimensions.

### 7. Exact certificates

An appendix specifies the integer matrices used for:

- the \(12\times12\) matrix of \(\Theta\);
- the grade-four response matrices through depths zero to three;
- the restrictions to \(P\otimes P\), \(P\otimes R\), \(R\otimes P\), and \(R\otimes R\).

The accompanying SymPy scripts use exact arithmetic and reproduce all displayed ranks and determinants.

## Verification

The modular v0.2 source compiles twice under TeX Live to a 15-page A4 PDF. The final log contains no undefined references, citation warnings, overfull boxes, or compilation errors. All pages were rendered and visually checked for clipping, overlap, and broken glyphs.

The exact certificates return:

- \(\operatorname{rank}\Theta=12\), \(\det\Theta=256\);
- grade-four ranks \(4,32,72,81\);
- grade-four kernel dimensions \(77,49,9,0\);
- the stated sectorwise kernel dimensions at every depth.

## Remaining blockers

The remaining blockers are not mathematical extensions:

- bibliographic normalization and verification against final published records;
- individual author identity versus the project label;
- manuscript license;
- primary arXiv category and possible cross-list;
- endorsement/account status;
- final statement of the relationship to the Zenodo Core v1 artifact.

No arXiv submission or external review has occurred.
