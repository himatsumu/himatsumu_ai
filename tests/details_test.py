import json
from config.settings import get_setting
from utils.place_api import get_place_detail
from utils.extraction import extraction_detail

settings = get_setting()

details_datas = []

with open(settings.MOCK_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

place_details = get_place_detail(data)

details_datas = [extraction_detail(place_data) for place_data in place_details]

# ダミーデータ作成用：重複なしの結果を新しいJSONに保存
with open(settings.MOCK_DETAILE_JSON, "w", encoding="utf-8") as f:
    json.dump(details_datas, f, ensure_ascii=False, indent=2)