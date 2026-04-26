from fastapi import APIRouter, HTTPException
from .models import User

router = APIRouter()

users = []

@router.post("/users")
def create_user(user: User):
    if not user.name:
        raise HTTPException(status_code=400, detail="Nama tidak boleh kosong")
    new_user = {"id": len(users)+1, "name": user.name}
    users.append(new_user)
    return new_user

@router.get("/users")
def get_users():
    return users