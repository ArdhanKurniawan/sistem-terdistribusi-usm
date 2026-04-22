from fastapi import FastAPI
import requests

app = FastAPI()

orders = []

# Buat order
@app.post("/orders")
def create_order(user_id: int, product_id: int):
    # Ambil data user dari User Service
    user = requests.get(f"http://localhost:8001/users").json()
    
    # Ambil data produk dari Product Service
    product = requests.get(f"http://localhost:8002/products").json()

    # Cari user berdasarkan ID
    selected_user = next((u for u in user if u["id"] == user_id), None)
    
    # Cari produk berdasarkan ID
    selected_product = next((p for p in product if p["id"] == product_id), None)

    if not selected_user or not selected_product:
        return {"error": "User atau Product tidak ditemukan"}

    order = {
        "id": len(orders)+1,
        "user": selected_user,
        "product": selected_product
    }

    orders.append(order)
    return order

# Ambil semua order
@app.get("/orders")
def get_orders():
    return orders