import time
from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")

    sku: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    price_cents: Optional[int] = None
    currency: str
    stock: int

    images: Optional[List[str]] = None  # ✅ supports list of image URLs
    attributes: Optional[Dict[str, str]] = None  # ✅ supports attributes like brand, color, etc.

    is_active: bool = True
    is_deleted: bool = False
    created_at: Optional[float] = Field(default_factory=time.time)
    updated_at: Optional[float] = Field(default_factory=time.time)

    class Config:
        populate_by_name = True
        json_encoders = {
            "ObjectId": str
        }