from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.db import get_db
from models.user import User
from security.auth import oauth2_scheme
from schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserRead,
)
from schemas.response_schema import ItemResponse, ListResponse

router = APIRouter(prefix="/users", tags=["users"])

## Type Aliases to reusability
DbDepends = Depends(get_db)
TokenDepends = Depends(oauth2_scheme)

@router.get("/", response_model=ListResponse[UserRead])
async def get_users(token: str = TokenDepends, db: AsyncSession = DbDepends):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return ListResponse(entity="users", results=users)


@router.get("/{user_id}", response_model=ItemResponse[UserRead])
async def get_user(
    user_id: str, token: str = TokenDepends, db: AsyncSession = DbDepends
):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return ItemResponse(entity="users", result=user)


@router.put("/{user_id}")
async def update_user(user_id: str, body: UserUpdate, token: str = TokenDepends):
    return {"message": "This is a placeholder for the user controller."}


@router.delete("/{user_id}")
async def delete_user(user_id: str, token: str = TokenDepends):
    return {"message": "This is a placeholder for the user controller."}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Some logic goes here
    return {"access_token": "email", "token_type": "bearer"}


@router.post("/signup", response_model=ItemResponse[UserRead])
async def signup(new_user: UserCreate, db: AsyncSession = DbDepends):
    user = await User.create(new_user, db)
    if not user:
        raise HTTPException(status_code=500, detail="Failed to create user")
    resp = ItemResponse(entity="users", result=user)
    headers = {
        # Fill out other header parts
        # Store session in redis?
        "Set-Cookie": f"session={user.id}; HttpOnly; Path=/",
        # Custom redirect header for the client to handle
        "X-Redirect-To": "/dashboard", 
    }
    return Response(content=resp.json(), media_type="application/json", headers=headers)
