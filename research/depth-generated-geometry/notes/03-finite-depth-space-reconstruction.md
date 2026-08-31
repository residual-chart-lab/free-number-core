# Note 03 — 有限 Depth–Space Reconstruction Theorem

## 部分深度の観測像から空間の塔を作る

**Status:** formal theorem; low-grade layer dimensions are exact-checked in Free Numbers Core v1  
**Depends on:** Note 02; the established probe-insertion profile

---

## 0. 主結果

Note 02 では、終端 all-gap response space

\[
\mathfrak Q_n
\subset
\operatorname{Hom}(V^{\otimes(n-1)},\mathbb H)
\]

を ambient state (V^{\otimes n}) の像としてではなく、局所デコーダ (Theta^{-1}) の admissibility recursion だけから構成した。

本ノートでは、(mathfrak Q_n) を「全情報を持つ深度 (n-1) の応答空間」とし、そこから浅い深度の観測像を切り出す。これにより、固定 (n) ごとに

\[
\boxed{
\mathcal Q_{n,0}
\longleftarrow
\mathcal Q_{n,1}
\longleftarrow\cdots\longleftarrow
\mathcal Q_{n,n-1}
}
\]

という有限の response tower が得られる。

各写像は「深度 (d) で初めて得た応答成分を忘れる」切断である。終端では

