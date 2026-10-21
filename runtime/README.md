# Free Numbers — 要求に応じて残差を読む実行層 v0.1.1

Free Numbers Core v1.0.0を土台に、保持した差を必要な範囲だけ読むためのPython実装を加える。Coreの凍結版・定理・等値関係は変更しない。

今回加える機能は三つ。

1. **要求から残差へ引き戻す。** 登録済みの観測・演算について、保持パラメータへの完全な多項式依存を作る。混合項と同じ残差の反復使用を含める。
2. **観測の深さと数値精度を分ける。** 深さ不足、証明予算不足、数値精度不足を別々の未判定として返す。合否の問いは外向き区間で決まれば精査を止め、厳密な値の問いは必要なパラメータだけ読む。
3. **差を保持して合成・保存する。** 順序付き生成式を共有DAGとして保持する。今の観測で読まない差も消さず、後の観測へ持ち越す。保存には原本の有理数も含める。

## 実行

Python 3.10以上、標準ライブラリのみ。インストールは不要。

```text
python runtime/validate.py
```

当初の29件とAstra監査の回帰11件、計40テストと主実験9群を実行し、`.work/demand-runtime-validation/`へ新しい結果を書く。公開済みの検証記録は上書きしない。

TEとの任意の照合も含める場合は、固定したTEのcheckoutを用意する。

```text
git clone https://github.com/residual-chart-lab/time-engine.git ../time-engine
git -C ../time-engine checkout --detach 5e0b40871ccda4f0bbf2b6d49b6a9c62d0580bd8
python runtime/validate.py --time-engine ../time-engine
```

TEの259ファイルをGit blobハッシュへ照合し、追加9群を実行する。TEの実装・認証・元記録は編集しない。3+1を再学習しない。

## 入口

```python
from fractions import Fraction as Q
from free_numbers import *

vault = Vault()
zero = block(2, ())
direction = matrix_block(((1,0,0), (0,-1,0), (0,0,0)))
x = retained(vault, 'r', Q(1,3), (-1,1), 'source-receipt', zero, direction)
scope = Scope('entry', 'declared-continuation', 'compression')
proof = evaluate(Query(read(x), scope), vault)
assert proof.value == ZERO  # rを読まずに、指定した応答が0だと分かる。

later = Observation(2, (Channel(((1,0,0),)),))
query = Query(read(x,later), Scope('entry', 'later-continuation', 'insertion'))
assert plan(query,vault).dependencies == ('r',)
assert evaluate(query,vault).value != ZERO
```

このコードを利用するプログラムからは`runtime/`をPythonの検索パスへ加える。`pip install .`でも利用できるが、再現検査に追加パッケージは要らない。

## 保証の読み方

- `Scope`は、実際に構成した有限の観測・継続についての指定。未知の全未来を自動的に量化するものではない。
- `Plan.dependencies`は、観測値の**形式的な依存先**。与えられた許容誤差や特定の値で、その全ての精査が必須とは限らない。最小集合を求めたという主張もしない。
- `within-l1`の成功証は、数値の作用やTEセル昇格を許可しない。`exact-value`は別の問い。
- `assess_replacement`の`REPLACEABLE_IN_SCOPE`は、指定した読出しで代表を使えるという保証。原本・差・履歴の消去許可を返す操作はない。
- `verify_certificate`は元の問い・保持参照・規則で証拠を再計算する。保存や検証が無償であるとは主張しない。
- `checkpoint.loads`には外部から信頼したSHA-256を渡す。自己申告されたハッシュは作者認証にならない。

[設計・保証範囲](../research/demand-runtime-v001/DESIGN.md) ／ [Astra向け監査手順](../research/demand-runtime-v001/AUDIT.md)

## Astra監査への補修：v0.1.1

保存と復元は共通の`CheckpointLimits`を使う。既定値はnode 10,000、保持参照10,000、20,000,000 bytes。超過時は保存成功を返さない。上限を変更する場合は同じ設定を保存・復元の両方へ渡す。未使用参照は削除しない。

```python
from free_numbers.checkpoint import CheckpointLimits, dumps, loads
limits = CheckpointLimits(max_references=12000)
payload, trusted_hash = dumps(roots, vault, limits)
restored_roots, restored_vault = loads(payload, trusted_hash, limits)
```

コンパイルとDAG走査は明示的なstackを用いる。生成式の鎖長を観測深さと混同せず、Pythonの再帰設定を変更しない。整数の十進変換は9桁以下の塊で行い、Python全体の十進変換制限を変更しない。[修正記録と再検証結果](../research/demand-runtime-v001/repairs-2026-10-21/REPAIR.md)。
