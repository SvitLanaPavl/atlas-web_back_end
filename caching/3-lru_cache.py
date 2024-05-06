#!/usr/bin/env python3
'''LRU caching'''
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRU caching system'''
    def __init__(self):
        '''Constructor'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Assigns key to dictionary'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self.cache_data.popitem(last=False)
            print(f'DISCARD: {key}')
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = item

    def get(self, key):
        '''Returns the value'''
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
