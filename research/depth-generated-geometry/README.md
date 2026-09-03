# Depth-Generated Geometry — Research Notes

> 作業仮説：空間が深度を許すのではなく、関係深度が空間を紡ぐ。

自由数の probe-depth filtration から、depth-gated observability を独立した代数幾何プログラムとして切り出す研究ノート群。

## Start here

[`notes/00-checkpoint-through-note12.md`](notes/00-checkpoint-through-note12.md) は、Note 01–12 の定理依存、次元表、到達点、未解決境界、および proof audit を一枚にまとめた入口である。

[`synthesis/ordered-tetrahedral-spectator-atlas.md`](synthesis/ordered-tetrahedral-spectator-atlas.md) は、Note 14–20 を placement memory、二 chart 被覆、中央 cross-product transition、chart-independent residual という一本の有限代数として再構成した独立読解層である。probe-depth filtration 全体を先に追わず、現在の tetrahedral / spectator 機構だけを把握したい場合はこちらから読める。

## Claim boundary

- **Proved:** probe depth は識別可能性と再構成の有限 filtration を与える。
- **Proved at depth 0→1:** response space は value space と新生層の明示的な代数的 extension として組み上がる。
- **Exact-checked:** 低 grade の dimension profiles と、全長 depth-one formula の有限範囲検算。
- **Hypothesis:** depth filtration が幾何学的空間そのものの生成機構である。
- **Proved at \(n=4,d=2\):** 三つの pair charts は明示的 boundary maps により exact に貼り合わさる。
- **Proved:** 40次元 birth layer は coherence 条件そのものではなく、pair origin により \(12+16+12\) へ分解する。
- **Proved at \(n=4,d=3\):** compatible pair boundary は一意な \(SO(3)\)-equivariant top-spin-free filler を持ち、全 filler は terminal \(V_4\) だけ異なる。
- **Proved:** terminal response から三つの pair faces への局所公式は、一層の decoder だけで明示できる。
- **Proved for all \(n\):** exact-depth-\((n-2)\) terminal boundary の kernel は \(S^n_0V\) であり、terminal birth 全体と一致する。
- **Proved for all \(n\):** penultimate dimension は \(3^n-(2n+1)\)、terminal birth は \(2n+1\)、canonical \(SO(3)\)-equivariant filling は一意。
- **Proved at \(n=5\):** 四つの terminal faces は六つの pairwise common shadows の一致だけで完全に glue し、\(\mathcal P_{5,3}=\ker\partial_5\) となる。
- **Proved at \(n=5\):** matching equations の最初の syzygy は16次元で、\(2V_0\oplus3V_1\oplus V_2\) に分解する。
- **Proved at \(n=6\):** 五つの terminal faces は十個の pairwise common shadows の一致だけで完全に glue し、\(\mathcal P_{6,4}=\ker\partial_6\) となる。
- **Proved at \(n=6\):** 1080個の matching coordinates の compatibility syzygy は176次元で、\(10V_0\oplus21V_1\oplus15V_2\oplus4V_3\) に分解する。
- **Proved for all \(n\):** pairwise common-shadow compatibility は terminal boundary の global filling に十分であり、\(\mathcal P_{n,n-2}=\ker\partial_n\) となる。
- **Proved for all \(n\):** 最初の compatibility syzygy は普遍 character law を持ち、\(n=7\) では1200次元 \(45V_0\oplus100V_1\oplus90V_2\oplus45V_3\oplus10V_4\) となる。
- **Constructed for all \(n\ge5\):** 四つの face と六つの edge の局所 cokernel から tetrahedral second differential \(\partial_n^{(2)}\) を定義し、\(\partial_n^{(2)}\partial_n=0\) を得る。
- **Proved at \(n=5\):** \(\ker\partial_5^{(2)}=\operatorname{im}\partial_5\) が有理数上で成立し、16次元局所商は \(\mathbb H\otimes\mathbb H\) 型である。
- **Exact-checked at \(n=6,7\):** tetrahedral second complex は二つの素数体上で middle-exact である。
- **Exact-checked at \(n=7\):** exceptional \(2\!-!1\!-!2\) support \(Q=(1,3,4,6)\) だけに generic local quotient より余分な \(\mathbb H\) が生じ、その全体が次の cokernel へ survive する。
- **Proved at \(n=5\):** 16次元 tetrahedral quotient は五つの明示的な四元数作用素からなる閉写像 \(\omega_5:\mathcal R_2^{\oplus6}\to\mathbb H\otimes\mathbb H\) で実現され、\(\ker\omega_5=\operatorname{im}\partial_5\) である。
- **Proved at \(n=5\):** \(\omega_5\) の edge images は \(16,12,16,4,12,16\) 次元となり、共通12次元 channel と中央 \(\mathbb H\) channel が \(\mathbb H\otimes\mathbb H\) を直和分解する。
- **Proved at \(n=5\):** 中央 channel は Frobenius 埋込み \(\iota(q)=\sum_\alpha e_\alpha\otimes qe_\alpha\) の像であり、\(\nu=\frac14\iota^*\) が canonical quaternion coordinate を与える。\(12+4\) 分解は直交し、六つの labelled edge の中央成分も閉形式で決まる。
- **Exact-checked at \(n=6,7\):** total local quotient が同型でも、六つの labelled edge images は spectator placement を記憶する。中央区間への挿入は long-edge image から \(\mathbb H\) または \(\mathbb H\otimes V\) を隠す。
- **Exact-checked at \(n=7\):** exceptional \(2\!-!1\!-!2\) residual は、等しい二つの outer-edge images による144次元 core の商として canonical に切り出され、四つの cross edges だけがその \(\mathbb H\) へ全射する。
- **Proved for every odd \(n\ge7\):** odd-odd \(\mid\) even-even support では、adjacent-pair metric collapse の \(+,-,-,+\) square operator が cross-edge matching を消し、cokernel から \(\mathbb H\) への canonical surjection を与える。
- **Proved over \(\mathbb Q\) at \(n=7\):** exceptional \((1,3\mid4,6)\) cross square の cokernel はちょうど \(\mathbb H\) で、閉形式 \(\kappa_{212}\) により完全に検出される。
- **Proved for every even \(n\ge6\):** odd-even-even-odd support では、left/right cap collapse の五辺作用素が matching を消し、cokernel から \(\mathbb H\) への canonical surjection を与える。
- **Proved over \(\mathbb Q\) at \(n=6\):** central-spectator quotient \(Y_{6,(1,2,4,5)}/E_{14}\) はちょうど \(\mathbb H\) で、閉形式 \(\chi_6=(-\lambda^L,+\lambda^L,0,-\lambda^R,+\lambda^R)\) により完全に検出される。
- **Proved over \(\mathbb Q\) at \(n=6\):** outer edge で規格化された一意な48次元 quotient map \(\Omega_6\) が存在し、\(\beta((x\otimes y)\otimes w)=xw\bar y\) に対して \(\beta\Omega_6=\chi_6\) となる。
- **Proved over \(\mathbb Q\) at \(n=6\):** \(\beta\) は \(K_4\otimes V\) を全消去し、long-edge image は \(\ker\beta\) に等しい。central-spectator \(\mathbb H\) は seed \(K_4\) の直積輸送ではなく、直交 channel \(W_{12}\otimes V\) の商から生じる。
- **Proved over \(\mathbb Q\) at \(n=6\):** 五つの spectator placements は direct seed の left/right 二 chart で被覆される。外側 overlap の transition は恒等だが、中央 overlap は閉形式 \(G=\operatorname{id}_{\mathbb H}\otimes\theta\) を持つ。
- **Proved over \(\mathbb Q\) at \(n=6\):** 中央 transition は \(\theta(1\otimes w)=1\otimes w+\sum_a e_a\otimes(e_a\times w)\), \(\theta(a\otimes w)=-w\otimes a\) であり、最小多項式は \((t-1)^2(t+1)\)。seed の \(K_4\otimes V\) / \(W_{12}\otimes V\) channels を非自明に混合する。
- **Open:** tetrahedral generation の all-\(n\) proof、multi-spectator transport、decorated quotient の一般分類、full intermediate filtration、および closed-path transport / curvature との接続。

