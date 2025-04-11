import redis
import os

class RedisConnector:
    def __init__(self, uri=None):
        self.uri = uri or os.getenv("REDIS_URL", "redis://localhost:6379")
        self.client = redis.StrictRedis(host='redis', port=6379, db=0)

    def is_duplicate(self, key):
        return self.client.exists(key)

    def mark_as_scraped(self, key):
        self.client.setex(key, 3600, "scraped")  # expires in 1 hour
