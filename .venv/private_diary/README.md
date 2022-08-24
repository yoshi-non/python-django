# 日記アプリ

- accounts : ユーザー認証フォルダ
- backup : 日記データのバックアップフォルダ(gitignore)
- diary : 日記アプリケーションフォルダ
- media : 投稿画像保存フォルダ(gitignore)
- private_diary : プロジェクトフォルダ(ルーティング設定、環境設定など)
- static : 静的ファイル(画像、CSSなど)
- manage.py : サーバ起動用ファイル
- .env : private_diary/settings.pyには載せられないKEYや環境変数

※動かして学ぶ! [Python Django開発入門第2版](https://www.amazon.co.jp/%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E5%AD%A6%E3%81%B6-Python-Django%E9%96%8B%E7%99%BA%E5%85%A5%E9%96%80-%E7%AC%AC2%E7%89%88-NEXT/dp/479817419X)を参考に作ったアプリケーションになります。

# アレンジで変更した点

- CSSはBootStrapではなくCSS設計規則のBEMを使用
- os.environの環境変数はdjango-environを使用し.envに記載
  - 参考記事 : https://e-tec-memo.herokuapp.com/article/172/

# 遭遇したエラーの解決法

- Staticフォルダが読み込まれないエラー
- seleniumのバージョンによるエラーの解決法

## Staticフォルダが読み込まれないエラー

DEBUG = Falseになっていると読み込まれないのでTrueにする

## seleniumのバージョンによるエラーの解決法

```
pip install selenium==4.1.0
```

参考記事 : https://qiita.com/syoshika_/items/288fc8bf552672589f4c
