from typing import Dict
import re

#取得した情報から必要項目を抽出する
def extraction_place(place_data: Dict) -> Dict:
    return{
        "business_status": place_data.get("business_status"),
        "formatted_address": place_data.get("formatted_address"),
        "geometry": place_data.get("geometry", {}),
        "name": place_data.get("name"),
        "opening_hours":place_data.get("opening_hours",{}),
        "place_id":place_data.get("place_id"),
        "rating":place_data.get("rating"),
        "types":place_data.get("types", []),
        "user_ratings_total":place_data.get("user_ratings_total"),
    }

#詳細情報を取得した情報から必要項目を抽出する
def extraction_detail(place_details: Dict) -> Dict:
    return{
        "business_status": place_details.get("business_status"),
        "current_opening_hours": place_details.get("current_opening_hours",{}),
        "dine_in": place_details.get("dine_in"),
        "overview": place_details.get("editorial_summary",{}).get("overview"),
        "formatted_address": place_details.get("formatted_address"),
        "geometry": place_details.get("geometry",{}),
        "name": place_details.get("name"),
        "opening_hours": place_details.get("opening_hours",{}),
        "place_id": place_details.get("place_id"),
        "rating": place_details.get("rating"),
        "reviews": place_details.get("reviews",{}),
        "types": place_details.get("types"),
        "user_ratings_total": place_details.get("user_ratings_total"),
        "utc_offset": place_details.get("utc_offset"),
        "website": place_details.get("website"),
        "distance": place_details.get("distance"),
        "score": place_details.get("score")
    }

#バック側に返す項目を抽出する
def extrsction_responce(responce_results: Dict) ->Dict:
    #お店のレビュー全件取得
    reviews = [review.get("text","") for review in responce_results.get("reviews",{})]


    title = "" #タイトル格納

    #point_of_interest(観光地的なジャンル)をタイトルとして弾く処理
    for t in responce_results.get("types"):
        if t != "point_of_interest":
            title = t
            break
    
    #住所の表示を少なくする
    address = responce_results.get("formatted_address")
    print(address)
    formatted_address = re.split(r'[ \u3000,、]+',address)[2]

    return{
        "end_hours": responce_results.get("end_hours"),
        "location": responce_results.get("geometry", {}).get("location", {}),
        "reviews": reviews,
        "start_hours": responce_results.get("start_hours"),
        "store_address": formatted_address,
        "store_name" : responce_results.get("name"),
        "types": responce_results.get("types")
    }