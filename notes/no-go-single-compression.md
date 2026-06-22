# No-Go Note: Single Quaternionic Compression Cannot Preserve Residual History

> **Subtitle:** local closure does not imply global collapse

This note records a limited no-go result for a single quaternionic compression model.

It does **not** claim that free numbers are impossible.  
It claims only that, inside a single compression model `m : B -> H`, residual detection and history preservation cannot be achieved at the same time.

Here:

- `B` is a boundary-word space.
- `H` is the quaternion algebra.
- `m` is a compression map from boundary words into `H`.

The conclusion is that the single-compression model is too small.  
The next formulation must move beyond a single projection into `H`, most likely toward a staged, Hopf-algebraic, or renormalization-like structure.

---

## 1. Boundary-word space

Let `B₂` be the two-letter boundary-word space:

`B₂ = span_R { i|i, i|j, j|i, j|j }`

Define the quaternionic compression map:

`m₂ : B₂ -> H`

by:

`m₂(a|b) = ba`

Using the quaternion relations:

`i² = j² = k² = -1`

`ij = k`

`ji = -k`

we have:

`m₂(i|i) = -1`

`m₂(i|j) = ji = -k`

`m₂(j|i) = ij = k`

`m₂(j|j) = -1`

---

## 2. Kernel calculation

Take a general element:

`x = α(i|i) + β(i|j) + γ(j|i) + δ(j|j)`

Then:

`m₂(x) = -(α + δ) + (γ - β)k`

Therefore `m₂(x) = 0` if and only if:

`α + δ = 0`

`γ - β = 0`

Hence:

`ker m₂ = span_R { i|i - j|j, i|j + j|i }`

This is the first stable result.

The quaternionic compression kills the symmetric mixed component:

`i|j + j|i`

because:

`m₂(i|j + j|i) = ji + ij = -k + k = 0`

By contrast, the antisymmetric component survives.

---

## 3. Boundary antisymmetry leakage

Define the boundary antisymmetry:

`Δ∂(i|j) = i|j - j|i`

Then:

`m₂(Δ∂(i|j)) = m₂(i|j) - m₂(j|i) = ji - ij`

Since:

`ji = -k`

`ij = k`

we get:

`m₂(Δ∂(i|j)) = -2k ≠ 0`

Therefore:

`Δ∂(i|j) ∉ ker m₂`

This gives the minimal residual obstruction:

`Ω_min = [Δ∂(i|j)] ≠ 0`

This is a hand-computable model of the principle:

**local closure does not imply global collapse.**

---

## 4. Residual quotient

Define:

`Q₂ = B₂ / ker m₂`

Since:

`dim B₂ = 4`

`dim ker m₂ = 2`

we have:

`dim Q₂ = 2`

Let:

`e = -[i|i]`

`κ = [j|i]`

Then:

`Q₂ = span_R { e, κ }`

Moreover:

`[i|j] = -[j|i] = -κ`

Thus:

`[Δ∂(i|j)] = [i|j] - [j|i] = -2κ`

So:

`Ω_min = -2κ ≠ 0`

The local image of `Q₂` is the complex plane inside `H` spanned by `1` and `k`.

Thus:

`Q₂ ≅ C_k`

This observation is important.

Although `Q₂` is produced as a residual quotient, its local algebraic image is the familiar complex plane `C_k` inside `H`.

Therefore, `Q₂` alone cannot be claimed as a new multiplication table or a new algebraic object.

The positive result is not that `Q₂` is a new algebra.  
The positive result is that the boundary antisymmetry `Δ∂(i|j)` fails to lie in `ker m₂`.

---

## 5. The no-go

The single-compression model faces the following obstruction.

To detect the residual obstruction, we quotient by the kernel:

`Q₂ = B₂ / ker m₂`

This makes the residual class visible:

`Ω_min = [Δ∂] ≠ 0`

However, quotienting also removes the detailed boundary-word information contained in `ker m₂`.

If we want the erased history to affect later operations, we must retain the pre-quotient word space `B₂`.

