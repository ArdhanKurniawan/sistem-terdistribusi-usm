from fastapi import APIRouter
import requests

router = APIRouter()

# ====================
# USER SERVICE
# ====================
@router.get("/users")
def get_users():
    return requests.get("http://localhost:8001/users").json()

@router.post("/users")
def create_user(user: dict):
    return requests.post("http://localhost:8001/users", json=user).json()

# ====================
# PRODUCT SERVICE
# ====================
@router.get("/products")
def get_products():
    return requests.get("http://localhost:8002/products").json()

@router.post("/products")
def create_product(product: dict):
    # Simpan hasil request ke variable response
    response = requests.post("http://localhost:8002/products", json=product)

    # Return hasil dari product service
    return {
        "status_code": response.status_code,
        "content": response.json() # gunakan json() bukan text
    }

# ====================
# ORDER SERVICE
# ====================
@router.get("/orders")
def get_orders():
    return requests.get("http://localhost:8003/orders").json()

@router.post("/orders")
def create_order(order: dict):
    return requests.post("http://localhost:8003/orders", json=order).json()