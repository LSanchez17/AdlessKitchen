import os
from dotenv import load_dotenv
from redis.asyncio import Redis

load_dotenv()
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# create a single, global connection/pool
redis: Redis = Redis.from_url(
    REDIS_URL,
    encoding="utf-8",
    decode_responses=True,
)

async def get_redis() -> Redis:
    """
    Dependency you can use in controllers/services.
    """
    return redis