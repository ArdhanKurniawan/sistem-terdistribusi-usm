from fastapi import FastAPI
from .routes import router 

app = FastAPI()

app.include_router(router)

@app.get("/")
def home():
    return {"message": "API aktif"}

products = []
# Tambah produk
@app.post("/products")
def create_product(name: str, price: int):
    product = {
        "id": len(products)+1,
        "name": name,
        "price": price
    }
    products.append(product)
    return product

# Ambil semua produk
@app.get("/products")
def get_products():
    return products