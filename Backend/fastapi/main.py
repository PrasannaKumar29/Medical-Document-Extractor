from fastapi import FastAPI
from enum import Enum
app=FastAPI()

class AvailableCuisines(str,Enum):
    indian='indian'
    american='american'
    italian='italian'

food_items={
    'indian':['Samosa','Kachori'],
    'italian':['pizza','nacho'],
    'american':['burger','burrito']
}
valid_cuisines=food_items.keys()
@app.get("/get_items/{cuisine}")
async def hello(cuisine:AvailableCuisines):
    return food_items.get(cuisine)