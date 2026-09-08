# Note 02 — 全グレード内在的終端応答定理

## (V^{\otimes n}) を先に置かず、局所デコーダだけから exact-response space を作る

**Status:** proved from the Core v1 local decoder  
**Depends on:** Note 01; the invertibility of the local quaternionic decoder (Theta)

---

## 0. 主結果

Free Numbers Core v1 では exact-response space を

\[
\mathfrak A_n:=\operatorname{im}A_n
\]

と定義していた。これは復元理論として正しいが、存在論的な順序は

\[
V^{\otimes n}
\longrightarrow
\operatorname{im}A_n
\]

であり、state space が先にある。

本ノートでは順序を反転する。局所デコーダだけから response space

\[
\mathfrak Q_n
\]

を先に再帰定義し、その後で

\[
\boxed{
A_n:V^{\otimes n}\xrightarrow{\ \cong\ }\mathfrak Q_n
}
\]

を表現定理として証明する。

結論は次である。

> 有限グレードの終端 all-gap response space は、ambient state space の像として定義する必要がない。局所 quaternionic admissibility を深度方向へ反復するだけで、一意に構成できる。

---

## 1. 局所デコーダ

局所データを

\[
V=\operatorname{Im}\mathbb H
\]

とする。Core v1 の局所 encoder は

\[
\Theta:
V\otimes\mathbb H
\longrightarrow
\operatorname{Hom}(V,\mathbb H)
\]

であり、向きづけられた正規直交基底 ((e_1,e_2,e_3)) に対して

\[
\boxed{
\Theta\!\left(\sum_{a=1}^3e_a\otimes h_a\right)(d)
=
\sum_{a=1}^3e_adh_a.
}
\]

その逆は

