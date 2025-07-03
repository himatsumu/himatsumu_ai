from utils.place_api import getplace
from utils.geo import add_distance_to_shops
from services.scoring import score_shops

def recommend_shops(center_lat,center_lng,genre,time,budget):

    #現在地からのAPI呼び出し
    shop_list = getplace(
        center_lat = center_lat, #現在地の緯度
        center_lng = center_lng, #現在地の軽度
        keyword = genre, #選択したジャンル
        use_mock = False #モックを使うかどうか
    )

    #現在地とお店との距離を計算
    shop_list = add_distance_to_shops(shop_list,center_lat,center_lng)

    #お店の簡易スコアリング
    shop_list = score_shops(shop_list)

    #上位５件を返す
    shop_list = shop_list[0:4]
    return shop_list