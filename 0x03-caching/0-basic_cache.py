#!/usr/bin/python3
"""
Creating a new class BasicCache
Inhereted from BaseCaching
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Creat a cashing system
    Inherited form BaseCaching
    """
    def put(self, key, item):
        """
        Append to cashe_data
        in key position with item as value
        """
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return content of cache_data
        And None if key is none
        """
        if key:
            return self.cache_data.get(key)
        else:
            return None
