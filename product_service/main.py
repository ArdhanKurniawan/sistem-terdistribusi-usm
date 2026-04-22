from fastapi import FastAPI

app = FastAPI()

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