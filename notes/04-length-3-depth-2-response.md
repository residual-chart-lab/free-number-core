# Length-3 Residuals at Probe Depth 2

This note records the first vertical step of the residual filtration.

In `notes/03-length-2-and-3-residual-filtration.md`, we established that the length-3 next-null residual is

$$
K_3^{null}=S^3_0V.
$$
Thus the highest-spin component $S^3_0V$ is invisible to the length-3 compression $m_3$ and also invisible to the depth-1 internal insertion response. Here we show that this same residual becomes visible at probe depth 2. The result is intentionally limited to length 3 and probe depth 2. We do not claim a general ladder theorem in this note. --- ## 1. Setup Let
$$
V=\mathrm{Im}\,\mathbb{H}=\mathrm{span}_{\mathbb{R}}\{i,j,k\}.
$$
Let
$$
B_3=V^{\otimes3}.
$$
For a boundary word $a|b|c$, the reversed compression is
$$
m_3(a|b|c)=cba.
$$
The previous note showed that the full depth-1 internal insertion response cannot see the highest-spin component
$$
S^3_0V.
$$
Equivalently,
$$
S^3_0V=K_3^{null}.
$$
The question here is whether this residual is invisible forever, or only invisible at probe depth 1. --- ## 2. Full depth-2 insertion profile The full depth-2 insertion profile consists of all maps obtained by inserting two probe variables into a length-3 boundary word and then applying the length-5 reversed compression $m_5$. For this note, we only need one component of that full profile. For a word
$$
e_a|e_b|e_c,
$$
take the internal-internal double insertion
$$
e_a|x|e_b|y|e_c.
$$
After reversed compression, this gives
$$
m_5(e_a|x|e_b|y|e_c)=e_cye_bxe_a.
$$
Define the corresponding component $A_3$ by linear extension:
$$
A_3(T)(x,y)=\sum_{a,b,c}T_{abc}\,e_cye_bxe_a.
$$
Here
$$
T=\sum_{a,b,c}T_{abc}\,e_a|e_b|e_c.
$$
Important: this note does not claim that other depth-2 insertion components vanish. We only use the following safe implication: if one component of the full depth-2 profile is injective on a subspace, then the full depth-2 profile detects that subspace. Thus $A_3$ is used as an internal-internal component of the canonical full profile, not as an arbitrary replacement for the full profile. --- ## 3. The contraction embedding For
$$
S\in S^3_0V,
$$
we view $S$ as a symmetric trace-free third-order tensor. Its ordinary two-variable contraction is the map
$$
C_S:V\otimes V\to V
$$
defined by
$$
C_S(x,y)=S(x,y).
$$
In coordinates,
$$
C_S(x,y)=\sum_{a,b,c}S_{abc}\,x_a y_b e_c.
$$
Since $V\subset\mathbb{H}$, we also view this as a map
$$
C_S:V\otimes V\to\mathbb{H}.
$$
Thus there is a natural embedding
$$
C:S^3_0V\to\mathrm{Hom}(V^{\otimes2},\mathbb{H}).
$$
When we write $A_3=4\,\mathrm{id}$ on $S^3_0V$, the precise meaning is
$$
A_3(S)=4C_S.
$$
--- ## 4. Depth 2 contains spin 3 At depth 1, the response codomain is
$$
\mathrm{Hom}(V,\mathbb{H}).
$$
As an $SO(3)$-representation,
$$
\mathrm{Hom}(V,\mathbb{H})\simeq V_0\oplus2V_1\oplus V_2.
$$
There is no $V_3$ component. This is why $S^3_0V=V_3$ is invisible at depth 1. At depth 2, the codomain becomes
$$
\mathrm{Hom}(V^{\otimes2},\mathbb{H}).
$$
Using
$$
V\otimes V\simeq V_0\oplus V_1\oplus V_2
$$
and
$$
\mathbb{H}\simeq V_0\oplus V_1,
$$
we get
$$
\mathrm{Hom}(V^{\otimes2},\mathbb{H})\simeq2V_0\oplus4V_1\oplus3V_2\oplus V_3.
$$
Thus, unlike depth 1, the depth-2 response codomain contains a $V_3$ component. This does not by itself prove visibility. It only shows that visibility of $S^3_0V$ becomes representation-theoretically possible at depth 2. The actual nonzero coefficient is computed below. --- ## 5. Main result For every
$$
S\in S^3_0V,
$$
the internal-internal depth-2 component $A_3$ satisfies
$$
A_3(S)=4C_S.
$$
Equivalently, for all $x,y\in V$,
$$
A_3(S)(x,y)=4S(x,y).
$$
Therefore $A_3$ is injective on $S^3_0V$. Since $A_3$ is one component of the full depth-2 insertion profile, the full depth-2 profile detects the entire length-3 next-null residual
$$
K_3^{null}=S^3_0V.
$$
In words: length-3 highest-spin residuals are invisible at probe depth 1, but visible at probe depth 2. --- ## 6. Example calculation Consider
$$
S=i|i|i-i|j|j-j|i|j-j|j|i.
$$
This is the harmonic cubic component corresponding to $x^3-3xy^2$, hence
$$
S\in S^3_0V.
$$
From note 03, this element is invisible at depth 1:
$$
m_3(S)=0,
$$
and
$$
R_3^{(1)}(S)=0,\qquad R_3^{(2)}(S)=0.
$$
Now evaluate the depth-2 component $A_3$. For $x=y=i$,
$$
A_3(S)(i,i)=4i.
$$
Also,
$$
S(i,i)=i.
$$
Thus
$$
A_3(S)(i,i)=4S(i,i).
$$
Similarly,
$$
A_3(S)(i,j)=-4j,
$$
and
$$
A_3(S)(j,j)=-4i.
$$
These agree with
$$
4S(i,j),\qquad4S(j,j).
$$
The full exact basis check below verifies the identity on all seven basis directions of $S^3_0V$. --- ## 7. Reproducible exact basis check The following script constructs the exact integer matrix for $A_3$, constructs the symmetric trace-free subspace $S^3_0V$, and verifies
$$
A_3(S)-4C_S=0
$$
on a basis of $S^3_0V$. It also checks that $A_3$ has rank $7$ on this subspace. ```python import sympy as sp from itertools import product, permutations # Quaternion basis order: # 0 = 1, 1 = i, 2 = j, 3 = k def qmul(x, y): a0, a1, a2, a3 = x b0, b1, b2, b3 = y return sp.Matrix([ a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2, a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0, ]) basis = [ sp.Matrix([1, 0, 0, 0]), # 1 sp.Matrix([0, 1, 0, 0]), # i sp.Matrix([0, 0, 1, 0]), # j sp.Matrix([0, 0, 0, 1]), # k ] imag = [basis[1], basis[2], basis[3]] def prodq(seq): v = basis[0] for x in seq: v = qmul(v, x) return v triples = list(product(range(3), repeat=3)) idx = {t: i for i, t in enumerate(triples)} # A3 matrix: # rows are indexed by (x, y, quaternion_component), dimension 3*3*4 = 36. # columns are indexed by (a, b, c), dimension 27. A = sp.zeros(36, 27) # C matrix: # ordinary contraction C_S(x,y)=S(x,y), viewed in H. C = sp.zeros(36, 27) for col, (a, b, c) in enumerate(triples): ea, eb, ec = imag[a], imag[b], imag[c] for x in range(3): ex = imag[x] for y in range(3): ey = imag[y] rowbase = (x*3 + y)*4 # A3(e_a|e_b|e_c)(x,y) = e_c y e_b x e_a out = prodq([ec, ey, eb, ex, ea]) for h in range(4): A[rowbase + h, col] = out[h] # C(e_a|e_b|e_c)(x,y) = delta_{a,x} delta_{b,y} e_c if a == x and b == y: for h in range(4): C[rowbase + h, col] = ec[h] # Build equations for S^3_0 V inside V^{tensor 3}. eqs = [] # Symmetry equations: T_abc = T_perm(a,b,c). for t in triples: for p in set(permutations(t)): if t < p: row = [0]*27 row[idx[t]] = 1 row[idx[p]] = -1 eqs.append(row) # Trace-free equations: sum_a T_aac = 0 for c = 0,1,2. for c in range(3): row = [0]*27 for a in range(3): row[idx[(a, a, c)]] = 1 eqs.append(row) E = sp.Matrix(eqs) S3_basis = E.nullspace() print("dim S^3_0 V =", len(S3_basis)) D = A - 4*C checks = [D*v == sp.zeros(36, 1) for v in S3_basis] print("A3 - 4C vanishes on basis:", all(checks)) restricted_images = sp.Matrix.hstack(*[A*v for v in S3_basis]) print("rank of A3 on S^3_0 V =", restricted_images.rank()) ``` Expected output: ```text dim S^3_0 V = 7 A3 - 4C vanishes on basis: True rank of A3 on S^3_0 V = 7 ``` This is an exact integer computation. No floating-point arithmetic is used. --- ## 8. Consequence The result of note 03 was
$$
K_3^{null}=S^3_0V.
$$
That statement means: the length-3 highest-spin residual is invisible at probe depth 1. This note adds: the same residual is visible at probe depth 2. Thus the residual is not absolutely invisible. It is only invisible at insufficient probe depth. This is the first vertical step of the residual filtration. --- ## 9. Suggested pattern, not claimed The calculations for length 2 and length 3 suggest the pattern
$$
A_n|_{S^n_0V}=(-2)^{n-1}\mathrm{id}.
$$
For $n=2$, the coefficient is
$$
-2.
$$
For $n=3$, the coefficient is
$$
+4=(-2)^2.
$$
However, this note does not claim the general theorem. It does not claim that all highest-spin residuals are detected exactly at depth $n-1$. It does not claim an infinite residual ladder. The only claim of this note is the verified length-3, depth-2 statement:
$$
A_3(S)=4S(x,y)\quad\text{through the contraction embedding }C.
$$
More precisely,
$$
A_3(S)=4C_S\qquad(S\in S^3_0V).
$$
--- ## 10. Summary At length 3, note 03 showed
$$
K_3^{null}=S^3_0V.
$$
So $S^3_0V$ is invisible at depth 1. This note shows that the internal-internal component of the full depth-2 insertion profile satisfies
$$
A_3|_{S^3_0V}=4C.
$$
Therefore $S^3_0V$ is visible at depth 2. This gives the first vertical step of the residual filtration:
$$
\text{depth 1: invisible},\qquad\text{depth 2: visible}.
$$
