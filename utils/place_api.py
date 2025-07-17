import json
import googlemaps
from typing import Dict , List
from config.settings import get_setting
from utils.extraction import extraction_place

settings = get_setting()
client = googlemaps.Client(settings.GOOGLE_PLACE_KEY) #API使用のためのインスタンス生成
mock_json_path = settings.MOCK_JSON_PATH #MOCKを使う場合のパス
mock_detaile_json = settings.MOCK_DETAILE_JSON

#PlaceAPIを３回叩き、リストにして返す関数
def getplace(center_lat,center_lng,keyword,budget,schedule,use_mock):
    #検索件数を増やし、3方位に300mずらすためのリスト
    directions = [ 
        (0.003, 0),        # 北
        (0, 0.003),        # 東
        (-0.003, 0)       # 南
    ]

    #API呼び出し結果を格納するリスト
    api_results = []
    today_plan_genre_results = []
    visited_place_ids = []

    #重複していない場所を格納
    unique_places = {}

    #APIの使用/非使用
    if use_mock: #使用
        #ダミーデータ呼び出し
        with open(mock_json_path, "r", encoding="utf-8") as f:
            shop_list = json.load(f)
    else:
        #API呼び出し
        for dlat, dlng in directions:
            lat = center_lat + dlat #現在地に緯度300m追加
            lng = center_lng + dlng #現在地に軽度300m追加
            #半径500m以内で指定ジャンルのお店をGoogle placeAPIで呼び出す
            place_result = client.places(query = (keyword, ",", budget), location=(lat, lng), radius=300,language = "ja")
            api_results.extend(place_result['results']) #結果を追加する
        
        today_plan_genre = client.places(query = schedule, location = (lat,lng), radius = 300 , language = "ja")
        today_plan_genre_results.extend(today_plan_genre['results'])

        visited_place_ids = set([shop["place_id"] for shop in today_plan_genre_results])

        # place_id を使って重複排除
        for place in api_results:
            place_id = place.get("place_id") #お店の固有AIを取得
            if place_id not in visited_place_ids:
                unique_places[place_id] = place  # 辞書のキーにすることで重複が自動で消える


        # 値だけ取り出してリストに
        shop_list = list(unique_places.values())

        shop_list = [extraction_place(place_data) for place_data in shop_list]

        # ダミーデータ作成用：重複なしの結果を新しいJSONに保存
        with open(mock_json_path, "w", encoding="utf-8") as f:
            json.dump(shop_list, f, ensure_ascii=False, indent=2)

    return shop_list

#簡易スコアリングで上位に選ばれたお店の詳しい情報を取得
def get_place_detail(place_data: List[Dict]) -> List[Dict]:

    #API呼び出し結果を格納するリスト
    details_results = []

    for place_detail in place_data[:10]:
        place_id = place_detail.get("place_id")
        get_detail = client.place(place_id,language='ja')
        details_results.append(get_detail["result"])

    # details_results = [extraction_place(place_data) for place_data in details_results]

    return details_results