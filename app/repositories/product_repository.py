from typing import List, Optional
from app.models.product import Product
from app.core.database import collection
from bson import ObjectId

class ProductRepository:
    def create(self, product: Product):
        res = collection.insert_one(product.model_dump(by_alias=True, exclude={"id"}))
        return str(res.inserted_id)

    def list(self) -> List[Product]:
        products = list(collection.find())
        return [Product(**p) for p in products]

    def get(self, id: str) -> Optional[Product]:
        data = collection.find_one({"_id": ObjectId(id)})
        return Product(**data) if data else None

    def update(self, id: str, product: dict):
        result = collection.update_one({"_id": ObjectId(id)}, {"$set": product})
        return result.modified_count > 0

    def delete(self, id: str):
        result = collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
