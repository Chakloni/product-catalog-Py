from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    description: str
    price: float
    stock: int

    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}
