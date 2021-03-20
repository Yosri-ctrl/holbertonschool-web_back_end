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
    FIFO (first in first out) cache system
    if the cache dict pass the limit 
    delete the first element created
    """
    def put(self, key, item):
        """
        Add to the cache_data
        And delete the fist element if full
        """
        if key or item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                print('DISCARD: {}'.format(first))
                del self.cache_data[first]
                
    def get(self, key):
        """
        Return the value of key in cache_data
        And None if key is none
        """
        if key:
            return self.cache_data.get(key)
        else:
            return None
