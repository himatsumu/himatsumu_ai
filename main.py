from fastapi import FastAPI, Response
from models.request_schema import RecommendRequest
from services.recommender import recommend_shops

app = FastAPI()

#python起動コマンド:uvicorn main:app --host 0.0.0.0 --port 8000 --reload

@app.post("/auth/quest/recommend")
def recommend(req: RecommendRequest , response: Response):
    shop_list = recommend_shops(
        req.start_prace,
        req.genre,
        req.end_time,
        req.budget,
        req.schedule
    )
   
    return {
        "data":{
		    "stores": shop_list
	    },
	    "status": 200
    }