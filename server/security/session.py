from uuid import uuid4

from fastapi import HTTPException
from fastapi.params import Cookie, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis

from cache.redis import get_redis
from db.db import get_db
from models.user import User


async def create_session(user_id: str, redis: Redis) -> str:
    """
    Creates a session for the given user ID and stores it in Redis.
    Returns the session token to be set as a cookie.
    """
    token = uuid4().hex
    key = f"session:{token}"
    # 24 hours expiration for the session
    await redis.set(key, user_id, ex=60 * 60 * 24)
    
    return token


async def get_user_from_session(
    session_token: str | None = Cookie(None),
    redis: Redis = Depends(get_redis),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Retrieves the user associated with the session token from Redis and database.
    Raises HTTPException if the session is invalid or expired.
    """
    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = await redis.get(f"session:{session_token}")

    if not user_id:
        raise HTTPException(status_code=401, detail="Session expired")
    
    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user