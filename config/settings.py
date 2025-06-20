import os
from dotenv import load_dotenv

load_dotenv() #読み込み

GOOGLE_MAP_KEY = os.getenv("GOOGLE_MAP_KEY") # 上記で作成したAPIキーを入れる

SEARCH_RADIUS = 500  # meters
USE_MOCK = True  # ダミーモード切替用

# JSON保存パス（共通化しておくと後で楽）
MOCK_JSON_PATH = "tests/test_recommend/places_results.json"