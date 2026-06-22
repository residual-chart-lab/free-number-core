# No-Go Note: Single Quaternionic Compression Cannot Preserve Residual History

> Subtitle: local closure does not imply global collapse

This note records a limited no-go result for a single quaternionic compression model.

It does not claim that free numbers are impossible.  
It claims only that, inside a single compression model $m:B\to\mathbb H$, residual detection and history preservation cannot be achieved at the same time.

Here, $B$ is a boundary-word space, $\mathbb H$ is the quaternion algebra, and $m$ is a compression map from boundary words into $\mathbb H$.

The conclusion is that the single-compression model is too small. The next formulation must move beyond a single projection into $\mathbb H$, most likely toward a staged, Hopf-algebraic, or renormalization-like structure.

---

## 1. Boundary-word space

Let $B_2$ be the two-letter boundary-word space:

$$
B_2=
\\mathrm{span}_{\mathbb R}
\{\,i\mid i,\ i\mid j,\ j\mid i,\ j\mid j\,\}.
$$

Define the quaternionic compression map

$$
m_2:B_2\to\mathbb H
$$

by

$$
m_2(a\mid b)=ba.
$$

Using the quaternion relations

$$
i^2=j^2=k^2=-1,\qquad ij=k,\qquad ji=-k,
$$

we have

$$
m_2(i\mid i)=-1,
$$

$$
m_2(i\mid j)=ji=-k,
$$

$$
m_2(j\mid i)=ij=k,
$$

$$
m_2(j\mid j)=-1.
$$

---

## 2. Kernel calculation

Take a general element

$$
x=\alpha(i\mid i)+\beta(i\mid j)+\gamma(j\mid i)+\delta(j\mid j).
$$

Then

$$
m_2(x)=-(\alpha+\delta)+(\gamma-\beta)k.
$$

Therefore, $m_2(x)=0$ if and only if

$$
\alpha+\delta=0,
\qquad
\gamma-\beta=0.
$$

Hence

$$
\ker m_2=
\\mathrm{span}_{\mathbb R}
\{\,i\mid i-j\mid j,\ i\mid j+j\mid i\,\}.
$$

This is the first stable result.

The quaternionic compression kills the symmetric mixed component

$$
i\mid j+j\mid i
$$

because

$$
m_2(i\mid j+j\mid i)=ji+ij=-k+k=0.
$$

By contrast, the antisymmetric component survives.

---

## 3. Boundary antisymmetry leakage

Define the boundary antisymmetry

$$
\Delta_{\partial}(i\mid j)=i\mid j-j\mid i.
$$

Then

$$
m_2(\Delta_{\partial}(i\mid j))=m_2(i\mid j)-m_2(j\mid i)=ji-ij.
$$

Since

$$
ji=-k,
\qquad
ij=k,
$$

we get

$$
m_2(\Delta_{\partial}(i\mid j))=-2k\neq0.
$$

Therefore

$$
\Delta_{\partial}(i\mid j)\notin\ker m_2.
$$

This gives the minimal residual obstruction

$$
\Omega_{\min}=[\Delta_{\partial}(i\mid j)]\neq0.
$$

This is a hand-computable model of the principle:

> local closure does not imply global collapse.

---

## 4. Residual quotient

Define

$$
Q_2=B_2/\ker m_2.
$$

Since

$$
\dim B_2=4,
\qquad
\dim\ker m_2=2,
$$

we have

$$
\dim Q_2=2.
$$

Let

$$
e=-[i\mid i],
\qquad
\kappa=[j\mid i].
$$

Then

$$
Q_2=\\mathrm{span}_{\mathbb R}\{e,\kappa\}.
$$

Moreover,

$$
[i\mid j]=-[j\mid i]=-\kappa.
$$

Thus

$$
[\Delta_{\partial}(i\mid j)]=[i\mid j]-[j\mid i]=-2\kappa.
$$

So

$$
\Omega_{\min}=-2\kappa\neq0.
$$

The local image of $Q_2$ is the complex plane inside $\mathbb H$ spanned by $1$ and $k$:

$$
\mathbb R\oplus\mathbb R k\subset\mathbb H.
$$

Thus

$$
Q_2\cong\mathbb C_k.
$$

This observation is important.

Although $Q_2$ is produced as a residual quotient, its local algebraic image is the familiar complex plane $\mathbb C_k$ inside $\mathbb H$.

Therefore, $Q_2$ alone cannot be claimed as a new multiplication table or a new algebraic object.

The positive result is not that $Q_2$ is a new algebra. The positive result is that the boundary antisymmetry $\Delta_{\partial}(i\mid j)$ fails to lie in $\ker m_2$.

---

## 5. The no-go

The single-compression model faces the following obstruction.

To detect the residual obstruction, we quotient by the kernel:

$$
Q_2=B_2/\ker m_2.
$$

This makes the residual class visible:

