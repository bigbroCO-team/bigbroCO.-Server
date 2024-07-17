from django.core.cache import cache


class Redis:
    @classmethod
    def set(cls, key: str, value: str, ttl: int):
        return cache.set(key, value, timeout=ttl)

    @classmethod
    def get(cls, key: str):
        return cache.get(key)

    @classmethod
    def delete(cls, key: str):
        return cache.delete(key)
