# Note 01 — (n=2) 内在的応答塔

## ambient tensor を先に置かず、深度1から (V^{\otimes2}) を復元する

**Status:** proved; exact certificate attached  
**Conventions:** Free Numbers Core v1 と同じ reversed compression

---

## 0. 結果

局所データとして

\[
V=\operatorname{Im}\mathbb H
\]

だけを固定する。実線形写像 (F:V\to\mathbb H) を

\[
F(d)=\alpha_F(d)+M_F(d),
\qquad
\alpha_F:V\to\mathbb R,
\quad
M_F:V\to V
\]

と実部・虚部に分ける。

深度0と深度1の空間を、(V^{\otimes2}) を使わずに次で定義する。

\[
\boxed{
\mathcal Q_{2,0}:=\mathbb H
}
\]

および

\[
\boxed{
\mathcal Q_{2,1}
:=
\{F\in\operatorname{Hom}_{\mathbb R}(V,\mathbb H)
\mid M_F=M_F^{*}\}.
}
\]

すなわち、深度1で許容される応答とは、**虚部が自己共役な線形作用素になる写像** である。

深度1から深度0への切断を

\[
\boxed{
\tau_{2,1}(F)
:=
-\operatorname{tr}(M_F)+\alpha_F^{\sharp}
\in\mathbb R\oplus V=\mathbb H
}
\]

と定める。ここで (alpha_F^{\sharp}\in V) は内積による covector–vector 同一視である。

すると split exact sequence

\[
\boxed{
0
\longrightarrow
S^2_0V
\longrightarrow
\mathcal Q_{2,1}
\xrightarrow{\ \tau_{2,1}\ }
\mathcal Q_{2,0}
\longrightarrow0
}
\]

が得られる。

さらに、通常のテンソル状態空間は後から表現定理として

\[
\boxed{
A_2:V^{\otimes2}\xrightarrow{\ \cong\ }\mathcal Q_{2,1}
}
\]

と復元される。この同型の下で

\[
\tau_{2,1}\circ A_2=m_2
\]

が成り立ち、最高スピン層 (S^2_0V) は

\[
\boxed{
A_2(S)=-2S
}
\]

として深度1に誕生する。

これは Depth–Space Reversal の最小有限モデルである。

---

## 1. 局所データと応答の分解

(V=\operatorname{Im}\mathbb H) に quaternionic multiplication から定まる向きと Euclidean inner product を入れる。

任意の

\[
F\in\operatorname{Hom}_{\mathbb R}(V,\mathbb H)
\]

は一意に

\[
F=\alpha_F+M_F
\]

と分かれる。次元は

\[
\dim V^*=3,
\qquad
\dim\operatorname{End}(V)=9,
\]

したがって

\[
\dim\operatorname{Hom}_{\mathbb R}(V,\mathbb H)=12.
\]

条件

\[
M_F=M_F^*
\]

は (M_F) の反対称成分3次元を消す。よって

\[
\dim\mathcal Q_{2,1}=3+6=9.
\]

この9次元性はテンソル空間から移した次元数ではない。応答写像に対する内在的な三つの整合条件から直接得られる。

---

## 2. 切断写像の基底表示

向きづけられた正規直交基底を

\[
(e_1,e_2,e_3)
\]

とする。許容応答 (F\in\mathcal Q_{2,1}) に対し、切断写像は

\[
\boxed{
\tau_{2,1}(F)
=
\sum_{a=1}^3 e_aF(e_a)
}
\]

とも書ける。

実際、

\[
\sum_a e_a\alpha_F(e_a)=\alpha_F^\sharp
\]

である。また、(M_F) が自己共役なら

\[
\sum_a e_aM_F(e_a)
=
-\operatorname{tr}(M_F)
+
\sum_a e_a\times M_F(e_a)
\]

の vector part は消える。最後の和は (M_F) の反対称成分だけを読むからである。したがって

\[
\sum_a e_aF(e_a)
=
-\operatorname{tr}(M_F)+\alpha_F^\sharp.
\]

