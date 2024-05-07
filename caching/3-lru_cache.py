#!/usr/bin/env python3
'''LRU caching'''
from collections import OrderedDict


BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''LRU caching system'''
    def __init__(self):
        '''Constructor'''
        super().__init__()
        self.order = OrderedDict()

    def put(self, key, item):
        '''Assigns key to dictionary'''
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = next(iter(self.order))
            del self.order[discarded]
            del self.cache_data[discarded]
            print(f'DISCARD: {discarded}')
        self.cache_data[key] = item
        self.order[key] = True

    def get(self, key):
        '''Returns the value'''
        if key is None or key not in self.cache_data:
            return None
        self.order.move_to_end(key)
        return self.cache_data[key]
