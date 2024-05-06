#!/usr/bin/env python3
'''LIFO caching'''


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''LIFO Caching system'''
    def __init__(self):
        '''Constructor'''
        super().__init__()

    def put(self, key, item):
        '''Assigning value to dictionary'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = list(self.cache_data.keys())[-1]
            del self.cache_data[discarded]
            print("DISCARD:", discarded)
        self.cache_data[key] = item

    def get(self, key):
        '''Returns the value of key'''
        if key is not None or key in self.cache_data:
            return self.cache_data[key]
        return None
