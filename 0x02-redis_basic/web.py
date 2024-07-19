#!/usr/bin/env python3
"""Web cache and tracker"""

import redis
import requests
from functools import wraps
from typing import Callable

redis_client = redis.Redis()

def cache_with_expiration(expiration: int = 10) -> Callable:
    """Decorator to cache the result of a function with expiration"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            """Wrapper function"""
            # Increment the access count
            redis_client.incr(f"count:{url}")

            # Check if the result is cached
            cached_result = redis_client.get(f"cache:{url}")
            if cached_result:
                return cached_result.decode('utf-8')

            # If not cached, call the original function
            result = func(url)

            # Cache the result with expiration
            redis_client.setex(f"cache:{url}", expiration, result)

            return result
        return wrapper
    return decorator

@cache_with_expiration()
def get_page(url: str) -> str:
    """Obtain the HTML content of a particular URL"""
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com"
    print(get_page(url))
    print(get_page(url))
    print(redis_client.get(f"count:{url}"))
