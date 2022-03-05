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
### aiwolf_talk_analyzer.py
https://github.com/lark-parser/lark
larkを使って構文解析を行ってます。
ノードで行う処理はこのファイルに加筆する。
例えば、estimateのノードで何か処理を行うにはここに書く。
![image](https://user-images.githubusercontent.com/71608299/156884677-fa4873e9-8364-4d31-82c4-64b9d26d8fef.png)


### aiwolf_talk_grammer.txt
文法ファイル
これを使って構文解析を行う。
http://aiwolf.org/control-panel/wp-content/uploads/2019/02/protocol_2019_3_6m.pdf
をベースに書いています。

### text.py
テスト用プログラム
