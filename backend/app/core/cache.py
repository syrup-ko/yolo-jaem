from typing import Optional
from redis.asyncio import Redis
from .config import settings

redis_client: Optional[Redis] = None


async def init_redis() -> None:
    global redis_client
    if redis_client is None:
        redis_client = Redis.from_url(settings.REDIS_URL, decode_responses=True)


async def close_redis() -> None:
    global redis_client
    if redis_client is not None:
        await redis_client.close()
        redis_client = None


def get_redis() -> Redis:
    assert redis_client is not None, "Redis is not initialized"
    return redis_client



