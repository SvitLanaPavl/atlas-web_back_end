#!/usr/bin/env python3
'''LRU caching'''


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRU caching system'''
    def __init__(self):
        '''Constructor'''
        super().__init__()

    def put(self, key, item):
        '''Assigns key to dictionary'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.cache_data))
            del self.cache_data[discarded]
            print(f'DISCARDED: {discarded}')
        self.cache_data[key] = item

    def get(self, key):
        '''Returns the value'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
