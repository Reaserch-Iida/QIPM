# QIPM
Quantum Interior Point Methods for solving a variety of convex optimization problems such as LO, SDO and so on.

You need to install the following Python packages before installing ipm:
numpy 1.20.1 qiskit ~~0.18.3~~必要なAPIが揃っていないバージョン. 現行は `pyproject.toml` 参照 scipy 1.6.1 setuptools 49.2.1

Please make sure that you are installing the correct version!

---
## Set up
`poetry` を使用するためインストールが必要

### パッケージインストール
#### プロジェクトのディレクトリ配下に仮想環境を作成するようにする
```
poetry config virtualenvs.in-project true
```

プロジェクトの root 配下に `.venv` ディレクトリが作成され, 仮想環境にかかわるファイルはそこへ格納されるようになる

#### 開発環境
```
poetry install
```

#### 本番環境
```
poetry install --no-dev
```

## テスト
```
poetry run pytest
```

### テストの対象関数
`test_*.py` のファイルにある `test_*`という形式のメソッド.
テストを追加する際は上記の形式

### 処理の遅いテストを実行する場合
```
poetry run pytest -m slow
```

### すべてのテストを実行し, カバレッジを測定する
```
poetry run pytest -v --cov=src/
```

## 仮想環境関連
### パッケージインストール
```
poetry add <module> {--dev}
```

`pyproject.toml` に書き込みが行われるので, commit すること

### 現在の `pyprofect.toml` もとに更新
```
poetry update --no-dev
```

開発環境であれば `--no-dev` を消す

### 削除
```
poetry env remove .venv
```

install で原因不明のエラーが起きたときとかに再セットアップするため
