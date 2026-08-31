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
- **Open:** terminal response による response triangle の filling law、および transport / curvature との接続。

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

## Exact certificate

```bash
python3 certificates/n2_intrinsic_response_certificate.py
python3 certificates/n3_depth1_fiber_product_certificate.py
python3 certificates/depth1_outer_gluing_certificate.py
python3 certificates/n4_depth2_structure_certificate.py
```

外部ライブラリを使わず、有理数上の完全計算で (n=2) の内在的応答塔、(n=3,d=1) の fiber product、(n=3,\ldots,7) の all-length depth-one formula、\(n=4,d=2\) の exact pair-chart complex を検証する。

Expected final line:

```text
ALL CHECKS PASSED
```

## Next target

次は \(n=4,d=3\) の terminal all-gap response から三つの pair charts への face maps を明示し、depth-indexed response triangle の filling law を調べる。

その後で、response simplex に四元数値 transport を加えたときの path nonconfluence residual と curvature 候補を検討する。