以下で「生成」という語を線形像・生成元の意味で使う場合を除き、確立している順序は ontological / causal order ではなく **visibility / reconstruction order** である。

## 現在の到達点

- (n=2) の深度1応答空間を、(V^{\otimes2}) を先に置かず内在的に定義した。
- 新しい5次元誕生層 (S^2_0V) と埋込み係数 (-2) を証明した。
- 全有限 (n) の終端 exact-response space を、局所デコーダだけから再帰構成した。
- 固定 (n) の部分深度 response tower、birth layers、有限逆極限、depth ultrametric を構成した。
- (n=2,3,4) の既知の exact checks を dimension-growth profile として読み替えた。
- (n=3,d=1) の20次元空間を、二つの局所応答の fiber product として直接 presentation した。
- 全 (n\ge3) の depth-one 空間を outer-gluing law だけで完全分類した。
- \(n=4,d=2\) の72次元空間を、三つの36次元 pair charts の exact matching kernel として直接 presentation した。
- 40次元 depth-two birth layer を \((V_2\oplus V_3)\oplus(V_0\oplus V_1\oplus V_2\oplus V_3)\oplus(V_2\oplus V_3)\) に局在分解した。
- \(n=4,d=3\) の terminal filling を \(72+9\) の canonical \(SO(3)\)-splitting として閉じ、最高スピン・pair-boundary kernel・terminal birth・pure interior の四重一致を得た。
- 全 \(n\ge2\) で highest spin = terminal boundary kernel = terminal birth = pure interior を証明した。
- 新しい \(n=5\) rung \(232+11=243\) と terminal coefficient \(A_5=16C\) を exact-check した。
- \(n=5\) の232次元 terminal boundary を、四つの108次元 faces と六つの36次元 common shadows の pairwise matching kernel として intrinsic に presentation した。
- \(n=4\) response triangle では消えていた compatibility syzygy が、\(n=5\) response tetrahedron で16次元 \(2V_0\oplus3V_1\oplus V_2\) として初出することを証明した。
- \(n=6\) の716次元 terminal boundary を、五つの324次元 faces と十個の108次元 common shadows の pairwise matching kernel として intrinsic に presentation した。
- response 4-simplex の matching rank 904 と176次元 syzygy \(10V_0\oplus21V_1\oplus15V_2\oplus4V_3\) を二つの素数体上の exact rank certificate から有理数上へ持ち上げた。
- 全 \(n\ge2\) で actual face restrictions を simple slot contractions へ局所的に triangularize し、その Cartan kernel \(S^m_0V\oplus S^{m+1}_0V\) から pairwise terminal descent を証明した。
- \(n=4,5,6\) の個別 exactness を普遍定理の事例へ引き上げ、matching rank・compatible boundary dimension・first syzygy character の全長公式を得た。
- naive な triangle descent が存在しないことを \(n=5\) で確認し、最初の row relation の最小支持が四つの faces であることを切り出した。
- 全 \(n\ge5\) で四面体支持の局所 cokernel を束ねた second differential を構成し、complex identity \(\partial_n^{(2)}\partial_n=0\) を得た。
- \(n=5\) では有理数上、\(n=6,7\) では二素数体上で \(\ker\partial_n^{(2)}=\operatorname{im}\partial_n\) を確認した。
- \(n=7\) で、単純な spectator tensor law を破る exceptional \(2\!-!1\!-!2\) \(\mathbb H\) residual を初めて検出した。
- \(n=5\) の16次元 tetrahedral quotient を quotient basis から解放し、五つの \(SO(3)\)-natural quaternion operators による閉形式 \(\omega_5\) として実現した。
- \(\omega_5\) の内部に \((\mathbb H\otimes V)\oplus\mathbb H\) という \(12+4\) channel decomposition を同定した。
- 中央 channel を \(K_4=\iota(\mathbb H)\) と同定し、\(\mathbb H\otimes\mathbb H=W_{12}\overset{\perp}{\oplus}K_4\) および projector \(P_{K_4}=\frac14\iota\iota^*\) を得た。
- canonical coordinate \(\nu=\frac14\iota^*\) により六つの seed edge の中央成分を \((+\,\frac14uv\bar h,0,-\,\frac14uv\bar h,-\,\frac14uv(\bar h+2h),0,+\,\frac14uv\bar h)\) として完全に書き下した。
- \(n=6,7\) の全四面体支持について、total quotient に加えて六つの labelled edge images の rank と Casimir profile を二素数体上で完全分類した。
- 同じ total \(SO(3)\)-type の背後に spectator placement が edge-incidence data として残ることを検出し、中央挿入の \(\mathbb H\) / \(\mathbb H\otimes V\) defect を分離した。
- exceptional \(2\!-!1\!-!2\) の148次元商を、144次元 outer core と canonical cross-edge quotient \(K_{212}\cong\mathbb H\) に分解した。
- 偶数深度 response の adjacent-pair metric collapse \(\varepsilon_{2r}\) を構成し、odd-before-even の actual common shadows がすべて同じ reverse quaternion product へ落ちる全 \(r\) 恒等式を証明した。
- この parity-collapse から全奇数 \(n\ge7\) の quaternionic square complex を構成し、\(n=7\) では \(3888\to1296\to4\) の exact sequence を有理数上で閉じた。
- 奇数深度 response の left/right cap collapses \(\lambda_{2r+1}^L,\lambda_{2r+1}^R\) を構成し、odd-even / even-odd の actual common shadows を同じ total product へ落とす全 \(r\) 恒等式を証明した。
- この cap-collapse から全偶数 \(n\ge6\) の capped five-edge complex を構成し、\(n=6\) では \(1296\to540\to4\) の exact sequence と central-spectator quotient を有理数上で閉じた。
- central \(n=6\) local quotient を outer block で seed 座標へ一意に規格化し、48次元の \(\Omega_6\) を有理数上で構成した。
- insert-between-and-conjugate contraction \(\beta((x\otimes y)\otimes w)=xw\bar y\) が \(\beta\Omega_6=\chi_6\) を満たし、\(K_4\otimes V\subset E_{14}=\ker\beta\) となる channel transfer を証明した。
- 五つの \(n=6\) spectator placements を direct seed の left/right 二 chart で完全被覆し、全 direct full-edge normalization の存在・非存在を有理数上で分類した。
- 中央 spectator overlap の座標変換を \(G=\operatorname{id}_{\mathbb H}\otimes\theta\) と閉じ、\(\theta\) が involutive reflection と三次元 cross-product shear の和であることを証明した。
- 外側 overlap では \(G=I\)、中央 overlap では \(m_G(t)=(t-1)^2(t+1)\) となること、および cap residual が \(\beta_R\Omega^R=\beta_L\Omega^L\) と chart-independent であることを得た。

