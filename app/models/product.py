import time
from typing import Optional, List, Dict, Union
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class Product(BaseModel):
    id: Optional[str] = Field(alias="_id")

    sku: str
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    price_cents: Optional[int] = None
    currency: str
    stock: int

    images: Optional[List[str]] = None
    attributes: Optional[Dict[str, str]] = None

    is_active: bool = True
    is_deleted: bool = False
    created_at: Optional[Union[float, datetime]] = Field(default_factory=time.time)
    updated_at: Optional[Union[float, datetime]] = Field(default_factory=time.time)

    # ✅ Convert datetime → float automatically
    @field_validator("created_at", "updated_at", mode="before")
    def convert_datetime(cls, v):
        if isinstance(v, datetime):
            return v.timestamp()
        return v

    class Config:
        populate_by_name = True
        json_encoders = {
            datetime: lambda v: v.timestamp(),  # just in case
        }
