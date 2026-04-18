import redis

from app.config.settings import settings

class RedisCache:
    def __init__(self) -> None:
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,
        )

    def set(self, key: str, value: str) -> None:
        self.client.set(key, value)

    def get(self, key: str):
        return self.client.get(key)