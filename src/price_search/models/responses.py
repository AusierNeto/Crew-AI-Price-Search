from typing import List
from pydantic import BaseModel, Field

class Price(BaseModel):
    product_name: str
    quantity_or_measure: float
    price: float
    website_of_research: str

class Prices(BaseModel):
    items: List[Price] = Field(description="Lista de ofertas encontradas")
