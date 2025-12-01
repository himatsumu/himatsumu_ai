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

## ディレクトリ構成(重要な部分のみ記載)  
config      # パス定義や、環境変数読み込み  
&emsp;─ settings.py  
main.py     # fastAPIのエントリーポイント  
models      # 送られてくるJsonデータのバリデーション  
&emsp;─ request_schema.py  
requirements.txt    # 使用ライブラリ  
services    # 実行の芯となるディレクトリ   
&emsp;─ recommender.py      # 各実行ファイル  
&emsp;─ scoring.py      # お店の評価全般の処理  
tests       #各機能のテストコードを置いているディレクトリ  
&emsp;─ MeCab_test.py  
&emsp;─ details_test.py  
&emsp;─ geocoder_test.py  
&emsp;─ mock        #mock、一時利用するJsonデータが入るディレクトリ  
&emsp;─ predict_test.py  
&emsp;─ run_recommend.py  
&emsp;─ test_recommend  
&emsp;&emsp;─ googlemaps_test.py  
&emsp;&emsp;─ places_results.json  
utils       #使い回す可能性のあるアルゴリズムがはいっているディレクトリ  
&emsp;─ extraction.py　#Jsonデータ整形  
&emsp;─ geo.py      #緯度経度から距離を算出する処理  
&emsp;─ json_write.py #Jsonに書き込む処理  
&emsp;─ place_api.py        #place_apiを呼び出す処理  
