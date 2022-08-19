# 自分用コマンド
```
.venv/Scripts/Activate.ps1

cd .venv/private_diary

python manage.py runserver
```

# PythonでのDjangoの環境構築

- pythonの仮想環境構築
  - プロジェクト用の仮想環境作成
  - 仮想環境に入る (activate)
  - 仮想環境から抜ける (deactivate)
  - 参考資料

- Djangoの環境構築
  - Djangoのインストール
  - ドライバのインストール
  - Djangoプロジェクトの作成
  - Djangoアプリケーションの作成
  - Djangoアプリケーションの作成(ファイル編集)
  - 言語とタイムゾーンを日本仕様に変更
  - Djangoのデータベース設定をPostgreSQLに変更
  - ロギングの設定(欲しい方のみ)
  - ルーティングの設定
  - ビューの作成
  - テンプレートの作成
  - サーバの起動

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

## Djangoのデータベース設定をPostgreSQLに変更

.venv/private_diary/private_diary/settings.py

```py
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'private_diary',
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '',
        'PORT': '',
    }
}

「NAME」は接続するデータベース名です。
```

## ロギングの設定(欲しい方のみ)

※デフォルトだとコンソールに最低限のログ出力しかされないためここでは設定を行う。

| 用語 | 役割 |
|:-----------------|:------------------|
| ロガー | ログのエントリーポイント |
| ハンドラ | ログの出力先の設定 |
| フォーマッタ | ログの出力形式を設定 |


| ログレベル | 用途 |
|:-----------------|:------------------|
| DEBUG | 開発時のデバッグ用 |
| INFO | 正常処理の記録用 |
| WARNING | 想定外処理の記録用 |
| ERROR | CRITICALほどではないエラーの記録用 |
| CRITICAL | システムダウンクラスの重大問題用 |

.venv/private_diary/private_diary/settings.py

```py
# ロギング設定

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 既存ロガーを無視する

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'diary': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # コンソールに出力させる
            'formatter': 'dev',
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        },
    },
}
```

## ルーティングの設定

ここではdiaryアプリケーション用とトップページ用のルーティングを設定する。

### diaryアプリケーション用

.venv/private_diary/private_diary/urls.py

```py
from django.contrib import admin
from django.urls import path, include # <- ここを変更

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')), # <- ここに追加
]
```

### トップページ用

diaryディレクトリにurls.pyを作成し以下の内容を記載する。

.venv/private_diary/diary/urls.py

```py
from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]
```

## ビューの作成

diaryに自動作成されているviews.pyの中身を以下のものに書き換える。

.venv/private_diary/diary/views.py

```py
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "index.html"
```

## テンプレートの作成

diaryにtemplates/index.htmlを作成

※現段階では「Hello World」を表示させるだけです。

.venv/private_diary/diary/templates/index.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>トップページ</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```

## サーバの起動

サーバの起動ですがまだPostgreSQLと接続していないためsettings.pyのデータベースをコメントアウトする必要があります。
サーバの起動確認のため一時的なコメントアウトです。

.venv/private_diary/private_diary/settings.py

```py
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'private_diary',
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': '',
#         'PORT': '',
#     }
# }
```

以下コマンドで http://127.0.0.1:8000/ に開発用サーバを起動できます。

```
(.venv) .venv/private_diary > python manage.py runserver
```

![hello-world](https://user-images.githubusercontent.com/83369665/184890668-290ba987-52fd-4164-b75b-23d7a053d8c8.png)

この画面が出れば成功です。