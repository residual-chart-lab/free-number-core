# \# No-Go Note: Single Quaternionic Compression Cannot Preserve Residual History

# 

# 副題：

# 

# > local closure does not imply global collapse

# 

# \## 0. Scope

# 

# This note does \*\*not\*\* claim that free numbers are impossible.

# 

# It proves a narrower no-go result:

# 

# \[

# \\boxed{

# \\text{Within a single compression model } m:B\\to\\mathbb H,

# \\text{ residual detection and history preservation cannot be achieved at the same time.}

# }

# ]

# 

# Here (B) is a boundary-word space and (\\mathbb H) is the quaternion algebra.

# 

# The point of this note is to record why the single-compression model is insufficient, so that the next formulation must move to a staged or Hopf-algebraic structure.

# 

# \---

# 

# \## 1. Boundary-word space

# 

# Let

# 

# \[

# B\_2=

# \\mathrm{span}\_{\\mathbb R}

# {i|i,\\ i|j,\\ j|i,\\ j|j}

# ]

# 

# be the two-letter boundary-word space.

# 

# Define the quaternionic compression map

# 

# \[

# m\_2:B\_2\\to\\mathbb H

# ]

# 

# by

# 

# \[

# m\_2(a|b)=ba.

# ]

# 

# Using

# 

# \[

# i^2=j^2=k^2=-1,\\qquad ij=k,\\qquad ji=-k,

# ]

# 

# we have

# 

# \[

# m\_2(i|i)=-1,

# ]

# 

# \[

# m\_2(i|j)=ji=-k,

# ]

# 

# \[

# m\_2(j|i)=ij=k,

# ]

# 

# \[

# m\_2(j|j)=-1.

# ]

# 

# \---

# 

# \## 2. Kernel calculation

# 

# Take a general element

# 

# \[

# x=

# \\alpha(i|i)+\\beta(i|j)+\\gamma(j|i)+\\delta(j|j).

# ]

# 

# Then

# 

# \[

# m\_2(x)

# ======

# 

# \-(\\alpha+\\delta)+(\\gamma-\\beta)k.

# ]

# 

# Therefore

# 

# \[

# m\_2(x)=0

# ]

# 

# if and only if

# 

# \[

# \\alpha+\\delta=0,

# \\qquad

# \\gamma-\\beta=0.

# ]

# 

# Hence

# 

# \[

# \\boxed{

# \\ker m\_2

# ========

# 

# \\mathrm{span}\_{\\mathbb R}

# {,i|i-j|j,\\ i|j+j|i,}.

# }

# ]

# 

# This is the first stable result.

# 

# The quaternionic compression kills the symmetric mixed component

# 

# \[

# i|j+j|i,

# ]

# 

# because

# 

# \[

# m\_2(i|j+j|i)=ji+ij=-k+k=0.

# ]

# 

# By contrast, the antisymmetric component survives.

# 

# \---

# 

# \## 3. Boundary antisymmetry leakage

# 

# Define the boundary antisymmetry

# 

# \[

# \\Delta\_\\partial(i|j)=i|j-j|i.

# ]

# 

# Then

# 

# \[

# m\_2(\\Delta\_\\partial(i|j))

# =========================

# 

# \# m\_2(i|j)-m\_2(j|i)

# 

# ji-ij.

# ]

# 

# Since

# 

# \[

# ji=-k,\\qquad ij=k,

# ]

# 

# we get

# 

# \[

# m\_2(\\Delta\_\\partial(i|j))

# =========================

# 

# \-2k\\neq0.

# ]

# 

# Therefore

# 

# \[

# \\boxed{

# \\Delta\_\\partial(i|j)\\notin\\ker m\_2.

# }

# ]

# 

# This gives the minimal residual obstruction:

# 

# \[

# \\boxed{

# \\Omega\_{\\min}=\[\\Delta\_\\partial(i|j)]\\neq0.

# }

# ]

# 

# This is a hand-computable model of the principle:

# 

# \[

# \\boxed{

# \\text{local closure does not imply global collapse.}

# }

# ]

# 

# \---

# 

# \## 4. Residual quotient

# 

# Define

# 

# \[

# Q\_2=B\_2/\\ker m\_2.

# ]

# 

# Since

# 

# \[

# \\dim B\_2=4,

# \\qquad

# \\dim\\ker m\_2=2,

# ]

# 

# we have

# 

# \[

# \\dim Q\_2=2.

# ]

# 

# Let

# 

# \[

# e=-\[i|i],

# \\qquad

# \\kappa=\[j|i].

# ]

# 

# Then

# 

# \[

# Q\_2=

# \\mathrm{span}\_{\\mathbb R}{e,\\kappa}.

# ]

# 

# Moreover,

# 

# \[

# \[i|j]=-\[j|i]=-\\kappa.

# ]

# 

# Thus

# 

# \[

# \[\\Delta\_\\partial(i|j)]

# ======================

# 