\[
\boxed{
h_a
=
\frac12
\sum_{b,c=1}^3
\varepsilon_{abc}e_bF(e_c).
}

したがって

\[
\Theta^{-1}(F)
=
\sum_ae_a\otimes h_a.
\]

(Theta) は12次元実ベクトル空間の同型であり、Core v1 の規約では

\[
\det\Theta=256.
\]

重要なのは determinant の値ではなく、同じ局所逆写像を深度ごとに反復できることである。

---

## 2. 多重線形応答に対する一段デコーダ

(n\ge2) とし、

\[
F\in\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\]

を取る。最後の probe variable だけを見ると、各

\[
\mathbf d=(d_1,\ldots,d_{n-2})
\]

に対して slice

\[
F_{\mathbf d}:V\to\mathbb H,
\qquad
F_{\mathbf d}(d):=F(\mathbf d,d)
\]

が得られる。

各 slice に (Theta^{-1}) を適用し、

\[
\boxed{
\mathcal D_nF
\in
V\otimes
\operatorname{Hom}(V^{\otimes(n-2)},\mathbb H)
}

を定める。基底表示では

\[
\mathcal D_nF
=
\sum_{a=1}^3e_a\otimes\mathcal D_aF,
\]

\[
\boxed{
(\mathcal D_aF)(d_1,\ldots,d_{n-2})
=
\frac12
\sum_{b,c=1}^3
\varepsilon_{abc}
e_bF(d_1,\ldots,d_{n-2},e_c).
}
\]

(Theta) が同型なので、(mathcal D_n) も同型である。

\[
\boxed{
\mathcal D_n:
\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\xrightarrow{\ \cong\ }
V\otimes\operatorname{Hom}(V^{\otimes(n-2)},\mathbb H).
}
\]

これは単に、最後の probe layer を一枚剥がす操作である。

---

## 3. response space の先行再帰定義

最初の空間を

\[
\boxed{
\mathfrak Q_1:=V\subset\mathbb H
}
\]

とする。

(n\ge2) に対し、

\[
\boxed{
\mathfrak Q_n
:=
\mathcal D_n^{-1}
\bigl(V\otimes\mathfrak Q_{n-1}\bigr).
}
\]

成分表示では

\[
\boxed{
F\in\mathfrak Q_n
\iff
\mathcal D_aF\in\mathfrak Q_{n-1}
\quad(a=1,2,3).
}
\]

この定義には (B_n=V^{\otimes n}) も (A_n) も現れない。必要なのは

- probe space (V)
- local output (mathbb H)
- local response law (Theta)
- base admissibility (mathfrak Q_1=V)

だけである。

### Remark 3.1 — (n=2) との一致

(F:V\to\mathbb H) に対して

\[
\mathcal D_2F=\sum_ae_a\otimes h_a.
\]

再帰条件は

\[
h_a\in V
\qquad(a=1,2,3)
\]

である。Note 01 の計算により、これは

\[
\operatorname{Im}F:V\to V
\quad\text{が自己共役}
\]

であることと同値である。したがって

\[
\mathfrak Q_2=\mathcal Q_{2,1}.
\]

---

## 4. 内在的生成定理

### Theorem 4.1

各 (n\ge2) について、(mathcal D_n) は制限同型

\[
\boxed{
\mathcal D_n:
\mathfrak Q_n
\xrightarrow{\ \cong\ }
V\otimes\mathfrak Q_{n-1}
}
\]

を与える。

したがって

\[
\boxed{
\dim\mathfrak Q_n=3^n.
}

### Proof

(mathfrak Q_n) は定義により

\[
\mathcal D_n^{-1}(V\otimes\mathfrak Q_{n-1})
\]

である。ambient space 上で (mathcal D_n) は同型なので、その制限は (mathfrak Q_n) と (V\otimes\mathfrak Q_{n-1}) の同型になる。

基底段階では

\[
\dim\mathfrak Q_1=\dim V=3.
\]

ゆえに帰納的に

\[
\dim\mathfrak Q_n
=3\dim\mathfrak Q_{n-1}
=3^n.
\]

∎

### Corollary 4.2 — admissibility constraint の個数

ambient multilinear response space の次元は

\[
4\cdot3^{n-1}
\]

である。一方、(mathfrak Q_n) の次元は (3^n)。したがって codimension は

\[
\boxed{
4\cdot3^{n-1}-3^n=3^{n-1}.
}

深度を一段剥がすたびに、三つの子応答がそれぞれ前段の admissibility を満たす。このため constraint 数も

\[
3\cdot3^{n-2}=3^{n-1}
\]

と再帰する。

---

## 5. state space は表現定理として後置される

ここで初めて比較対象として

\[
B_n:=V^{\otimes n}
\]

を導入する。canonical all-gap response を

\[
A_n:B_n\to\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\]

\[
A_n(a_1|\cdots|a_n)(d_1,\ldots,d_{n-1})
=
a_nd_{n-1}a_{n-1}\cdots d_1a_1
\]

とする。

### Theorem 5.1 — 全グレード内在的終端応答定理

すべての有限 (n\ge1) について

\[
\boxed{
A_n:B_n\xrightarrow{\ \cong\ }\mathfrak Q_n.
}

### Proof

(n=1) では

\[
A_1:V\to\mathfrak Q_1=V
\]

は恒等写像である。

(n\ge2) とし、

\[
x=\sum_{a=1}^3x_a|e_a,
\qquad
x_a\in B_{n-1}
\]

と書く。Core v1 の recursive response identity は

\[
A_n(x)(\mathbf d,d)
=
\sum_{a=1}^3e_adA_{n-1}(x_a)(\mathbf d).
\]

局所デコーダを適用すると

\[
\boxed{
\mathcal D_n(A_n(x))
=
\sum_{a=1}^3e_a\otimes A_{n-1}(x_a).
}

帰納法の仮定により

\[
A_{n-1}(x_a)\in\mathfrak Q_{n-1},
\]

したがって

\[
A_n(x)\in\mathfrak Q_n.
\]

逆に (F\in\mathfrak Q_n) を取る。定義により

\[
\mathcal D_nF
=
\sum_ae_a\otimes F_a,
\qquad
F_a\in\mathfrak Q_{n-1}.
\]

帰納法の仮定から一意な (x_a\in B_{n-1}) が存在し、

\[
F_a=A_{n-1}(x_a).
\]

そこで

\[
x:=\sum_ax_a|e_a
\]

と置けば、局所 encoder (Theta) によって

\[
A_n(x)=F.
\]

一意性も (Theta) と帰納法から従う。∎

### Interpretation

Core v1 の式

\[
\mathfrak A_n=\operatorname{im}A_n
\]

と、本ノートの (mathfrak Q_n) は結果として同じ空間である。

\[
\mathfrak A_n=\mathfrak Q_n.
\]

違うのは論理順序である。

\[
\begin{array}{ll}
\text{従来順序:}
& B_n\ \text{を置く}\ \to\ A_n\ \to\ \operatorname{im}A_n,\\[4pt]
\text{反転順序:}
& (V,\mathbb H,\Theta)\ \to\ \mathfrak Q_n\ \to\ B_n\cong\mathfrak Q_n.
\end{array}
\]

後者では (B_n) は ontology ではなく representation である。

---

## 6. compression の内在的再帰

state space を経由せず、response space 上に compressed value を定義できる。

基底段階を

\[
\mu_1(v):=v
\qquad(v\in\mathfrak Q_1=V)
\]

とする。

(F\in\mathfrak Q_n) を

\[
\mathcal D_nF
=
\sum_{a=1}^3e_a\otimes F_a,
\qquad
F_a\in\mathfrak Q_{n-1}
\]

と decode し、

\[
\boxed{
\mu_n(F)
:=
\sum_{a=1}^3e_a\,\mu_{n-1}(F_a)
\in\mathbb H
}

と定める。

これは基底非依存である。より抽象的には、

\[
\mathfrak Q_n
\xrightarrow{\ \mathcal D_n\ }
V\otimes\mathfrak Q_{n-1}
\xrightarrow{\ \mathrm{id}\otimes\mu_{n-1}\ }
V\otimes\mathbb H
\xrightarrow{\ L\ }
\mathbb H,
\]

\[
L(v\otimes q):=vq
\]

の合成である。

### Theorem 6.1 — compression intertwining

\[
\boxed{
\mu_n\circ A_n=m_n.
}

### Proof

(x=\sum_ax_a|e_a) に対して

\[
\begin{aligned}
\mu_n(A_n(x))
&=\sum_ae_a\mu_{n-1}(A_{n-1}(x_a))\\
&=\sum_ae_am_{n-1}(x_a)\\
&=m_n(x).
\end{aligned}
\]

二行目は帰納法、三行目は reversed compression の定義である。∎

(n=2) では

\[
\mu_2(F)=\tau_{2,1}(F)
=
-\operatorname{tr}M_F+\alpha_F^\sharp
\]

となり、Note 01 の切断写像を回収する。

したがって、圧縮も state space に先立って response recursion の内部で定義できる。

---

## 7. depth principal symbol の位置

highest-spin sector を後置された表現 (B_n\cong\mathfrak Q_n) 上で読むと、vertical response theorem は

\[
A_n(S)=(-2)^{n-1}C_S
\]

である。

本ノートの順序では、右辺は「既存テンソルが response に写った値」というだけではない。終端 admissible response space (mathfrak Q_n) の中で、最高スピン表現が取る canonical coordinate である。

ただし、これだけでは初出深度 (n-1) の filtration 全体を response side に構成したことにはならない。ここで得たのは terminal object であり、固定 (n) における部分深度の塔

\[
\mathcal Q_{n,0}
\longleftarrow
\mathcal Q_{n,1}
\longleftarrow\cdots\longleftarrow
\mathcal Q_{n,n-1}
\]

は次に構成する必要がある。

---

## 8. 何が解け、何が残ったか

### 解けたもの

1. **終端 response space の循環定義を除去した。**  
   (mathfrak Q_n) は (operatorname{im}A_n) と呼ばず、局所 admissibility の再帰だけで定義できる。

2. **全有限グレードで representation theorem を得た。**

   \[
   V^{\otimes n}\cong\mathfrak Q_n.
   \]

3. **compressed value を response side に内在化した。**

   \[
   \mu_n:\mathfrak Q_n\to\mathbb H.
   \]

4. **局所から大域への生成則が明示された。**

   \[
   \mathfrak Q_n\cong V\otimes\mathfrak Q_{n-1}.
   \]

### 残ったもの

1. 部分深度 response profile を (mathfrak Q_n) 上の内在作用素として定義すること。
2. それらの像だけから (mathcal Q_{n,d}) を作り、忘却写像を与えること。
3. 誕生層

   \[
   \ker(\mathcal Q_{n,d}\to\mathcal Q_{n,d-1})
   \]

   の表現分解を response side だけで計算すること。
4. (n) と (d) を非有界にした極限と completion。

---

## 9. 次の定理

次に行うべきことは一つである。

終端応答 (F\in\mathfrak Q_n) を (mathcal D_n) で再帰的に decode すれば、すべての局所 coefficient tree が一意に得られる。この tree に対して、任意の slot subset への probe insertion と quaternionic collapse を response side の演算として定義する。

それを

\[
\rho_{n,d}:\mathfrak Q_n\to\mathcal O_{n,d}
\]

と書き、

\[
\mathcal Q_{n,d}:=\operatorname{im}\rho_{n,\le d}
\]

とすれば、ambient state (B_n) を使わずに有限 depth tower を構成できる。

目標は

\[
\boxed{
\mathfrak Q_n
\cong
\varprojlim_{0\le d\le n-1}\mathcal Q_{n,d}
}

および

\[
\boxed{
\operatorname{gr}^{\mathrm{depth}}_d\mathfrak Q_n
\cong
F_{d-1}^{(n)}/F_d^{(n)}
}

を、state-first notation を使わずに証明することである。

これが finite Depth–Space Reconstruction Theorem になる。

