import redis
import json

CACHE_KEY = "config_cache"
CACHE_TTL = 60  # Кэш живет 60 секунд (1 минута)

# Инициализируем клиент Redis (по умолчанию Redis запускается на порту 6379)
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def get_cache():
    cached_data = redis_client.get(CACHE_KEY)
    return cached_data


def set_cache(config_data):
    redis_client.set(CACHE_KEY, json.dumps(config_data), ex=CACHE_TTL)
