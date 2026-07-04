# Last Percent Delay Hypothesis v0.1

## A Minimal Model of Compound Persistence Near Zero

This note gives a minimal mathematical model for a common terminal phenomenon:

> the last small part of a quantity seems to persist longer than the earlier part.

The motivating image is the familiar “last 1%” effect, but the note does **not**
claim that real batteries, operating systems, or displayed percentages obey this
specific model. The aim is narrower: to isolate a simple mechanism by which
persistence compounds near zero.

The key idea is:

> near zero, the decay rate itself may decay.

When the remaining amount gets smaller, the process does not merely have less to
lose; it may also become worse at losing. This creates a terminal tail.

---

## 1. Baseline: ordinary exponential decay

Let $E(t)>0$ denote a remaining amount. The standard exponential model is

$$
\frac{dE}{dt}=-kE, \qquad k>0.
$$

Its solution is

$$
E(t)=E_0e^{-kt}.
$$

In this model the relative decay rate is constant:

$$
-\frac{d}{dt}\log E(t)=k.
$$

The time needed to halve the remaining amount is always

$$
\frac{\log 2}{k},
$$

regardless of whether one goes from $100$ to $50$, from $2$ to $1$, or from
$0.02$ to $0.01$.

Thus ordinary exponential decay does not by itself model terminal persistence.
It has no special “last percent” mechanism.

---

## 2. A residual slowdown factor

Introduce a slowdown factor $R(E)$ and replace the exponential model by

$$
\frac{dE}{dt}=-kE\,R(E).
$$

The effective relative decay rate is now

$$
h(E)=kR(E).
$$

To model terminal persistence, we want

$$
0<R(E)\le 1,
$$

and

$$
R(E)\to 0 \qquad (E\to 0).
$$

That is: as the remaining amount approaches zero, the process slows down.

A minimal smooth choice is

$$
R(E)=\left(\frac{E}{E+\alpha}\right)^p, \qquad \alpha>0,\quad p>0.
$$

Here:

- $k$ is the baseline decay scale,
- $\alpha$ is the terminal crossover scale,
- $p$ is the terminal persistence exponent.

This gives the model

$$
\frac{dE}{dt} = -kE\left(\frac{E}{E+\alpha}\right)^p.
$$

Equivalently,

$$
\frac{dE}{dt} = -k\,\frac{E^{p+1}}{(E+\alpha)^p}.
$$

---

## 3. Two regimes

### Away from zero

If $E\gg \alpha$, then

$$
\frac{E}{E+\alpha}\approx 1,
$$

so

$$
R(E)\approx 1.
$$

The model behaves like ordinary exponential decay:

$$
\frac{dE}{dt}\approx -kE.
$$

### Near zero

If $E\ll \alpha$, then

$$
\frac{E}{E+\alpha}\approx \frac{E}{\alpha},
$$

so

$$
R(E)\approx \left(\frac{E}{\alpha}\right)^p.
$$

The model becomes

$$
\frac{dE}{dt} \sim -\frac{k}{\alpha^p}E^{p+1}.
$$

This is no longer exponential. It is a terminal power-law tail.

---

## 4. Terminal asymptotic

Let

$$
\lambda=\frac{k}{\alpha^p}.
$$

Near zero, the leading equation is

$$
\frac{dE}{dt}=-\lambda E^{p+1}.
$$

Since

$$
\frac{d}{dt}E^{-p} = -pE^{-p-1}\frac{dE}{dt} = p\lambda,
$$

we obtain

$$
E(t)^{-p} = E(t_0)^{-p}+p\lambda(t-t_0).
$$

Therefore

$$
E(t) \sim \left( E(t_0)^{-p} + \frac{pk}{\alpha^p}(t-t_0) \right)^{-1/p}.
$$

So the terminal tail decays like

$$
E(t)\sim t^{-1/p}.
$$

The important point is that the quantity approaches zero much more slowly than an
exponential tail. In the ideal continuous model, it never reaches zero in finite
time.

---

## 5. Time to pass a terminal threshold

For $0<E_2<E_1$, separation of variables gives the exact time

$$
T(E_1\to E_2) = \frac{1}{k} \int_{E_2}^{E_1} \frac{(E+\alpha)^p}{E^{p+1}}\,dE.
$$

Near zero, this has the leading asymptotic