## Reading order

0. [`notes/00-checkpoint-through-note12.md`](notes/00-checkpoint-through-note12.md)

   Note 12 までの統合地図。最初に全体と claim boundary を確認するための checkpoint。

1. [`notes/01-n2-intrinsic-response-tower.md`](notes/01-n2-intrinsic-response-tower.md)  
   最小反転定理。深度1の許容条件は「応答の虚部が自己共役」。

2. [`notes/02-all-grade-intrinsic-terminal-response.md`](notes/02-all-grade-intrinsic-terminal-response.md)  
   全 (n) の終端応答空間を ambient state なしに構成する再帰定理。

3. [`notes/03-finite-depth-space-reconstruction.md`](notes/03-finite-depth-space-reconstruction.md)  
   部分深度の塔、誕生層、dimension profile、ultrametric。

4. [`notes/04-n3-depth1-fiber-product.md`](notes/04-n3-depth1-fiber-product.md)  
   二つの12次元局所応答を共通 (mathbb H) 上で貼り、20次元 depth-one space を作る。

5. [`notes/05-n4-depth1-factor-origin-and-outer-gluing.md`](notes/05-n4-depth1-factor-origin-and-outer-gluing.md)  
   left / middle / right の factor origin と (n=4) multiplicity-depth splitting。

