import googlemaps
import json
from utils.place_api import getplace
from config.settings import get_setting
from utils.geo import add_distance_to_shops
from services.scoring import score_shops
from models.request_schema import RecommendRequest

#settingsの情報を取得
settings = get_setting()

#レスポンス用のモックデータを読み込み
with open(settings.MOCK_RESPONSE_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)

#スキーマを導入しバリデーションチェック
req = RecommendRequest(**data)

#受け取ったJsonを使用しお店候補を取得
shop_list = getplace(
    client = googlemaps.Client(settings.GOOGLE_MAP_KEY), #インスタンス生成
    center_lat = req.location.lat, #現在地の緯度
    center_lng = req.location.lng, #現在地の軽度
    keyword = req.genre, #選択したジャンル
    mock_json_path = settings.MOCK_JSON_PATH, #MOCKを使う場合のパス
    use_mock = settings.USE_MOCK #モックを使うかどうか
)

shop_list = add_distance_to_shops(shop_list,req.location.lat,req.location.lng)

shop_list = score_shops(shop_list)

# ダミーデータ作成用：重複なしの結果を新しいJSONに保存
with open(settings.MOCK_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(shop_list, f, ensure_ascii=False, indent=2)

#検索結果のお店の名前：評価、距離、スコア、URLを表示
for id_num , result in enumerate(shop_list, start=1):
    print(f"{id_num}：[ {result['name']} ]\n 評価：{result['rating']} \n 距離：{result['distance']} \n スコア：{result['score']} \n URL： https://www.google.com/maps/place/?q=place_id:{result['place_id']} \n")