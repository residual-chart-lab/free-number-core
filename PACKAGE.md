# 配布物について

この配布物は、自由数Coreへ追加する**要求依存実行層v0.1.1と、その検証一式**。既存リポジトリの論文・DGG・PDFを全て含むものではない。既存の文書へのroot READMEのリンクは、GitHubのリポジトリ上で参照できる。

このフォルダだけでも、Python 3.10以上・標準ライブラリで実行層を検証できる。

```text
python runtime/validate.py
```

入口は[runtime/README.md](runtime/README.md)、監査手順は[research/demand-runtime-v001/AUDIT.md](research/demand-runtime-v001/AUDIT.md)。TEとの任意照合には、監査手順にある固定TE checkoutを別途用意する。

Coreの基礎となる4文書と固定コミットは[来歴](research/demand-runtime-v001/SOURCE.json)へ記録する。Core v1.0.0の凍結タグは変更しない。今回のコードはMIT LICENSE。
