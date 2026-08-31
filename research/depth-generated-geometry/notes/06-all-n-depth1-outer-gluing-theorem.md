# Note 06 — All-(n) Depth-One Outer-Gluing Theorem

## 局所 residual gadgets による全長の direct presentation

**Status:** proved for every (n\ge3)  
**Depends on:** Note 04 ((n=3) fiber product); Note 05 ((n=4) free middle chart)

---

## 0. 定理

\[
E:=\operatorname{Hom}_{\mathbb R}(V,\mathbb H)
\]

とし、

\[
r(F):=\sum_aF(e_a)e_a,
\qquad
\ell(F):=\sum_ae_aF(e_a)
\]

とする。

length (n\ge3) の depth-one profile を

\[
(q,F_1,\ldots,F_{n-1})
\in
\mathbb H\oplus E^{\oplus(n-1)}
\]

と書く。

### Theorem 0.1 — all-(n) outer gluing

この profile が実現可能であるための必要十分条件は

\[
\boxed{
q=r(F_1)=\ell(F_{n-1})
}

である。

すなわち

\[
\boxed{
\mathcal Q_{n,1}
=
\left\{
(q,F_1,\ldots,F_{n-1})
\ \middle|\
q=r(F_1)=\ell(F_{n-1})
\right\}.
}

同型として

\[
\boxed{
\mathcal Q_{n,1}
\cong
\mathbb H
\oplus\ker r
\oplus E^{\oplus(n-3)}
\oplus\ker\ell.
}

したがって

\[
\boxed{
\dim\mathcal Q_{n,1}=12n-16
}

および

\[
\boxed{
\dim K_{n,1}^{\mathrm{birth}}=12n-20.
}

この定理は fixed-spin multiplicity を factor origin に分け、depth one の全長分類を与える。

---

## 1. 必要条件

pure word を

\[
x=a_1|a_2|\cdots|a_n
\]

とし、

\[
q_x=a_n\cdots a_2a_1
\]

とする。

最初の internal slot response は

\[
F_{1,x}(d)
=
a_n\cdots a_2da_1.
\]

よって

\[
\begin{aligned}
r(F_{1,x})
&=\sum_bF_{1,x}(e_b)e_b\\
&=a_n\cdots a_2
\left(\sum_be_ba_1e_b\right)\\
&=a_n\cdots a_2a_1\\
&=q_x.
\end{aligned}
\]

最後の internal slot response は

\[
F_{n-1,x}(d)
=
a_nd a_{n-1}\cdots a_1.
\]

したがって

\[
\begin{aligned}
\ell(F_{n-1,x})
&=\sum_be_bF_{n-1,x}(e_b)\\
&=\left(\sum_be_ba_ne_b\right)
a_{n-1}\cdots a_1\\
&=a_n\cdots a_1\\
&=q_x.
\end{aligned}
\]

線形性により、すべての state について

\[
q=r(F_1)=\ell(F_{n-1})
\]

が成り立つ。

したがって必要性は全 (n\ge3) で証明済みである。

---

## 2. localized zero-compression gadget

全射性を示すため、zero-compression state を局所 block として埋め込む。

### Definition 2.1

(z\in V^{\otimes k}) が depth-one localized gadget at slot (t) であるとは、

\[
m_k(z)=0
\]

かつ、その internal depth-one responses が slot (t) 以外ですべて零であることをいう。

slot (t) の response を (H_z\in E) と書く。

### Lemma 2.2 — padding lemma

(z) を任意の fixed pure boundary words (p,s) で左右から挟む。

\[
\widetilde z:=p|z|s.
\]

padding の reversed compressed values を

\[
P:=m(p),
\qquad
S:=m(s)
\]

とする。空 padding では (P=1) または (S=1) と約束する。

このとき

1. (m(\widetilde z)=0)。
2. 狙った global slot 以外の depth-one responses はすべて零。
3. 狙った response は

   \[
   \boxed{
   H_{\widetilde z}(d)=S\,H_z(d)\,P.
   }
   \]

### Proof

probe が gadget (z) の狙った slot 以外に入る場合、reversed product は未probeの (z) を一つの block として含み、その compressed value

\[
m_k(z)=0
\]

が全積を零にする。

probe が狙った slot に入る場合だけ、zero block が (H_z(d)) として開き、左右 padding の compressed values がそれぞれ左・右から掛かる。∎

### Corollary 2.3

fixed pure padding の compressed values (P,S) は nonzero quaternions である。したがって

\[
T_{S,P}:E\to E,
\qquad
T_{S,P}(H)(d):=SH(d)P
\]

は同型である。

よって padding 後にも、局所 gadget の response space 全体を任意に指定できる。

---

## 3. 三種類の局所 generators

### 3.1 left-boundary gadget

Note 04 の (n=3) fiber-product theorem により、任意の

\[
U\in\ker r
\]

に対し profile

\[
(q,F_1,F_2)=(0,U,0)
\]

を持つ state

\[
z_L(U)\in V^{\otimes3}
\]

が存在する。

これは length-three slot 1 に局在する zero-compression gadget である。

### 3.2 right-boundary gadget

同様に任意の

\[
W\in\ker\ell
\]

に対し

\[
(q,F_1,F_2)=(0,0,W)
\]

を持つ

\[
z_R(W)\in V^{\otimes3}
\]

が存在する。

### 3.3 interior gadget

Note 05 の (n=4) intrinsic presentation により、任意の

\[
M\in E
\]

に対し

\[
(q,F_1,F_2,F_3)=(0,0,M,0)
\]

を持つ

\[
z_I(M)\in V^{\otimes4}
\]

が存在する。

これは length-four block の中央 slot に局在する zero-compression gadget である。

これら三種類が、任意長の depth-one profile を生成する局所 basis になる。

---

## 4. 任意 slot への埋込み

### Boundary slots

(z_L(U)) を global word の最初の三 letters に置き、残りを fixed pure letters で右 padding する。

Padding Lemma により、global profile は

- compression zero
- slot 1 以外の responses zero
- slot 1 response は (S U)

となる。左乗法 (U\mapsto SU) は (ker r) を保ち、nonzero (S) により可逆である。実際、

\[
r(SU)=Sr(U)=0.
\]

したがって global slot 1 に任意の element of (ker r) を独立に生成できる。

同様に、(z_R(W)) を最後の三 letters に置けば、global slot (n-1) に任意の element of (ker\ell) を独立に生成できる。

### Interior slots

任意の

\[
2\le t\le n-2
\]

を取る。length-four gadget (z_I(M)) の中央 slot が global slot (t) に一致するよう、global positions

\[
t-1, t, t+1, t+2
\]

へ置く。残りを fixed pure letters で padding する。

Padding Lemma と (T_{S,P}) の可逆性により、global slot (t) に任意の (M\in E) を生成し、他のすべての depth-one responses と compression を零にできる。

したがって各 interior chart

\[
F_2,\ldots,F_{n-2}
\]

は独立に調整可能である。

---

## 5. 十分性の証明

outer-compatible target profile

\[
\mathcal P
=
(q,F_1,\ldots,F_{n-1})
\]

を取る。すなわち

\[
q=r(F_1)=\ell(F_{n-1}).
\]

### Step 1 — value lift

(n\ge2) では compression

\[
m_n:V^{\otimes n}\to\mathbb H
\]

は全射である。

実際 (m_2) は全射であり、末尾に fixed nonzero imaginary letter を追加する操作は (mathbb H) 上の可逆な左乗法を与えるので、帰納的に全射性が保たれる。

したがって

\[
m_n(x_0)=q
\]

を満たす (x_0\in V^{\otimes n}) を選べる。その depth-one responses を

\[
F_1^{(0)},\ldots,F_{n-1}^{(0)}
\]

とする。

### Step 2 — differences

必要条件から

\[
r(F_1^{(0)})=q=r(F_1),
\]

よって

\[
U_L:=F_1-F_1^{(0)}\in\ker r.
\]

同様に

\[
U_R:=F_{n-1}-F_{n-1}^{(0)}\in\ker\ell.
\]

各 interior slot について

\[
M_t:=F_t-F_t^{(0)}\in E
\qquad(2\le t\le n-2)
\]

と置く。

### Step 3 — independent corrections

Section 4 の localized gadgets を用いて

- slot 1 に (U_L)
- 各 interior slot (t) に (M_t)
- slot (n-1) に (U_R)

を持ち、その他の responses と compression が零である global states をそれぞれ作る。

それらを (x_0) に加えた state を (x) とする。

localized corrections は compression を変えず、互いの slots に干渉しない。したがって

\[
D_n^{\le1}(x)
=
(q,F_1,\ldots,F_{n-1}).
\]

よって任意の outer-compatible profile が実現可能である。

必要性と合わせて Theorem 0.1 が証明された。∎

---

## 6. dimension and representation theorem

Theorem 0.1 から

\[
\mathcal Q_{n,1}
\cong
\mathbb H
\oplus\ker r
\oplus E^{\oplus(n-3)}
\oplus\ker\ell.
\]

次元は

\[
4+8+12(n-3)+8
=
\boxed{12n-16}.
\]

depth-zero quotient は (mathbb H) なので、birth layer は

\[
\boxed{
K_{n,1}^{\mathrm{birth}}
\cong
\ker r
\oplus E^{\oplus(n-3)}
\oplus\ker\ell
}

であり、

\[
\dim K_{n,1}^{\mathrm{birth}}
=
8+12(n-3)+8
=
\boxed{12n-20}.
\]

(SO(3))-decomposition

\[
E\cong V_0\oplus2V_1\oplus V_2,
\]

\[
\ker r\cong\ker\ell\cong V_1\oplus V_2
\]

から

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

したがって depth one で検出される spin は全長で (0,1,2) に限られ、その multiplicity は明示式で完全に決まる。

depth one までの全 visible space は depth-zero (mathbb H\cong V_0\oplus V_1) を加えて

\[
\boxed{
\mathcal Q_{n,1}
\cong
(n-2)V_0
\oplus
(2n-3)V_1
\oplus
(n-1)V_2.
}

---

## 7. kernel theorem

\[
B_n=V^{\otimes n}
\]

を後置された representation として使うと、rank–nullity から

\[
\boxed{
\dim\ker D_n^{\le1}
=
3^n-(12n-16)
\qquad(n\ge3).
}

representation multiplicities (m_n(s)) of (V_s\subset V^{\otimes n}) を用いれば、depth-one kernel は

\[
\boxed{
\ker D_n^{\le1}
\cong
\bigl(m_n(0)-(n-2)\bigr)V_0
\oplus
\bigl(m_n(1)-(2n-3)\bigr)V_1
\oplus
\bigl(m_n(2)-(n-1)\bigr)V_2
\oplus
\bigoplus_{s\ge3}m_n(s)V_s.
}

特に (s\ge3) は representation bandwidth によりすべて depth one では不可視である。

この式は depth-one multiplicity filtration の全長分類である。

---

## 8. (n=2) が例外である理由

(n=2) には internal slot が一つしかない。その同じ response (F) が left boundary と right boundary の両方を同時に担う。

したがって

\[
q=r(F),
\qquad
q=\ell(F)
\]

は独立な二 chart の gluing ではなく、一つの map (F) 自身への条件になる。

その差

\[
r(F)-\ell(F)
]

は (operatorname{Im}F) の反対称成分を測り、Note 01 の admissibility

\[
\operatorname{Im}F=(\operatorname{Im}F)^*
\]

を生む。

このため all-(n) outer-gluing formula は (n\ge3) から始まり、(n=2) は自己接着の特別な base case である。

---

## 9. 幾何学的帰結

Theorem 0.1 は depth-one geometry の形を全長で決定する。

\[
\boxed{
\text{二つの端 chart は共通 value へ固定され、内部 charts はまだ自由である。}
}

空間的に読むと、depth one は完成した interval ではない。

- endpoints は存在する。
- local charts は存在する。
- endpoints と最外 charts の incidence は存在する。
- interior charts 間の adjacency / overlap はまだ存在しない。

depth two 以上の simultaneous probes は、それらを同時に区別する追加データを与える。これが chart 間接続そのものを構成するかは未証明である。

したがって、証明済みの visibility / reconstruction order は次である。

\[
\boxed{
\text{value}
\to
\text{anchored local charts}
\to
\text{multi-gap response data}
\to
\text{deeper response data}.
}

---

## 10. 証明で使われた原理

この all-(n) proof の核心は、局所 residual を padding しても局在性が保たれることである。

\[
\boxed{
m(z)=0
\quad\Longrightarrow\quad
\text{probe が }z\text{ を直接開かない限り、global response も0。}
}

これは自由数の「圧縮で消えた residual が、非整列 probe の位置だけで再出現する」という原理を、生成定理へ使ったものでもある。

消えていることが、局所 gadget の隔離壁として働く。深度1空間は、その隔離された gadgets を gap ごとに独立配置することで生成される。

---

## 11. certificate の位置

`certificates/depth1_outer_gluing_certificate.py` は (n=3,4,5,6,7) について

\[
\operatorname{rank}D_n^{\le1}=12n-16
\]

と actual image = outer-gluing space を exact-check する。

本ノートの proof により、certificate は conjectural pattern の根拠ではなく、all-(n) theorem の独立な低グレード検算になった。

---

## 12. 次の問題

depth one は全長で閉じた。次は depth two である。

depth-two response は二つの distinct internal gaps を同時に probe する。したがって、depth-one で自由だった interior charts の関係を初めて読みうるが、それが pairwise coherence と一致するかはまだ証明されていない。

次の最小問題は (n=4,d=2)。既知の dimension は

\[
\dim\mathcal Q_{4,2}=72,
\]

depth-one からの birth dimension は

\[
72-32=40.
\]

目標は、この40次元を

- adjacent-gap overlaps
- non-adjacent cross-boundary overlap
- common lower-depth contractions

へ分解し、direct compatibility presentation を得ることである。

ここで初めて、複数経路を比較する plaquette-like structure が現れる可能性が高い。