6. [`notes/06-all-n-depth1-outer-gluing-theorem.md`](notes/06-all-n-depth1-outer-gluing-theorem.md)  
   局所 zero-compression gadgets による全 (n\ge3) の depth-one direct presentation。

7. [`notes/07-n4-depth2-pair-chart-gluing.md`](notes/07-n4-depth2-pair-chart-gluing.md)

   三つの pair charts の exact matching complex と、40次元 birth layer の \(12+16+12\) 分解。

8. [`notes/08-n4-canonical-terminal-filling.md`](notes/08-n4-canonical-terminal-filling.md)

   compatible pair boundary の一意な \(SO(3)\)-equivariant top-spin-free completion と、terminal interior \(V_4\)。

9. [`notes/09-all-n-terminal-boundary-and-filling.md`](notes/09-all-n-terminal-boundary-and-filling.md)

   adjacent-pair kernel theorem による全 \(n\) last-survivor equality、universal terminal dimension law、canonical filling。

10. [`notes/10-n5-terminal-response-tetrahedron.md`](notes/10-n5-terminal-response-tetrahedron.md)

    四つの terminal faces の intrinsic pairwise gluing、232次元 matching kernel、および16次元 compatibility syzygy。

11. [`notes/11-n6-terminal-response-4simplex.md`](notes/11-n6-terminal-response-4simplex.md)

    五つの terminal faces の intrinsic pairwise gluing、716次元 matching kernel、および176次元 compatibility syzygy。

