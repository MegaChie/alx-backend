#!/usr/bin/env python3
""""3. LRU Caching"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""
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
                out, _ = self.cache_data.popitem(True)
                print("DISCARD:", out)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value of the passed key"""
        if not key or key not in self.cache_data.keys():
            return
        return self.cache_data[key]
