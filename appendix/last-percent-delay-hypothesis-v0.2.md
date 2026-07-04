# Last Percent Delay Hypothesis v0.2

## From Minimal Terminal Persistence to Observer Surprise

This note integrates the minimal v0.1 model with a stronger exactly solvable
v0.2 model.

The shared question is simple:

> why can the last small part of a quantity appear to persist much longer than
> the earlier part?

The answer is not just that there is “less left.” The mathematical mechanism is:

> near zero, the decay rate itself can decrease.

Version v0.1 isolated this mechanism in a minimal form. Version v0.2 adds an
exactly solvable slowdown law, observer error, surprise factor, and finite
collapse corrections.

This is a mathematical model. It does not claim that real batteries,
smartphones, organisms, candles, or engineered systems obey this equation
exactly.

---

## 1. Generic terminal persistence model

Let $E(t)>0$ denote a remaining amount. Ordinary exponential decay is

$$
\frac{dE}{dt}=-kE,\qquad k>0.
$$

Its solution is

$$
E(t)=E_0e^{-kt}.
$$

The relative decay rate is constant:

$$
-\frac{d}{dt}\log E(t)=k.
$$

Thus every halving takes the same time:

$$
\frac{\log2}{k}.
$$

A terminal persistence model modifies this by inserting a slowdown factor
$R(E)$:

$$
\frac{dE}{dt}=-kE\,R(E).
$$

The effective relative decay rate is

$$
h(E)=kR(E).
$$

To model zero-near persistence, require

$$
0<R(E)\le1,
$$

and

$$
R(E)\to0\qquad(E\to0).
$$

Then the decay rate itself decreases near zero.

---

## 2. Minimal v0.1 slowdown family

A simple smooth choice is

$$
R(E)=\left(\frac{E}{E+\alpha}\right)^p,\qquad\alpha>0,\quad p>0.
$$

This gives

$$
\frac{dE}{dt}=-kE\left(\frac{E}{E+\alpha}\right)^p.
$$

Near zero, $E\ll\alpha$, so

$$
R(E)\sim\left(\frac{E}{\alpha}\right)^p.
$$

Therefore,

$$
\frac{dE}{dt}\sim-\frac{k}{\alpha^p}E^{p+1}.
$$

Writing

$$
\lambda=\frac{k}{\alpha^p},
$$

the terminal leading equation is

$$
\frac{dE}{dt}=-\lambda E^{p+1}.
$$

Since

$$
\frac{d}{dt}E^{-p}=p\lambda,
$$

we obtain

$$
E(t)\sim\left(E(t_0)^{-p}+\frac{pk}{\alpha^p}(t-t_0)\right)^{-1/p}.
$$

Thus the terminal tail is power-law:

$$
E(t)\sim t^{-1/p}.
$$

This is the v0.1 core:

> the process slows down because the decay rate itself decays near zero.

---

## 3. Exactly solvable v0.2 slowdown law

For v0.2, choose the Hill-type slowdown factor

$$
R_n(E)=\frac{1}{1+\left(\frac{\alpha}{E}\right)^n}=\frac{E^n}{E^n+\alpha^n},
$$

with

$$
\alpha>0,\qquad n\ge1.
$$

The model is

$$
\frac{dE}{dt}=-\frac{kE}{1+\left(\frac{\alpha}{E}\right)^n}.
$$

Equivalently,

$$
\frac{dE}{dt}=-k\,\frac{E^{n+1}}{E^n+\alpha^n}.
$$

The parameters are:

- $k>0$: ordinary-region decay rate,
- $\alpha>0$: terminal crossover scale,
- $n\ge1$: terminal resistance exponent.

This form is exactly integrable and cleanly separates the ordinary clock from
the terminal clock.

---

## 4. Ordinary region and terminal region

### Ordinary region

If $E\gg\alpha$, then

$$
\left(\frac{\alpha}{E}\right)^n\ll1.
$$

Therefore,

$$
\frac{dE}{dt}\approx-kE.
$$

The system behaves like ordinary exponential decay.

### Terminal region

If $E\ll\alpha$, then

$$
1+\left(\frac{\alpha}{E}\right)^n\sim\left(\frac{\alpha}{E}\right)^n.
$$

Therefore,

$$
\frac{dE}{dt}\sim-\frac{k}{\alpha^n}E^{n+1}.
$$

