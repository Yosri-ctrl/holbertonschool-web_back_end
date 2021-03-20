#!/usr/bin/python3
"""
Creating a new class FIFOCache
Inhereted from BaseCaching
Basd on the FIFO algo (first in first out)
If the chache pass the limit (MAX_ITEMS)
It delete the fist item created
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    """
    def put(self, key, item):
        """
        """
        if key or item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(first))
                del self.cache_data[first]
                
    def get(self, key):
        """
        """
        return self.cache_data.get(key)
