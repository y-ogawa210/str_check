# str_check 
# 文字数、キーワードの個数チェックツール  
WEB(SEO)ライティングに役立つと思うツールを作りました。

## ツールの特徴  
文章を貼り付けてボタンを押すことで  
①　全体の文字数を確認できます。  
②　文章の中にある特定のキーワードがいくつあるかを確認できます。（一度に最大5つ設定できます。）  
順に説明していきます。  
  
①　全体の文字数を確認できます。  
⇒全体の文字数を確認する為だけに文字数カウンターのサイトへ行く手間が省けます。  
  
②　文章の中にある特定のキーワードがいくつあるかを確認できます。（一度に最大5つ設定できます。）  
⇒特定のキーワードが少なすぎたら、そのキーワードを意識しながら文章を修正できると思います。  
  

## 言語
Python

## ライブラリ
PySimpleGUI

## ツールの場所
str_check-main/dist/main  
ダブルクリックするとツールが起動します。

## 実際に例えば下記のサンプル文で試してみるとします。
======ここからがサンプル文です======  
Pythonにはいくつかのwebフレームワークがあります。  
その中で有名なのがDjangoとFlaskです。  

DjangoはPythonのwebフレームワークで有名です。  
Djangoは中規模、大規模向けのwebフレームワークです。  
  
一方で小規模寄りのwebフレームワークとしてよく利用されているのがFlaskです。  
======ここまでがサンプル文です======  
  
======ここからが使い方の説明です======  
①サンプル文をコピーしたら「本文を入力してください」の入力ボックスに貼り付けてください。  
②抽出したいキーワードが「Django」と「Flask」の２つとする場合、  
・抽出したいキーワードの数を指定してください  
⇒ラジオボタンの選択を「２」  
・抽出したいキーワードを入力してください（左から入力してください）  
⇒入力ボックスには「Django」と「Flask」  
をそれぞれ記入して「抽出する」ボタンを押してください。  
  
そうすることで  
下のテキストボックスに本文の文字数、取得した文章のキーワードの出現回数が表示されます。  
  
「全部消す」をクリックすると入力した値、出力した値が空欄になります。  
  
====  
  
## あとがき
  
このツールを作成した経緯としまして  
自分が昔、ブログを書いているときに（今はしていません）  
こういうツールがあったらよかったかもと思うツールを作ってみました。  
  
なのでこのツールは、webライティングをしている方を意識して作成しました。  
  
昔、自分はwebアプリの某文字数確認アプリを使っていた時、  
  
「自分が書いた文章って抜き取られていないかな？」  
  
と少し抵抗があったことを思い出して  
同じことを思っている方もいるかもしれないと思い  
デスクトップアプリでの作成をしました。  
（ほとんどがそういうサイトじゃないと思いますが）  
  
そして、ツールを作るならもう少し機能がほしいと思い、  
ツールの特徴で記載した②を取り入れることにしました。  
  
  
以上、ここまで読んでくださりありがとうございます。  

