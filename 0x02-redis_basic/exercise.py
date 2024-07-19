#!/usr/bin/env python3
"""Redis basic operations"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """Decorator to count how many times a method is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(input_key, str(args))

        output = method(self, *args, **kwargs)

        self._redis.rpush(output_key, str(output))

        return output
    return wrapper

def replay(method: Callable) -> None:
    """Display the history of calls of a particular function"""
    r = redis.Redis()
    method_name = method.__qualname__
    calls_count = r.get(method_name).decode("utf-8")
    print(f"{method_name} was called {calls_count} times:")

    inputs = r.lrange(f"{method_name}:inputs", 0, -1)
    outputs = r.lrange(f"{method_name}:outputs", 0, -1)

    for input, output in zip(inputs, outputs):
        input = input.decode("utf-8")
        output = output.decode("utf-8")
        print(f"{method_name}(*{input}) -> {output}")

class Cache:
    """Cache class for Redis operations"""

    def __init__(self):
        """Initialize the Cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis and return a unique key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis and convert it if necessary"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve a string from Redis"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve an integer from Redis"""
        return self.get(key, fn=int)

if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))

    s1 = cache.store("first")
    s2 = cache.store("secont")
    s3 = cache.store("third")

    inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
    outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

    print("inputs:", inputs)
    print("outputs:", outputs)

    replay(cache.store)
