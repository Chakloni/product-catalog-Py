import time
from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.core.database import collection

router = APIRouter()
repo = ProductRepository(collection)

@router.post("", response_model=str)
def create_product(product: Product):
    try:
        return {"id": repo.create(product)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("", response_model=list[Product])
def list_products():
    try:
        return repo.list()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{id}", response_model=Product)
def get_product(id: str):
    product = repo.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.patch("/{id}")
def update(self, id: str, product: dict):
    product["updated_At"] = time.time()  # ✅ update timestamp
    result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": product})
    return result.modified_count > 0

@router.delete("/{id}")
def delete_product(id: str):
    if not repo.delete(id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"deleted": True}
