# Note 04 — (n=3,d=1) Fiber-Product Theorem

## 二つの局所応答を共通 quaternionic value 上で貼り合わせる

**Status:** proved; exact certificate attached  
**Depends on:** the proved length-three depth-one kernel (S^3_0V)

---

## 0. 主結果

\[
E:=\operatorname{Hom}_{\mathbb R}(V,\mathbb H)
\]

と置く。向きづけられた正規直交基底 ((e_1,e_2,e_3)) に対し、二つの contraction を

\[
\boxed{
r(F):=\sum_{a=1}^3F(e_a)e_a
}
\]

および

\[
\boxed{
\ell(G):=\sum_{a=1}^3e_aG(e_a)
}

と定義する。

length three の depth-one profile は、compressed value (q\in\mathbb H) と二つの internal responses (F,G\in E) からなる。

本ノートの定理は、その許容条件が正確に

\[
\boxed{
q=r(F)=\ell(G)
}

だけであることを示す。

したがって

\[
\boxed{
\mathcal Q_{3,1}
\cong
E\times_{\mathbb H}E
}

である。ここで右辺は (r:E\to\mathbb H) と (ell:E\to\mathbb H) による fiber product

\[
E\times_{\mathbb H}E
:=
\{(F,G)\in E\oplus E\mid r(F)=\ell(G)\}
\]

である。

次元は

\[
\boxed{
\dim\mathcal Q_{3,1}
=12+12-4
=20.
}

これは部分深度空間を「終端空間の像」と呼ばず、depth-one profile 自身の局所 compatibility equation だけで直接 presentation した最初の非自明な例である。

---

## 1. length-three profile

pure boundary word を

\[
x=u|v|w
\qquad(u,v,w\in V)
\]

とする。reversed compression は

\[
q_x:=m_3(x)=wvu.
\]

二つの internal slots に一つの probe (d\in V) を入れると

\[
\boxed{
F_x(d):=wvd u
}

および

\[
\boxed{
G_x(d):=wdvu
}

を得る。

一般の (x\in V^{\otimes3}) には線形に延長する。

depth-one combined profile map は

\[
D_3^{\le1}:
V^{\otimes3}
\to
\mathbb H\oplus E\oplus E,
\]

\[
D_3^{\le1}(x)
=
(q_x,F_x,G_x)
\]

である。

ambient target dimension は

\[
4+12+12=28.
\]

実現可能 profile の次元は20なので、8本の独立な線形整合条件が必要になる。以下では、それが二つの quaternion equations にまとまることを示す。

---

## 2. 二つの contraction

### Lemma 2.1

(r,\ell:E\to\mathbb H) は基底非依存な (SO(3))-equivariant surjections である。

### Proof

(SO(3)) は quaternion automorphisms として (mathbb H=\mathbb R\oplus V) に作用する。正規直交基底について contraction した和なので、(r) と (ell) は基底変更で不変であり、(SO(3))-equivariant である。

全射性は直接示せる。任意の (q\in\mathbb H) に対して、

\[
F(e_1):=-qe_1,
\qquad
F(e_2)=F(e_3)=0
\]

とすれば

\[
r(F)=(-qe_1)e_1=q.
\]

同様に

\[
G(e_1):=-e_1q,
\qquad
G(e_2)=G(e_3)=0
\]

とすれば

\[
\ell(G)=e_1(-e_1q)=q.
\]

∎

### Canonical equivariant section

(q=a+w\in\mathbb R\oplus V) に対して

\[
\boxed{
s(q)(d)
:=
\langle w,d\rangle-\frac a3d
}

と置くと

\[
r(s(q))=q,
\qquad
\ell(s(q))=q.
\]

この (s) は Note 01 の depth-zero section と同じである。

---

## 3. overlap compatibility

虚 quaternion (z\in V) に対して

\[
\boxed{
\sum_{a=1}^3e_aze_a=z
}

が成り立つ。

これを使うと、pure word (x=u|v|w) に対し

\[
\begin{aligned}
r(F_x)
&=\sum_aF_x(e_a)e_a\\
&=\sum_awve_aue_a\\
&=wv\left(\sum_ae_aue_a\right)\\
&=wvu\\
&=q_x.
\end{aligned}
\]

同様に

\[
\begin{aligned}
\ell(G_x)
&=\sum_ae_aG_x(e_a)\\
&=\sum_ae_awe_avu\\
&=\left(\sum_ae_awe_a\right)vu\\
&=wvu\\
&=q_x.
\end{aligned}
\]

線形性により、すべての (x\in V^{\otimes3}) について

\[
\boxed{
q_x=r(F_x)=\ell(G_x).
}

したがって実現可能 profile は必ず

\[
\mathcal P_{3,1}
:=
\{(q,F,G)\mid q=r(F)=\ell(G)\}
\]

に属する。

---

## 4. Fiber-Product Theorem

### Theorem 4.1

\[
\boxed{
\operatorname{im}D_3^{\le1}
=
\mathcal P_{3,1}.
}

したがって

\[
\boxed{
\mathcal Q_{3,1}
\cong
E\times_{\mathbb H}E.
}

### Proof

Section 3 により

\[
\operatorname{im}D_3^{\le1}
\subseteq
\mathcal P_{3,1}.
\]

条件写像

\[
C:\mathbb H\oplus E\oplus E
\to
\mathbb H\oplus\mathbb H,
\]

\[
C(q,F,G)
:=
(q-r(F),q-\ell(G))
\]

を考える。

(r) と (ell) は全射なので (C) も全射である。したがって

\[
\dim\ker C
=28-8
=20.
\]

一方、length-three depth-one detection theorem により

\[
\ker D_3^{\le1}=S^3_0V
\]

であり、

\[
\dim S^3_0V=7.
\]

よって

\[
\dim\operatorname{im}D_3^{\le1}
=27-7
=20.
\]

同じ20次元の部分空間の包含なので

\[
\operatorname{im}D_3^{\le1}
=
\ker C
=
\mathcal P_{3,1}.
\]

また (q) は (r(F)=\ell(G)) から一意に決まるので、(mathcal P_{3,1}) は fiber product (E\times_{\mathbb H}E) と同型である。∎

---

## 5. exact sequence

Theorem 4.1 により split exact sequence

\[
\boxed{
0
\longrightarrow
S^3_0V
\longrightarrow
V^{\otimes3}
\xrightarrow{\ D_3^{\le1}\ }
E\times_{\mathbb H}E
\longrightarrow0
}

を得る。

depth one では、length-three state は二つの局所応答の gluing data まで圧縮される。そこで消える唯一の既約成分が最高スピン

\[
S^3_0V\cong V_3
\]

である。

この exact sequence は、depth-one space を state quotient として読むことも、先行定義された fiber product として読むこともできる。

Depth–Space Reversal では後者を正面に置く。

---

## 6. depth-one birth layer の分解

fiber product から共通 value を読む写像を

\[
\nu:E\times_{\mathbb H}E\to\mathbb H,
\qquad
\nu(F,G):=r(F)=\ell(G)
\]

とする。

その kernel は

\[
\boxed{
\ker\nu
=
\ker r\oplus\ker\ell.
}

(r) と (ell) は12次元から4次元への全射なので

\[
\dim\ker r
=
\dim\ker\ell
=8.
\]

したがって depth zero から depth one への birth layer は

\[
\boxed{
K_{3,1}^{\mathrm{birth}}
\cong
\ker r\oplus\ker\ell,
\qquad
\dim K_{3,1}^{\mathrm{birth}}=16.
}

representation decomposition を見ると

\[
E
=
\operatorname{Hom}(V,\mathbb H)
\cong
V_0\oplus2V_1\oplus V_2.
\]

(r,ell) はそれぞれ一つの (V_0\oplus V_1\cong\mathbb H) を読むので

\[
\ker r\cong V_1\oplus V_2,
\qquad
\ker\ell\cong V_1\oplus V_2.
\]

ゆえに

\[
\boxed{
K_{3,1}^{\mathrm{birth}}
\cong
2V_1\oplus2V_2.
}

これは既知の length-three spin-depth table を、fiber-product geometry から直接再現する。

---

## 7. component form of the compatibility equations

(F\in E) を

\[
F(d)=\alpha_F(d)+M_F(d)
\]

と分け、

\[
\kappa(M_F)
:=
\sum_ae_a\times M_F(e_a)
\in V
\]

とする。すると

\[
\boxed{
r(F)
=
-\operatorname{tr}M_F
+\alpha_F^\sharp
-\kappa(M_F)
}

および

\[
\boxed{
\ell(F)
=
-\operatorname{tr}M_F
+\alpha_F^\sharp
+\kappa(M_F).
}

したがって profile ((q,F,G))、

\[
q=s+w
\qquad(s\in\mathbb R, w\in V)
\]

の compatibility は

\[
\boxed{
s=-\operatorname{tr}M_F
=-\operatorname{tr}M_G
}

および

\[
\boxed{
w
=
\alpha_F^\sharp-\kappa(M_F)
=
\alpha_G^\sharp+\kappa(M_G)
}

である。

これは

- scalar equations が2本
- vector equations が2本、すなわち6成分

の合計8条件である。

---

## 8. depth-two で初めて可視になる lift difference

depth-one tower は

\[
\mathcal Q_{3,0}=\mathbb H
\xleftarrow{\ \nu\ }
\mathcal Q_{3,1}=E\times_{\mathbb H}E.
\]

depth two では canonical all-gap response が加わり、

\[
\mathcal Q_{3,2}\cong\mathfrak Q_3,
\qquad
\dim\mathcal Q_{3,2}=27.
\]

したがって完全な有限 tower は

\[
\boxed{
\mathbb H_{\,4}
\longleftarrow
(E\times_{\mathbb H}E)_{\,20}
\longleftarrow
(\mathfrak Q_3)_{\,27}.
}

最後の切断の kernel は

\[
\boxed{
K_{3,2}^{\mathrm{birth}}
\cong
S^3_0V
\cong V_3,
\qquad
\dim K_{3,2}^{\mathrm{birth}}=7.
}

その canonical coordinate は

\[
\boxed{
A_3(S)=4C_S.
}

したがって (V_3) は pairwise overlap compatibility だけでは見えず、二つの internal relations を同時に probe したとき初めて可視になる lift direction である。

重要なのは、(V_3) を gluing defect と混同しないことである。実現可能な depth-one profiles はすべて overlap equation を満たす。(V_3) はその equation の破れではなく、**同じ gluing data を持つ異なる深い lifts の差** である。

---

## 9. 幾何学的解釈

この定理で、抽象的だった「関係が空間を作る」が具体化する。

### Depth zero

\[
q\in\mathbb H
\]

という一つの collapsed value しかない。

### Depth one

左右の局所 response charts

\[
F,G\in\operatorname{Hom}(V,\mathbb H)
\]

が現れ、両者は overlap 上で

\[
r(F)=\ell(G)
\]

を満たす必要がある。空間は二つの chart の直和ではなく、共通 boundary value 上の fiber product として生まれる。

### Depth two

pairwise gluing では区別できなかった7次元の lift difference が開き、完全な27次元 response state が復元される。

よって、観測 filtration に沿って

\[
\boxed{
\text{value}
\ \longrightarrow\
\text{overlap gluing}
\ \longrightarrow\
\text{deeper lift difference}
}

という識別・再構成順序が、

\[
4\longrightarrow20\longrightarrow27
\]

という厳密な dimension growth を伴って得られた。これは ontological / causal な生成順序を主張しない。

---

## 10. curvature への距離

fiber-product equation の非充足量

\[
\Omega_{\mathrm{glue}}(q,F,G)
:=
\bigl(q-r(F),\ q-\ell(G)\bigr)
\in\mathbb H\oplus\mathbb H
\]

は、任意の profile candidate が局所的に貼り合うかを測る obstruction である。

ただし、これはまだ gauge curvature ではない。実際の response states では

\[
\Omega_{\mathrm{glue}}=0.
\]

曲率には、同じ端点を持つ異なる transport paths と、その holonomy defect が必要になる。

この Note 04 が与えたのは、その一段手前の構造である。

> 非可換局所データを貼り合わせる overlap law が、ambient space なしに fiber product として書ける。

次に plaquette を入れれば、四辺の局所 response/transport を同じ方式で貼り、閉路上に残る非合流量を定義できる。

---

## 11. Exact certificate

`certificates/n3_depth1_fiber_product_certificate.py` は exact integer arithmetic で次を検証する。

- (r:E\to\mathbb H) と (ell:E\to\mathbb H) の rank が4。
- 二つの quaternion compatibility equations の rank が8。
- 実際の全 depth-one profiles が両式を満たす。
- length-three depth-one profile map の rank が20。
- fiber product の dimension が20。
- actual profile image と intrinsic fiber product が一致する。
- depth-one invisible layer の dimension が7。

Expected final line:

```text
ALL CHECKS PASSED
```

---

## 12. 次の一手

二つの候補がある。

1. **(n=4,d=1) の direct presentation**  
   三つの internal response charts の adjacent contractions が作る compatibility diagram を求め、32次元空間を直接切り出す。

2. **最小 noncommutative plaquette**  
   fiber-product gluing を辺へ移し、四元数値 transport の閉路 defect を定義して、first-detection depth を計算する。

解析順序としては、まず (n=4,d=1) を調べる。そこで単純な chain fiber product が成立するか、既に追加 compatibility が必要かを判定する。その結果が plaquette 候補の局所データ形式を制約する。
