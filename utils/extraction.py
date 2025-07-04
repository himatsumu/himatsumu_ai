from typing import Dict

#取得した情報から必要項目のみ抽出する
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

# def extrsction_responce(responce_results: Dict) ->Dict:
#     return{
#         "name" : responce_results.get("name"),
#         "location": responce_results.get("geometry", {}).get("location", {}),
#         "formatted_address": responce_results.get("formatted_address"),
#         "tytle": responce_results.get("types",[None])[0]
#     }

def extrsction_responce(responce_results: Dict) ->Dict:
    reviews = [review.get("text","") for review in responce_results.get("reviews",{})]
    return{
        "name" : responce_results.get("name"),
        "overview": responce_results.get("overview"),
        "reviews": reviews,
        "formatted_address": responce_results.get("formatted_address"),
        "title": responce_results.get("types")
    }