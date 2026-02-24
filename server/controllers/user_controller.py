from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from db.db import get_db
from security.auth import oauth2_scheme
from schemas.user_schema import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def get_users(token: str = Depends(oauth2_scheme)):

    return {"message": "This is a placeholder for the user controller."}

@router.get("/{user_id}")
async def get_user(user_id: str, token: str = Depends(oauth2_scheme)):
    return {"message": "This is a placeholder for the user controller."}

@router.put("/{user_id}")
async def update_user(user_id: str, body: UserUpdate, token: str = Depends(oauth2_scheme)):
    return {"message": "This is a placeholder for the user controller."}

@router.delete("/{user_id}")
async def delete_user(user_id: str, token: str = Depends(oauth2_scheme)):
    return {"message": "This is a placeholder for the user controller."}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Some logic goes here
    return { "access_token": "email", "token_type": "bearer" }

@router.post("/signup")
async def signup(new_user: UserCreate):
    print(f"\n New user: {new_user}\n")
    return {"message": "This is a placeholder for the user controller."}