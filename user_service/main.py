from fastapi import FastAPI

app = FastAPI()

# Data dummy user (sementara, belum pakai database)
users = []

# Endpoint untuk menambahkan user
@app.post("/users")
def create_user(name: str):
    user = {"id": len(users) + 1, "name": name}
    users.append(user)
    return user

# Endpoint untuk melihat semua user
@app.get("/users")
def get_users():
    return users