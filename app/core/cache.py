from cachetools import TTLCache
from app.core.config import settings

cache = TTLCache(maxsize=100, ttl=settings.CACHE_TTL)

def get_cache():
    return cache
