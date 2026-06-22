# No-Go Note: Single Quaternionic Compression Cannot Preserve Residual History

> **Subtitle:** local closure does not imply global collapse

## 0. Scope

This note does **not** claim that free numbers are impossible.

It proves a narrower no-go result:

**Within a single compression model from boundary words into the quaternion algebra, residual detection and history preservation cannot be achieved at the same time.**

Here:

- `B` is a boundary-word space.
- `H` is the quaternion algebra.
- `m : B -> H` is a single compression map.

The purpose of this note is to record the limitation of the single-compression model.

The conclusion is not that the free-number program fails. The conclusion is that the next formulation must move beyond a single projection into `H`, most likely toward a staged, Hopf-algebraic, or renormalization-like structure.

---

## 1. Boundary-word space

Let the two-letter boundary-word space be:

$$
B_2 = \mathrm{span}_{\mathbb R}\{\, i|i,\ i|j,\ j|i,\ j|j \,\}.
$$

Define the quaternionic compression map:

$$
m_2 : B_2 \to \mathbb H
$$

by:

$$
m_2(a|b)=ba.
$$

Using the quaternion relations:

$$
i^2=j^2=k^2=-1, \qquad ij=k, \qquad ji=-k,
$$

we have:

$$
m_2(i|i)=-1,
$$

$$
m_2(i|j)=ji=-k,
$$

$$
m_2(j|i)=ij=k,
$$

$$
m_2(j|j)=-1.
$$

---

## 2. Kernel calculation

Take a general element:

$$
x = \alpha(i|i)+\beta(i|j)+\gamma(j|i)+\delta(j|j).
$$

Then:

$$
m_2(x)=-(\alpha+\delta)+(\gamma-\beta)k.
$$

Therefore:

$$
m_2(x)=0
$$

if and only if:

$$
\alpha+\delta=0, \qquad \gamma-\beta=0.
$$

Hence:

$$
\ker m_2
=
\mathrm{span}_{\mathbb R}\{\, i|i-j|j,\ i|j+j|i \,\}.
$$

This is the first stable result.

The quaternionic compression kills the symmetric mixed component:

$$
i|j+j|i,
$$

because:

$$
m_2(i|j+j|i)=ji+ij=-k+k=0.
$$

By contrast, the antisymmetric component survives.

---

## 3. Boundary antisymmetry leakage

Define the boundary antisymmetry:

$$
\Delta_{\partial}(i|j)=i|j-j|i.
$$

Then:

$$
m_2(\Delta_{\partial}(i|j))
=
m_2(i|j)-m_2(j|i)
=
ji-ij.
$$

Since:

$$
ji=-k, \qquad ij=k,
$$

we get:

$$
m_2(\Delta_{\partial}(i|j))=-2k \neq 0.
$$

Therefore:

$$
\Delta_{\partial}(i|j) \notin \ker m_2.
$$

This gives the minimal residual obstruction:

$$
\Omega_{\min}=[\Delta_{\partial}(i|j)] \neq 0.
$$

This is a hand-computable model of the principle:

**local closure does not imply global collapse.**

---

## 4. Residual quotient

Define:

$$
Q_2=B_2/\ker m_2.
$$

Since:

$$
\dim B_2=4, \qquad \dim \ker m_2=2,
$$

we have:

$$
\dim Q_2=2.
$$

Let:

$$
e=-[i|i], \qquad \kappa=[j|i].
$$

Then:

$$
Q_2=\mathrm{span}_{\mathbb R}\{e,\kappa\}.
$$

Moreover:

$$
[i|j]=-[j|i]=-\kappa.
$$

Thus:

$$
[\Delta_{\partial}(i|j)]
=
[i|j]-[j|i]
=
-2\kappa.
$$

So:

$$
\Omega_{\min}=-2\kappa \neq 0.
$$

The local image of `Q_2` is:

$$
\mathbb R\oplus\mathbb R k \subset \mathbb H.
$$

Thus:

$$
Q_2 \cong \mathbb C_k.
$$

This observation is important.

Although `Q_2` is produced as a residual quotient, its local algebraic image is the familiar complex plane `C_k` inside `H`. Therefore, `Q_2` alone cannot be claimed as a new multiplication table or a new algebraic object.

The positive result is not that `Q_2` is a new algebra.

The positive result is that the boundary antisymmetry `Delta_partial(i|j)` fails to lie in `ker m_2`.

---

## 5. The no-go

The single-compression model faces the following obstruction.

To detect the residual obstruction, we quotient by the kernel:

