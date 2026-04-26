from fastapi import APIRouter, HTTPException
import requests

# from user_service.app import users
from .models import Order

router = APIRouter()

orders = []

@router.post("/orders")
def create_order(order: Order):
    # Ambil user dan product dari service lain
    try:
        users = requests.get("http://localhost:8001/users", timeout=5).json()
        products = requests.get("http://localhost:8002/products", timeout=5).json()
    except:
        raise HTTPException(status_code=500, detail="Service tidak tersedia")
    
    selected_user = next((u for u in users if u["id"] == order.user_id), None)
    selected_product = next((p for p in products if p["id"] == order.product_id), None)
    if not selected_user or not selected_product:
        raise HTTPException(status_code=404, detail="User atau Product tidak ditemukan")
    
    new_order = {
        "id": len(orders)+1,
        "user": selected_user,
        "product": selected_product
    }
    orders.append(new_order)
    return new_order

@router.get("/orders")
def get_orders():
    return orders