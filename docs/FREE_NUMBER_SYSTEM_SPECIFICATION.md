# 自由数の体系仕様 — Core と Notes 1–33

仕様版 0.1 / 2026-09-24

**目的：自由数が何を対象とし、何を計算し、どこまで保証するかを、一つの参照文書に固定する。**

対象原典は、凍結 Core v1.0.0（`9efc241d38e5ca2cd07f425b747bfb5d67ea0235`）と、DGG Notes 1–33（`2b1adb8b11a9ed0b566f7d82c686f4b78c1702aa`まで）。この文書の版は統合仕様の版であり、Core の公開版番号とは別である。

## 1. 自由数とは何か

**自由数は、順序を持つ有限の応答を一個の対象として保持し、連結して計算し、どの深度の観測で差が見えるかを調べる体系である。**

一個の自由数の完全な表現には、現在の四元数値と、その値だけでは失われる挿入応答の双方が含まれる。完全な対象の同一性は固定される。その対象をどこまで圧縮して使えるかは、支える観測・後続操作によって決まる。

現在の研究は、その上に、配置ごとの局所応答商、必要な情報を残す最小状態、および配置間の輸送を積み上げている。これらをつなぐ計算規則が、本仕様の統合対象である。

### 1.1 なぜ値だけでは足りないか

$V=\operatorname{Im}\mathbb H$ とし、$x=i|i-j|j$ を考える。四元数への圧縮は

$$
m_2(x)=ii-jj=0
$$

だが、間に $i$ を挿入すると

$$
A_2(x)(i)=iii-jij=-2i\ne0.
$$

したがって $x$ と加法零元を同一視すると、この挿入応答を計算するための情報がなくなる。自由数は、この差を完全な応答として表現できる。さらに、特定の操作だけを支える場合には、必要な差だけを残す商を構成する。

### 1.2 三つの対象を固定する

| 名称 | 数学的対象 | 同一性 | 役割 |
|---|---|---|---|
| 完全な自由数 | $F\in\mathfrak Q_n\cong B_n$、または有限個の次数成分の和 | exact response の一致 | 基礎となる数・積・深度 |
| 配置の応答商 | $Y_s=E_s/L_s$ | 指定された matching 関係を法とする一致 | 局所応答の貼合せと配置比較 |
| 操作族に対する保持状態 | $Q_s=E_s/K_s$ | 指定された全読出しの一致 | 更新に必要な情報を保存する計算状態 |

$E_s$ は局所辺応答の直和など、型 $s$ ごとに指定する提示空間である。一般に $B_n$ そのものとは異なる。各 $E_s$ がどの応答から構成されるかを写像で示すことが接続の条件になる。

## 2. 基礎対象と完全な同一性

### 2.1 応答からの定義

局所デコーダの逆になる encoder は

$$
\Theta:V\otimes\mathbb H\longrightarrow\operatorname{Hom}(V,\mathbb H),
\qquad
\Theta\Bigl(\sum_a e_a\otimes h_a\Bigr)(d)=\sum_a e_a d h_a.
$$

これは同型である。最後の probe 変数に $\Theta^{-1}$ を作用させる写像を $\mathcal D_n$ とすると、DGG [Note 02][N02] に従い

$$
\mathfrak Q_1=V,\qquad
\mathfrak Q_n=\mathcal D_n^{-1}(V\otimes\mathfrak Q_{n-1})\quad(n\ge2)
$$

と再帰定義できる。単位成分は $\mathfrak Q_0=\mathbb R$ とする。

表現定理により

$$
B_n=V^{\otimes n},\qquad
A_n(a_1|\cdots|a_n)(d_1,\ldots,d_{n-1})
=a_nd_{n-1}a_{n-1}\cdots d_1a_1,
$$

$$
A_n:B_n\xrightarrow{\sim}\mathfrak Q_n,\qquad
\dim\mathfrak Q_n=3^n.
$$