$$
T(E_1\to E_2) \sim \frac{\alpha^p}{kp} \left( E_2^{-p}-E_1^{-p} \right).
$$

In particular, the time to move from $2\varepsilon$ down to $\varepsilon$ is

$$
T(2\varepsilon\to \varepsilon) \sim \frac{\alpha^p}{kp} \left( 1-2^{-p} \right) \varepsilon^{-p}.
$$

As $\varepsilon\to 0$, this diverges.

Thus the closer the process is to zero, the longer the next halving takes.

---

## 6. Compound persistence

Define the terminal halving time

$$
\tau(\varepsilon)=T(2\varepsilon\to \varepsilon).
$$

From the previous section,

$$
\tau(\varepsilon) \sim \frac{\alpha^p}{kp} \left( 1-2^{-p} \right) \varepsilon^{-p}.
$$

Therefore

$$
\frac{\tau(\varepsilon)}{\tau(2\varepsilon)} \sim 2^p.
$$

Each later halving is longer than the previous terminal halving by the factor

$$
2^p.
$$

This is the “compound” part of the model:

```text
less remaining amount
=> smaller decay rate
=> more persistence
=> even slower terminal change
```

In ordinary exponential decay, halving time is constant. In the terminal
persistence model, halving time grows geometrically as one approaches zero.

---

## 7. The case $p=1$

The simplest case is

$$
R(E)=\frac{E}{E+\alpha}.
$$

Then

$$
\frac{dE}{dt} = -k\frac{E^2}{E+\alpha}.
$$

Separating variables,

$$
\frac{E+\alpha}{E^2}\,dE=-k\,dt.
$$

Since

$$
\int \frac{E+\alpha}{E^2}\,dE = \int\left(\frac{1}{E}+\frac{\alpha}{E^2}\right)dE = \log E-\frac{\alpha}{E},
$$

the time from $E_1$ to $E_2$ is

$$
T(E_1\to E_2) = \frac{1}{k} \left[ \log\frac{E_1}{E_2} + \alpha\left(\frac{1}{E_2}-\frac{1}{E_1}\right) \right].
$$

The exponential part contributes only

$$
\frac{1}{k}\log\frac{E_1}{E_2},
$$

while the terminal persistence term contributes

$$
\frac{\alpha}{k} \left( \frac{1}{E_2}-\frac{1}{E_1} \right).
$$

As $E_2\to 0$, the second term dominates.

For the halving step $2\varepsilon\to \varepsilon$,

$$
T(2\varepsilon\to \varepsilon) = \frac{1}{k} \left[ \log 2+\frac{\alpha}{2\varepsilon} \right].
$$

The terminal halving time grows like

$$
\frac{\alpha}{2k}\varepsilon^{-1}.
$$

---

## 8. Comparison with exponential decay

The contrast can be summarized as follows.

| model | equation | terminal halving time |
|---|---|---|
| exponential decay | $\frac{dE}{dt}=-kE$ | constant: $\frac{\log 2}{k}$ |
| terminal persistence | $\frac{dE}{dt}=-kE\left(\frac{E}{E+\alpha}\right)^p$ | grows like $\varepsilon^{-p}$ |

The terminal persistence model does not merely slow the entire process by a
constant factor. It changes the tail type.

The ordinary exponential tail is

$$
E(t)\sim e^{-kt}.
$$

The terminal persistence tail is

$$
E(t)\sim t^{-1/p}.
$$

---

## 9. Scope

This note is a minimal mathematical model.

It does not claim that a real battery, a smartphone display, a physical
discharge curve, or a particular engineered system follows this equation.

In real systems, there may be:

- quantization,
- thresholding,
- hidden reserve,
- display smoothing,
- cutoff rules,
- measurement error,
- nonlinear physical discharge laws.

Those effects may also produce last-percent behavior.

The present note isolates a different mechanism:

> the decay rate itself decreases near zero.

This alone is enough to produce compound terminal persistence.

---

## 10. Connection points

This note is not part of the Free Numbers core.

It is a nearby mathematical note about persistence near a boundary. Possible
future connection points include:

- residual persistence,
- boundary behavior,
- zero-near dynamics,
- delayed disappearance,
- compound effects in terminal regimes.

The intended relation is therefore:

> not a Free Numbers theorem, but a nearby model.

It is a small model of how “almost gone” can become structurally long-lived.
