# Note 08 — Transport Policy

This note fixes the transport policy used before the restricted confluence step.

The purpose of A10 is not to prove confluence.  
Its purpose is to separate the restricted reduction relation from transport, and to state when a transport step may be used as an admissible preparation step.

```text
Transport is external to Red.
```

At this stage, any confluence theorem is restricted to `Red`.  
A10 does not assert full transport-inclusive confluence.

---

## 1. Red, Transport, LayerTransport, and Prep

A10 distinguishes four layers.

```text
Red
Transport
LayerTransport
Prep
```

`Red` is the restricted reduction relation of the Gen-normalization kernel.

`Transport` is an external term-level relation.

`LayerTransport` is the part of transport that respects the admissible identity layer.

`Prep` is the cost-oriented preparation relation obtained from `LayerTransport`.

The order is:

```text
RawTransport
  ↓
LayerTransport
  ↓
kappa_T-decreasing Prep
```

The transport cost does not make a raw transport admissible.  
A raw transport must first pass the admissible identity layer.  
Only then can `kappa_T` orient it as a preparation step.

---

## 2. Raw transport is term-level but signature-visible

Raw transport is term-level.

```text
T : X ⇝ Y
```

However, a raw transport usable in A10 must not be a black-box relation.

It must be signature-visible: the transport witness `T` must canonically and uniquely induce a partial action on signatures.

```text
T_* : Sig(X) ⇀ Sig(Y)
```

Here `T_*` is not independent data.  
It must be induced by `T`.

```text
T_* must be induced by T.
```

It must also be unique.

```text
If T induces T_* and T_*',
then T_* = T_*'.
```

If the same raw transport `T` allowed multiple different signature actions, residual preservation could be chosen after the fact.  
Such transports are not usable as preparation steps in A10.

This note does not prove the existence of signature-visible transports.  
It also does not prove whether signature-visibility implies preservation of admissible identity.  
Those questions belong to the later transport-inclusive stage.

---

## 3. The admissible identity layer is two-branched

The admissible identity layer is not a flat list of independent conditions.

Its structure is:

```text
BoundaryIso -> EqAdm

ResidualPurity is complementary to EqAdm
```

Thus the identity-layer requirement for transport has two branches.

```text
PreservesAdmissibleIdentity(T)
and
PreservesResidualMismatch(T)
```

The first branch preserves admissible identity.  
The second branch prevents erasure of residual mismatch.

Signature-visibility is not a third branch of the identity layer.  
It is an entry condition for transport: only signature-visible transports can be tested against the two identity-layer branches.

---

## 4. PreservesAdmissibleIdentity

`PreservesAdmissibleIdentity(T)` means that transport preserves the `BoundaryIso -> EqAdm` chain.

```text
PreservesAdmissibleIdentity(T)
=
the BoundaryIso-to-EqAdm chain is preserved under T.
```

This does not mean that transport creates admissible equivalence.

```text
Transport(X, Y)
does not imply
EqAdm(X, Y)
```

Transport is not an identity generator.  
It may only be used when it does not break the admissible identity structure already controlled by the identity layer.

---

## 5. PreservesResidualMismatch

`PreservesResidualMismatch(T)` means that residual-pure signatures are preserved without whitening or loss.

Raw transport is term-level, so touched and untouched residuals are not primitive notions.  
They are read from the induced signature action `T_*`.

```text
touched residual
= a residual-pure signature on which T_* acts nontrivially

untouched residual
= a residual-pure signature fixed by T_*
```

Although `T_*` is a partial map on signatures in general, it must be total on residual-pure signatures for a layer-respecting transport.

That is, for every residual-pure signature in `X`, the induced action must be defined.

```text
T_* is partial on Sig(X),
but total on ResPure(X) for LayerTransport.
```

A transport `T : X ⇝ Y` preserves residual mismatch when, for every `r` in `ResPure(X)`:

```text
1. T_*(r) is defined.

2. If T_*(r) = r' nontrivially,
   then r' is in ResPure(Y)
   and BoundaryIsoSig_T(r, r') holds.

3. If T_* fixes r,
   then r remains residual-pure in Y.
```

This blocks three failure modes.

```text
whitening:
residual -> admissible

loss:
residual -> untracked / undefined

over-restriction:
all residuals must move by BoundaryIso
```

Moved residuals require BoundaryIso-corresponding residual-pure targets.  
Fixed residuals remain residual-pure.

