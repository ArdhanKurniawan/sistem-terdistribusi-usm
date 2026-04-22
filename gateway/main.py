from fastapi import FastAPI
import requests

app = FastAPI()

# Forward request ke user service
@app.get("/users")
def users():
    return requests.get("http://localhost:8001/users").json()

# Forward ke product service
@app.get("/products")
def products():
    return requests.get("http://localhost:8002/products").json()

# Forward ke order service
@app.get("/orders")
def orders():
    return requests.get("http://localhost:8003/orders").json()