So the terminal region is no longer exponential. It has a power-law tail.

---

## 5. Nondimensional form

Set

$$
x=\frac{E}{\alpha},\qquad\tau=kt.
$$

Then the equation becomes

$$
\frac{dx}{d\tau}=-\frac{x^{n+1}}{1+x^n}.
$$

In this form:

- $k$ sets the ordinary clock speed,
- $\alpha$ sets the terminal entrance scale,
- $n$ sets the strength of the terminal delay.

---

## 6. Exact implicit solution

The equation is separable:

$$
dt=-\frac{1+\left(\frac{\alpha}{E}\right)^n}{kE}\,dE.
$$

For decay from $E_0$ to $E$, where $0<E<E_0$, the elapsed time is

$$
t(E)=\frac{1}{k}\int_E^{E_0}\left(\frac{1}{u}+\alpha^n u^{-n-1}\right)du.
$$

Therefore,

$$
t(E)=\frac{1}{k}\left[\log\frac{E_0}{E}+\frac{\alpha^n}{n}\left(E^{-n}-E_0^{-n}\right)\right].
$$

This has two terms:

$$
t(E)=t_{\mathrm{ordinary}}(E)+t_{\mathrm{terminal}}(E).
$$

The ordinary clock is

$$
t_{\mathrm{ordinary}}(E)=\frac{1}{k}\log\frac{E_0}{E}.
$$

The terminal clock is

$$
t_{\mathrm{terminal}}(E)=\frac{\alpha^n}{kn}\left(E^{-n}-E_0^{-n}\right).
$$

As $E\to0$, the terminal term diverges. Thus the ideal continuous model does
not reach zero in finite time.

---

## 7. Observer error

Now define an observer who only saw the ordinary region and therefore assumes
ordinary exponential decay:

$$
\frac{dE}{dt}=-kE.
$$

For a transition from $A$ down to $B$, with $A>B>0$, this observer predicts

$$
t_{\mathrm{pred}}=\frac{1}{k}\log\frac{A}{B}.
$$

The actual time under the v0.2 slowdown model is

$$
t_{\mathrm{actual}}=\frac{1}{k}\left[\log\frac{A}{B}+\frac{\alpha^n}{n}\left(B^{-n}-A^{-n}\right)\right].
$$

Define observer error by

$$
\Delta t=t_{\mathrm{actual}}-t_{\mathrm{pred}}.
$$

Then

$$
\Delta t=\frac{\alpha^n}{kn}\left(B^{-n}-A^{-n}\right).
$$

In the ordinary region, this error is small. In the terminal region, it can
become large.

The observer is surprised because the extrapolated clock is wrong.

---

## 8. Surprise factor

Define the surprise factor by

$$
S=\frac{t_{\mathrm{actual}}}{t_{\mathrm{pred}}}.
$$

Then

$$
S=1+\frac{\frac{\alpha^n}{n}\left(B^{-n}-A^{-n}\right)}{\log(A/B)}.
$$

This dimensionless number measures how much longer the transition takes than the
ordinary exponential observer expected.

For a terminal halving step $2\varepsilon\to\varepsilon$, we get

$$
S(2\varepsilon\to\varepsilon)=1+\frac{\left(\frac{\alpha}{\varepsilon}\right)^n\left(1-2^{-n}\right)}{n\log2}.
$$

Thus,

$$
S(2\varepsilon\to\varepsilon)\to\infty\qquad(\varepsilon\to0).
$$

The closer the system is to zero, the more wrong the ordinary observer becomes.

---

## 9. Terminal halving time

The actual time for the terminal halving step $2\varepsilon\to\varepsilon$ is

$$
T(2\varepsilon\to\varepsilon)=\frac{1}{k}\left[\log2+\frac{\alpha^n}{n}\left(\varepsilon^{-n}-(2\varepsilon)^{-n}\right)\right].
$$

Equivalently,

$$
T(2\varepsilon\to\varepsilon)=\frac{1}{k}\left[\log2+\frac{\alpha^n}{n}\left(1-2^{-n}\right)\varepsilon^{-n}\right].
$$

So, as $\varepsilon\to0$,

$$
T(2\varepsilon\to\varepsilon)\sim\frac{\alpha^n}{kn}\left(1-2^{-n}\right)\varepsilon^{-n}.
$$

