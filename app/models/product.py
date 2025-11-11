from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    category: Optional[str] = None
    is_active: bool = True

    class Config:
        populate_by_name = True
        json_encoders = {
            # convert ObjectId -> str automatically
            # This prevents validation errors
            "ObjectId": str
        }
