import googlemaps
import json
from config.settings import get_setting

# APIキーの取得
settings = get_setting()
client = googlemaps.Client(settings.GOOGLE_MAP_KEY) #インスタンス生成


# Place ID を指定（例: 中崎町の服屋など）
place_id = 'ChIJszdHEQN9GGARy9MJ1TY22eQ'  # ※適当なPlace IDに置き換えてください

# 詳細取得
place_details = client.place(place_id)

# 出力
from pprint import pprint
pprint(place_details["result"])

# ダミーデータ作成用：重複なしの結果を新しいJSONに保存
with open(settings.MOCK_DETAILE_JSON, "w", encoding="utf-8") as f:
    json.dump(place_details, f, ensure_ascii=False, indent=2)