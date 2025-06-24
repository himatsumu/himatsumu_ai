from pydantic import BaseModel

class Location(BaseModel):
    lat:float
    lng:float

class RecommendRequest(BaseModel):
    location: Location
    genre: str
    time: str
    budget:  int