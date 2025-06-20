from himatsumu_ai.config.settings import settings
import json

def getplace(client,center_lat,center_lng,keyword,use_mock=False):
    #検索件数を増やし、3方位に300mずらすためのリスト
    directions = [ 
        (0.003, 0),        # 北
        (0, 0.003),        # 東
        (-0.003, 0)       # 南
    ]

    #API呼び出し結果を格納するリスト
    api_results = []

    #重複していない場所を格納
    unique_places = {}

    #APIの使用/非使用
    if use_mock: #使用
        #ダミーデータ呼び出し
        with open(settings.MOCK_JSON_PATH, "r", encoding="utf-8") as f:
            api_results = json.load(f)
    else:
        #API呼び出し
        for dlat, dlng in directions:
            lat = center_lat + dlat #現在地に緯度300m追加
            lng = center_lng + dlng #現在地に軽度300m追加
            #半径500m以内で指定ジャンルのお店をGoogle placeAPIで呼び出す
            place_result = client.places_nearby(location=(lat, lng), radius=500, keyword=keyword)
            api_results.extend(place_result['results']) #結果を追加する

    #API呼び出し処理
    for dlat, dlng in directions:
        lat = center_lat + dlat #現在地に緯度300m追加
        lng = center_lng + dlng #現在地に3軽度00m追加
        #半径300m以内で指定ジャンルのお店をGoogle placeAPIで呼び出す
        place_result = client.places_nearby(location=(lat, lng), radius=300, keyword=keyword)
        api_results.extend(place_result['results']) #結果を追加する

    #API利用しないためテストデータ呼び出し
    with open("tests/test_recommend/places_results.json", "r", encoding="utf-8") as f:
        api_results = json.load(f)

    # place_id を使って重複排除
    for place in api_results:
        place_id = place.get("place_id") #お店の固有AIを取得
        if place_id:
            unique_places[place_id] = place  # 辞書のキーにすることで重複が自動で消える

    # 値だけ取り出してリストに
    shop_list = list(unique_places.values())

    # ダミーデータ作成用：重複なしの結果を新しいJSONに保存
    with open(settings.MOCK_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(shop_list, f, ensure_ascii=False, indent=2)

    return shop_list