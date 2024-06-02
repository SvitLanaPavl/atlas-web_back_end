#!/usr/bin/env python3
'''Module Documentation'''
import redis
import uuid
from typing import Union
from typing import Callable, Optional


class Cache:
    '''Cache class documentation'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Generates a random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data) #stores data in redis using generated key
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        '''Recovering the original type'''
        data = self._redis.get(key)
        if key is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        '''Get str'''
        return self.get(key, lambda k: k.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        '''Get int'''
        return self.get(key, lambda k: int(k))
