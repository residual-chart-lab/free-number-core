# The Last-Percent Delay Hypothesis — v0.2.1-register-closed

*An appendix note. Not a Free Numbers theorem. Not a Y-axis theorem. A neighbouring model that happens to share the same soil.*

Many people report a similar experience near a limit. A battery at one percent seems to hold longer than one percent should. A runner past “I can’t” sometimes gets another stretch of distance. A prognosis may be outlived by a factor. These reports are common enough, across enough independent settings, to be worth treating as a modelling question rather than dismissing as mere illusion — while being equally careful not to infer a physical law from anecdote.

This note separates two things that the common report fuses:

```text
The tail is a hypothesis.
The surprise is a measurable mismatch.
```

The tail is something we put into a decay model. Whether any real system has such a tail is an empirical question.

The surprise is the gap between an ordinary-regime prediction and the behaviour of the tailed model. It is computable once the tail is assumed. Its computation does not require the tail to be physically real; physical reality is what later measurement must decide.

That separation is the point of the note.

---

## 1. A decay model with a terminal tail

Let `E(t) ≥ 0` be a remaining quantity — charge, reserve, fuel, capacity, or any positive amount that depletes.

Ordinary depletion is exponential:

```text
dE/dt = -kE.
```

Its relative decay rate is constant:

```text
-Ė/E = k.
```

The “last percent holds on” report can be modelled as the claim that the relative decay rate drops as `E → 0`.

A simple terminal-tail model is:

```text
dE/dt = -k · E^{n+1} / (E^n + α^n),      k > 0, α > 0, n > 0.
```

Equivalently,

```text
dE/dt = -kE / (1 + (α/E)^n).
```

For `E ≫ α`, this becomes ordinary exponential decay:

```text
dE/dt ≈ -kE.
```

For `E ≪ α`, it becomes

```text
dE/dt ≈ -(k/α^n) E^{n+1}.
```

Thus the terminal region is no longer exponential. It has a power-law crawl. The smaller `E` becomes, the slower the relative decay becomes.

The parameter `α` sets the scale at which the tail begins to matter. The exponent `n` sets how strongly the tail bites.

This is an assumption. Nothing here claims that a real battery, body, flame, organism, or engineered system obeys this equation. It is the minimal shape that turns “the last percent holds on” into a solvable time law.

---

## 2. The exact time law

The model integrates exactly. Separating variables gives

```text
t(E) = (1/k) ∫_E^{E₀} ( 1/u + α^n u^{-n-1} ) du.
```

Therefore,

```text
t(E) = (1/k) [ log(E₀/E) + (α^n/n)(E^{-n} - E₀^{-n}) ].
```

The first term is ordinary exponential time:

```text
t_ordinary(E) = (1/k) log(E₀/E).
```

The second term is terminal-tail time:

```text
t_tail(E) = (α^n/(kn))(E^{-n} - E₀^{-n}).
```

While `E ≫ α`, the tail term is negligible. As `E → 0`, the tail term diverges like `E^{-n}`.

So the ideal model never reaches zero in finite time. All extra terminal time lives in the second term.

---

## 3. The observer error

Now introduce an observer who has learned only the ordinary regime and extrapolates it into the terminal regime.

For a fall from `A` to `B`, with `A > B > 0`, the ordinary observer predicts

```text
t_pred(A,B) = (1/k) log(A/B).
```

The actual time under the tailed model is

```text
t_actual(A,B) = (1/k) [ log(A/B) + (α^n/n)(B^{-n} - A^{-n}) ].
```

Define observer error by

```text
Δt(A,B; α,n) = t_actual - t_pred.
```

Then

```text
Δt(A,B; α,n) = (α^n/(kn))(B^{-n} - A^{-n}).
```

This is the surprise, made quantitative: the gap between what an ordinary-regime observer expects and what the assumed tailed model delivers.

Three features fix its meaning:

