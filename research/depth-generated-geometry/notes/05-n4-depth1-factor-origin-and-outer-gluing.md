# Note 05 — (n=4,d=1) Factor-Origin Theorem

## 両端だけが値へ縫い付けられ、中央 response chart は自由に残る

**Status:** (n=4) proved here; the all-(n\) extension is proved in Note 06

---

## 0. 主結果

\[
E:=\operatorname{Hom}_{\mathbb R}(V,\mathbb H)
\]

とし、Note 04 の contractions

\[
r(F)=\sum_aF(e_a)e_a,
\qquad
\ell(F)=\sum_ae_aF(e_a)
\]

を使う。

length four の depth-one profile を

\[
(q,F_1,F_2,F_3)
\in
\mathbb H\oplus E^{\oplus3}
\]

とする。この profile が実現可能であるための必要十分条件は

\[
\boxed{
q=r(F_1)=\ell(F_3).
}

中央の response

\[
F_2\in E
\]

には、depth one では追加の線形 compatibility condition がない。

したがって

\[
\boxed{
\mathcal Q_{4,1}
\cong
\bigl(E\times_{\mathbb H}E\bigr)
\oplus E,
}

ここで fiber product は両端の ((F_1,F_3)) に対して取る。

次元は

\[
\boxed{
\dim\mathcal Q_{4,1}
=20+12
=32.
}

depth-zero value を固定した birth layer は

\[
\boxed{
K_{4,1}^{\mathrm{birth}}
\cong
\ker r
\oplus E
\oplus\ker\ell,
}

よって

\[
\boxed{
\dim K_{4,1}^{\mathrm{birth}}
=8+12+8
=28.
}

この三分解が、(n=4) で同じ spin の複数 copy が異なる深度へ分裂し始める factor origin を明示する。

---

## 1. length-four depth-one profile

pure word を

\[
x=a|b|c|d
\qquad(a,b,c,d\in V)
\]

とする。compressed value は

\[
q_x=dcba.
\]

三つの internal responses は

\[
\boxed{
F_{1,x}(z)=dcbza,
}

\[
\boxed{
F_{2,x}(z)=dczba,
}

\[
\boxed{
F_{3,x}(z)=dzcba.
}

したがって combined map は

\[
D_4^{\le1}:
V^{\otimes4}
\to
\mathbb H\oplus E^{\oplus3}.
\]

ambient target dimension は

\[
4+3\cdot12=40.
\]

---

## 2. outer-gluing identities

虚 quaternion (u\in V) に対する恒等式

\[
\sum_ae_aue_a=u
\]

を使う。

第一 response の right contraction は

\[
\begin{aligned}
r(F_{1,x})
&=\sum_aF_{1,x}(e_a)e_a\\
&=\sum_adcbe_aae_a\\
&=dcb\left(\sum_ae_aae_a\right)\\
&=dcba\\
&=q_x.
\end{aligned}
\]

第三 response の left contraction は

\[
\begin{aligned}
\ell(F_{3,x})
&=\sum_ae_aF_{3,x}(e_a)\\
&=\sum_ae_ade_acba\\
&=\left(\sum_ae_ade_a\right)cba\\
&=dcba\\
&=q_x.
\end{aligned}
\]

したがって、すべての actual profiles は

\[
\boxed{
q=r(F_1)=\ell(F_3)
}

を満たす。

中央 response (F_2) には、同じ一段 contraction で (q) を回収する外端がない。左にも右にも未圧縮の boundary block が残るからである。

---

## 3. Intrinsic Presentation Theorem at (n=4,d=1)

候補空間を

\[
\mathcal P_{4,1}
:=
\{(q,F_1,F_2,F_3)
\mid q=r(F_1)=\ell(F_3)\}
\]

とする。

二つの quaternion equations は独立な8条件なので

\[
\dim\mathcal P_{4,1}
=40-8
=32.
\]

一方、Free Numbers Core v1 の exact depth-one certificate は

\[
\operatorname{rank}D_4^{\le1}=32
\]

を与える。

Section 2 で

\[
\operatorname{im}D_4^{\le1}
\subseteq
\mathcal P_{4,1}
\]

を示した。両者の次元が等しいので次を得る。

### Theorem 3.1

\[
\boxed{
\operatorname{im}D_4^{\le1}
=
\mathcal P_{4,1}.
}

すなわち

\[
\boxed{
\mathcal Q_{4,1}
\cong
\bigl(E\times_{\mathbb H}E\bigr)\oplus E.
}

中央 (E) は (F_2) に対応する。∎

---

## 4. depth-one normal form

Note 04 の canonical section

\[
s(q)(z)
=
\langle\operatorname{Im}q,z\rangle
-\frac{\operatorname{Re}q}{3}z
\]

は

\[
r(s(q))=\ell(s(q))=q
\]

を満たす。

したがって、すべての depth-one profiles は一意に

\[
\boxed{
(q,F_1,F_2,F_3)
=
\bigl(q,\ s(q)+U_L,\ M,\ s(q)+U_R\bigr)
}

と書ける。ここで

\[
U_L\in\ker r,
\qquad
M\in E,
\qquad
U_R\in\ker\ell.
\]

よって vector-space decomposition として

\[
\boxed{
\mathcal Q_{4,1}
\cong
\mathbb H
\oplus\ker r
\oplus E
\oplus\ker\ell.
}

depth zero から新たに加わる部分は、後三項である。

---

## 5. factor-origin decomposition

(SO(3))-modules として

\[
\mathbb H\cong V_0\oplus V_1,
\]

\[
E\cong V_0\oplus2V_1\oplus V_2,
\]

\[
\ker r\cong\ker\ell\cong V_1\oplus V_2.
\]

したがって depth-one birth layer は

\[
\begin{aligned}
K_{4,1}^{\mathrm{birth}}
&\cong
(V_1\oplus V_2)
\oplus
(V_0\oplus2V_1\oplus V_2)
\oplus
(V_1\oplus V_2)\\
&\cong
\boxed{V_0\oplus4V_1\oplus3V_2}.
\end{aligned}
\]

次元は

\[
1+4\cdot3+3\cdot5
=28.
\]

これは Core v1 の verified depth-one table と完全に一致する。

| factor origin | response sector | (SO(3)) content | dimension |
|---|---|---|---:|
| left boundary | (ker r) | (V_1\oplus V_2) | 8 |
| middle gap | (E) | (V_0\oplus2V_1\oplus V_2) | 12 |
| right boundary | (ker\ell) | (V_1\oplus V_2) | 8 |
| total |  | (V_0\oplus4V_1\oplus3V_2) | 28 |

ここで同じ spin label を持つ copy が、どの gap から来たかによって区別される。

---

## 6. multiplicity-depth splitting の起源

length four の全 state space は

\[
V^{\otimes4}
\cong
3V_0\oplus6V_1\oplus6V_2\oplus3V_3\oplus V_4.
\]

depth zero の compressed value が

\[
V_0\oplus V_1
\]

を読む。

depth one で Note 05 の factor-origin layer

\[
V_0\oplus4V_1\oplus3V_2
\]

が加わる。したがって depth one までの visible space は

\[
\boxed{
\mathcal Q_{4,1}
\cong
2V_0\oplus5V_1\oplus3V_2.
}

残る invisible space は差を取って

\[
\boxed{
\widehat F_1^{(4)}
\cong
V_0\oplus V_1\oplus3V_2\oplus3V_3\oplus V_4.
}

ここから重要な事実が読める。

- six copies of (V_2) のうち、三つは left / middle / right の gap origin を持つため depth one で見える。
- 残り三つの (V_2) は単一 gap response では区別されず、depth two まで不可視である。Note 07 により、この40次元層は coherence 条件そのものではなく、三つの pair-origin residual factors に分解することが判明した。
- (V_1) も、depth zero で一つ、depth one で四つ、depth two で一つという origin split を持つ。
- (V_0) も、value、middle-gap response、depth-two-visible direction の三段に分かれる。

したがって (n=4) で起きた multiplicity-depth splitting は、同一 spin 内のランダムな分裂ではない。

\[
\boxed{
\text{spin multiplicity}
\quad\text{の内部に}\quad
\text{relation-slot origin}
\quad\text{がある。}
}

---

## 7. all-(n) outer-gluing pattern

length (n\ge3) の depth-one profile を

\[
(q,F_1,\ldots,F_{n-1})
\in
\mathbb H\oplus E^{\oplus(n-1)}
\]

とする。

pure word に対する同じ外端 contraction により、すべての (n\ge3) で

\[
\boxed{
q=r(F_1),
\qquad
q=\ell(F_{n-1})
}

が成り立つ。

したがって intrinsic outer-gluing candidate を

\[
\boxed{
\mathcal P_{n,1}
:=
\left\{
(q,F_1,\ldots,F_{n-1})
\ \middle|\
q=r(F_1)=\ell(F_{n-1})
\right\}
}

と定義できる。

vector-space structure は

\[
\boxed{
\mathcal P_{n,1}
\cong
\mathbb H
\oplus\ker r
\oplus E^{\oplus(n-3)}
\oplus\ker\ell.
}

したがって

\[
\boxed{
\dim\mathcal P_{n,1}
=4+8+12(n-3)+8
=12n-16.
}

depth-one birth dimension は

\[
\boxed{
h_n(1)=12n-20.
}

representation content は

\[
\boxed{
K_{n,1}^{\mathrm{birth}}
\cong
(n-3)V_0
\oplus
(2n-4)V_1
\oplus
(n-1)V_2.
}

### Theorem 7.1 — all-(n) depth-one outer-gluing theorem

すべての (n\ge3) について

\[
\boxed{
\mathcal Q_{n,1}
=
\mathcal P_{n,1},
}

すなわち

\[
\boxed{
\operatorname{rank}D_n^{\le1}
=12n-16.
}

### Status

- (n=3): Note 04 で proved。
- (n=4): 本ノートで proved from the exact rank certificate。
- 全 (n\ge3): Note 06 で localized zero-compression gadgets を用いて proved。
- (n=3,4,5,6,7): exact integer certificate で独立検算。

Note 06 は、他の universal linear relations が存在しないことを、各 slot を独立に生成する局所 residual gadgets によって示す。

---

## 8. depth-one における「空間」の形

Theorem 7.1 が示す生成像は明快である。

### 両端

最初と最後の response charts は、depth-zero quaternionic value へ縫い付けられる。

\[
r(F_1)=q=\ell(F_{n-1}).
\]

### 内部

中間の

\[
F_2,\ldots,F_{n-2}
\]

は、depth one では互いにも (q) にもまだ接続されない。各 chart は12次元のまま自由である。

### deeper depth

depth two の probes は複数 gaps を同時に読む。Note 07 は (n=4) について、それらが三つの pair charts と明示的 boundary matching equations で完全に記述できることを示す。

したがって depth one の空間は、完成した鎖ではない。

\[
\boxed{
\text{端点だけが固定され、内部 chart が未接続で浮いている。}
}

深度を増やすと、その浮いた charts を区別しうる simultaneous-response data が追加される。

これは「空間が先にある」の反転を、かなり具体的に表す。

---

## 9. curvature への含意

depth one では internal charts が独立なので、まだ loop consistency を問えない。Note 07 の depth-two matching complex は chart gluing を与えるが、transport composition や holonomy はまだ与えない。

このため plaquette を最初から既成空間上に置くのではなく、次の順序で作るべきである。

1. depth-one charts (F_r\in E) を置く。
2. depth-two overlap responses で adjacent charts を接続する。
3. 四つ以上の charts が閉路を作る最小 configuration を選ぶ。
4. 二つの合成経路の差を nonconfluence residual とする。
5. その residual の first-detection depth を測る。

つまり curve / loop さえも先に置くのではなく、relation-depth compatibility から後置する。

---

## 10. Exact certificate

`certificates/depth1_outer_gluing_certificate.py` は外部ライブラリを使わず、exact integer arithmetic で (n=3,4,5,6,7) について次を検証する。

- outer compatibility map の rank が8。
- actual profiles が outer equations を満たす。
- actual depth-one rank が (12n-16)。
- actual image と intrinsic outer-gluing candidate が一致する。

Expected final line:

```text
ALL CHECKS PASSED
```

---

## 11. 次の証明課題

all-(n) depth-one theorem は Note 06 で閉じた。

この対象は Note 07 で解かれた。(n=4,d=2) の40次元 birth layer は

\[
\dim\mathcal Q_{4,2}-\dim\mathcal Q_{4,1}
=72-32
=40.
\]

pair origin により (12+16+12) へ分解する。ただし、これは curvature ではなく、固定された depth-one boundary 上の独立な pair-chart residual freedom である。
