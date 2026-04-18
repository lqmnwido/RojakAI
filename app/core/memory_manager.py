from app.storage.redis_cache import RedisCache

class MemoryManager:
    def __init__(self) -> None:
        self.cache = RedisCache()

    def save_last_question(self, question: str) -> None:
        self.cache.set("last_question", question)

    def get_last_question(self):
        return self.cache.get("last_question")