凍結 Core の $\mathfrak A_n=\operatorname{im}A_n$ と、応答から定義した $\mathfrak Q_n$ は同じ応答部分空間を与える。体系全体の有限対象は $\bigoplus_{n\ge0}\mathfrak Q_n$ に置く。以下の深度公式は、明示した同次次数ごとに用いる。

### 2.2 同一性・零・観測

同じ次数で

$$
A_n(x)=A_n(y)\iff x=y.
$$

四元数値は

$$
m_n(a_1|\cdots|a_n)=a_n\cdots a_1,
\qquad \mu_n=m_nA_n^{-1}.
$$

完全な同一性、$\mu_n(F)=\mu_n(G)$、制限した観測族での同値は、それぞれ名前を付けて扱う。$\ker\mu_n$ に属する非零応答は、値が零の自由数である。加法零元はすべての応答が零の対象である。

全有限長の完全復元・同一性は [Core closure theorem][C09] の確立済み部分である。

## 3. 演算と型

### 3.1 連結積

テンソル表示では $x|y\in B_{m+n}$。応答表示では、$m,n\ge1$ に対して

$$
(F\star G)(\mathbf d,p,\mathbf e)=G(\mathbf e)\,p\,F(\mathbf d),
\qquad
A_{m+n}(x|y)=A_m(x)\star A_n(y).
$$

$\mathfrak Q_0$ は実スカラーとして作用する。加法・実スカラー倍・この積・単位により、完全な応答空間は単位的結合的次数付き実代数となる。ここには [C09] の全次数の証明がある。

### 3.2 操作台帳

| 操作 | 入出力の型 | 固定するデータ |
|---|---|---|
| 圧縮 | $B_n\to\mathbb H$ | 積の向き |
| 部分 probe 応答 | $B_n\to\operatorname{Hom}(V^{\otimes d},\mathbb H)$ | 元の gap の集合と順序 |
| 連結 | $B_m\otimes B_n\to B_{m+n}$ | 因子の順序 |
| 係数読出し | $E_t\to E_s\otimes V$ など | 左右 decoder、対象 gap、係数方向 |
| decoder suspension | $E_s\otimes V\to E_t$ | 実際の probe gap と、値を掛ける側 |
| chart 座標変更 | 同じ配置商の二つの座標表示間 | 両 encoder と規格化 |
| 配置輸送 | 別配置の core・商・保持状態間 | 共通 anchor、対象部分、残差上の作用 |

例えば Note 26 の右 suspension は、gap 4 に probe 引数を置き、値を右から掛ける指定操作である。その式を保持して比較する。文脈に現れる「挿入」は、この操作台帳のどの写像かを併記する。

## 4. 深度と単一積の分解障害

元の内部 gap の部分集合 $S$ に一個ずつ probe を置く応答を $R_{n,S}$ とし、$R_{n,\varnothing}=m_n$ とする。

$$
D_{n,\le d}=\bigoplus_{|S|\le d}R_{n,S},\quad
K_{n,d}=\ker D_{n,\le d},\quad
\delta(x)=\min\{|S|:R_{n,S}(x)\ne0\}.
$$

$x\ne0\in B_n$、$n\ge1$ では $0\le\delta(x)\le n-1$。深度は最初に検出する **probe 数** であり、更新回数や spectator 数とは別の量である。零には便宜上 $\delta(0)=\infty$ を与える。

DGG [Note 03][N03] の有限観測 tower は $B_n/K_{n,d}$ で表せる。これは観測解像度を落とした状態であり、完全な自由数は終端で回復する。

### 4.1 深度加法性：定義からの短証明

非零の同次状態 $x\in B_m,y\in B_n$、$m,n\ge1$ に対して

$$
\boxed{\delta(x|y)=\delta(x)+\delta(y).}
$$

