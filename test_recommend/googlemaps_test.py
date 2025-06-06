
import googlemaps
import pprint # list型やdict型を見やすくprintするライブラリ

key = 'AIzaSyCeX7wBPxmP64RdLd936C00iX-RUtlkUEI' # 上記で作成したAPIキーを入れる
client = googlemaps.Client(key) #インスタンス生成

geocode_result = client.geocode('東京都渋谷駅') # 位置情報を検索
loc = geocode_result[0]['geometry']['location'] # 軽度・緯度の情報のみ取り出す
place_result = client.places_nearby(location=loc, radius=200, type='food') #半径200m以内のレストランの情報を取得
pprint.pprint(place_result)