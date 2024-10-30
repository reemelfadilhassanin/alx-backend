#!/usr/bin/env python3
"""This module defines LIFOCache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching and implements
       a LIFO caching system.
    """

    def __init__(self):
        """Initialize the LIFO cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign an item to the cache using LIFO algorithm.

        Args:
            key: The key to store the item under.
            item: The item to store in the cache.

        If key or item is None, this method does not do anything.
        If the cache exceeds MAX_ITEMS, discard the last item.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)
