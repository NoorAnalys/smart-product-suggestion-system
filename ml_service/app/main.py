from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class PredictionRequest(BaseModel):
    user_id : int
    recent_products : List[int]

class PredictionResponse(BaseModel):
    recommended_products : List[int]

@app.post("/predict",response_model=PredictionResponse)
def predict(request : PredictionRequest):
    user_id = request.user_id
    recent_products = request.recent_products

    recommended_products = get_recomendations(user_id,recent_products)
    return PredictionResponse(recommended_products=recommended_products)