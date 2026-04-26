from fastapi import APIRouter, HTTPException
from .models import Product

router = APIRouter()

products = []

@router.post("/products")
def create_product(product: Product):
    # validasi sederhana
    if not product.name:
        raise HTTPException(status_code=400, detail="Name is required")
    
    new_product = {"id": len(products)+1, "name": product.name}
    products.append(new_product)
    return new_product

@router.get("/products")
def get_products():
    return products