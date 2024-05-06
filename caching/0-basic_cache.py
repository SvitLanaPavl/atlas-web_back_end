#!/usr/bin/env python3
'''Basic dictionary'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Basic dictionary class'''

    def put(self, key, item):
        '''Assigns to the dictionary the item value for the key'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Returns the value of cache_data linked to key'''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
