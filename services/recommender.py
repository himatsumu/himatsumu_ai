from utils.place_api import getplace
from utils.place_api import get_place_detail
from utils.extraction import extraction_detail
from utils.geo import add_distance_to_shops
from services.scoring import score_shops
from services.scoring import score_details_shops

def recommend_shops(center_lat,center_lng,genre,time,budget,schedule):

    #現在地からのAPI呼び出し
    shop_list = getplace(
        center_lat = center_lat, #現在地の緯度
        center_lng = center_lng, #現在地の軽度
        keyword = genre, #選択したジャンル
        budget = budget, #予算
        schedule = schedule,
        use_mock = False #モックを使うかどうか
    )

    #現在地とお店との距離を計算
    shop_list = add_distance_to_shops(shop_list,center_lat,center_lng)

    #お店の簡易スコアリング
    shop_list = score_shops(shop_list)

    shop_list = get_place_detail(shop_list)

    shop_list = [extraction_detail(place_data) for place_data in shop_list]

    shop_list = add_distance_to_shops(shop_list,center_lat,center_lng)

    shop_list = score_details_shops(shop_list,time)

    #上位５件を返す
    shop_list = shop_list[0:4]

    return shop_list