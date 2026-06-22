# No-Go Note: Single Quaternionic Compression Cannot Preserve Residual History

> **Subtitle:** local closure does not imply global collapse

This is the GitHub-safe Markdown version.  
All formulas are written as plain text blocks instead of LaTeX math blocks, so GitHub will not break the rendering.

---

## 0. Scope

This note does **not** claim that free numbers are impossible.

It proves a narrower no-go result:

```text
Within a single compression model

    m : B -> H

residual detection and history preservation cannot be achieved at the same time.
```

Here:

```text
B = boundary-word space
H = quaternion algebra
```

The purpose of this note is to record the limitation of the single-compression model.

The conclusion is not that the free-number program fails.  
The conclusion is that the next formulation must move beyond a single projection into `H`, most likely toward a staged, Hopf-algebraic, or renormalization-like structure.

---

## 1. Boundary-word space

Let:

```text
B_2 = span_R { i|i, i|j, j|i, j|j }
```

be the two-letter boundary-word space.

Define the quaternionic compression map:

```text
m_2 : B_2 -> H
```

by:

```text
m_2(a|b) = ba
```

Using the quaternion relations:

```text
i^2 = j^2 = k^2 = -1
ij = k
ji = -k
```

we have:

```text
m_2(i|i) = -1
m_2(i|j) = ji = -k
m_2(j|i) = ij = k
m_2(j|j) = -1
```

---

## 2. Kernel calculation

Take a general element:

```text
x = alpha(i|i) + beta(i|j) + gamma(j|i) + delta(j|j)
```

Then:

```text
m_2(x) = -(alpha + delta) + (gamma - beta)k
```

Therefore:

```text
m_2(x) = 0
```

if and only if:

```text
alpha + delta = 0
gamma - beta = 0
```

Hence:

```text
ker m_2 = span_R { i|i - j|j, i|j + j|i }
```

This is the first stable result.

The quaternionic compression kills the symmetric mixed component:

```text
i|j + j|i
```

because:

```text
m_2(i|j + j|i)
= ji + ij
= -k + k
= 0
```

By contrast, the antisymmetric component survives.

---

## 3. Boundary antisymmetry leakage

Define the boundary antisymmetry:

```text
Delta_partial(i|j) = i|j - j|i
```

Then:

```text
m_2(Delta_partial(i|j))
= m_2(i|j) - m_2(j|i)
= ji - ij
```

Since:

```text
ji = -k
ij = k
```

we get:

```text
m_2(Delta_partial(i|j))
= -2k
!= 0
```

Therefore:

```text
Delta_partial(i|j) is not in ker m_2.
```

This gives the minimal residual obstruction:

```text
Omega_min = [Delta_partial(i|j)] != 0
```

This is a hand-computable model of the principle:

```text
local closure does not imply global collapse.
```

---

## 4. Residual quotient

Define:

```text
Q_2 = B_2 / ker m_2
```

Since:

```text
dim B_2 = 4
dim ker m_2 = 2
```

we have:

```text
dim Q_2 = 2
```

Let:

```text
e = -[i|i]
kappa = [j|i]
```

Then:

```text
Q_2 = span_R { e, kappa }
```

Moreover:

```text
[i|j] = -[j|i] = -kappa
```

Thus:

```text
[Delta_partial(i|j)]
= [i|j] - [j|i]
= -2kappa
```

So:

```text
Omega_min = -2kappa != 0
```

The local image of `Q_2` is:

```text
R + Rk inside H
```

Thus:

```text
Q_2 is isomorphic to C_k.
```

This observation is important.

Although `Q_2` is produced as a residual quotient, its local algebraic image is the familiar complex plane `C_k` inside `H`.

Therefore, `Q_2` alone cannot be claimed as a new multiplication table or a new algebraic object.

The positive result is not that `Q_2` is a new algebra.  
The positive result is that the boundary antisymmetry `Delta_partial(i|j)` fails to lie in `ker m_2`.

---

## 5. The no-go

The single-compression model faces the following obstruction.

To detect the residual obstruction, we quotient by the kernel:

```text
Q_2 = B_2 / ker m_2
```

This makes the residual class visible:

```text
Omega_min = [Delta_partial] != 0
```