$$
Q_2=B_2/\ker m_2.
$$

This makes the residual class visible:

$$
\Omega_{\min}=[\Delta_{\partial}] \neq 0.
$$

However, quotienting also removes the detailed boundary-word information contained in `ker m_2`.

If we want the erased history to affect later operations, we must retain the pre-quotient word space `B_2`.

But then the later effect is produced by information retained in `B_2`, not by `Q_2` itself.

Hence the tension:

**To obtain `Omega`, we quotient by `ker m`.**

**To preserve history for later operations, we must retain the pre-quotient boundary words.**

Thus:

**In a single compression model `m : B -> H`, `Omega` and history preservation are structurally incompatible.**

This is the no-go result.

---

## 6. Failed escape routes

Several attempted escapes collapse back into the same obstruction.

### 6.1 Value-level noncommutativity

Using only:

$$
[R_i,R_j](1)=2k
$$

detects quaternionic noncommutativity, but the result remains inside `H`.

So it is absorbed as an ordinary quaternionic value.

This does not produce a residual object outside the local algebra.

---

### 6.2 Adding an epsilon grade

Introducing an auxiliary residual grade such as:

$$
\mathbb H\oplus\varepsilon\mathbb H
$$

can create a nonzero term.

However, unless the residual grade has an independent structural role, it is either an enlarged algebra or an artificially retained term.

It does not solve the single-compression problem.

The issue is not merely that some extra symbol can be retained.

The issue is whether the retained information survives in a way that is not reducible to the local projection into `H`.

---

### 6.3 Adding an external tag eta_ij

Writing a residual as:

$$
(-2k)\eta_{ij}
$$

prevents absorption into `H`, but only by adding a non-absorbed tag by hand.

This is not a structural derivation.

It is equivalent to declaring that the history should not be forgotten, rather than deriving a mechanism by which the history remains active.

---

### 6.4 Keeping a presentation

One may keep the short exact sequence:

$$
0\to K_2\to B_2\to Q_2\to0
$$

and define obstruction maps from `K_2` to later quotients.

This is technically meaningful.

For example, with:

$$
K_2=\ker m_2,
$$

one can take:

$$
\sigma=i|j+j|i \in K_2
$$

and define an internal insertion:

$$
I_i(a|b)=a|i|b.
$$

Then:

$$
I_i(\sigma)=i|i|j+j|i|i.
$$

Using:

$$
m_3(a|b|c)=cba,
$$

we get:

$$
m_3(i|i|j)=jii=-j,
$$

and:

$$
m_3(j|i|i)=iij=-j.
$$

Therefore:

$$
m_3(I_i(\sigma))=-2j \neq 0.
$$

This shows that:

$$
I_i(K_2)\not\subset \ker m_3.
$$

So the kernel of one stage is not stable under the next insertion.

This is an important signal.

However, it does not yet solve the no-go.

The reason is that this effect depends on retaining the `B_2`-level word information. In `Q_2 = B_2 / K_2`, the element `sigma` is already zero:

$$
[\sigma]=0 \in Q_2.
$$

Thus the insertion calculation uses information from the pre-quotient presentation, not from `Q_2` alone.

Keeping the presentation is a meaningful record of origin, but it does not by itself produce a non-projective residual object inside the single-compression model.

---

## 7. The criterion for the next formulation

The core test is:

**Does the structure carry information that is not killed by the local projection `Phi`?**

Here `Phi` denotes the local projection or local image into `H`.

The failed attempts above all collapse because the relevant information is either:

1. absorbed into `H`,
2. retained only by keeping the pre-quotient word space `B_2`, or
3. added as an external tag.

Therefore, the next formulation must carry data that is not reducible to the local quaternionic image.

This suggests that a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure is required.

The essential requirement is:

**The next structure must contain non-projective data not killed by `Phi`.**

---

## 8. Conclusion

The stable positive result is:

$$
\Delta_{\partial}(i|j)\notin\ker m_2.
$$

The stable negative result is:

**A single quaternionic compression can detect a residual obstruction, but cannot also preserve the history needed for later causal propagation.**

Therefore, this no-go does not refute free numbers.

It shows that the single-compression model is too small.

The next formulation must carry information that is not destroyed by the local projection:

$$
\Phi:\text{residual structure}\to\mathbb H.
$$

A natural candidate is a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure.

However, the free-number direction must retain the distinction:

**Connes-Kreimer: grafting first.**

**Free numbers: quaternionic local rigidity first.**

This note identifies the obstruction that forces us beyond a single-compression model.
