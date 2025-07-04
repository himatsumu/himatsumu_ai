from fastapi import FastAPI
from models.request_schema import RecommendRequest
from services.recommender import recommend_shops
from utils.extraction import extrsction_responce

app = FastAPI()

#uvicorn main:app --reload

@app.post("/auth/quest/recommend")
def recommend(req: RecommendRequest):
    shop_list = recommend_shops(
        req.location.lat,
        req.location.lng,
        req.genre,
        req.time,
        req.budget
    )

    shop_name = [shop.get("name") for shop in shop_list]
    shop_location = [shop.get("geometry", {}).get("location", {}) for shop in shop_list]
    shop_today_schedule = [shop.get("today_schedule") for shop in shop_list]
    shop_formatted_address = [shop.get("formatted_address") for shop in shop_list]
    shop_tytle = [shop.get("types",[None])[0] for shop in shop_list]
    recommend_history = [extrsction_responce(shop) for shop in shop_list ]
    return{
        "name" : shop_name,
        "location": shop_location,
        "today_schedule": shop_today_schedule,
        "formatted_address": shop_formatted_address,
        "tytle":shop_tytle,
        "recommend": 4,
        "history": recommend_history
    }