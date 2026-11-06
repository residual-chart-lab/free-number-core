# 一般証明束 F01 訂正監査・最終判定

監査者: Astra / 2026-11-06

**判定: PASS_UNDER_STATED_HYPOTHESES。F01（P2）は解消済み。**

前回の主16項目・二追補に対する独立監査と、今回の一段落の訂正を組み合わせた最終判定である。今回新たに主16項目全体を再監査・再実行したという意味ではない。原本の旧版へ遡ってPASSを与えない。

## 対象と版の組合せ

リポジトリ: 非公開 `[original research workspace]`。

- 主束: `698cc1cd500b3f4c8cd05e1d50c861c6e0b437a3`、`2026-11-06-general-proofs-draft1/`。
- T03追補: `b0e0d181863412dc5f5c42450382af0ed3e26a4a`、`2026-11-06-general-proofs-draft1-extra/04_IMAGINARY_GAPS_EN.md`。
- T08追補: `8a6f918659a4c4ed7b6b331306cec29cfa655d38`、同extraの `05_LINE_DIMENSION_CLASSIFICATION_EN.md`。
- 今回の置換本文: `3bd56721a8eb53965ed44e124d171a68351f5620`、`2026-11-06-general-proofs-correction-v0.1/02_SPECTRAL_TRANSPORT_EN.md`。

上記提出はすべて `original-submissions/ronnie/` 以下。主束の `study/02_SPECTRAL_TRANSPORT_EN.md` を今回の置換本文に差し替えた組合せを対象とする。

前回監査: commit `86414fc13581b95ae34c8f821615542a8df4f487`、`original-submissions/astra/2026-11-06-general-proofs-audit-v0.1/`。その報告・未実施事項・証明と有限検査の区別を引き継ぐ。

## 変更範囲の確認

旧新本文をUTF-8バイトから比較した。変更はT08主証明直後の一段落の置換だけで、T07–T12の主証明と残りの本文は一致する。差分は `VERIFIED_DIFF.patch` に保存。

- 旧本文SHA-256: `4b77cf1cb037a9b1dc04521c431a0dc37b828e3bd650954c1f2179b90e13ff0f`
- 訂正本文SHA-256: `3fe2ac101634d584fe8dd26c6f75087fa869d590a56355304d8cf340db9c79e5`
- 訂正本文Git blob SHA: `8422979b3a9f0c771befc7edadb06086ce0817c6`

いずれもCORRECTION.jsonと一致。同梱exact.pyは旧版とバイト一致。今回の固定commitにある旧draft1のchecker.pyも取得し、前回監査版と一致するblob SHA `2316a2d4fd56a1f1a5f0ae72e868c375b1d4d946` を確認した。

## 数学的確認

三次元の非等方単軸行列 `S=λ₂I+aP`、`P²=P`、`tr(P)=1`、`a≠0` について、中心化により

`S₀=S−tr(S)I/3=a(P−I/3)`。

P−I/3の固有値は2/3, −1/3, −1/3だから、

`tr(S₀²)=2a²/3>0`、`tr(S₀³)=2a³/9`。

従って `3tr(S₀³)/tr(S₀²)=a`。正負両方のaに成立し、任意の等方シフトと直交座標変換にも依存しない。有理Sなら中心化と非零分母の商は有理演算で完結する。跡なし領域ではS₀=Sとなる。

等方SではS₀=0となり商は未定義。訂正文はこの点を明示的に除外し、T08の等方分岐へ戻している。定義域の穴は解消された。主たる一意性証明の前提を強めたり弱めたりしていない。

F01の反例 `diag(2,1,1)` は、旧式が5、修正式が正しい振幅1を返す。今回のPASSは非等方単軸という前提付きであり、この商を任意の三軸行列の振幅判定器と認定するものではない。

## 今回実行した有限検査

Python 3.12.14 / Linux x86_64、標準ライブラリーのみ。訂正フォルダーの構成を保った作業用コピーで次を実行した。

`python -I -B source/extensions/centered_amplitude_checks.py --out CENTERED_AMPLITUDE_RESULTS.json`

正負振幅・等方シフト・有理回転の36ケース、等方4ケース、F01反例がすべて通過。出力は同梱 `run/CENTERED_AMPLITUDE_RESULTS.json` とバイト一致した。計算はFractionによる厳密有理数演算。

今回の一般式の妥当性は上記のトレース恒等式で判断した。有限ケース数を一般証明の根拠に置き換えていない。主束の29検査と前回の独立53確認は今回再実行しておらず、前回監査の証拠として参照する。

## 最終判定の範囲

| 対象 | 最終判定 |
|---|---|
| T01–T16、T08の一段落を今回の訂正文へ置換 | 明記された前提下でPASS |
| T03純虚プローブ追補 | 前回PASS維持 |
| T08全次元rank-one分類追補 | 前回PASS維持 |
| F01 | CLOSED_VERIFIED |

この組合せについて、今回の監査で未解消の修正必須事項はない。証明支援系による形式認証、物理的実証、文献上の新規性・優先権の認定ではない。今後組み直される最終ZIP等はまだ取得していないため、その梱包の同一性は別確認となる。