**証明。** $x|y$ の probe 集合を、$x$ 内部、$y$ 内部、接合 gap に分ける。内部応答を $f=R_{m,S_x}(x)$、$g=R_{n,S_y}(y)$ とすると、全体の応答は接合 probe がなければ $gf$、あれば $gpf$ になる。これは各因子内の任意の線形結合にも双線形性により成立する。

probe 総数が $\delta(x)+\delta(y)$ より小さければ、少なくとも一方の内部 probe 数がその因子の深度に達せず、その応答は恒等的に零になる。したがって全体も零である。

逆に、各因子を初めて検出する probe を独立に選び、接合 gap を空ける。各応答に非零値を与える引数を選べ、四元数の非零積は非零なので、総数 $\delta(x)+\delta(y)$ で検出できる。以上で等号が成立する。

この短証明は本仕様の probe 規約と Core の圧縮から直接導く。過去の有限因子対検算を証明の前提には用いない。

### 4.2 分解不能性の正確な帰結

非零 $z\in B_N$、$N\ge2$ が最大深度 $\delta(z)=N-1$ を持つとする。正の長さ $m+n=N$ の非零二因子で $z=x|y$ と書けるなら

$$
\delta(z)=\delta(x)+\delta(y)\le(m-1)+(n-1)=N-2
$$

となり矛盾する。よって **どの内部切断でも単一の二因子積に分解できない**。単位因子や、複数の積の和による表示はこの命題の対象外である。

[DGG Note 09][N09] は全 $N\ge2$ について

$$
K_{N,N-2}=S_0^N V,\qquad
A_N(S)=(-2)^{N-1}C_S
$$

を与える。ここで $C_S$ は、対称テンソル $S$ のうち $N-1$ 個の添字を probe 引数と縮約して得る $V$ 値応答である。したがって最高スピン部分の非零元はすべて、この分解障害を持つ。最大深度は分解不能性の十分条件であり、その逆をこの議論から要求しない。

## 5. 配置幾何は応答の提示から作る

DGG の局所四面体では、四 face から六 edge への matching map を取り

$$
C_s^0\xrightarrow{\partial_s}E_s\xrightarrow{\pi_s}Y_s\to0,
\qquad L_s=\operatorname{im}\partial_s
$$

とする。配置の情報には、商の次元とともに、ラベル付き各 edge の像と有効な anchor を含める。

全長の terminal gluing は [Note 12][N12] で

$$
\ker\partial_n=\operatorname{im}\mathbf B_n
$$

まで証明されている。一方、[Note 13][N13] の次の differential は全 $n\ge5$ で構成され、$\partial_n^{(2)}\partial_n=0$ を満たすが、次の場所の exactness は別の主張である。

$$
\ker\partial_n^{(2)}=\operatorname{im}\partial_n.
$$

これは $n=5$ で有理数上の定理、$n=6,7$ では指定された二素数体上の検算、全 $n$ では課題として記録する。

配置 atlas の現在の範囲は、一 spectator の全配置、二 spectator の reduced 全六配置と外側への延長、三・四 spectator にまたがる指定の更新列と cell である。全内部配置への拡張には、各配置の商と各辺の具体的な写像が必要になる。

## 6. 最小保持を一般構成にする

### 6.1 有限の観測・操作出力

$E$、現在の線形観測 $q$、追加の線形出力族 $F_a$ を固定する。

$$
K=\ker q\cap\bigcap_a\ker F_a,\qquad
Q=E/K\cong\operatorname{im}(q,(F_a)_a).
$$

これが双方を支える最小の線形商である。別の商 $E/H$ が同じ出力を支えるなら $H\subseteq K$ だから、$E/H\to E/K$ が一意に誘導される。[Note 27][N27] に一般証明がある。

有限次元では、追加保持量は

$$
\operatorname{rank}(q,(F_a)_a)-\operatorname{rank}q.
$$

一つの追加出力 $F$ の場合、現在隠れているが追加出力で必要な差は

$$
\ker q/(\ker q\cap\ker F)\cong F(\ker q)
$$

