import time
from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")
    SKU: str
    name: str
    category: Optional[str] = None
    description: Optional[str] = None
    PriceCents: Optional[int] = None
    Currency: str
    Stock: int
    Images: Optional[str] = None
    is_active: bool = True
    Is_deleted: bool = False
    created_At: float = Field(default_factory=time.time)
    updated_At: float = Field(default_factory=time.time)

    class Config:
        populate_by_name = True
        json_encoders = {
            "ObjectId": str
        }