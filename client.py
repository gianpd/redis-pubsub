import redis

class RedisClient:

    def __init__(self, host: str, port: int, db: int):
        self._r = redis.Redis(host, port, db)
        
