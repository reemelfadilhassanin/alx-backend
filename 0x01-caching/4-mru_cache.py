#!/usr/bin/env python3
"""Task 4: MRU Caching.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class `MRUCache` that inherits
       from `BaseCaching` and is a caching system
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            # If adding this item exceeds the max limit, discard the MRU item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)  # Mark as recently used
        else:
            self.cache_data[key] = item  # Update existing item
            self.cache_data.move_to_end(key)  # Mark as recently used

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)  # Mark as recently used
        return self.cache_data.get(key, None)
