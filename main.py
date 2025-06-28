from fastapi import FastAPI
from models.request_schema import RecommendRequest
from services.recommender import recommend_shops
from config.settings import get_setting

app = FastAPI()
settings = get_setting()

@app.post("/recommend")
def recommend(req: RecommendRequest):
    results = recommend_shops(
        req.location.lat,
        req.location.lng,
        req.genre,
        req.time,
        req.budget
    )
    return {"results": results}