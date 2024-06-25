#!/usr/bin/env python3
"""Task 0. Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic caching"""
    def put(self, key, item):
        """Assign to the dictionary cache_data"""
        if not key or not item:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to passed key"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
