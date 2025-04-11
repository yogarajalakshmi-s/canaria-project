import redis
import os

class RedisConnector:
    def __init__(self):
        self.redis = redis.Redis(
            host=os.getenv("REDIS_HOST", "redis"),
            port=int(os.getenv("REDIS_PORT", 6379)),
            db=0
        )

    def is_duplicate(self, key):
        return self.redis.sismember("scraped_jobs", key)

    def mark_as_scraped(self, key):
        self.redis.sadd("scraped_jobs", key)