$$
\Omega_{\min}=[\Delta_{\partial}]\neq0.
$$

However, quotienting also removes the detailed boundary-word information contained in $\ker m_2$.

If we want the erased history to affect later operations, we must retain the pre-quotient word space $B_2$.

But then the later effect is produced by information retained in $B_2$, not by $Q_2$ itself.

So the tension is:

$$
\text{To obtain }\Omega,\text{ we quotient by }\ker m.
$$

$$
\text{To preserve history for later operations, we must retain the pre-quotient boundary words.}
$$

Thus:

$$
\text{In a single compression model }m:B\to\mathbb H,
\quad
\Omega\text{ and history preservation are structurally incompatible.}
$$

This is the no-go result.

---

## 6. Failed escape routes

Several attempted escapes collapse back into the same obstruction.

---

### 6.1 Value-level noncommutativity

Using only the commutator

$$
R_i,R_j=2k
$$

detects quaternionic noncommutativity.

However, the result still lies inside the quaternion algebra:

$$
2k\in\mathbb H.
$$

Therefore it is absorbed as an ordinary quaternionic value.

This does not produce a residual object outside the local algebra.

---

### 6.2 Adding $\varepsilon\mathbb H$

Introducing an auxiliary residual grade such as

$$
\mathbb H\oplus\varepsilon\mathbb H
$$

can create a nonzero term.

However, unless the residual grade has an independent structural role, it is either an enlarged algebra or an artificially retained term.

It does not solve the single-compression problem.

The issue is not merely that some extra symbol can be retained. The issue is whether the retained information survives in a way that is not reducible to the local projection into $\mathbb H$.

---

### 6.3 Adding an external tag $\eta_{ij}$

Writing a residual as

$$
(-2k)\eta_{ij}
$$

prevents absorption into $\mathbb H$, but only by adding a non-absorbed tag by hand.

This is not a structural derivation.

It is equivalent to declaring that the history should not be forgotten, rather than deriving a mechanism by which the history remains active.

---

### 6.4 Keeping a presentation

One may keep the short exact sequence

$$
0\to K_2\to B_2\to Q_2\to0
$$

and define obstruction maps from $K_2$ to later quotients.

This is technically meaningful.

For example, with

$$
K_2=\ker m_2,
$$

one can take

$$
\sigma=i\mid j+j\mid i.
$$

Then

$$
\sigma\in K_2.
$$

Define an internal insertion

$$
I_i(a\mid b)=a\mid i\mid b.
$$

Then

$$
I_i(\sigma)=i\mid i\mid j+j\mid i\mid i.
$$

Using

$$
m_3(a\mid b\mid c)=cba,
$$

we get

$$
m_3(i\mid i\mid j)=jii=-j,
$$

and

$$
m_3(j\mid i\mid i)=iij=-j.
$$

Therefore

$$
m_3(I_i(\sigma))=-2j\neq0.
$$

This shows

$$
I_i(K_2)\not\subset\ker m_3.
$$

So the kernel of one stage is not stable under the next insertion.

This is an important signal.

However, it does not yet solve the no-go.

The reason is that this effect depends on retaining the $B_2$-level word information.

In

$$
Q_2=B_2/K_2,
$$

the element $\sigma$ is already zero:

$$
[\sigma]=0\in Q_2.
$$

Thus the insertion calculation uses information from the pre-quotient presentation, not from $Q_2$ alone.

Keeping the presentation is a meaningful record of origin, but it does not by itself produce a non-projective residual object inside the single-compression model.

---

## 7. The criterion for the next formulation

The core test is:

$$
\text{Does the structure carry information that is not killed by }\Phi?
$$

Here $\Phi$ denotes the local projection or local image into $\mathbb H$.

The failed attempts above all collapse because the relevant information is either:

1. absorbed into $\mathbb H$,
2. retained only by keeping the pre-quotient word space $B_2$, or
3. added as an external tag.

Therefore, the next formulation must carry data that is not reducible to the local quaternionic image.

This suggests that a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure is required.

The essential requirement is:

$$
\text{The next structure must contain non-projective data not killed by }\Phi.
$$

---

## 8. Conclusion

The stable positive result is:

$$
\Delta_{\partial}(i\mid j)\notin\ker m_2.
$$

The stable negative result is:

$$
\text{A single quaternionic compression can detect a residual obstruction,}
$$

$$
\text{but cannot also preserve the history needed for later causal propagation.}
$$

Therefore, this no-go does not refute free numbers.

It shows that the single-compression model is too small.

The next formulation must carry information that is not destroyed by the local projection

$$
\Phi:\text{residual structure}\to\mathbb H.
$$

A natural candidate is a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure.

However, the free-number direction must retain the distinction:

$$
\text{Connes-Kreimer: grafting first.}
$$

$$
\text{Free numbers: quaternionic local rigidity first.}
$$

This note identifies the obstruction that forces us beyond a single-compression model.


