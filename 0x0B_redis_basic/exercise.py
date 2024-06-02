#!/usr/bin/env python3
'''Module Documentation'''
import redis
import uuid
from typing import Union
from typing import Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Decorator documentation'''
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = f'count:{method.__qualname__}'
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper

class Cache:
    '''Cache class documentation'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Generates a random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data) #stores data in redis using generated key
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''Retrieve data from redis'''
        data = self._redis.get(key)
        if key is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        '''Decode bytes to str'''
        return self.get(key, lambda k: k.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        '''Decode bytes to int'''
        return self.get(key, lambda k: int(k))
