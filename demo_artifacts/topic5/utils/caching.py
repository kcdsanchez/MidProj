# This file handles utility functions like caching.

import time

# FIXME: This is an in-memory dictionary cache, not suitable for production.
# It's not shared between processes and will run out of memory.
# This entire module should be rewritten to use Redis.
_cache = {}
_cache_expiry = {}

DEFAULT_TTL = 300  # 5 minutes


def cache_data(key, data, ttl=DEFAULT_TTL):
    """
    Simulates saving data to a cache (like Redis) with an expiry.

    :param key: The key to store the data under.
    :param data: The data to store.
    :param ttl: Time To Live in seconds.
    """

    # TODO: Add cache invalidation logic (e.g., TTL - Time To Live)
    # This is a basic implementation of TTL

    print(f"Caching data for key: {key} (TTL: {ttl}s)")
    _cache[key] = data
    _cache_expiry[key] = time.time() + ttl


def get_from_cache(key):
    """
    Simulates fetching data from a cache, checking for expiry.
    """
    if key not in _cache:
        print(f"CACHE MISS: {key}")
        return None

    expiry_time = _cache_expiry.get(key)

    if time.time() > expiry_time:
        # TODO: Add logic to automatically clear expired keys
        print(f"CACHE EXPIRED: {key}")
        _cache.pop(key)
        _cache_expiry.pop(key)
        return None

    print(f"CACHE HIT: {key}")
    return _cache[key]


def clear_cache():
    """
    Clears the entire in-memory cache.
    """
    # REVIEW: Is this function safe to call?
    # This could cause a "thundering herd" problem if called in production.
    # Maybe we should just clear expired keys?

    print("Clearing all cache...")
    _cache.clear()
    _cache_expiry.clear()


def get_cache_stats():
    """
    Returns statistics about the cache.
    """
    # TODO: Implement cache stats (hits, misses, size)
    return {
        'size': len(_cache),
        'hits': 0,  # FIXME: Not implemented
        'misses': 0  # FIXME: Not implemented
    }