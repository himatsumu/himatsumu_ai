from functools import lru_cache
from pydantic_settings import BaseSettings
from pathlib import Path

# この settings.py の2階層上 = プロジェクトルート
BASE_DIR = Path(__file__).resolve().parent.parent

class Setting(BaseSettings):
    GOOGLE_MAP_KEY: str
    SEARCH_RADIUS: int = 500  # meters
    USE_MOCK: bool = True  # ダミーモード切替用
    MOCK_JSON_PATH: str = str(BASE_DIR / "tests" / "mock" / "places_results.json") # JSON保存パス
    MOCK_RESPONSE_JSON: str = str(BASE_DIR / "tests" / "mock" / "mock_response.json") #レスポンスデータのMOCKパス

    class Config:
        env_file = ".env"

# キャッシュ（呼び出しを初回のみにするため）
@lru_cache
def get_setting():
    return Setting()