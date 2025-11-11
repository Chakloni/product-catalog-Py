from typing import Optional
from app.models.product import Product
from bson import ObjectId

class ProductRepository:
    def __init__(self, collection):
        self.collection = collection

    def create(self, product: Product):
        res = self.collection.insert_one(product.model_dump(by_alias=True, exclude={"id"}))
        return str(res.inserted_id)

    def list(self):
        products = list(self.collection.find())
        for p in products:
            p["_id"] = str(p["_id"])
        return [Product(**p) for p in products]

    def get(self, id: str) -> Optional[Product]:
        data = self.collection.find_one({"_id": ObjectId(id)})
        return Product(**data) if data else None

    def update(self, id: str, product: dict):
        result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": product})
        return result.modified_count > 0

    def delete(self, id: str):
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
