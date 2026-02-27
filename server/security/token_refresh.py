import os

from fastapi import Depends, Cookie, HTTPException, Response, Header
from sqlalchemy.ext.asyncio import AsyncSession
from redis.asyncio import Redis
from datetime import datetime, timedelta, timezone

from db.db import get_db
from cache.redis import get_redis
from models.user import User

import jwt

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

async def get_user_and_refresh(
    response: Response,
    session_token: str | None = Cookie(None),
    authorization: str | None = Header(None),
    redis: Redis = Depends(get_redis),
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Validate a Redis-backed session and optionally refresh the client's JWT.

    This dependency only produces side effects (raising 401 on failure and
    writing a new token header).  Callers that also need the user object should
    instead depend on :func:`security.session.get_user_from_session`

    Behavior summary:
      * The Redis session is checked and, if its remaining TTL is less than one
        hour, extended back to 24 hours.
      * If an Authorization header bearing a JWT is supplied and the token has
        <5 minutes remaining, a fresh token is encoded and placed in
        ``response.headers['X-Auth-Token']``.
    """
    if not session_token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user_id = await redis.get(f"session:{session_token}")

    if not user_id:
        raise HTTPException(status_code=401, detail="Session expired")

    user = await db.get(User, user_id)

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    key = f"session:{session_token}"
    ttl = await redis.ttl(key)
    # When the session is close to expiring, extend it.
    if ttl is not None and ttl < 60 * 60:
        # extend session for another 24 hours
        await redis.expire(key, 60 * 60 * 24)

    # only refresh the JWT if the existing token has less than five minutes left
    if authorization:
        # authorization should be of the form "Bearer <token>"; strip the prefix
        jwt_in = authorization.split(" ", 1)[1]

        try:
            payload = jwt.decode(
                jwt_in,
                SECRET_KEY,
                algorithms=[ALGORITHM],
                options={"verify_exp": False},
            )
            exp_ts = payload.get("exp")
            if exp_ts:
                exp_dt = datetime.fromtimestamp(exp_ts, timezone.utc)
                remaining = exp_dt - datetime.now(timezone.utc)
                if remaining < timedelta(minutes=5):
                    # mint a fresh token for the response headers
                    new_payload = {
                        "sub": user.id,
                        "exp": datetime.now(timezone.utc) + timedelta(hours=1),
                    }
                    response.headers["X-Auth-Token"] = jwt.encode(
                        new_payload, SECRET_KEY, algorithm=ALGORITHM
                    )
        except Exception:
            # if the header was malformed or can't be decoded we simply skip refresh
            pass

    return None