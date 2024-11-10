import os

import redis
import json

CACHE_KEY = "config_cache"
CACHE_TTL = 60  # Кэш живет 60 секунд (1 минута)

redis_host = os.getenv("REDIS_HOST", "source-service")

redis_client = redis.Redis(host=redis_host, port=6379, db=0)


def get_cache():
    cached_data = redis_client.get(CACHE_KEY)
    return cached_data


def set_cache(config_data):
    redis_client.set(CACHE_KEY, json.dumps(config_data), ex=CACHE_TTL)
