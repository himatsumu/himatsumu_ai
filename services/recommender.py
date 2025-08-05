from utils.place_api import getplace
from utils.place_api import get_place_detail
from utils.extraction import extraction_detail
from utils.geo import add_distance_to_shops
from utils.geo import geocoder
from services.scoring import score_shops
from services.scoring import score_details_shops
from utils.extraction import extraction_responce
from utils.json_write import update_json
from utils.json_write import update_detaile_json

def recommend_shops(start_place,genre,time,budget,schedule):

    location = geocoder(start_place)
    mock = False

    #現在地からのAPI呼び出し
    nearby_shops = getplace(
        center_lat = location[0],
        center_lng =  location[1],#現在地の軽度
        keyword = genre, #選択したジャンル
        budget = budget, #予算
        schedule = schedule,
        use_mock = mock #モックを使うかどうか
    )

    #現在地とお店との距離を計算
    shops_distance = add_distance_to_shops(nearby_shops,location[0],location[1])

    #お店の簡易スコアリング
    scored_shops = score_shops(shops_distance)

    #JSONデータとして書き出し
    update_json(scored_shops)

    #上位のお店の詳細データ取得
    detailed_shops = get_place_detail(scored_shops,mock)

    #必要項目のみ抽出
    shop_list = [extraction_detail(place_data) for place_data in detailed_shops]

    #JSONデータとして書き出し
    update_json(detailed_shops)

    #店舗リストに中心地点からの距離を追加する
    extracted_shops = add_distance_to_shops(shop_list,location[0],location[1])

    #詳細データを元に再度スコアリング
    scored_details_shops = score_details_shops(extracted_shops,time)

    #上位５件を返す
    top_shops = scored_details_shops[0:4]

    #バックエンドに返す値に整形
    response_shops = [extraction_responce(place_data) for place_data in top_shops]

    return response_shops