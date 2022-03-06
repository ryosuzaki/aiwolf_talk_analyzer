# aiwolf_talk_analyzer

## どんなプログラム？？
人狼知能プロジェクトのトークを解析して、階層情報をディクショナリ型配列として返すプログラムです。
http://aiwolf.org/

## 使い方
1. 構文解析ライブラリ Lark をインストールする。
 ```
 pip install lark
 ```

2. test.pyを実行する。talkに解析したい文を入れる。

![image](https://user-images.githubusercontent.com/71608299/156884160-32be3689-9f3e-488a-a15b-61b2a03198d9.png)


3. そうするとディクショナリ型配列として主力される。

![image](https://user-images.githubusercontent.com/71608299/156884035-2f1eb25e-92b6-4418-98ba-ddf57cf270d8.png)


## ファイル構成

aiwolf_talk_analyzer.py　必須

aiwolf_talk_grammer.txt　文法のみ　無くても動く

text.py　使用例　無くても動く

### aiwolf_talk_analyzer.py
https://github.com/lark-parser/lark
larkを使って構文解析を行ってます。
ノードで行う処理はこのファイルに加筆する。
例えば、estimateのノードで何か処理を行うにはここに書く。
![image](https://user-images.githubusercontent.com/71608299/156884677-fa4873e9-8364-4d31-82c4-64b9d26d8fef.png)

文法記述部分
これを使って構文解析を行う。
http://aiwolf.org/control-panel/wp-content/uploads/2019/02/protocol_2019_3_6m.pdf
をベースに書いています。
![image](https://user-images.githubusercontent.com/71608299/156893311-42457286-7334-49c8-825a-e583a7bcef75.png)


### aiwolf_talk_grammer.txt
文法ファイル
aiwolf_talk_analyzer.pyに移動
多分こっちでやった方が編集しやすい

### text.py
テスト用プログラム

## 参考資料
Lark基本解説 (Python, Larkでシェルっぽいやつをつくる)
https://qiita.com/Hoshimi/items/fccd42ac6b1f005b46e5

Extended Backus–Naur form
https://www.wikiwand.com/en/Extended_Backus%E2%80%93Naur_form

Lark
https://lark-parser.readthedocs.io/en/latest/json_tutorial.html
