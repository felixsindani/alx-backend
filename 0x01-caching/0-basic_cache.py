#!/usr/bin/env python3
""" caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache
    """
    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item value for the key
        """
        if not (key is None or item is None):
            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data[key]
