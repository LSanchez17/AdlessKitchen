from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from db.db import get_db
from models.user import User
from security.auth import oauth2_scheme
from schemas.user_schema import UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])

## Type Aliases to reusability
DbDepends = Depends(get_db)
TokenDepends = Depends(oauth2_scheme)

@router.get("/")
async def get_users(token: str = TokenDepends):

    return {"message": "This is a placeholder for the user controller."}

@router.get("/{user_id}")
async def get_user(user_id: str, token: str = TokenDepends):
    return {"message": "This is a placeholder for the user controller."}

@router.put("/{user_id}")
async def update_user(user_id: str, body: UserUpdate, token: str = TokenDepends):
    return {"message": "This is a placeholder for the user controller."}

@router.delete("/{user_id}")
async def delete_user(user_id: str, token: str = TokenDepends):
    return {"message": "This is a placeholder for the user controller."}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Some logic goes here
    return { "access_token": "email", "token_type": "bearer" }

@router.post("/signup")
async def signup(new_user: UserCreate, db = DbDepends):
    user = await User.create(new_user, db)

    if user:
        # ensure the cookie is set in the response
        return {"message": "User created successfully."}
    else:
        return {"message": "Failed to create user."}