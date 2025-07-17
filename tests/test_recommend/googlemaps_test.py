import googlemaps
from dotenv import load_dotenv
import os
import json

genre = 'アミューズメント' #絞るジャンル

load_dotenv

key = os.getenv("GOOGLE_PLACE_KEY") # 上記で作成したAPIキーを入れる
client = googlemaps.Client(key) #インスタンス生成

#緯度と軽度 ※現在は中崎町で固定
center_lat = 34.70605201690028
center_lng = 135.503858174402

#API呼び出し結果を格納するリスト
api_results = []

#重複していない場所を格納
unique_places = {}

#検索件数を増やし、4方位に300mずらすためのリスト
directions = [
    (0.003, 0),        # 北
    (0, 0.003),        # 東
    (-0.003, 0)       # 南
]

#API呼び出し処理
for dlat, dlng in directions:
    lat = center_lat + dlat #現在地に緯度300m追加
    lng = center_lng + dlng #現在地に3軽度00m追加
    #半径300m以内で指定ジャンルのお店をGoogle placeAPIで呼び出す
    place_result = client.places(query = genre, location=(lat, lng), radius=300)
    api_results.extend(place_result['results']) #結果を追加する

#API利用しないためテストデータ呼び出し
# with open("test_recommend/places_results.json", "r", encoding="utf-8") as f:
#     api_results = json.load(f)

# place_id を使って重複排除
for place in api_results:
    place_id = place.get("place_id") #お店の固有AIを取得
    if place_id:
        unique_places[place_id] = place  # 辞書のキーにすることで重複が自動で消える

# 値だけ取り出してリストに
shop_list = list(unique_places.values())

# 重複なしの結果を新しいJSONに保存
with open("tests/test_recommend/places_results.json", "w", encoding="utf-8") as f:
    json.dump(shop_list, f, ensure_ascii=False, indent=2)

#検索結果のMAPURLを表示
for id_num , result in enumerate(shop_list, start=1):
    print(id_num , ': [' ,result['name'], ']  https://www.google.com/maps/place/?q=place_id:' + result['place_id'])