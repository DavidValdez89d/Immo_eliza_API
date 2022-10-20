from fastapi import FastAPI
# from enum import Enum
from typing import Literal
from pydantic import BaseModel
import pickle

from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

app = FastAPI()

class ScoringItem(BaseModel):
    """
    class that contains the expected inpunt and format
    """
    area: int
    property_type: Literal["APARTMENT", "HOUSE", "OTHERS"]
    rooms_number: int
    zip_code: int
    land_area: int = None #Optional[int]
    garden: bool = None #Optional[bool],
    garden_area: int = None #Optional[int],
    equipped_kitchen: bool = None #Optional[bool],
    full_address: str = None #Optional[str],
    swimming_pool: bool = None #Optional[bool],
    furnished: bool = None #Optional[bool],
    open_fire: bool = None #Optional[bool],
    terrace: bool = None #Optional[bool],
    terrace_area: int = None #Optional[int],
    facades_number: int = None #Optional[int],
    building_state: Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"] = None
    
class Input(BaseModel):
    """
    Class that add a level of json to the input
    """
    data: ScoringItem


@app.get('/')
async def alive():
    """
    Request and return "alive" if the server is alive
    """
    return('alive')


@app.post('/predict/')
async def scoring_endpoint(item: Input):
    """
    POST request that receives the data of a house in JSON format and returns a price prediction
    """
    #Preprocess the input
    preprocess_item = preprocess(item)
    #Predict the price
    prediction_item = predict(preprocess_item)
    return prediction_item
    

@app.get('/predict/')
async def explain(
    # area: int,
    # property_type: Literal["APARTMENT", "HOUSE", "OTHERS"], #fsfs
    # rooms_number: int,
    # zip_code: int,
    # land_area: int = None, #Optional[int]
    # garden: bool = None, #Optional[bool],
    # garden_area: int = None, #Optional[int],
    # equipped_kitchen: bool = None, #Optional[bool],
    # full_address: str = None, #Optional[str],
    # swimming_pool: bool = None, #Optional[bool],
    # furnished: bool = None, #Optional[bool],
    # open_fire: bool = None, #Optional[bool],
    # terrace: bool = None, #Optional[bool],
    # terrace_area: int = None, #Optional[int],
    # facades_number: int = None, #Optional[int],
    # building_state: Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"] = None,
):
    
    """
    GET request returning a string to explain what the POST expect (data and format).
    """
    return('''
    This model is takes the nex information as an input:
    area: int
    property_type: str #"APARTMENT" | "HOUSE" | "OTHERS",
    rooms_number: int
    zip_code: int
    land_area: int | None #Optional[int]
    garden: bool | None #Optional[bool],
    garden_area: int | None #Optional[int],
    equipped_kitchen: bool | None #Optional[bool],
    full_address: str | None #Optional[str],
    swimming_pool: bool | None #Optional[bool],
    furnished: bool | None #Optional[bool],
    open_fire: bool | None #Optional[bool],
    terrace: bool | None #Optional[bool],
    terrace_area: int | None #Optional[int],
    facades_number: int | None #Optional[int],
    building_state: str | None # Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
    ''')