12. [`notes/12-all-n-pairwise-terminal-descent.md`](notes/12-all-n-pairwise-terminal-descent.md)

    局所 quaternion slide、Cartan kernel、last-face correction による全 \(n\) pairwise descent と普遍 syzygy law。

13. [`notes/13-tetrahedral-second-differential.md`](notes/13-tetrahedral-second-differential.md)

    四面体支持の second differential、\(n=5,6,7\) middle exactness、および \(n=7\) exceptional \(2\!-!1\!-!2\) quaternionic residual。

14. [`notes/14-closed-quaternionic-tetrahedral-operator.md`](notes/14-closed-quaternionic-tetrahedral-operator.md)

    五つの明示的 quaternion operators による \(\omega_5\) の閉形式、tetrahedral exact sequence、および target 内部の \(12+4\) channel decomposition。

15. [`notes/15-spectator-placement-residuals.md`](notes/15-spectator-placement-residuals.md)

    六つの labelled edge images による配置記憶、中央 spectator defect、および exceptional \(2\!-!1\!-!2\) の canonical quaternionic cross-edge quotient。

16. [`notes/16-parity-square-quaternionic-residual.md`](notes/16-parity-square-quaternionic-residual.md)

    adjacent-pair metric collapse、全奇数長の parity-square complex、および \(n=7\) exceptional cross-square cokernel の閉四元数公式。

17. [notes/17-even-length-capped-five-edge-residual.md](notes/17-even-length-capped-five-edge-residual.md)

    left/right cap collapse、全偶数長の odd-even-even-odd complex、および \(n=6\) central-spectator quotient の閉四元数公式。

18. [notes/18-canonical-seed-quaternion-coordinate.md](notes/18-canonical-seed-quaternion-coordinate.md)

    Frobenius 埋込みによる seed \(K_4\) の canonical quaternion coordinate、直交 \(12+4\) 分解、および六辺すべての中央成分。

