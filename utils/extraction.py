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
    }