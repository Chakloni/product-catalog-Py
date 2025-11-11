import time
from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")
    sku: str = Field(..., alias="sku")
    name: str
    category: Optional[str] = None
    description: Optional[str] = None
    price_cents: Optional[int] = Field(None, alias="price_cents")
    currency: str
    stock: int

    images: Optional[str] = None
    is_active: bool = True
    is_deleted: bool = False
    created_at: Optional[float] = Field(default_factory=time.time, alias="created_at")
    updated_at: Optional[float] = Field(default_factory=time.time, alias="updated_at")

    class Config:
        populate_by_name = True
        json_encoders = {
            "ObjectId": str
        }
