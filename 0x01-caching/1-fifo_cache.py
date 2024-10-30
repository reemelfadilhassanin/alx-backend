#!/usr/bin/env python3
"""this module defines FIFOCache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and implements
       a FIFO caching system.
    """

    def __init__(self):
        """Initialize the FIFO cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign an item to the cache using FIFO algorithm.

        Args:
            key: The key to store the item under.
            item: The item to store in the cache.

        If key or item is None, this method does not do anything.
        If the cache exceeds MAX_ITEMS, discard the first item.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            # Check if we need to discard an item
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Get the first key added to cache (FIFO)
                first_key = next(iter(self.cache_data))
                discarded_item = self.cache_data.pop(first_key)
                print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache.

        Args:
            key: The key for which to retrieve the item.

        Returns:
            The value associated with the key, or None if key
            is None or does not exist in the cache.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
