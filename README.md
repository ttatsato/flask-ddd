# FlaskでDDD
webフレームワークFlaskでDDDをやってみる

----
下記は、メモ

# はじめに
FlaskはPython用の軽量マイクロWebフレームワークです。  

# 実行環境
```
Python 3.7.0
```

# 公式サイト
http://flask.pocoo.org/

# venvで仮想環境を作る(pycharmなら設定不要)
仮想環境を作成するためにツールvenvを導入する。

```
# python<version> -m vnev <つけたい名前>
# pycharmなら自動設定できる。
python3.7 -m venv getting_started
```

# Flaskを環境にインストールする
```
pip3.7 install flask
```

# Flaskを動かしてみる
```
flask run
```

## IPアドレスを指定して、Runする
通常のrunだとローカルPCからしか接続できないが、
以下のように--hostオプションを設定すると
サーバー上でListenするIPアドレスを指定できます。
```
flask run --host=0.0.0.0
```

# Pythonで型定義する
mypyというツールを使います。

## mypyのインストール
```angular2html
pip install mypy
```

## 型チェック
```
# mypy <ファイル名/ディレクトリ名>
mypy . 
```

## 型チェック正誤

### 型チェックアウト
```
Found 1 error in 1 file (checked 1 source file)
```

### 型チェックOK
```angular2html
Success: no issues found in 1 source file
```

## Pycharmにmypyプラグインを入れて、型チェックする
https://plugins.jetbrains.com/plugin/11086-mypy