The terminal halving time diverges as a power law.

---

## 10. Finite collapse corrections

The ideal slowdown model never reaches zero in finite time. Real systems often
do. A finite-collapse correction describes how the infinite terminal tail is
broken.

This note separates three types.

---

### Type I: cutoff model

Choose a small cutoff threshold

$$
0<E_{\mathrm{cut}}\ll\alpha.
$$

The system follows the slowdown equation until $E(t)=E_{\mathrm{cut}}$, and then
is set to zero by a boundary rule:

$$
E(t)=E_{\mathrm{cut}}\quad\Rightarrow\quad E(t^+)=0.
$$

This is a discontinuous engineering collapse.

Interpretation examples include shutdown thresholds, safety cutoff rules, and
display-level termination.

---

### Type II: external drain model

A tempting but incorrect finite-death attempt is

$$
\frac{dE}{dt}=-\frac{kE+\mu}{1+\left(\frac{\alpha}{E}\right)^n}.
$$

Near zero, this behaves as

$$
\frac{dE}{dt}\sim-\frac{\mu}{\alpha^n}E^n.
$$

For $n\ge1$, this does not generally force finite-time arrival at zero.

The corrected external-drain model puts the fixed drain outside the slowdown
factor:

$$
\frac{dE}{dt}=-\frac{kE}{1+\left(\frac{\alpha}{E}\right)^n}-\mu,\qquad\mu>0.
$$

Then

$$
\frac{dE}{dt}\to-\mu\qquad(E\to0).
$$

Thus the system reaches zero in finite time, provided $E=0$ is treated as an
absorbing boundary.

The crossover point where the terminal slowdown term and the external drain have
comparable magnitude is obtained from

$$
\frac{k}{\alpha^n}E_\ast^{n+1}\sim\mu.
$$

Hence

$$
E_\ast\sim\left(\frac{\mu\alpha^n}{k}\right)^{1/(n+1)}.
$$

For $E\gg E_\ast$, terminal persistence dominates. For $E\ll E_\ast$, the
external drain dominates and cuts the tail.

---

### Type III: structural collapse model

In a structural collapse model, the system itself changes near a critical
threshold

$$
E_{\mathrm{collapse}}.
$$

The slowdown law is no longer valid below this threshold because the structure
that supported the tail has failed.

One may describe this by a piecewise rule:

$$
\frac{dE}{dt}=-\frac{kE}{1+\left(\frac{\alpha}{E}\right)^n}\qquad(E>E_{\mathrm{collapse}}),
$$

with a collapse condition

$$
E=E_{\mathrm{collapse}}\quad\Rightarrow\quad E(t^+)=0.
$$

The point is not the specific formula. The point is that finite death can occur
because the structure that maintained terminal persistence is destroyed.

---

## 11. What v0.2 adds

Version v0.1 established the minimal mechanism:

> near zero, the decay rate itself decreases.

Version v0.2 adds:

1. an exactly solvable Hill-type slowdown law,
2. a decomposition into ordinary clock and terminal clock,
3. observer error,
4. surprise factor,
5. finite-collapse corrections.

The central message becomes:

> the last percent is surprising because the observer continues to use the
> ordinary clock after the terminal clock has taken over.

---

## 12. Scope and non-claims

This is not a complete theory of batteries, living systems, candles, or
engineered shutdown behavior.

The model does not claim that any particular physical system obeys this ODE.

Real systems may involve:

- measurement quantization,
- display smoothing,
- cutoff rules,
- hidden reserves,
- nonlinear material behavior,
- structural degradation,
- external drains,
- threshold effects.

The point is narrower:

> terminal persistence can be produced by a smooth transition from ordinary
> decay to a zero-near slowdown law.

The observer experiences this as delay because the observer extrapolates the
ordinary region into the terminal region.

---

## 13. Connection points

This note is not part of the Free Numbers core.

It is a nearby mathematical model about terminal persistence, observer error,
and boundary behavior. Possible future connection points include:

- residual persistence,
- delayed disappearance,
- zero-near dynamics,
- observer extrapolation error,
- boundary collapse,
- finite death after infinite-tail dynamics.

The intended relation is therefore:

> not a Free Numbers theorem, but a nearby model with compatible geometry.

The useful slogan is:

> the tail is real, but the surprise belongs to the observer.
