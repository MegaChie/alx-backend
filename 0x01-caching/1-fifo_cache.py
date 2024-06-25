#!/usr/bin/env python3
"""Task 1"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """BaseCaching"""
    def __init__(self):
        """Initializes the class object"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns to the cache dictionary"""
        if not key or not item:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            out, _ = self.cache_data.popitem(False)
            print("DISCARD:", out)

    def get(self, key):
        """Returns the value of the passed key"""
        if not key or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