But then the later effect is produced by information retained in `B₂`, not by `Q₂` itself.

So the tension is:

- To obtain `Ω`, we quotient by `ker m`.
- To preserve history for later operations, we must retain the pre-quotient boundary words.

Thus:

**In a single compression model `m : B -> H`, `Ω` and history preservation are structurally incompatible.**

This is the no-go result.

---

## 6. Failed escape routes

Several attempted escapes collapse back into the same obstruction.

### 6.1 Value-level noncommutativity

Using only:

`[R_i, R_j](1) = 2k`

detects quaternionic noncommutativity, but the result remains inside `H`.

So it is absorbed as an ordinary quaternionic value.

This does not produce a residual object outside the local algebra.

### 6.2 Adding epsilon-H

Introducing an auxiliary residual grade such as:

`H + εH`

can create a nonzero term.

However, unless the residual grade has an independent structural role, it is either an enlarged algebra or an artificially retained term.

It does not solve the single-compression problem.

The issue is not merely that some extra symbol can be retained.  
The issue is whether the retained information survives in a way that is not reducible to the local projection into `H`.

### 6.3 Adding an external tag eta_ij

Writing a residual as:

`(-2k)η_ij`

prevents absorption into `H`, but only by adding a non-absorbed tag by hand.

This is not a structural derivation.

It is equivalent to declaring that the history should not be forgotten, rather than deriving a mechanism by which the history remains active.

### 6.4 Keeping a presentation

One may keep the short exact sequence:

`0 -> K₂ -> B₂ -> Q₂ -> 0`

and define obstruction maps from `K₂` to later quotients.

This is technically meaningful.

For example, with:

`K₂ = ker m₂`

one can take:

`sigma = i|j + j|i`

Then:

`sigma ∈ K₂`

Define an internal insertion:

`I_i(a|b) = a|i|b`

Then:

`I_i(sigma) = i|i|j + j|i|i`

Using:

`m₃(a|b|c) = cba`

we get:

`m₃(i|i|j) = jii = -j`

`m₃(j|i|i) = iij = -j`

Therefore:

`m₃(I_i(sigma)) = -2j ≠ 0`

This shows:

`I_i(K₂) ⊄ ker m₃`

So the kernel of one stage is not stable under the next insertion.

This is an important signal.

However, it does not yet solve the no-go.

The reason is that this effect depends on retaining the `B₂`-level word information.

In:

`Q₂ = B₂ / K₂`

the element `sigma` is already zero:

`[sigma] = 0 in Q₂`

Thus the insertion calculation uses information from the pre-quotient presentation, not from `Q₂` alone.

Keeping the presentation is a meaningful record of origin, but it does not by itself produce a non-projective residual object inside the single-compression model.

---

## 7. The criterion for the next formulation

The core test is:

**Does the structure carry information that is not killed by `Φ`?**

Here `Φ` denotes the local projection or local image into `H`.

The failed attempts above all collapse because the relevant information is either:

1. absorbed into `H`,
2. retained only by keeping the pre-quotient word space `B₂`, or
3. added as an external tag.

Therefore, the next formulation must carry data that is not reducible to the local quaternionic image.

This suggests that a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure is required.

The essential requirement is:

**The next structure must contain non-projective data not killed by `Φ`.**

---

## 8. Conclusion

The stable positive result is:

`Δ∂(i|j) ∉ ker m₂`

The stable negative result is:

**A single quaternionic compression can detect a residual obstruction, but cannot also preserve the history needed for later causal propagation.**

Therefore, this no-go does not refute free numbers.

It shows that the single-compression model is too small.

The next formulation must carry information that is not destroyed by the local projection:

`Φ : residual structure -> H`

A natural candidate is a staged, Hopf-algebraic, or Connes-Kreimer-like renormalization structure.

However, the free-number direction must retain the distinction:

- Connes-Kreimer: grafting first.
- Free numbers: quaternionic local rigidity first.

This note identifies the obstruction that forces us beyond a single-compression model.
