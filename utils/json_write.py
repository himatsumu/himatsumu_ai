import json
from typing import Dict , List
from config.settings import get_setting

settings = get_setting()
#MOCKを使う場合のパス
mock_json_path = settings.MOCK_JSON_PATH
mock_json_detaile_json = settings.MOCK_DETAILE_JSON_PATH

#元々のJSONにスコアを追加して保存する関数
def update_json(place_data: List[Dict]):
    with open(mock_json_path, "w", encoding="utf-8") as f:
        json.dump(place_data, f, ensure_ascii=False, indent=2)

#元々のJSONにスコアを追加して保存する関数(detaile)
def update_detaile_json(place_deta: List[Dict]):
    with open(mock_json_detaile_json, "w", encoding="utf8") as f:
        json.dump(place_deta, f, ensure_ascii=False, indent=2)