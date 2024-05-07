#!/usr/bin/env python3
'''MRU caching'''


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''MRU Caching system'''
    def __init__(self):
        '''Constructor'''
        super().__init__()

    def put(self, key, item):
        '''Assign key to dict'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = next(reversed(self.cache_data))
            del self.cache_data[discard]
            print(f'DISCARD: {discard}')
        self.cache_data[key] = item

    def get(self, key):
        '''Returns the value'''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