\[
\boxed{
\mathcal Q_{n,n-1}\cong\mathfrak Q_n.
}

さらに

\[
\boxed{
\mathfrak Q_n
\cong
\varprojlim_{0\le d\le n-1}\mathcal Q_{n,d}.
}

一段深くしたときに生まれる方向は

\[
\boxed{
\ker\!\left(
\mathcal Q_{n,d}\to\mathcal Q_{n,d-1}
\right)
\cong
\widehat F_{d-1}^{(n)}/\widehat F_d^{(n)},
}

ここで (widehat F_d^{(n)}subset\mathfrak Q_n) は深度 (d) まで不可視な exact responses である。

したがって、既存の residual filtration は state space 内の分類から、response tower における **新方向の可視化則** へ反転される。

---

## 1. 終端 response space を原始対象とする

局所デコーダから再帰的に定義された exact-response space を

\[
\mathfrak Q_n
\]

とする。Note 02 により、後置された representation として

\[
A_n:V^{\otimes n}\xrightarrow{\ \cong\ }\mathfrak Q_n
\]

が存在する。

その明示的な再帰逆写像を

\[
\Psi_n:\mathfrak Q_n\to V^{\otimes n}
\]

と書く。

論理順序は次である。

1. ((V,\mathbb H,\Theta)) から (mathfrak Q_n) を構成する。
2. 表現定理として (Psi_n=A_n^{-1}) を得る。
3. 既知の probe-insertion operations を (mathfrak Q_n) 上へ輸送する。

したがって、以下で (Psi_n) を使うことは循環ではない。state representation は response space の構成後に導出されている。

また (Psi_n) は単なる存在写像ではない。局所 decoder

\[
\mathcal D_nF
=
\sum_ae_a\otimes F_a
\]

を繰り返し、最後に (mathfrak Q_1=V) へ到達する有限アルゴリズムである。よって以下の観測作用素は、原理的には (V^{\otimes n}) を経由せず response tree 上だけで実行できる。

---

## 2. 内部 slot response の内在化

length (n) には (n-1) 個の internal slots がある。

深度 (q) の internal slot choice を

\[
\vec r=(r_1,\ldots,r_q),
\qquad
1\le r_1<\cdots<r_q\le n-1
\]

とする。その集合を

\[
\mathcal S_{\mathrm{int}}(n,q)
\]

と書く。

通常の insertion response は

\[
\mathcal R_{n,q}^{\vec r}:
V^{\otimes n}
\to
\operatorname{Hom}(V^{\otimes q},\mathbb H).
\]

これを exact-response side へ輸送して

\[
\boxed{
\widehat{\mathcal R}_{n,q}^{\vec r}
:=
\mathcal R_{n,q}^{\vec r}\circ\Psi_n:
\mathfrak Q_n
\to
\operatorname{Hom}(V^{\otimes q},\mathbb H)
}

と定める。

compression は Note 02 で response side に内在的再帰

\[
\mu_n:\mathfrak Q_n\to\mathbb H
\]

として定義済みである。

### State-free evaluation algorithm

(widehat{\mathcal R}_{n,q}^{\vec r}(F)) は次の手順で (F) だけから計算できる。

1. (mathcal D_n,\mathcal D_{n-1},\ldots) を反復し、(F) を有限の coefficient tree に decode する。
2. 選択した internal slots (ec r) に probe variables を置く。
3. tree の局所 quaternionic multiplication を reversed order で畳む。

(Psi_n) を使った定義は、このアルゴリズムを短く書いたものである。

---

## 3. 深度 (d) までの観測空間

深度 (d) の ambient observation target を

\[
\mathcal O_{n,d}
:=
\mathbb H
\oplus
\bigoplus_{q=1}^{d}
\bigoplus_{\vec r\in\mathcal S_{\mathrm{int}}(n,q)}
\operatorname{Hom}(V^{\otimes q},\mathbb H)
\]

とする。

combined response map を

\[
\boxed{
\widehat D_n^{\le d}:
\mathfrak Q_n\to\mathcal O_{n,d}
}

\[
\boxed{
\widehat D_n^{\le d}(F)
:=
\left(
\mu_n(F),
\bigl(
\widehat{\mathcal R}_{n,q}^{\vec r}(F)
\bigr)_{
1\le q\le d,
\ \vec r\in\mathcal S_{\mathrm{int}}(n,q)}
\right)
}

と定める。

そして深度 (d) までに実現可能な応答プロファイル全体を

\[
\boxed{
\mathcal Q_{n,d}
:=
\operatorname{im}\widehat D_n^{\le d}
\subseteq\mathcal O_{n,d}
}

とする。

ここで像を取っている元は ambient tensor state ではなく、先行構成された exact-response space (mathfrak Q_n) である。

---

## 4. 忘却写像と response tower

(mathcal O_{n,d}) から深度ちょうど (d) の成分を忘れる線形射影を

\[
p_{n,d}:\mathcal O_{n,d}\to\mathcal O_{n,d-1}
\]

とする。定義から

\[
p_{n,d}\circ\widehat D_n^{\le d}
=
\widehat D_n^{\le d-1}.
\]

したがって (p_{n,d}) は像へ制限され、全射

\[
\boxed{
\pi_{n,d}:
\mathcal Q_{n,d}\twoheadrightarrow\mathcal Q_{n,d-1}
}

を与える。

これにより

\[
\boxed{
\mathcal Q_{n,0}
\xleftarrow{\ \pi_{n,1}\ }
\mathcal Q_{n,1}
\xleftarrow{\ \pi_{n,2}\ }
\cdots
\xleftarrow{\ \pi_{n,n-1}\ }
\mathcal Q_{n,n-1}
}

が得られる。

この tower は、深度が増えるたびに新しい response coordinates が追加される過程そのものである。

---

## 5. 終端分離性

深度 (n-1) では、全 internal gaps

\[
(1,2,\ldots,n-1)
\]

を選ぶ唯一の response component が含まれる。

この成分は canonical all-gap response である。exact-response coordinate (F\in\mathfrak Q_n) に対しては

\[
\widehat{\mathcal R}_{n,n-1}^{(1,\ldots,n-1)}(F)
=
A_n(\Psi_n(F))
=F.
\]

したがって (widehat D_n^{\le n-1}) は (F) 自身を一成分として含み、単射である。

### Theorem 5.1 — finite terminal reconstruction

\[
\boxed{
\widehat D_n^{\le n-1}:
\mathfrak Q_n
\xrightarrow{\ \cong\ }
\mathcal Q_{n,n-1}.
}

特に

\[
\boxed{
\dim\mathcal Q_{n,n-1}=\dim\mathfrak Q_n=3^n.
}

これは全有限 response state が深度 (n-1) までに分離されることを、state-first notation なしで述べたものである。

---

## 6. 有限 Depth–Space Reconstruction Theorem

### Theorem 6.1

各有限 (n\ge2) について、

\[
\boxed{
\mathfrak Q_n
\cong
\varprojlim_{0\le d\le n-1}\mathcal Q_{n,d}.
}

### Proof

各 (F\in\mathfrak Q_n) は互いに整合する profile family

\[
\bigl(widehat D_n^{\le d}(F)\bigr)_{0\le d\le n-1}
\]

を与えるので、自然な写像

\[
\Xi_n:\mathfrak Q_n\to\varprojlim_d\mathcal Q_{n,d}
\]

がある。

終端成分

\[
\widehat D_n^{\le n-1}(F)
\]

が (F) 自身を含むため、(Xi_n) は単射である。

逆に、有限 tower の整合 family はその終端成分によって一意に決まる。Theorem 5.1 により、その終端成分は一意な (F\in\mathfrak Q_n) から来る。よって (Xi_n) は全射でもある。∎

### Important limitation

固定 (n) の tower は有限であり、終端項が存在する。したがって、この逆極限だけで連続空間や無限次元幾何が創発したとは言えない。

ここで証明したのは **finite reconstruction** である。真の completion には (n) と depth を非有界にした tower が必要になる。

---

## 7. 誕生層

深度 (d) まで不可視な exact responses を

\[
\boxed{
\widehat F_d^{(n)}
:=
\ker\widehat D_n^{\le d}
\subseteq\mathfrak Q_n
}

とする。

すると

\[
\mathfrak Q_n
\supseteq
\widehat F_0^{(n)}
\supseteq
\widehat F_1^{(n)}
\supseteq\cdots\supseteq
\widehat F_{n-1}^{(n)}=0.
\]

### Theorem 7.1 — birth-layer identification

各 (1\le d\le n-1) について

\[
\boxed{
\ker\pi_{n,d}
\cong
\widehat F_{d-1}^{(n)}/\widehat F_d^{(n)}.
}

### Proof

(ker\pi_{n,d}) の元は、深度 (d-1) までの成分がすべて零で、深度 (d) 成分だけを持つ実現可能 profile である。

その preimage は

\[
\ker\widehat D_n^{\le d-1}
=
\widehat F_{d-1}^{(n)}.
\]

同じ depth-(d) profile を与える二つの preimages の差は

\[
\ker\widehat D_n^{\le d}
=
\widehat F_d^{(n)}
\]

に属する。第一同型定理から結論を得る。∎

したがって

\[
\boxed{
K_{n,d}^{\mathrm{birth}}
:=
\ker\pi_{n,d}
}

は、深度を (d-1) から (d) へ上げた瞬間に新しく生まれる方向空間である。

---

## 8. dimension profile

深度 (d) までに立ち上がった可視空間の次元を

\[
\boxed{
N_n(d):=\dim\mathcal Q_{n,d}
}

とする。rank–nullity により

\[
\boxed{
N_n(d)
=
3^n-\dim\widehat F_d^{(n)}.
}

一段で増える次元は

\[
\boxed{
h_n(d)
:=
N_n(d)-N_n(d-1)
=
\dim K_{n,d}^{\mathrm{birth}}.
}

Free Numbers Core v1 の exact certificates for (n=2,3,4) を、この向きで読み替えると次になる。

| grade (n) | (N_n(0)) | (N_n(1)) | (N_n(2)) | (N_n(3)) | terminal |
|---:|---:|---:|---:|---:|---:|
| 2 | 4 | 9 | — | — | (3^2=9) |
| 3 | 4 | 20 | 27 | — | (3^3=27) |
| 4 | 4 | 32 | 72 | 81 | (3^4=81) |

birth dimensions は

| grade (n) | depth 1 | depth 2 | depth 3 |
|---:|---:|---:|---:|
| 2 | 5 | — | — |
| 3 | 16 | 7 | — |
| 4 | 28 | 40 | 9 |

である。

つまり、圧縮だけを見る深度0では (n=2,3,4) のいずれも4次元の quaternionic value space しか見えない。しかし深度を増やすと、

\[
\boxed{
n=2:\quad4\longrightarrow9,
}

\[
\boxed{
n=3:\quad4\longrightarrow20\longrightarrow27,
}

\[
\boxed{
n=4:\quad4\longrightarrow32\longrightarrow72\longrightarrow81
}

と、識別可能な空間方向が段階的に増える。

これが「深度が空間を紡ぐ」という仮説を支える、最初の厳密な **visibility dimension profile** である。

ただし (N_n(d)) は現時点では **response-state dimension** であり、物理的時空次元と同一視してはならない。

---

## 9. highest-spin birth certificate

highest-spin representation を exact-response side で

\[
\mathfrak H_n
:=
A_n(S^n_0V)
\subseteq\mathfrak Q_n
\]

とする。

depth (d<n-1) の response target が持ちうる最高 spin は (V_{d+1}) なので、

\[
\widehat D_n^{\le n-2}(\mathfrak H_n)=0.
\]

一方、終端 vertical component は

\[
\widehat{\mathcal R}_{n,n-1}^{(1,\ldots,n-1)}(A_n(S))
=
A_n(S)
=
(-2)^{n-1}C_S.
\]

したがって

\[
\boxed{
\mathfrak H_n
\hookrightarrow
K_{n,n-1}^{\mathrm{birth}}
}

であり、その depth principal symbol は

\[
\boxed{
\sigma_{n-1}^{\mathrm{depth}}(S)
=
(-2)^{n-1}C_S.
}

これは最高スピン成分の birth certificate である。

注意すべきは包含と等号の違いである。

\[
\mathfrak H_n
=
K_{n,n-1}^{\mathrm{birth}}
\]

は (n=2,3,4) では exact-checked されているが、一般 (n) では full-profile conjecture である。全 (n) で証明済みなのは、最高スピンがそれ以前には見えず、深度 (n-1) の canonical component で非零になることまでである。

---

## 10. first-separation depth と ultrametric

非零 (F\in\mathfrak Q_n) の first-detection depth を

\[
\boxed{
\delta_n(F)
:=
\min\{d\mid\widehat D_n^{\le d}(F)\ne0\}
}

とする。終端分離性により

\[
0\le\delta_n(F)\le n-1.
\]

(F=0) には (delta_n(0)=+\infty) と置く。

(0<\rho<1) を固定し、

\[
\boxed{
d_{n,\rho}(F,G)
:=
\rho^{\delta_n(F-G)}
}

と定める。

filtration が線形部分空間の降下列なので

\[
\delta_n(X+Y)
\ge
\min\{\delta_n(X),\delta_n(Y)\}.
\]

したがって

\[
d_{n,\rho}(F,H)
\le
\max\{d_{n,\rho}(F,G),d_{n,\rho}(G,H)\}.
\]

### Theorem 10.1

(d_{n,\rho}) は (mathfrak Q_n) 上の ultrametric である。

この距離では、浅い深度ですぐ区別される二状態は遠く、深い関係を辿らなければ区別できない二状態は近い。

したがって depth filtration は、既存の Euclidean metric を測るだけではなく、独自の離散幾何を実際に誘導する。

---

## 11. この定理が意味すること

### 数学的に成立した反転

従来の読みは

\[
V^{\otimes n}
\quad\text{が先にあり、}\quad
D_n^{\le d}
\quad\text{がその一部を見る}
\]

である。

本ノートの読みは

\[
(V,\mathbb H,\Theta)
\longrightarrow
\mathfrak Q_n
\longrightarrow
\{\mathcal Q_{n,d}\}_d
\longrightarrow
\varprojlim_d\mathcal Q_{n,d}
\cong\mathfrak Q_n
\]

である。

ここでは「全状態」は、有限深度応答の整合 family として再構成される。

### まだ物理ではない

この定理が与えるのは

- response topology
- first-separation ultrametric
- depth birth layers
- dimension growth profile
- highest-spin principal symbol

である。

まだ与えていないのは

- 局所輸送
- path holonomy
- gauge connection
- curvature
- action / dynamics
- 物理的時空との同定

である。

したがって、有限応答空間が深度別の整合 family から再構成されることは成立した。ただし「深度が空間そのものを生成する」こと、および「その空間の曲率が物理的な力である」ことは未証明である。

---

## 12. 残る循環と次の仕事

本ノートは (mathcal Q_{n,d}) を、先行構成された (mathfrak Q_n) の観測像として定義した。これは ambient tensor state への循環を除いているが、各部分深度空間を **その深度だけの局所整合式** で直接 presentation したわけではない。

次の強化は

\[
\mathcal Q_{n,d}
=
\{\text{depth-}d\text{ profiles satisfying explicit compatibility relations}\}
\]

という generators-and-relations theorem を得ることである。

最初の対象は (n=3,d=1) である。

既知の次元は

\[
\dim\mathcal Q_{3,1}=20,
\]

ambient depth-one profile target から、どの linear / equivariant compatibility conditions がこの20次元を直接切り出すかを求める。

その後、最小 quaternionic plaquette を導入し、

\[
\text{path nonconfluence residual}
\quad\longleftrightarrow\quad
K_{n,d}^{\mathrm{birth}}
\]

を接続する。

ここから先が、depth-generated geometry と noncommutative curvature の橋になる。