19. [notes/19-central-spectator-channel-transfer.md](notes/19-central-spectator-channel-transfer.md)

    outer-normalized \(n=6\) quotient、閉 contraction \(\beta(x\otimes y\otimes w)=xw\bar y\)、および \(K_4\otimes V\) から \(W_{12}\otimes V\) への channel transfer。

20. [notes/20-n6-spectator-atlas-and-central-shear.md](notes/20-n6-spectator-atlas-and-central-shear.md)

    五つの spectator placements の二 chart 被覆、中央 overlap の閉 cross-product transition、および reflection-plus-shear decomposition。

## Exact certificate

```bash
python3 certificates/n2_intrinsic_response_certificate.py
python3 certificates/n3_depth1_fiber_product_certificate.py
python3 certificates/depth1_outer_gluing_certificate.py
python3 certificates/n4_depth2_structure_certificate.py
python3 certificates/n4_canonical_filling_certificate.py
python3 certificates/all_n_terminal_boundary_certificate.py
python3 certificates/n5_response_tetrahedron_certificate.py
python3 certificates/all_n_pairwise_terminal_descent_certificate.py
python3 certificates/n5_quaternionic_second_differential_certificate.py
python3 certificates/n5_central_channel_factorization_certificate.py
python3 certificates/n6_response_4simplex_modular_certificate.py
python3 certificates/n7_local_descent_modular_stress.py
python3 certificates/second_response_simplex_differential_certificate.py
python3 certificates/n7_tetrahedral_syzygy_modular_stress.py
python3 certificates/spectator_placement_residual_certificate.py
python3 certificates/n7_exceptional_square_operator_certificate.py
python3 certificates/n6_capped_five_edge_operator_certificate.py
python3 certificates/n6_seed_cap_bridge_certificate.py
python3 certificates/n6_spectator_chart_transition_certificate.py
```

最初の十本は外部ライブラリを使わず、有理数上の完全計算で (n=2) の内在的応答塔、(n=3,d=1) の fiber product、(n=3,\ldots,7) の all-length depth-one formula、\(n=4,d=2\) の exact pair-chart complex、\(n=4,d=3\) の canonical terminal splitting、\(n=2,\ldots,5\) の terminal boundary theorem、\(n=5\) response tetrahedron の pairwise gluing と16次元 syzygy、all-\(n\) descent proof の固定局所恒等式、閉形式 \(\omega_5\) とその \(12+4\) channel decomposition、および seed \(K_4\) の Frobenius factorization と直交 projector を検証する。

NumPy を使う九本は、整数行列の格納と有限体上の行基本変形にだけ用い、浮動小数点計算は行わない。\(n=6\) certificate は \(\mathbb F_{1009}\) と \(\mathbb F_{1013}\) 上で rank 904 を独立に確認し、有理数上の rank 上界と modular minor の下界から \(\mathbb Q\) 上の exactness と176次元 syzygy を証明する。\(n=7\) local descent stress は all-\(n\) proof の代用ではなく、最初の未使用局所次数 \(m=5\) を検査する。second-differential certificate は \(n=5\) を有理数上、\(n=6\) を両素数体上で検証する。\(n=7\) tetrahedral stress は十五の局所商、middle exactness、exceptional \(2\!-!1\!-!2\) residual、および次余核の Casimir 型を両素数体上で検査する。spectator-placement certificate は \(n=6,7\) の全 labelled edge-image profile と canonical outer-core quotient を同じ二素数体上で検査する。exceptional-square certificate は paired collapse と square cancellation を有理数上で確認し、二つの modular minors から cross-square exactness を \(\mathbb Q\) 上へ持ち上げる。capped-five-edge certificate は left/right cap identities を整数上で確認し、二つの modular minors から \(n=6\) central-spectator quotient の exactness を \(\mathbb Q\) 上へ持ち上げる。seed-cap bridge certificate は二素数から同じ \(4\Omega_6\) を復元した後、matching cancellation、\(\beta\Omega_6=\chi_6\)、channel ranks、および \(E_{14}=\ker\beta\) を整数・有理数上で検証する。spectator-atlas certificate は全五配置の direct seed charts を同じ二素数から復元し、非存在側を exact rational rank で排除したうえで、中央 transition の閉形式、最小多項式、channel mixing、および chart-independent cap decoder を整数・有理数上で検証する。

