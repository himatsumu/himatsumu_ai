from utils.place_api import getplace
from utils.place_api import get_place_detail
from utils.extraction import extraction_detail
from utils.geo import add_distance_to_shops
from utils.geo import geocoder
from services.scoring import score_shops
from services.scoring import score_details_shops
from utils.extraction import extrsction_responce
from utils.place_api import update_json

def recommend_shops(start_place,genre,time,budget,schedule):

    location = geocoder(start_place)

    #現在地からのAPI呼び出し
    shop_list = getplace(
        center_lat = location[0],
        center_lng =  location[1],#現在地の軽度
        keyword = genre, #選択したジャンル
        budget = budget, #予算
        schedule = schedule,
        use_mock = False #モックを使うかどうか
    )

    #現在地とお店との距離を計算
    shop_list = add_distance_to_shops(shop_list,location[0],location[1])

    #お店の簡易スコアリング
    shop_list = score_shops(shop_list)

    update_json(shop_list)

    shop_list = get_place_detail(shop_list)

    shop_list = [extraction_detail(place_data) for place_data in shop_list]

    shop_list = add_distance_to_shops(shop_list,location[0],location[1])

    shop_list = score_details_shops(shop_list,time)

    #上位５件を返す
    shop_list = shop_list[0:4]

    shop_list = [extrsction_responce(shop) for shop in shop_list]

    return shop_list