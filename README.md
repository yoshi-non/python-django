# PythonでのDjangoの環境構築

- pythonの仮想環境構築

- Djangoの環境構築

# pythonの仮想環境構築

※デスクトップ下で構築するとツリーでデスクトップという文字列でpipコマンドなどが打てない恐れがあるためCドライブ直下のフォルダなどで行うことを推奨。

※Windowsのみpython3コマンドをpythonまたはpyと省略可能

## プロジェクト用の仮想環境作成

```
py -m venv <仮想環境ディレクトリ>
```

ここでは.venvという仮想環境を作成。

## 仮想環境に入る (activate)

```
// ↓ターミナルの場合
.venv/Scripts/activate.bat

// ↓powershellの場合
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
(.venv) > deactivate
```

## 参考資料

https://maku77.github.io/python/env/venv.html

https://zenn.dev/nekocodex/articles/eb3403961ad9b966ff6e

# Djangoの環境構築

## Djangoのインストール

```
// ↓最新のバージョン
(.venv) > pip install django

// ↓今回使用するバージョン
(.venv) > pip install django==3.2.7
```

## ドライバのインストール

PythonからPostgreSQLに接続するためのドライバ「psycopg2」をインストール

```
(.venv) > pip install psycopg2-binary==2.9.1
```

## Djangoプロジェクトの作成

```
(.venv) > cd .venv

(.venv) .venv > django-admin startproject <プロジェクト名>
```

ここではprivate_diaryというプロジェクトを作成。

## Djangoアプリケーションの作成

```
(.venv) .venv > cd private_diary

(.venv) .venv/private_diary > python manage.py startapp diary
```

## Djangoアプリケーションの作成(ファイル編集)

.venv/private_diary/private_diary/settings.py

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'diary.apps.DiaryConfig' # <-ここを追加
]
```

DiaryConfigは.venv/private_diary/diary/apps.pyのDiaryConfigクラスを指しています。　

## 言語とタイムゾーンを日本仕様に変更

.venv/private_diary/private_diary/settings.py

```py
LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
```