で表される。従って $\ker q$ 全体と、そのうち後続操作が区別する部分は区別して扱う。

### 6.2 合成を許す操作族

型付きの生の線形操作 $J_a:E_s\to E_t$ と、観測 $q_s:E_s\to Y_s$ を指定する。空経路を含むすべての許容有限経路 $w:s\to t$ について

$$
K_s=\bigcap_{w:s\to t}\ker(q_tJ_w)
$$

と定義すれば

$$
J_aK_s\subseteq K_t.
$$

従って $Q_s=E_s/K_s$ 上に合成可能な更新が誘導される。これは元の観測を保存する最大の不変な関係族であり、操作族に対する最小保持状態を与える。

有限グラフ・有限次元では

$$
K_s^{(0)}=\ker q_s,\qquad
K_s^{(r+1)}=K_s^{(r)}\cap\bigcap_{a:s\to t}J_a^{-1}K_t^{(r)}
$$

が有限回で停止する。各厳密な変化は全頂点の核の次元和を減らす。長さが無限に増える操作網への一様な停止保証は、追加の証明対象となる。

外部入力 $v\in V$ に依存する双線形操作は、$E_s\otimes V$ 上の線形写像として扱うか、全 $v$ についての不変性を要求する。入力を固定した検査と tensorized な全入力の次元を混同しない。

### 6.3 失われた差の再検出の意味

Note 28 の再検出は、粗い子商へ落とす前の応答データ上にある係数読出しを支えるため、子状態を精密化する構成である。差を完全に捨てた商だけを入力とする写像は、その差を区別できない。実装では保持先・読出し元・商への射影を明示する。

## 7. 商の上で演算・輸送を実行する条件

この節は一般の線形代数による判定規則である。自由数の各具体操作が条件を満たすかは、その式と証明を添える。

### 7.1 更新の降下

$U:E_s\to E_t$ が $E_s/K_s\to E_t/K_t$ を誘導する必要十分条件は

$$
U(K_s)\subseteq K_t.
$$

不足するとき、標的の商を固定し、元の源情報も保存する最小の源精密化は

$$
E_s/(K_s\cap U^{-1}K_t).
$$

必要条件は零の代表元の像を比べて得られ、十分性は代表元差を送れば得られる。

### 7.2 積の降下

双線形積 $b:E_s\otimes E_t\to E_u$ が両因子の商上で定義できる必要十分条件は

$$
b(K_s\otimes E_t+E_s\otimes K_t)\subseteq K_u.
$$

完全な Core の連結積では同一性が厳密なので条件は満たされる。圧縮した保持状態にも積を載せる場合は、この条件を別途検査する。左右から任意の因子を付ける操作まで許容するなら、その文脈を操作族へ含める。

### 7.3 輸送・更新の整合

可逆な生の輸送 $T:E_s\to E_{s'}$ について $T(K_s)=K_{s'}$ なら商同型が誘導される。既知の core 同型だけから、保持状態全体の同型を仮定せず、残りの情報の作用を指定する。

