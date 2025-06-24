from utils.place_api import getplace
import googlemaps
from config.settings import get_setting

settings = get_setting()

keyword = 'スイーツ' #絞るジャンル

client = googlemaps.Client(settings.GOOGLE_MAP_KEY) #インスタンス生成

mock_json_path = settings.MOCK_JSON_PATH

#緯度と軽度 ※現在は中崎町で固定
center_lat = 34.70605201690028
center_lng = 135.503858174402

shop_list = getplace(client,center_lat,center_lng,keyword,mock_json_path,use_mock=False)

#検索結果のMAPURLを表示
for id_num , result in enumerate(shop_list, start=1):
    print(id_num , ': [' ,result['name'], ']  https://www.google.com/maps/place/?q=place_id:' + result['place_id'])