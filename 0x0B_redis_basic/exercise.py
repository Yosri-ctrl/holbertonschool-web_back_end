#!/usr/bin/env python3
"""Cashe Module
"""
from redis import Redis
from uuid import uuid4
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """
        """
        self._redis.rpush("{}:inputs".format(key), str(args))
        output = method(self, *args)
        self._redis.rpush("{}:outputs".format(key), str(output))
        return output
    return wrapper


class Cache():
    """Cashe class
    """
    def __init__(self):
        """initialise redis
        """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data in redis using rand key
        """
        key = str(uuid4())
        # print(key)
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn=None):
        """convert the data back to the desired format
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        """
        return int.from_bytes(data, byteorder)