Expected final line:

```text
ALL CHECKS PASSED
```

## Next target

pairwise terminal descent は全 \(n\) で成立し、tetrahedral second map も構成された。さらに Note 14 で、最小局所商は quotient basis なしの閉四元数写像

\[
\omega_5:\mathcal R_2^{\oplus6}
\longrightarrow\mathbb H\otimes\mathbb H,
\qquad
\ker\omega_5=\operatorname{im}\partial_5
\]

として解決した。Note 15 は、placement-blind な spectator tensor law では不十分であることを edge-image incidence から示した。次の主標的は、五つの primitive operators に order-sensitive slide/correction を加え、\(n=6,7\) の全 decorated local quotients

\[
\mathscr Y_{n,Q}
=
\left(Y_{n,Q};E_{12},E_{13},E_{14},E_{23},E_{24},E_{34}\right)
\]

を同じ placement-aware transport law から回収することである。

Note 16 は exceptional spacing \((2,1,2)\) の cross-edge quotient を、paired collapse

\[
\varepsilon_4(F)=\sum_{a,b}F(e_a,e_a,e_b,e_b)
\]

の alternating square \(\kappa_{212}\) として有理数上で閉じた。さらに odd-odd \(\mid\) even-even support へ同じ構成が全奇数長で伸びる。Note 17 は \(n=6\) central-spectator quotient を left/right cap collapse \(\chi_6\) として有理数上で閉じ、odd-even-even-odd support へ全偶数長で伸ばした。Note 18 は seed channel を \(K_4=\iota(\mathbb H)\) と固定し、\(\nu=\frac14\iota^*\) によりその canonical quaternion coordinate と全 edge-incidence pattern を与えた。

Note 19 は最初の一観客比較を閉じた。central support では一意な outer-normalized quotient \(\Omega_6\) が存在し、

\[
\beta((x\otimes y)\otimes w)=xw\bar y,
\qquad
\beta\Omega_6=\chi_6.
\]

しかし \(\beta(K_4\otimes V)=0\) であり、\(K_4\otimes V\subset E_{14}=\ker\beta\) となる。したがって cap residual は seed \(K_4\) の直積輸送ではなく、\(W_{12}\otimes V\) の商から生じる。

Note 20 は全五配置を left/right direct-seed charts で覆い、その overlap transition を完全に閉じた。外側 overlap は恒等だが、central spectator では

\[
G=\operatorname{id}_{\mathbb H}\otimes\theta,
\qquad
\theta(1\otimes w)=1\otimes w+\sum_a e_a\otimes(e_a\times w),
\qquad
\theta(a\otimes w)=-w\otimes a
\]

となる。\(m_G(t)=(t-1)^2(t+1)\) であり、これは単なる slot permutation ではなく三次元 nilpotent shear を含む。残る核心は、\(\Omega_6\) 全ブロックの短い primitive formula、二人目の spectator がこの transition を \(n=7\) parity square へどう運ぶか、および複数経路の閉比較である。これが成立すれば、response-simplex complex

\[
C_n^0\xrightarrow{\partial_n}C_n^1
\xrightarrow{\partial_n^{(2)}}C_n^2
\]

の middle exactness を全 \(n\) へ上げるための local transport law が得られる。

Casimir complement 上の逆写像として得られた canonical section の短い response-side 局所公式も引き続き open である。

その後で、response simplex に四元数値 transport を加えたときの path nonconfluence residual と curvature 候補を検討する。
