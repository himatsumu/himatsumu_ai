from functools import lru_cache
from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    GOOGLE_MAP_KEY: str
    SEARCH_RADIUS: int = 500  # meters
    USE_MOCK: bool = True  # ダミーモード切替用
    MOCK_JSON_PATH: str = "tests/test_recommend/places_results.json" # JSON保存パス

    class Config:
        env_file = ".env"

# キャッシュ（呼び出しを初回のみにするため）
@lru_cache
def get_setting():
    return Setting()