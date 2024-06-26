#!/usr/bin/env python3
"""4. MRU Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching"""
    def __init__(self):
        """Initializes the class object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns to the cache dictionary"""
        if not key or not item:
            return
        if key not in self.cache_data.keys():
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                out, _ = self.cache_data.popitem(False)
                print("DISCARD:", out)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value of the passed key"""
        if key and key in self.cache_data.keys():
            self.cache_data.move_to_end(key, False)
        return self.cache_data.get(key, None)
