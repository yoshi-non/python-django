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

# サンプル画像

![home](https://user-images.githubusercontent.com/83369665/186470862-dc158972-6ac1-4510-a146-766a06a6e238.png)
![diary-list](https://user-images.githubusercontent.com/83369665/186471066-78260f92-ef47-4a24-9de4-474db0906b9e.png)
![diary-detail](https://user-images.githubusercontent.com/83369665/186471111-3cff26f7-d4df-492a-aeba-78a487cfcb08.png)
![diary-create](https://user-images.githubusercontent.com/83369665/186471140-77289fb1-5a8c-48a9-a631-430ec8c2363a.png)
![diary-update](https://user-images.githubusercontent.com/83369665/186471172-0d006647-3628-4b8a-99da-58f49bf60595.png)
![inquiry](https://user-images.githubusercontent.com/83369665/186471207-5ec1a4e2-7e71-49fd-a99a-da706bb3f32b.png)
