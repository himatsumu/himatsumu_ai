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
├── config      # パス定義や、環境変数読み込み
│   └── settings.py
│
├── main.py     # fastAPIのエントリーポイント
│
├── models      # 送られてくるJsonデータのバリデーション
│   └── request_schema.py
│
├── requirements.txt    # 使用ライブラリ
│
├── services    # 実行の芯となるディレクトリ 
│   ├── recommender.py      # 各実行ファイル
│   └── scoring.py      # お店の評価全般の処理
│
├── tests       #各機能のテストコードを置いているディレクトリ
│   ├── MeCab_test.py
│   ├── details_test.py
│   ├── geocoder_test.py
│   ├── mock        #mock、一時利用するJsonデータが入るディレクトリ
│   ├── predict_test.py
│   ├── run_recommend.py
│   └── test_recommend
│       ├── googlemaps_test.py
│       └── places_results.json
│
└── utils       #使い回す可能性のあるアルゴリズムがはいっているディレクトリ
    ├── extraction.py　#Jsonデータ整形
    ├── geo.py      #緯度経度から距離を算出する処理
    ├── json_write.py #Jsonに書き込む処理
    └── place_api.py        #place_apiを呼び出す処理