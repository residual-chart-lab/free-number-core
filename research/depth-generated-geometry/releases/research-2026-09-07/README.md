# Depth-Generated Geometry — Research Snapshot 2026-09-07

## 公開単位として固定した内容

自由数の研究系列に置く、独立した数学稿と再現資料です。
Core v1.0.0の凍結内容・版番号・DOIは変更しません。
2026-09-07に独立したZenodoプレプリントとして公開しました。

本文：**Ordered Quaternionic Response Quotients: Flat Cores, Local Residuals,
and a Three-Spectator Descent Obstruction**。
著者表記は既存成果物と同じ **Residual Chart Lab**。
公開版名は `research-2026-09-07-audit1`。

| 項目 | 公開情報 |
|---|---|
| 公開ページ | [Zenodo record 22646591](https://zenodo.org/records/22646591) |
| この版のDOI | [10.5281/zenodo.22646591](https://doi.org/10.5281/zenodo.22646591) |
| DGGの全版共通DOI | [10.5281/zenodo.22646590](https://doi.org/10.5281/zenodo.22646590) |
| 公開日 | 2026-09-07 |
| ライセンス | MIT |
| 元履歴のソースタグ | `dgg-research-2026-09-07-audit1` |
| 公開ZIPのソースコミット | `b9ec03f3e9788b41ba1a560e299407b388db41e1` |
| 同一内容のGitHubソース | [`110113dd`](https://github.com/residual-chart-lab/free-number-core/tree/110113dd763da371bb6e02c6c5083b40dd12aecc) |

## 読む順番

1. `AUDIT_REPORT.md` — 監査結果と修正箇所。
2. `manuscript/ordered-quaternionic-response-quotients.pdf` — 独立読解稿。
3. `CLAIMS_LEDGER.md` — 定理、指定条件、有限体検算、未解決問題の境界。
4. `REPRODUCIBILITY.md` — 実行手順と、今回検証した範囲。
5. [`Note 26`](../../notes/26-n8-222-residual-redetection.md) — 最新結果の詳細。展開したZIPでは `notes/26-n8-222-residual-redetection.md`。

本文は四元数、応答、局所制限、商空間を定義してから、種の四面体、
一観客のchart、二観客の平坦なコア、222の残差接続へ進みます。
自由数全体の理論やタイムエンジンの理解を前提にしません。

## 今回の監査

主定理の数値は維持しました。共有辺から残差を捨てる写像の選択条件、
例外点の共有面にある4次元の核、デコーダ前後の写像の定義域を明記しました。
検証コードはキャッシュ利用時も対応行列のランクを再計算します。
別実装の四元数積と第三の素数1019でも、新結果と三つの親を照合しています。
再実行の範囲・ログは監査記録に示します。

## 終点

222で444次元の商、432次元の外側コア、12次元の残差商を得ます。
指定した中央スロット右デコーダでは、親212の4次元残差を全て読み戻せます。
しかし同じ操作の全体輸送は成立せず、その障害の像は432次元コア全体です。
この成立範囲と非成立範囲までを、今回の閉じた結果として固定しました。

## 同梱範囲

- 数学稿のPDF・Markdown・LaTeX、組版設定。
- Notes 00–26、既存の独立読解稿、全DGG検証コード。
- 主張台帳、再現手順、今回の検証ログ・環境・結果。
- 公開説明文、著者・版・関連DOIを含む公開準備時のメタデータ草案。
- MITライセンス、来歴情報、ファイル一覧とSHA-256チェックサム。

過去ノートは導出履歴として保持しています。主張の現時点の境界は
本文とCLAIMS_LEDGERを優先してください。古いNext targetは当時の記録です。

## 公開記録と引用

DGGは独立したZenodoレコードです。
Coreのversion DOI `10.5281/zenodo.21328471` を `References` として関連付けています。
[`ZENODO_METADATA.json`](ZENODO_METADATA.json) に公開設定、公開ファイルのサイズ・
チェックサム、ソースコミットを記録しています。
[`ZENODO_DESCRIPTION.md`](ZENODO_DESCRIPTION.md) は公開ページの説明文です。

```text
Residual Chart Lab. (2026). Depth-Generated Geometry: Ordered Quaternionic Response Quotients, Flat Cores, and Residual Descent (research-2026-09-07-audit1) [Preprint]. Zenodo. https://doi.org/10.5281/zenodo.22646591
```

機械可読の引用情報は [`CITATION.cff`](CITATION.cff) にあります。

## 公開ZIPと現在のGitの関係

ZenodoのPDF・ZIP・監査報告書は、上記のソースコミットで固定したファイルです。
ZIP内のREADME・引用情報・メタデータ草案は公開準備時の記録を保持しています。
公開ページの研究ナビゲーションは、その後のコミット `32c38d7` で追加しました。
2026-09-08のDOI追記はGit側の案内・引用情報の更新であり、数学稿や証明コードの改版ではありません。

GitHub接続経由の転送ではコミット番号が付け直されるため、GitHub側の
`110113dd763da371bb6e02c6c5083b40dd12aecc` を取得用の参照にしています。
元のコミットとこのコミットのGit treeは、どちらも
`24dd03c1f118752f5a08914076a7669055acbd9b` であり、ファイル内容は完全に一致します。
元のコミット履歴とタグは復元用Git bundleに保持しています。タグのGitHubへの直接転送は保留です。

公開済みZIPのSHA-256は次のとおりです。

```text
752a5894768d2f25b642f354fd7e2cd63abab5532d2f08af1fe67b9d2d989400
```
