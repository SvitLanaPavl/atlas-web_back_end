#!/usr/bin/env python3
'''Module Documentation'''
import redis
import uuid
from typing import Union


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
