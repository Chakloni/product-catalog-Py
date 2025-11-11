from fastapi import APIRouter
from app.handlers import product_handler

router = APIRouter()
router.include_router(product_handler.router, prefix="/products", tags=["products"])
