from fastapi import APIRouter, Depends, HTTPException, Response, Cookie
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import uuid4

from db.db import get_db
from models.user import User
from security.session import create_session, get_user_from_session
from schemas.user_schema import (
    UserCreate,
    UserUpdate,
    UserRead,
    UserLogin,
)
from schemas.response_schema import ServerResponse
from cache.redis import get_redis
from redis.asyncio import Redis


router = APIRouter(prefix="/users", tags=["users"])

# Type Aliases to reusability
DbDepends = Depends(get_db)
UserDepends = Depends(get_user_from_session)

@router.get("/", response_model=ServerResponse[UserRead])
async def get_users(user: User = UserDepends, db: AsyncSession = DbDepends):
    # `user` is the currently authenticated user; you can check roles/permissions
    result = await db.execute(select(User))
    users = result.scalars().all()
    return ServerResponse(entity="users", results=users)

@router.get("/{user_id}", response_model=ServerResponse[UserRead])
async def get_user(
    user_id: str,
    current: User = UserDepends,
    db: AsyncSession = DbDepends,
):
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return ServerResponse(entity="users", results=[UserRead.model_validate(user)])

@router.put("/{user_id}")
async def update_user(
    user_id: str,
    body: UserUpdate,
    current: User = UserDepends,
):
    return {"message": "This is a placeholder for the user controller."}

@router.delete("/{user_id}")
async def delete_user(user_id: str, current: User = UserDepends):
    return {"message": "This is a placeholder for the user controller."}

@router.post("/login")
async def login(login: UserLogin, db: AsyncSession = DbDepends, redis: Redis = Depends(get_redis)):
    user = await User.login(login.email, login.password, db)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = await create_session(user.id, redis)

    # We need to validate the model since we are returning a SQLAlchemy model instance, and the response model expects a Pydantic model
    resp = ServerResponse(entity="users", results=[UserRead.model_validate(user)])
    headers = {
        "Set-Cookie": (
            f"session={token}; HttpOnly; Path=/; "
            "SameSite=lax; Secure"
        ),
        "X-Redirect-To": "/home",
    }

    return Response(content=resp.model_dump_json(), media_type="application/json", headers=headers)

@router.post("/signup", response_model=ServerResponse[UserRead])
async def signup(new_user: UserCreate, db: AsyncSession = DbDepends, redis: Redis = Depends(get_redis)):
    user = await User.create(new_user, db)
    if not user:
        raise HTTPException(status_code=500, detail="Failed to create user")

    token = await create_session(user.id, redis)

    # We need to validate the model since we are returning a SQLAlchemy model instance, and the response model expects a Pydantic model
    resp = ServerResponse(entity="users", results=[UserRead.model_validate(user)])
    headers = {
        "Set-Cookie": (
            f"session={token}; HttpOnly; Path=/; "
            "SameSite=lax; Secure"
        ),
        "X-Redirect-To": "/home",
    }

    return Response(content=resp.model_dump_json(), media_type="application/json", headers=headers)

@router.post("/logout")
async def logout(
    session_token: str | None = Cookie(None),
    redis: Redis = Depends(get_redis),
):
    if session_token:
        await redis.delete(f"session:{session_token}")

    headers = {
        "Set-Cookie": "session=; HttpOnly; Path=/; Max-Age=0",
        "X-Redirect-To": "/login",

    }
    return Response(
        content='{"message": "Logged out successfully"}',
        media_type="application/json",
        headers=headers,
    )