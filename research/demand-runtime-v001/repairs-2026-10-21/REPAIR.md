# Astra監査の三点への補修 — 実行層 v0.1.1

対象PR：[#13](https://github.com/residual-chart-lab/free-number-core/pull/13)。初回対象コミット：`f7837c4e3a1fa3ef095da2bad59ae59ff10a9ea0`。

監査原文：[Astraの記録と再現コード](https://github.com/residual-chart-lab/free-number-core/blob/audit/pr13-astra-2026-10-21/research/demand-runtime-v001/astra-audit-2026-10-21/REVIEW.md)。原文の再現コードを変更せずに初回版へ実行し、三点とも再現した。監査ブランチと初回の検証記録は変更しない。

## 1. 保存・復元の上限を共有する

`CheckpointLimits`を導入し、両側が同じnode数・保持参照数・byte数を検査する。既定値はそれぞれ10,000、10,000、20,000,000。上限を超える場合、保存時点で`ValueError`とし、成功した保存物を返さない。未使用参照を捨てて回避しない。

参照9,999件と10,000件は保存・復元・再出力が一致する。10,001件は既定の保存時点で拒否する。両側へ`CheckpointLimits(max_references=10001)`を渡せば、10,001件全てを保持したまま保存・復元できる。異なる小さな読込予算を指定した場合の拒否は明示的な仕様。

node数とbyte数も上限直前・一致・直後の境界を同じ規則で検査する。nodeとbyteの回帰検査には小さな明示予算を使い、境界の不等号を照合する。

## 2. 生成式の処理を反復走査にする

`Compiler.tensor`と`Compiler.circuit`を明示的なstackで計算する。保存・復元のトポロジカル走査も反復処理へ置き換える。四元数の積の順序、隙間の分割、共有キャッシュを維持する。

Astraの1,201 circuit nodeの加算鎖が、既定予算で厳密に1,201へ評価され、保存・復元できる。同じ長さのテンソル加算鎖と、1,201個の順序付き因子の連結も照合する。`Policy(max_nodes=1000)`では未判定、保存予算1,000では明示的拒否となる。観測深さを増やしたり、Python全体の再帰上限を引き上げたりしない。

## 3. 大きな整数を環境共通のcodecで扱う

整数の十進化と読込みを9桁以下のchunkで行う。有理数の既約性、分母の正符号、先頭0や`-0`の拒否を維持する。計算・digest・保持参照・checkpointは同じcodecを使う。通常の`q`表現を維持し、丸めで回避しない。

16共有nodeの15回自乗で`2**32768`を正確に計算し、Plan・証拠digest・保存・復元を確認する。さらに、分子40,001 bit・分母33,001 bitの入力から正確な有理数を保持し、未使用の負の参照も一緒に保存する。十進上限4,300の別プロセスで復元・exact評価・再保存が一致する。下限640の別プロセスでも共通codecのbytesが一致する。再帰・整数変換のグローバル設定を変更しない。

## 再検証

```text
python runtime/validate.py --time-engine ../time-engine
```

TEは初回と同じ`5e0b40871ccda4f0bbf2b6d49b6a9c62d0580bd8`へ固定する。当初29テスト＋回帰11件＝40テスト、主実験9群＋TE接続9群＝18群。

新しい記録は本ディレクトリの`validation.json`・`validation.log`・`COMPATIBILITY.json`。初回の`study.json`と`te-bridge.json`は保存版とのバイト比較を行う。初回結果を別の数値へ置き換えない。

三点の補修後も、依存先は形式的な依存先、置換可能性は指定Scopeの読出し保証として扱う。TEの実行・セル認証や、自由数Coreの凍結版は変更しない。mainへは統合せず、修正版を同じdraft PRへ追加して再監査できる形にする。