更新 $U:E_s\to E_t$ と比較先の $U':E_{s'}\to E_{t'}$、輸送 $T_s,T_t$ が与えられた場合、各写像の降下を確認した上で

$$
C=T_tU-U'T_s
$$

を測る。商の上で更新順序が一致する条件は $C(E_s)\subseteq K_{t'}$。生の空間で一致する条件は $C=0$。両者を分けて報告する。

### 7.4 経路・holonomy・合流性

各経路の操作を合成し、同じ始域・終域で差を取る。輸送の閉路では holonomy を測る。書換えの合流性では、二つの分岐後に許容される再合流と、その際の同値関係を指定する。

Note 30 の挿入順序差と Note 33 の配置輸送の平坦性は、異なる操作を比べた結果である。これらを保存したまま計算体系を構成する。

## 8. 27–33を仕様の各項へ割り当てる

| Note | 操作と保存する情報 | 確立した結果 |
|---|---|---|
| 27 | 元の444次元親情報と、指定右 suspension の444次元子出力 | 最小源876次元。追加432次元。子への更新核432次元 |
| 28 | 中央 probe の係数方向を1・2・3方向読む | 最小子588・732・876次元。全係数で更新核432次元を検出し、指定 encode/decode を可逆化 |
| 29 | 保持状態に新入力を tensorize し、次の右操作 $222\to232$ を支える | 2628次元から3924次元へ。追加1296次元は子の outer core 全体 |
| 30 | 共通源・二つの途中状態・二つの終点、さらに同じ後続読出し | 6516次元、読出しも含め7668次元。終点差 rank 1320。同じ終点の条件下でも読出し差 rank 1296 |
| 31 | 共通源と終点和から決まる読出し | 不定部分 $W$ は1152次元。$T_R/W\cong T_{212}$ は144次元 |
| 32 | 指定した隣接三段配置の core と読出し則 | $W$ を輸送し、144次元の同定・終点項と可換 |
| 33 | 四配置cellの三段と四辺の読出し則 | core holonomy $I_{144},I_{432},I_{1296}$。このcell上で確定coreは経路独立 |

Note 31 の法則は、指定された写像と $Sx=c\otimes a\otimes b$、$c\in T_{212}$ の下で

$$
\Psi^{-1}([Nx])=\langle a,b\rangle c+
\Lambda_{\mathrm{sym}}\bigl((F_{ab}+F_{ba})x\bigr).
$$

これを運ぶのが Notes 32–33 である。$T_R/W$ は商としての確定部分であり、補空間を選ぶことなく定義される。

Note 33 の full readout quotient は三配置で144次元、例外配置Dで180次元（144 core + 36 residual）である。今後の全保持状態の輸送では、この型と次元の差も構成へ含める。

## 9. 計算可能性と証明の区分

係数を有理数など演算・等号判定が有効な体で表す場合、有限の対象について次が実行できる。

- 局所 decoder の反復による完全応答の復元と同値判定。
- probe 基底値による深度の決定。
- 核・像・階数による追加保持量と降下障害の計算。
- 指定輸送の合成と閉路差・更新の可換性の検査。
- 有限操作グラフでの不変核の反復計算。

完全なCoreは、各次数で $i,j,k$ の語基底を順序付けた係数表を標準表現にできる。有限の線形商も、基底と消去規約を固定すれば行簡約による比較表現を持つ。これらの座標上の標準表現と、generated-chart 書換えの正規形は、それぞれの手続きとして扱う。

任意の実数を不透明な入力として与えた場合の等号判定までを、有限アルゴリズムの保証に含めない。大きな次元での計算量は、決定可能性とは別に評価する。

| 区分 | 本仕様での意味 |
|---|---|
| 定義 | 対象・観測・許容操作を定める規約 |
| 一般定理 | 明示された全次数または一般の線形空間に適用される証明 |
| 有限定理 | 指定された配置・作用素についての厳密な証明と証明書 |
| 有限体検算 | 記載した素数体上の結果。標数零への持上げには別の根拠が必要 |
| 実装記録 | 実行時点・ソース・検算範囲の記録 |
| 完成義務 | 次の統合版に必要な定義・構成・証明 |

本仕様の整理では原典の定義・証明範囲・記録を照合した。過去の全証明書の再実行は行っていない。有限行列の結果は、各 Note の再構成コードと結果記録へ参照を戻す。

## 10. 完成と呼ぶ範囲・次の受入条件

Core v1 は有限 exact-response 代数として完成済みである。次の統合版は、**Core の完全な対象を維持し、明示した配置・操作族について、最小保持状態の上で演算・更新・輸送を繰り返せる体系**を目標とする。

有限の操作範囲を閉じた版と、任意長・任意内部配置の全体版は、対応範囲を版ごとに宣言する。範囲を限定して完成させる場合も、既に見つかった差・操作・障害は台帳へ残す。

| ID | 完成条件 | 33までの状態 | 次に必要なもの |
|---|---|---|---|
| G1 | 完全な対象・同一性・加法・積・単位・深度 | Core、DGG 02–03・09で成立。深度加法性の短証明は本仕様§4 | 統合実装の入口と表現規約を固定 |
| G2 | 操作族と合成を型付きで列挙 | 各 Note に具体式、27に一般閉包定理 | 対象範囲の操作台帳を一つにし、全継続を指定 |
| G3 | 必要十分な保持と、各更新の降下 | 27–31の指定問題で成立 | 選んだ操作網全体で不変核・保持量を構成 |
| G4 | 保持状態の輸送と更新の可換性 | 32–33は確定coreと読出し商で成立 | 保持情報全体への持ち上げと更新squareの検証 |
| G5 | 支える圧縮状態上の連結・挿入 | 完全Coreで閉じる。29–30に追加保持の障害 | §7.2の文脈安定性、必要な最小精密化 |
| G6 | 有限対象の同値・障害・経路比較を再現 | 個別のexact certificatesが存在 | 共通の入出力形式、失敗時の具体的witness、統合使用例 |

**次の数理作業は G4。** Note 33 の四配置・三段を起点に、どの保持状態間の写像を構成するかを先に指定し、更新squareを検査する。型や次元が合わない場合は、共通保持・片方向写像・追加情報のいずれが必要かを結果として記録する。この仕様作成の段階では、その持ち上げを成立済みに数えない。

## 11. 大域化の四課題をどこへ置くか

| 課題 | 現在の根拠 | 閉じるべき内容 |
|---|---|---|
| 全 $n$ の四面体生成 | 13で第二differentialを全長構成。middle exactnessは限定範囲 | 全長の kernel=image の証明、または不足を示す反例と修正 |
| 内部spectatorが3個以上の輸送 | 26の222、29の232、32–33の指定ladder/cell | 全内部配置の型、anchor、残差、辺写像の構成 |
| 四元数輸送を含む非合流残差・曲率候補 | 24のchart非可換性、25・33の平坦core、30の順序差 | 比較する操作を固定し、残差を含む閉路作用を実際に計算 |
| BoundaryIsoを法とする文脈的局所合流性 | root-onlyの制限付き正規化と修正版の条件整理 | 文脈規則、証明書保存、判定安定性、適合する同値、停止性、critical pairs |

最後の課題は generated-chart 書換え層に属する。基礎Coreの結合律・完全応答の等号を使う計算は、既に独立して成立する。generated-chart の正規化も統合版の機能として約束する時点で、その課題を受入条件へ追加する。

参照すべき合流性の基準は [修正版 Note 12a][C12a] である。root-only 系は functional な LocalMul の下で一段決定的。文脈を含む系には追加仮定と証明が必要である。現行 Lean の制限付き重み減少と、全体系の合流性は別々の保証として記載する。

## 12. 外部接続の位置

Time Engine は、保持したい差と更新についての要求を供給する研究先として置く。three-plus-one のSGD例は、同じ核の共通部分による保持判定を適用した外部検証例として置く。いずれも、本仕様の基礎定義・Coreの証明・完成判定の前提には加えない。

自由数側で固定する成果は、**完全な応答対象、深度、指定操作に必要な最小保持、その上の演算と輸送の成立条件**である。

## 13. 原典への索引

Core の原典は研究枝と別の凍結コミットにあるため、次の固定リンクを用いる。

- [Core closure theorem][C09]：対象、同一性、復元、結合積。
- [Core claims ledger][CL]：各層の証明状態。
- [Certified Red confluence repair][C12a]：書換え層の現行保証と追加条件。
- [DGG監査済みsnapshotの台帳](../research/depth-generated-geometry/releases/research-2026-09-07/CLAIMS_LEDGER.md)：14–26の有限定理と検証来歴。
- [保持・更新・経路読出しの見取り図](../research/depth-generated-geometry/synthesis/retention-and-path-readout-checkpoint.md)：27–33の詳細。

| DGG Note | 体系内の担当 | 証明範囲の目印 |
|---:|---|---|
| [01](../research/depth-generated-geometry/notes/01-n2-intrinsic-response-tower.md) | 長さ2の内在的応答 | 定理：自己共役条件と零値層 |
| [02](../research/depth-generated-geometry/notes/02-all-grade-intrinsic-terminal-response.md) | 全次数の応答先行定義 | 全有限長の表現定理 |
| [03](../research/depth-generated-geometry/notes/03-finite-depth-space-reconstruction.md) | 有限深度tower | 一般構成：切断・新生層・終端復元 |
| [04](../research/depth-generated-geometry/notes/04-n3-depth1-fiber-product.md) | 長さ3のdepth 1 | 有限定理：20次元fiber product |
| [05](../research/depth-generated-geometry/notes/05-n4-depth1-factor-origin-and-outer-gluing.md) | 長さ4のdepth 1 | 有限定理：factor originと外側gluing |
| [06](../research/depth-generated-geometry/notes/06-all-n-depth1-outer-gluing-theorem.md) | depth 1の全長gluing | 全 n≥3 の定理：次元12n−16 |
| [07](../research/depth-generated-geometry/notes/07-n4-depth2-pair-chart-gluing.md) | 長さ4のpair charts | 有限定理：72次元の貼合せ |
| [08](../research/depth-generated-geometry/notes/08-n4-canonical-terminal-filling.md) | 長さ4の終端filling | 有限定理：top-spin-free filling |
| [09](../research/depth-generated-geometry/notes/09-all-n-terminal-boundary-and-filling.md) | 終端境界と最高スピン | 全 n≥2 の定理：最後の不可視層 S₀ⁿV |
| [10](../research/depth-generated-geometry/notes/10-n5-terminal-response-tetrahedron.md) | 長さ5のresponse tetrahedron | 有理数上の有限定理：syzygy16次元 |
| [11](../research/depth-generated-geometry/notes/11-n6-terminal-response-4simplex.md) | 長さ6のterminal response | terminal gluingの有限証明；全長化は12 |
| [12](../research/depth-generated-geometry/notes/12-all-n-pairwise-terminal-descent.md) | pairwise terminal descent | 全 n≥3 の定理：pairwise条件からglobal filling |
| [13](../research/depth-generated-geometry/notes/13-tetrahedral-second-differential.md) | tetrahedral second differential | 全長構成；middle exactnessはQでn=5、指定有限体でn=6,7 |
| [14](../research/depth-generated-geometry/notes/14-closed-quaternionic-tetrahedral-operator.md) | 閉じた四元数四面体作用素 | n=5の有限定理：H⊗H型の商 |
| [15](../research/depth-generated-geometry/notes/15-spectator-placement-residuals.md) | spectator配置によるedge像 | 指定低次数の配置分類・検算；体と範囲は原典 |
| [16](../research/depth-generated-geometry/notes/16-parity-square-quaternionic-residual.md) | 奇数長のparity square | 指定parity族の全長全射；n=7の完全cokernel |
| [17](../research/depth-generated-geometry/notes/17-even-length-capped-five-edge-residual.md) | 偶数長のcap残差 | 指定parity族の全長全射；n=6の完全cokernel |
| [18](../research/depth-generated-geometry/notes/18-canonical-seed-quaternion-coordinate.md) | seedの四元数座標 | n=5の有限定理：直交12+4分解 |
| [19](../research/depth-generated-geometry/notes/19-central-spectator-channel-transfer.md) | 中央spectatorでのchannel移動 | n=6の有限定理：指定商写像とcapの因子化 |
| [20](../research/depth-generated-geometry/notes/20-n6-spectator-atlas-and-central-shear.md) | 一spectatorの二chart atlas | n=6の全5配置と中央transition |
| [21](../research/depth-generated-geometry/notes/21-n7-exceptional-core-decomposition.md) | 例外212のcoreと残差 | n=7の有限定理：指定座標で144+4 |
| [22](../research/depth-generated-geometry/notes/22-exterior-spectator-suspension.md) | 外側spectator suspension | 全長定理：外側tensorizationと左右可換 |
| [23](../research/depth-generated-geometry/notes/23-n7-reduced-internal-word-atlas.md) | 二spectatorのreduced atlas | n=7の全6内部wordと外側拡張 |
| [24](../research/depth-generated-geometry/notes/24-n7-transported-anchor-transition-groupoid.md) | transported-anchor groupoid | n=7の指定全anchor履歴と三生成作用素 |
| [25](../research/depth-generated-geometry/notes/25-n7-spacing-word-flat-core-and-quaternionic-defect.md) | spacing-word connection | n=7の全6辺、唯一の独立閉路でI144 |
| [26](../research/depth-generated-geometry/notes/26-n8-222-residual-redetection.md) | 222の商と212からの右操作 | 指定作用素の有理数上の有限定理 |
| [27](../research/depth-generated-geometry/notes/27-minimal-state-refinement-for-central-update.md) | 最小源精密化 | 一般商定理と指定876次元の有限適用 |
| [28](../research/depth-generated-geometry/notes/28-decoder-continuations-and-retained-core.md) | 係数読出しによる再検出 | 指定432次元の全再検出、対応する最小子 |
| [29](../research/depth-generated-geometry/notes/29-forward-insertion-beyond-decoder-closure.md) | 次の内部挿入 | 指定232出力に必要な3924次元 |
| [30](../research/depth-generated-geometry/notes/30-ordered-insertion-paths-and-local-interchange.md) | 二挿入順序と共通後続読出し | 指定経路の差・最小共通保持・再検出 |
| [31](../research/depth-generated-geometry/notes/31-symmetric-endpoint-law-and-recovered-core.md) | 対称終点則と回復core | 指定144次元商の同定と読出し則 |
| [32](../research/depth-generated-geometry/notes/32-adjacent-core-transport-preserves-readout.md) | 隣接配置での読出し輸送 | 指定ladderの不定部分保存と可換性 |
| [33](../research/depth-generated-geometry/notes/33-readout-transport-around-a-configuration-cell.md) | 四配置cellの読出し輸送 | 指定三段cellの平坦coreと四辺の整合 |

ここで「Note」はDGGの番号。凍結Coreの同番号ノートとはパスで区別する。

[N02]: ../research/depth-generated-geometry/notes/02-all-grade-intrinsic-terminal-response.md
[N03]: ../research/depth-generated-geometry/notes/03-finite-depth-space-reconstruction.md
[N09]: ../research/depth-generated-geometry/notes/09-all-n-terminal-boundary-and-filling.md
[N12]: ../research/depth-generated-geometry/notes/12-all-n-pairwise-terminal-descent.md
[N13]: ../research/depth-generated-geometry/notes/13-tetrahedral-second-differential.md
[N27]: ../research/depth-generated-geometry/notes/27-minimal-state-refinement-for-central-update.md
[C09]: https://github.com/residual-chart-lab/free-number-core/blob/9efc241d38e5ca2cd07f425b747bfb5d67ea0235/core/09-core-closure-theorem.md
[CL]: https://github.com/residual-chart-lab/free-number-core/blob/9efc241d38e5ca2cd07f425b747bfb5d67ea0235/CLAIMS_LEDGER.md
[C12a]: https://github.com/residual-chart-lab/free-number-core/blob/9efc241d38e5ca2cd07f425b747bfb5d67ea0235/notes/12a-certified-red-confluence-repair.md
