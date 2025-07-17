from pydantic import BaseModel

class RecommendRequest(BaseModel):
    schedule: str
    end_time: str
    start_prace: str
    budget: int
    genre: str