This allows partial induced preservation without allowing residual loss.

---

## 6. Partial preservation and full preservation

A realistic transport need not move every residual nontrivially.

In the partial-preservation regime:

```text
T_* acts nontrivially only on some residual-pure signatures.
Moved residuals must have BoundaryIso-corresponding residual-pure targets.
Fixed residuals remain residual-pure.
```

In the full-preservation regime:

```text
T_* preserves the entire residual structure.
```

The full-preservation case is the strict limiting case of transport.  
When the admissible and residual structures are fully preserved, the situation approaches the admissible-transition regime.

Thus A10 separates:

```text
partial induced preservation
= transport regime

full induced preservation
= admissible-transition regime
```

---

## 7. LayerTransport

A `LayerTransport` is a raw transport that passes the entry condition and the two identity-layer branches.

More precisely, `LayerTransport(T)` requires:

```text
1. SignatureVisible(T)

2. PreservesAdmissibleIdentity(T)

3. PreservesResidualMismatch(T)
```

These are not three parallel identity-layer branches.

`SignatureVisible(T)` is the entry condition: `T_*` must be canonically and uniquely induced by `T`.

`PreservesAdmissibleIdentity(T)` preserves the `BoundaryIso -> EqAdm` chain.

`PreservesResidualMismatch(T)` preserves residual-pure signatures without whitening or loss.

Only after these conditions are met can transport be used as preparation.

---

## 8. Transport cost kappa_T

Transport cost is distinct from the reduction weight of `Red`.

The restricted reduction kernel has its own reduction weight.

```text
weight_R = measure for Red
```

Transport preparation uses a separate well-founded measure.

```text
kappa_T : Term -> Nat
```

`kappa_T` is a term-level measure, not a witness-dependent measure.

However, `kappa_T` is used for preparation only after `LayerTransport` has been established.

```text
Prep(X, Y) :=
  exists T : X ⇝ Y,
    LayerTransport(T)
    and
    kappa_T(Y) < kappa_T(X).
```

Therefore `kappa_T` is downstream of `LayerTransport`.

```text
kappa_T is downstream of LayerTransport.
```

The transport cost is not the reduction weight.

```text
kappa_T != weight_R
```

`weight_R` controls termination of `Red`.  
`kappa_T` controls transport preparation sequences.

---

## 9. Prep asymmetry and BoundaryIso symmetry

`BoundaryIso` is symmetric.

`Prep` is generally asymmetric because it is oriented by strict decrease of `kappa_T`.

```text
BoundaryIso may go both ways.
Prep generally cannot.
```

This asymmetry is not a defect.  
It is the point of cost-oriented preparation.

The later transport-inclusive confluence question is:

```text
Can Prep-branches be closed by BoundaryIso-compatible targets?
```

A10 does not answer this question.  
It records it as a later transport-inclusive problem.

---

## 10. A10 Transport Separation Principle

```text
A10 Transport Separation Principle

Transport is external to Red.

A raw transport T : X ⇝ Y is usable for preparation only if it is signature-visible:
it must canonically and uniquely induce a partial signature action T_*.

Signature-visibility is the entry condition for LayerTransport,
not a third branch of the admissible identity layer.

LayerTransport is the part of RawTransport that respects the admissible identity layer.

It must preserve the BoundaryIso -> EqAdm chain
and preserve residual-pure signatures without whitening or loss.

The induced action T_* may be partial on signatures in general,
but it must be total on residual-pure signatures for LayerTransport.

Prep is the kappa_T-decreasing subrelation of LayerTransport.

kappa_T is a term-level well-founded measure,
distinct from the reduction weight of Red.

This policy fixes the scope of the next confluence question:
any confluence theorem at this stage is restricted to Red.

A10 does not assert full transport-inclusive confluence.
```

---

## 11. What A10 does not claim

A10 does not claim:

```text
full transport-inclusive confluence
restricted Red confluence
unique transport normal form
global normal form uniqueness
existence of signature-visible transports
signature-visibility implies admissible-identity preservation
geometric interpretation of kappa_T
kappa_T = vertical response coefficient
kappa_T = phase-loss measure
```

A10 fixes the admissibility policy for transport.

It is a selection rule for which transports may be used as preparation, not an existence theorem for such transports.

The next mathematical target is:

```text
restricted Red confluence
```

Only after the restricted confluence problem is separated can transport-inclusive reduction be revisited.
