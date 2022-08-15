# PythonでのDjangoの環境構築

- pythonの仮想環境構築

# pythonの仮想環境構築

※Windowsのみpython3コマンドをpythonまたはpyと省略可能

## プロジェクト用の仮想環境作成

```
py -m venv <仮想環境ディレクトリ>
```

ここでは.venvという仮想環境を作成。
作成したらgitignoreに.venvを入れておくとよい。

## 仮想環境に入る (activate)

```
//↓ターミナルの場合
.venv/Scripts/activate.bat

//↓powershellの場合
.venv/Scripts/Activate.ps1
```

※vscodeで仮想環境に入る場合はF1を押してsettingsと入力して基本設定:ユーザ設定を開く(JSON)を選択して、settings.jsonの中に以下のものを記載する必要がある。

```json
{
    "terminal.integrated.env.windows": {
        "PSExecutionPolicyPreference": "RemoteSigned"
    }
}
```

## 仮想環境から抜ける (deactivate)

```
(.venv) PS deactivate
```

## 参考資料

https://maku77.github.io/python/env/venv.html

https://zenn.dev/nekocodex/articles/eb3403961ad9b966ff6e