- `Δt → 0` as `α → 0`. No assumed tail, no model-generated surprise.
- `Δt → ∞` as `B → 0` for `n > 0`. The nearer the terminal region, the larger the predicted surprise.
- `Δt` scales with `α^n`. The surprise is controlled by the tail’s onset scale and shape.

The observer is not surprised because the equation is mysterious. The observer is surprised because the ordinary clock has been extrapolated beyond its regime.

---

## 4. The surprise factor

For a terminal halving step from `2ε` to `ε`, the ordinary observer predicts the usual halving time:

```text
t_pred = (1/k) log 2.
```

The tailed model gives

```text
t_actual = (1/k) [ log 2 + (α^n/n)(ε^{-n} - (2ε)^{-n}) ].
```

Define the surprise factor by

```text
S(ε) = t_actual/t_pred.
```

Then

```text
S(ε) = 1 + ((α/ε)^n(1 - 2^{-n}))/(n log 2).
```

This depends on `ε` only through the ratio

```text
ρ = α/ε.
```

So the surprise is scale-free in this limited sense: it is not literally “one percent” that matters, but how deep into the tail the observer is watching.

At `ε ≈ α`, the surprise is order one. For `ε ≪ α`, it grows like `(α/ε)^n`.

This is why the “last percent” can feel special regardless of the full scale: the model says the felt anomaly tracks tail-depth, not the absolute reading.

---

## 5. The graft: surprise magnitude as a diagnostic map

The two halves of the note are not merely placed side by side. They are connected by a map.

A purely psychological explanation could say, qualitatively, that time feels stretched near an endpoint. This model does something narrower and more testable: it makes the magnitude of the surprise a definite function of the assumed tail shape.

```text
Δt = (α^n/(kn))(B^{-n} - A^{-n}).
```

For halving near the terminal region,

```text
S - 1 = ((α/ε)^n(1 - 2^{-n}))/(n log 2).
```

Thus the surprise is not a free psychological quantity inside this model. It is shaped by `α` and `n`.

A single surprise measurement does not uniquely recover `(α,n)`. It constrains a family of possible tails.

However, in the ideal noiseless halving case, two measurements at two distinct terminal depths are enough in principle to determine the two parameters.

Let

```text
Q_i = S(ε_i) - 1,
```

for two distinct depths `ε_1` and `ε_2`. Then

```text
Q_i = ((α/ε_i)^n(1 - 2^{-n}))/(n log 2).
```

Taking the ratio cancels `α` and gives

```text
Q_1/Q_2 = (ε_2/ε_1)^n.
```

Hence, when the data are compatible and non-degenerate,

```text
n = log(Q_1/Q_2) / log(ε_2/ε_1).
```

Once `n` is obtained, `α` is recovered from either measurement:

```text
α = ε_i [ Q_i · n log 2 / (1 - 2^{-n}) ]^{1/n}.
```

Thus the diagnostic structure is:

```text
one depth        → family of possible tails
two depths       → parameter recovery in the ideal two-parameter model
three or more    → overdetermined consistency check or falsification
```

If a physical tail is present, the map should fit the measured terminal delays with a stable parameter pair or a stable parameter family.

If no physical tail is present, the same map should fail to recover a stable tail shape. That failure is not a defeat of the note. It is the clean way to say that the last-percent feeling was observer-side only.

This is where the note survives its own uncertainty. It does not need the tail to be physically real in advance. It provides a coordinate system in which tail-real and observer-only explanations can be separated by measurement.

---

## 6. Two regimes of the report

The reports likely mix two different regimes.

### Type I — physical tail

The system really does slow its relative decay near zero.

Possible mechanisms could include protective circuitry, reserve mobilization, saturating kinetics, nonlinear readout correction, or other threshold behaviour.

In this case, `Δt` corresponds to real extra time, and the observer’s surprise is a response to a real terminal tail.

### Type II — observer error only

The system does not physically slow in the relevant variable, but the observer’s terminal attention, expectation, display interpretation, or readout nonlinearity creates the felt anomaly.

In this case, `Δt` is zero for the physical system, but the surprise remains observer-side.

