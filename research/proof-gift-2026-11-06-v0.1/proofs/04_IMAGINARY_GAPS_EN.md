# T03 supplementary corollary: pure imaginary gap probes suffice on B_m

This supplement strengthens only the concrete tensor statement for `B_m=V^{tensor m}`, V=Im H. It preserves T03's distinction between tensor equality, a factorization of that tensor, and an original narrative history. Allowing these formal gap operations in an abstract Core is a separate decision.

## One-gap inversion

Let A1,A2,A3 be arbitrary quaternions, and let

```
f(c)=sum_(i=1)^3 A_i c e_i,  c in V,
f_r=f(e_r),  B=sum_(r=1)^3 f_r e_r.
```

Then

```
B=sum_i A_i e_i,
A_i=-(f_i+B e_i)/2.                                  (19)
```

**Proof.** Hamilton basis products give `e_r e_i e_r=e_i` for r!=i and `e_i e_i e_i=-e_i`. Hence `f_r e_r=sum_i A_i e_i-2A_r e_r`. Summing the three equations gives B. Solving the r-th equation and right-multiplying by -e_r gives (19). ∎

## Arbitrary finite length with only V-valued probes

For every finite m>=1, the restriction of F_m to B_m and to all `m-1` probe arguments in V is injective. Its values on the `3^(m-1)` tuples of the imaginary basis e1,e2,e3 determine the tensor explicitly by recursion.

**Proof.** For m=1 the response is the vector itself. For m>=2 split `T=sum_i e_i tensor T_i`. For each fixed choice of the remaining probes,

```
F_m(T)(c1,c2,...)=sum_i F_(m-1)(T_i)(c2,...) c1 e_i.
```

Use (19) on c1 to recover all three shorter response functions `F_(m-1)(T_i)`. Induction recovers each T_i. This proves existence of the inverse on the image and injectivity for every m. ∎

## Norm bounds

Equip the restricted response data with the sum of squared quaternion norms over all imaginary basis probe tuples. Then

```
||T||^2 <= ||F_m^V(T)||_HS^2 <= 4^(m-1)||T||^2.      (20)
```

**Proof.** The full one-gap identity (4) in the main note, minus its real-probe term, gives

```
sum_(r=1)^3 |sum_i A_i e_r e_i|^2
  =4 sum_i |A_i|^2-|sum_i A_i e_i|^2.
```

Cauchy–Schwarz bounds the last squared norm by `3 sum_i |A_i|^2`, so the expression lies between `sum_i|A_i|^2` and `4 sum_i|A_i|^2`. Apply this estimate to the first gap at each remaining probe tuple, and then induct on the shorter responses. The m=1 bound is equality. ∎

The exact scaled isometry (2) still concerns the **full quaternion probe** target on W_m. For the smaller pure-probe target, (20) is the stated bound; it is not falsely advertised as the same scaled isometry.

This corollary needs fewer probe tuples than the full H construction and stays within pure imaginary probes as algebraic inputs. The number of records still grows with length: it is not a constant-size signature for arbitrary histories.
