# himatsumu_ai
himatsumuのクエスト提案をするAI

## 開発環境
appディレクトリに移動し、リポジトリをクローンする。  
もしapp内に何かファイルがあった場合は削除してからクローン

## 実行方法
pip list をターミナルで実行し、requirements.txt内に記載されたライブラリがあるか確認。  
※ない場合は pip install -r requirements.txt をターミナルで実行し、ライブラリが入ったかどうか確認する。
.envファイルを作り、GOOGLE_PLACE_KEY = "apikey"(チームのaiチャンネルにて記載)と入力

実行コマンド  
uvicorn main:app --host 0.0.0.0 --port 8000 --reload 

## test_recommender
テストデータを使い、pythonのみで実行確認をするディレクトリ
