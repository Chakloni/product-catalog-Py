from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.repositories.product_repository import ProductRepository

router = APIRouter()
repo = ProductRepository()

@router.post("", response_model=str)
def create_product(product: Product):
    return repo.create(product)

@router.get("", response_model=list[Product])
def list_products():
    return repo.list()

@router.get("/{id}", response_model=Product)
def get_product(id: str):
    product = repo.get(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.patch("/{id}")
def update_product(id: str, product: dict):
    if not repo.update(id, product):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"updated": True}

@router.delete("/{id}")
def delete_product(id: str):
    if not repo.delete(id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"deleted": True}
