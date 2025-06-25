from typing import List, Dict
import math

#2地点間の距離を測る関数
def calc_distance(center_lat: float,center_lng: float,shop_lat:float,shop_lng:float):

    R = 6371 #地球の半径(km)

    #2地点間の緯度経度から距離を計算　※公式：distance = 6371 × arccos(sinϕ 1​ × sinϕ2​ + cosϕ1​ × cosϕ2​ × cos(λ1​ − λ2))
    distance = R * math.acos(
        math.sin(math.radians(center_lat))*
        math.sin(math.radians(shop_lat))+
        math.cos(math.radians(center_lat))*
        math.cos(math.radians(shop_lat))*
        math.cos(math.radians(center_lng)-math.radians(shop_lng)))
    
    return distance

#店舗リストに中心地点からの距離を追加する
def add_distance_to_shops(shop_list: List[Dict], center_lat: float, center_lng: float) -> List[Dict]:

    for shop in shop_list:
        #お店の緯度経度を取得
        location = shop.get("geometry", {}).get("location", {})
        lat = location.get("lat")
        lng = location.get("lng")

        #取得できた場合関数呼び出し
        if lat is not None and lng is not None:
            distance = calc_distance(center_lat, center_lng, lat, lng)
            shop["distance"] = distance * 1000
        else:
            shop["distance"] = None  # 緯度経度が不明な場合は None にする

    return shop_list