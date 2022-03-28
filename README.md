# summarize
haitlab8Awebアプリ開発

現段階ではテストの文章をうまく要約することはできました。しかしそれ以外の文章がうまくいくかは
わかりません。例外処理に関しては全然書いてないのでそことあとはuiにもっとこだわる必要があるかなと思います


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
再起動したらまたもっかいpath通さないといけないかもです


出ていたエラー

1,
ImportError: DLL load failed while importing _MeCab: 指定されたモジュールが見つかりません。

http://harmonizedai.com/article/mecabdll-load-failed/

【解決策】上のサイトにあるようにいろんなとこにlibmecab.dllをコピーしたらエラーが取れました

2,
Non-UTF-8 code starting with '\xe3'

文字を取り込むときに文字数が長すぎたため分割したらこのエラーは取れました

https://stabucky.com/wp/archives/13198
