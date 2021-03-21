#!/usr/bin/python3
"""

"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO (last in first out) cache system
    if the cache dict pass the limit
    delete the last element created
    """
    def put(self, key, item):
        """
        Add to the cache_data
        And delete the fist element if full
        """
        if key or item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.last))
                del self.cache_data[self.last]
            self.last = key

    def get(self, key):
        """
        Return the value of key in cache_data
        And None if key is none
        """
        if key:
            return self.cache_data.get(key)
        else:
            return None