# \# \[i|j]-\[j|i]

# 

# \-2\\kappa.

# ]

# 

# So

# 

# \[

# \\boxed{

# \\Omega\_{\\min}=-2\\kappa\\neq0.

# }

# ]

# 

# The local image of (Q\_2) is

# 

# \[

# \\mathbb R\\oplus\\mathbb R k\\subset\\mathbb H.

# ]

# 

# Thus

# 

# \[

# Q\_2\\cong\\mathbb C\_k.

# ]

# 

# This observation is important: (Q\_2) is not a new multiplication table. Locally, it is isomorphic to the familiar complex plane inside (\\mathbb H).

# 

# Therefore, (Q\_2) alone cannot be claimed as a new algebraic object.

# 

# \---

# 

# \## 5. The no-go

# 

# The single-compression model faces the following obstruction.

# 

# To detect the residual obstruction, we quotient by the kernel:

# 

# \[

# Q\_2=B\_2/\\ker m\_2.

# ]

# 

# This makes

# 

# \[

# \\Omega\_{\\min}=\[\\Delta\_\\partial]\\neq0

# ]

# 

# visible as a residual class.

# 

# However, quotienting also removes the detailed boundary-word information contained in (\\ker m\_2).

# 

# If we want the erased history to affect later operations, we must keep the pre-quotient word space (B\_2).

# 

# But then the later effect is produced by information retained in (B\_2), not by (Q\_2) itself.

# 

# Hence the tension:

# 

# \[

# \\boxed{

# \\text{To obtain }\\Omega\\text{, we quotient by }\\ker m.

# }

# ]

# 

# \[

# \\boxed{

# \\text{To preserve history for later operations, we must retain the pre-quotient boundary words.}

# }

# ]

# 

# Thus:

# 

# \[

# \\boxed{

# \\text{In a single compression model }m:B\\to\\mathbb H,

# \\Omega\\text{ and history preservation are structurally incompatible.}

# }

# ]

# 

# This is the no-go result.

# 

# \---

# 

# \## 6. Failed escape routes

# 

# Several attempted escapes collapse back into the same obstruction.

# 

# \### 6.1 Value-level noncommutativity

# 

# Using only

# 

# \[

# \[R\_i,R\_j](1)=2k

# ]

# 

# detects quaternionic noncommutativity, but the result remains inside (\\mathbb H).

# 

# So it is absorbed as an ordinary quaternionic value.

# 

# \### 6.2 Adding (\\varepsilon\\mathbb H)

# 

# Introducing an auxiliary residual grade such as

# 

# \[

# \\mathbb H\\oplus\\varepsilon\\mathbb H

# ]

# 

# can create a nonzero term, but unless the residual grade has an independent structural role, it is either an enlarged algebra or an artificially retained term.

# 

# It does not solve the single-compression problem.

# 

# \### 6.3 Adding an external tag (\\eta\_{ij})

# 

# Writing a residual as

# 

# \[

# (-2k)\\eta\_{ij}

# ]

# 

# prevents absorption into (\\mathbb H), but only by adding a non-absorbed tag by hand.

# 

# This is not a structural derivation.

# 

# \### 6.4 Keeping a presentation

# 

# One may keep the short exact sequence

# 

# \[

# 0\\to K\_2\\to B\_2\\to Q\_2\\to0

# ]

# 

# and define obstruction maps from (K\_2) to later quotients.

# 

# This is technically meaningful.

# 

# However, any later effect obtained in this way depends on retaining (B\_2)-level word information.

# 

# Therefore it is not an effect of (Q\_2) alone.

# 

# The presentation records where the obstruction came from, but it does not by itself give a non-projective residual object inside the single-compression model.

# 

# \---

# 

# \## 7. Conclusion

# 

# The stable positive result is:

# 

# \[

# \\boxed{

# \\Delta\_\\partial(i|j)\\notin\\ker m\_2.

# }

# ]

# 

# The stable negative result is:

# 

# \[

# \\boxed{

# \\text{A single quaternionic compression can detect a residual obstruction, but cannot also preserve the history needed for later causal propagation.}

# }

# ]

# 

# Therefore, this no-go does not refute free numbers.

# 

# It shows that the single-compression model is too small.

# 

# The next formulation must carry information that is not destroyed by the local projection

# 

# \[

# \\Phi:\\text{residual structure}\\to\\mathbb H.

# ]

# 

# The next test is:

# 

# \[

# \\boxed{

# \\text{Does the next structure contain information not killed by }\\Phi?

# }

# ]

# 

# A natural candidate is a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure.

# 

# However, the free-number direction must retain the distinction:

# 

# \[

# \\boxed{

# \\text{Connes-Kreimer: grafting first.}

# }

# ]

# 

# \[

# \\boxed{

# \\text{Free numbers: quaternionic local rigidity first.}

# }

# ]

# 

# This note identifies the obstruction that forces us beyond a single-compression model.

# 

