from typing import Optional
from pydantic import BaseModel, Field


class Store(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=15)
    address: int = Field(None, gt=5, lt=200) #no optional, age range
    
class Product(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=15)
    Price: float = Field(None, gt=0, lt=1000)

class Inventory(BaseModel):
    store_id: int
    store_name: str
    product_id: int
    product_name: str
    count: int = Field(None, gt=0, lt=1000)