However, quotienting also removes the detailed boundary-word information contained in `ker m_2`.

If we want the erased history to affect later operations, we must retain the pre-quotient word space `B_2`.

But then the later effect is produced by information retained in `B_2`, not by `Q_2` itself.

Hence the tension:

```text
To obtain Omega, we quotient by ker m.
```

```text
To preserve history for later operations, we must retain the pre-quotient boundary words.
```

Thus:

```text
In a single compression model m : B -> H,
Omega and history preservation are structurally incompatible.
```

This is the no-go result.

---

## 6. Failed escape routes

Several attempted escapes collapse back into the same obstruction.

---

### 6.1 Value-level noncommutativity

Using only:

```text
[R_i, R_j](1) = 2k
```

detects quaternionic noncommutativity, but the result remains inside `H`.

So it is absorbed as an ordinary quaternionic value.

This does not produce a residual object outside the local algebra.

---

### 6.2 Adding epsilon-H

Introducing an auxiliary residual grade such as:

```text
H + epsilon H
```

can create a nonzero term.

However, unless the residual grade has an independent structural role, it is either an enlarged algebra or an artificially retained term.

It does not solve the single-compression problem.

The issue is not merely that some extra symbol can be retained.  
The issue is whether the retained information survives in a way that is not reducible to the local projection into `H`.

---

### 6.3 Adding an external tag eta_ij

Writing a residual as:

```text
(-2k) eta_ij
```

prevents absorption into `H`, but only by adding a non-absorbed tag by hand.

This is not a structural derivation.

It is equivalent to declaring that the history should not be forgotten, rather than deriving a mechanism by which the history remains active.

---

### 6.4 Keeping a presentation

One may keep the short exact sequence:

```text
0 -> K_2 -> B_2 -> Q_2 -> 0
```

and define obstruction maps from `K_2` to later quotients.

This is technically meaningful.

For example, with:

```text
K_2 = ker m_2
```

one can take:

```text
sigma = i|j + j|i
```

Then:

```text
sigma is in K_2.
```

Define an internal insertion:

```text
I_i(a|b) = a|i|b
```

Then:

```text
I_i(sigma) = i|i|j + j|i|i
```

Using:

```text
m_3(a|b|c) = cba
```

we get:

```text
m_3(i|i|j) = jii = -j
m_3(j|i|i) = iij = -j
```

Therefore:

```text
m_3(I_i(sigma)) = -2j != 0
```

This shows:

```text
I_i(K_2) is not contained in ker m_3.
```

So the kernel of one stage is not stable under the next insertion.

This is an important signal.

However, it does not yet solve the no-go.

The reason is that this effect depends on retaining the `B_2`-level word information.

In:

```text
Q_2 = B_2 / K_2
```

the element `sigma` is already zero:

```text
[sigma] = 0 in Q_2
```

Thus the insertion calculation uses information from the pre-quotient presentation, not from `Q_2` alone.

Keeping the presentation is a meaningful record of origin, but it does not by itself produce a non-projective residual object inside the single-compression model.

---

## 7. The criterion for the next formulation

The core test is:

```text
Does the structure carry information that is not killed by Phi?
```

Here `Phi` denotes the local projection or local image into `H`.

The failed attempts above all collapse because the relevant information is either:

1. absorbed into `H`,
2. retained only by keeping the pre-quotient word space `B_2`, or
3. added as an external tag.

Therefore, the next formulation must carry data that is not reducible to the local quaternionic image.

This suggests that a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure is required.

The essential requirement is:

```text
The next structure must contain non-projective data not killed by Phi.
```

---

## 8. Conclusion

The stable positive result is:

```text
Delta_partial(i|j) is not in ker m_2.
```

The stable negative result is:

```text
A single quaternionic compression can detect a residual obstruction,
but cannot also preserve the history needed for later causal propagation.
```

Therefore, this no-go does not refute free numbers.

It shows that the single-compression model is too small.

The next formulation must carry information that is not destroyed by the local projection:

```text
Phi : residual structure -> H
```

A natural candidate is a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure.

However, the free-number direction must retain the distinction:

```text
Connes-Kreimer: grafting first.
Free numbers: quaternionic local rigidity first.
```

This note identifies the obstruction that forces us beyond a single-compression model.
