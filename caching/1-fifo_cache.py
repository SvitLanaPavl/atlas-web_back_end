#!/usr/bin/env python3
'''FIFO caching'''


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO caching system'''
    def __init__(self):
        '''Constructor'''
        super().__init__()

    def put(self, key, item):
        '''Assigning value for the key'''
        if key and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.cache_data))
            del self.cache_data[discarded]
            print(f'DISCARD: {discarded}')
        return
    def get(self, key):
        '''Returns value linked to key'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
