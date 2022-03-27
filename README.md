# summarize
haitlab8Awebアプリ開発
参考にしたサイト

FlaskでFormを使うための、必要最低限の知識
https://qiita.com/owgreen/items/7d9db1bc36b043af20da

はじめての Flask #3 ~htmlをrenderしてみよう~
https://qiita.com/nagataaaas/items/4662237cfb7b92f0f839

【自然言語処理（日本語）】自動要約ライブラリのpysummarizationを使う為の準備と実装
https://zerofromlight.com/blogs/detail/35/

【Python】Flask+WTFormsで簡単にフォームを作成する
https://hirahira.blog/flask-wtforms/



・MeCabについて
MecabをインストールしてPythonで使う【Windows】
https://self-development.info/mecab%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%97%E3%81%A6python%E3%81%A7%E4%BD%BF%E3%81%86%E3%80%90windows%E3%80%91/
ここのpathの通し方については別途説明
環境変数をクリックしてからシステム環境変数のとこでPathを選択
それで編集を押して次に新規を押して、MeCabの下にあるbinのpathをコピーして、そこに貼り付ける



出ているエラー

ImportError: DLL load failed while importing _MeCab: 指定されたモジュールが見つかりません。
http://harmonizedai.com/article/mecabdll-load-failed/

Non-UTF-8 code starting with '\xe3'
https://stabucky.com/wp/archives/13198

とりあえずここに書かれているようにMeCabの下にあるbinの下にあるlibmecab.dllをAnaconda3\Lib\site-packages”
に移動させてみたけどうまくいかなかった


C:\Program Files\MeCabの中身をC:\Users\shanb\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\MeCab
に移動させてみたけどダメだった

C:\Program Files\MeCab\bin￥


いろいろ思うにこの作業をしなければならないみたいです
https://own-search-and-study.xyz/2017/06/28/mecab%e3%82%92%e3%82%a4%e3%83%b3%e3%82%b9%e3%83%88%e3%83%bc%e3%83%ab%e3%81%97python%e3%81%8b%e3%82%89%e4%bd%bf%e3%81%86%e6%96%b9%e6%b3%95%e3%81%be%e3%81%a8%e3%82%81/
