# 日記アプリ

- diary : アプリケーションフォルダ
  - templates
    - base.html : 全体レイアウト
    - index.html : ホームページ(未ログイン)

- private_diary : プロジェクトフォルダ

- static : 静的ファイル
  - assets
    - img : 画像フォルダ
  - css
    - base.css : base.html用のcss
    - index.css : index.html用のcss

- manage.py : サーバ起動用ファイル

※CSS設計規則はBEMを使用しています。

# 目次

- 静的ファイルが配置されている場所の設定

## 静的ファイルが配置されている場所の設定

static/cssフォルダを作成し、settings.pyに静的ファイルの配置場所を追加する。

private_diary/settings.py

```py
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```

## レイアウトの継承

staticタグを使えるようにする。

```
{% load static %}
```

```
<!-- 継承されるファイル -->
{% extends '継承するファイル名' %}
{% block ブロック名 %}

<header>
    <div>
        <h1>Private Diary</h1>
        <h2>あなた専用の日記保存サービス</h2>
        <a href="/">LOG IN</a>
    </div>
</header>

{% endblock %}

<!-- 継承するファイル -->
{% block ブロック名 %}{% endblock %}
```