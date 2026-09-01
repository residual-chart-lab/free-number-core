# Depth-Generated Geometry — Research Notes

> 作業仮説：空間が深度を許すのではなく、関係深度が空間を紡ぐ。

自由数の probe-depth filtration から、depth-gated observability を独立した代数幾何プログラムとして切り出す研究ノート群。

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
- **Open:** terminal boundary image の \(n\ge6\) intrinsic presentation、canonical filler 自体の短い局所公式、および transport / curvature との接続。

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

## Reading order

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

## Exact certificate

```bash
python3 certificates/n2_intrinsic_response_certificate.py
python3 certificates/n3_depth1_fiber_product_certificate.py
python3 certificates/depth1_outer_gluing_certificate.py
python3 certificates/n4_depth2_structure_certificate.py
python3 certificates/n4_canonical_filling_certificate.py
python3 certificates/all_n_terminal_boundary_certificate.py
python3 certificates/n5_response_tetrahedron_certificate.py
```

外部ライブラリを使わず、有理数上の完全計算で (n=2) の内在的応答塔、(n=3,d=1) の fiber product、(n=3,\ldots,7) の all-length depth-one formula、\(n=4,d=2\) の exact pair-chart complex、\(n=4,d=3\) の canonical terminal splitting、\(n=2,\ldots,5\) の terminal boundary theorem、および \(n=5\) response tetrahedron の pairwise gluing と16次元 syzygy を検証する。

Expected final line:

```text
ALL CHECKS PASSED
```

## Next target

次は、\(n=4,5\) で成立した pairwise terminal descent

\[
\mathcal P_{n,n-2}
\stackrel{?}{=}
\ker\partial_n
\]

を \(n=6\) で exact-check する。成立する場合の checkpoint は

\[
\operatorname{rank}\partial_6=904,
\qquad
\dim\ker\partial_6=716,
\qquad
\dim\operatorname{coker}\partial_6=176.
\]

その後、pairwise descent の all-\(n\) 証明、または最初に失敗する長さでの higher gluing obstruction を切り出す。並行して、\(n=5\) の16次元 syzygy を quotient 定義によらない局所 higher differential として書き下す。

Casimir complement 上の逆写像として得られた canonical section の短い response-side 局所公式も引き続き open である。

その後で、response simplex に四元数値 transport を加えたときの path nonconfluence residual と curvature 候補を検討する。