右辺は基底に依存しないので、(	au_{2,1}) は内在的に定義されている。

---

## 3. 内在的応答塔定理

### Theorem 3.1

写像

\[
\tau_{2,1}:\mathcal Q_{2,1}\to\mathbb H
\]

は全射であり、

\[
\ker\tau_{2,1}
=
\{F(d)=R(d)\mid R=R^*,\ \operatorname{tr}R=0\}
\cong S^2_0V.
\]

さらに (	au_{2,1}) は標準的な線形 section を持つ。

### Proof

Quaternion を

\[
q=a+w,
\qquad
a\in\mathbb R,
\quad
w\in V
\]

と書き、

\[
\boxed{
s(q)(d)
:=
\langle w,d\rangle-\frac a3d
}
\]

と定める。

この応答の虚部

\[
M_{s(q)}=-\frac a3I
\]

は自己共役なので (s(q)\in\mathcal Q_{2,1}) である。また

\[
\tau_{2,1}(s(q))
=
-\operatorname{tr}\!\left(-\frac a3I\right)+w
=a+w=q.
\]

よって (	au_{2,1}) は全射であり、(s) は section である。

一方、(	au_{2,1}(F)=0) なら scalar part と vector part が独立に消えるので

\[
\operatorname{tr}M_F=0,
\qquad
\alpha_F=0.
\]

許容条件 (M_F=M_F^*) と合わせると、(M_F) は symmetric trace-free endomorphism である。逆向きは明らかである。したがって

\[
\ker\tau_{2,1}\cong S^2_0V.
\]

∎

### Corollary 3.2 — 深度正規形

すべての (F\in\mathcal Q_{2,1}) は一意に

\[
\boxed{
F(d)
=
\langle w,d\rangle
-\frac a3d
+R(d)
}
\]

と書ける。ここで

\[
a+w=\tau_{2,1}(F),
\qquad
R=R^*,
\qquad
\operatorname{tr}R=0.
\]

したがって、内在的に

\[
\boxed{
\mathcal Q_{2,1}
\cong
\mathbb H\oplus S^2_0V
}
\]

である。第一成分は深度0ですでに見える値、第二成分は深度1で初めて生まれる方向である。

---

## 4. テンソル空間は後から現れる

ここから初めて、通常の length-two state を比較対象として導入する。

任意の (T\in\operatorname{End}(V)) に対して

\[
x_T
:=
\sum_{a=1}^3T(e_a)|e_a
\in V^{\otimes2}
\]

と置く。これは (operatorname{End}(V)\cong V^{\otimes2}) の基底非依存な書き方である。

Free Numbers Core v1 の規約では

\[
m_2(u|v)=vu
\]

であり、canonical depth-one response は

\[
\boxed{
A_2(x_T)(d)
=
\sum_{a=1}^3 e_a dT(e_a).
}
\]

### Lemma 4.1 — 応答分解公式

\[
w_T:=\sum_{a=1}^3e_a\times T(e_a)
\]

と置くと、

\[
\boxed{
A_2(x_T)(d)
=
\langle w_T,d\rangle
+
\bigl((\operatorname{tr}T)I-(T+T^*)\bigr)d.
}
\]

### Proof sketch

三つの虚 quaternion (u,d,v\in V) に対する恒等式

\[
udv
=
-\det(u,d,v)
-(u\cdot d)v
+d(u\cdot v)
-u(d\cdot v)
\]

を (u=e_a, v=T(e_a)) に適用して (a) について和を取る。

scalar part は

\[
\left\langle\sum_ae_a\times T(e_a),d\right\rangle
=\langle w_T,d\rangle
\]

となる。vector part を作用素として整理すると

\[
(\operatorname{tr}T)I-(T+T^*)
\]

を得る。∎

この公式から、(A_2(x_T)) の虚部は必ず自己共役である。したがって

\[
A_2(V^{\otimes2})\subseteq\mathcal Q_{2,1}.
\]

