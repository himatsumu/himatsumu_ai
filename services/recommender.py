import googlemaps
from utils.place_api import getplace
from config.settings import get_setting
from utils.geo import add_distance_to_shops
from services.scoring import score_shops

def recommend_shops(center_lat,center_lng,genre,time,budget):

    settings = get_setting()

    shop_list = getplace(
        client = googlemaps.Client(settings.GOOGLE_MAP_KEY), #インスタンス生成
        center_lat = center_lat, #現在地の緯度
        center_lng = center_lng, #現在地の軽度
        keyword = genre, #選択したジャンル
        mock_json_path = settings.MOCK_JSON_PATH, #MOCKを使う場合のパス
        use_mock = False #モックを使うかどうか
    )

    shop_list = add_distance_to_shops(shop_list,center_lat,center_lng)

    shop_list = score_shops(shop_list)

    shop_list = shop_list[0]

    return shop_list