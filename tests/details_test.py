import json
from config.settings import get_setting
from utils.place_api import get_place_detail
from utils.extraction import extraction_detail
from services.scoring import score_details_shops
from services.scoring import score_shops
from utils.geo import add_distance_to_shops
from models.request_schema import RecommendRequest

settings = get_setting()

#レスポンス用のモックデータを読み込み
with open(settings.MOCK_RESPONSE_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)

#スキーマを導入しバリデーションチェック
req = RecommendRequest(**data)

details_datas = []

with open(settings.MOCK_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

details_datas = get_place_detail(data)

# details_datas = [extraction_detail(place_data) for place_data in details_datas]

# with open(settings.MOCK_DETAILE_JSON_PATH, "r", encoding="utf-8") as f:
#             details_datas = json.load(f)

details_datas = add_distance_to_shops(details_datas,34.70605201690028,135.503858174402)

details_datas = score_details_shops(details_datas,req.end_time)

# ダミーデータ作成用：重複なしの結果を新しいJSONに保存
with open(settings.MOCK_DETAILE_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(details_datas, f, ensure_ascii=False, indent=2)