---

## 5. 内在的デコーダ

逆に、(F\in\mathcal Q_{2,1}) からテンソル座標を復元できる。

簡単のため

\[
\alpha:=\alpha_F^\sharp,
\qquad
M:=M_F
\]

と書く。cross-product operator を

\[
[\alpha]_\times(v):=\alpha\times v
\]

とする。

次の作用素を定める。

\[
\boxed{
T_F
:=
\frac12
\left(
(\operatorname{tr}M)I
-M
+[\alpha]_\times
\right).
}
\]

### Theorem 5.1 — (n=2) 内在的表示定理

\[
\boxed{
A_2(x_{T_F})=F.
}
\]

したがって

\[
\boxed{
A_2:V^{\otimes2}\xrightarrow{\ \cong\ }\mathcal Q_{2,1}
}

は同型である。

### Proof

(M=M^*) なので

\[
T_F+T_F^*
=
(\operatorname{tr}M)I-M.
\]

また

\[
\operatorname{tr}T_F
=
\frac12(3\operatorname{tr}M-\operatorname{tr}M)
=
\operatorname{tr}M.
\]

よって Lemma 4.1 の vector part は

\[
(\operatorname{tr}T_F)I-(T_F+T_F^*)
=M.
\]

対称部分は (w_T) に寄与しない。一方、(rac12[\alpha]_\times) について

\[
\sum_ae_a\times
\left(\frac12\alpha\times e_a\right)
=\alpha
\]

なので、scalar covector は (d\mapsto\langle\alpha,d\rangle=\alpha_F(d)) になる。

したがって (A_2(x_{T_F})=\alpha_F+M_F=F) である。∎

この証明では、(mathcal Q_{2,1}) は先に応答整合条件から定義されている。(V^{\otimes2}) はその後で、(mathcal Q_{2,1}) の完全な座標表示として回収された。

---

## 6. 圧縮は内在的切断になる

Lemma 4.1 の記号で

\[
m_2(x_T)
=
\sum_ae_aT(e_a)
=
-\operatorname{tr}T+w_T.
\]

一方、

\[
\operatorname{tr}M_{A_2(x_T)}=\operatorname{tr}T,
\qquad
\alpha_{A_2(x_T)}^\sharp=w_T.
\]

したがって

\[
\boxed{
\tau_{2,1}(A_2(x_T))=m_2(x_T).
}

すなわち図式

\[
\begin{array}{ccc}
V^{\otimes2} & \xrightarrow{\ A_2\ } & \mathcal Q_{2,1}\\
{\scriptstyle m_2}\downarrow && \downarrow{\scriptstyle\tau_{2,1}}\\
\mathbb H & = & \mathcal Q_{2,0}
\end{array}
\]

は可換である。

ここで圧縮 (m_2) は state space 上の原始操作ではなく、深度1応答を深度0へ忘却する切断 (	au_{2,1}) として内在化された。

---

## 7. 係数 (-2) は誕生層の埋込み係数である

(S\in S^2_0V) を symmetric trace-free endomorphism と見る。このとき

\[
\operatorname{tr}S=0,
\qquad
S=S^*,
\qquad
w_S=0.
\]

Lemma 4.1 より

\[
\boxed{
A_2(x_S)(d)=-2S(d).
}

また

\[
\tau_{2,1}(A_2(x_S))=0.
\]

したがって

\[
\boxed{
A_2|_{S^2_0V}
=
-2\,\mathrm{id}_{S^2_0V}
}

は、最高スピンが深度1の誕生層へ入るときの正確な埋込み係数である。

Corollary 3.2 の (R) を自然な tensor contraction coordinate (S) で書けば

\[
R=-2S.
\]

よって深度正規形は

\[
\boxed{
F(d)
=
\langle w,d\rangle
-\frac a3d
-2S(d),
\qquad
a+w=\tau_{2,1}(F).
}

となる。

深度0では (a+w\in\mathbb H) しか残らない。深度1に上がった瞬間、5次元の (S^2_0V) が (-2) を伴って立ち上がる。

---

## 8. 対称性と表示独立性

(g\in SO(3)\) は quaternion automorphism として (mathbb H=\mathbb R\oplus V) に作用する。応答への作用を

\[
(g\cdot F)(d)
:=
g\cdot F(g^{-1}d)
\]

とする。

このとき

\[
M_{g\cdot F}=gM_Fg^{-1}
\]

なので、自己共役条件は保存される。また

\[
\tau_{2,1}(g\cdot F)
=
g\cdot\tau_{2,1}(F).
\]

したがって、(mathcal Q_{2,1})、切断 (	au_{2,1})、誕生層 (ker\tau_{2,1}) は、選んだ基底の偶然ではなく (SO(3))-equivariant な対象である。

---

## 9. この段階で証明できたこと

### 証明済み

1. 深度1の許容応答空間は、tensor state を参照せず

   \[
   M_F=M_F^*
   \]

   という内在条件だけで定義できる。

2. 深度0への切断も

   \[
   \tau_{2,1}(F)=-\operatorname{tr}M_F+\alpha_F^\sharp
   \]

   と応答側だけで定義できる。

3. 新しい方向は

   \[
   \ker\tau_{2,1}\cong S^2_0V
   \]

   であり、正確に5次元である。

4. (V^{\otimes2}) は出発点ではなく、応答空間 (mathcal Q_{2,1}) の representation として後から復元できる。

5. 既存の compression と highest-spin response は

   \[
   \tau_{2,1}\circ A_2=m_2,
   \qquad
   A_2(S)=-2S
   \]

   として同じ応答塔の内部に回収される。

### まだ証明していないこと

1. (V) と (mathbb H) そのものの深度からの生成。
2. (n\ge3) における全ての部分深度空間 (mathcal Q_{n,d}) の内在表示。
3. 誕生層と経路非合流曲率の同一視。
4. 非有界深度極限からの位相・距離・次元の再構成。

この Note 01 が証明したのは、最小段階ではあるが重要な向きの反転である。

> 既存の (V^{\otimes2}) に filtration を載せただけではない。  
> 応答整合性から9次元空間を先に作り、(V^{\otimes2}) を後からその表現として得た。

---

## 10. 次の一手

Core v1 の局所デコーダを

\[
\mathcal D_aF(d_1,\ldots,d_{n-2})
:=
\frac12
\sum_{b,c=1}^3
\varepsilon_{abc}
e_bF(d_1,\ldots,d_{n-2},e_c)
\]

と書く。

終端 all-gap response については、次の ambient-state-free recursion が候補になる。

\[
\mathfrak Q_1:=V,
\]

\[
\boxed{
\mathfrak Q_n
:=
\left\{
F\in\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\ \middle|\
\mathcal D_aF\in\mathfrak Q_{n-1}
\text{ for }a=1,2,3
\right\}.
}
\]

(n=2) では、この再帰条件が本ノートの

\[
M_F=M_F^*
\]

に等価である。

次の Note 02 では、

\[
\mathfrak Q_n\cong V^{\otimes n}
\]

を state space を後置した帰納的表現定理として閉じる。その後、終端応答から圧縮および部分深度応答への切断を、(mathcal D_a) だけで再帰的に構成する。

---

## Exact certificate

`certificates/n2_intrinsic_response_certificate.py` は外部ライブラリを使わず、有理数上の完全計算で次を検証する。

- (A_2) の rank が9である。
- 自己共役条件が独立な3条件である。
- (operatorname{im}A_2=\mathcal Q_{2,1}) である。
- (	au_{2,1}\circ A_2=m_2) である。
- (	au_{2,1}) の rank が4、kernel dimension が5である。
- section が (	au_{2,1}) を split する。
- 明示デコーダ (T_F) が全許容応答を復元する。
- (S^2_0V) 上の係数が正確に (-2) である。

Expected final line:

```text
ALL CHECKS PASSED
```