The model does not decide which case holds. It provides shared coordinates — `Δt`, `S`, and the tail-to-surprise diagnostic map — in which Type I and Type II can be distinguished.

Type I should leave a stable tail signature across measurements. Type II should not.

---

## 7. Conditional finite collapse corrections for Type I

This section is conditional.

It applies only if Type I is true: that is, only if a real system has a physical terminal tail of the modelled kind.

If Type II is true, there is no physical tail to collapse. In that case the finite ending belongs to the underlying ordinary system, while the surprise belongs to the observer, display, or interpretation layer. The following corrections are therefore not part of the observer-only case.

Under the Type I assumption, the ideal tailed model still has a problem: it never reaches zero in finite time. Real systems often do. A finite-collapse correction describes how a physical terminal tail, if present, is broken.

Three broad corrections are useful.

### Type A — cutoff

Choose a small threshold `E_cut`, with

```text
0 < E_cut ≪ α.
```

The system follows the tailed law until `E(t) = E_cut`, then shuts down by rule:

```text
E(t) = E_cut  ⇒  E(t⁺) = 0.
```

This is an engineering or boundary-condition collapse.

### Type B — external drain

A tempting but incorrect finite-death attempt is

```text
dE/dt = -(kE + μ)/(1 + (α/E)^n).
```

Near zero this behaves as

```text
dE/dt ≈ -(μ/α^n)E^n.
```

For `n ≥ 1`, this still does not generally force finite-time arrival at zero.

The corrected external-drain model puts the fixed drain outside the slowdown factor:

```text
dE/dt = -kE/(1 + (α/E)^n) - μ,      μ > 0.
```

Then

```text
dE/dt → -μ     as E → 0.
```

So the system reaches zero in finite time, provided `E = 0` is treated as an absorbing boundary.

The crossover where the terminal slowdown term and the external drain have comparable magnitude is

```text
(k/α^n)E_*^{n+1} ≈ μ.
```

Hence

```text
E_* ≈ (μα^n/k)^{1/(n+1)}.
```

For `E ≫ E_*`, terminal persistence dominates. For `E ≪ E_*`, the external drain cuts the tail.

### Type C — structural collapse

In a structural collapse model, the system itself changes near a critical threshold `E_collapse`.

Below that point, the tail law is no longer valid because the structure that supported it has failed.

A schematic piecewise form is:

```text
dE/dt = -kE/(1 + (α/E)^n)       for E > E_collapse,
E = E_collapse                 ⇒ E(t⁺) = 0.
```

The point is not the specific formula. The point is that finite death can occur because the structure maintaining terminal persistence is destroyed.

The role of this section is therefore narrow: it classifies how a physical tail would terminate, if such a tail exists. It does not strengthen the claim that the tail exists.

---

## 8. Scope and non-claims

This note does not claim that any real system obeys the model equation.

It does not claim that the last-percent tail is physical.

It claims only:

1. the equation is a minimal solvable shape encoding terminal relative-slowdown;
2. the equation has an exact time law;
3. the difference between ordinary prediction and tailed evolution gives an observer-error term;
4. the surprise factor is a diagnostic function of the assumed tail shape;
5. two ideal halving-depth measurements can in principle determine the two-parameter tail model;
6. three or more measurements can overdetermine, test, or falsify the model;
7. finite-collapse corrections are conditional Type I submodels, not evidence that Type I is true.

The clean slogan is:

```text
The tail is a hypothesis.
The surprise is a measurable mismatch.
```

---

## 9. Relation to Free Numbers and the Y-axis theory

This is not a Free Numbers theorem.

This is not a Y-axis theorem.

At this stage, the relation is only metaphorical resonance:

```text
something that seemed almost gone may still be acting,
and the observer may misread the terminal regime.
```

No formal map to Free Numbers is claimed. No formal map to the Y-axis theory is claimed.

They share soil, not structure.

The note should therefore be treated as an independent appendix model: a detachable branch, not part of the trunk.
