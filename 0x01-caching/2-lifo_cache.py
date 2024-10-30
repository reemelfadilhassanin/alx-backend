#!/usr/bin/env python3
"""This module defines LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache inherits from BaseCaching and implements
       a LIFO caching system.
    """

    def __init__(self):
        """Initialize the LIFO cache.
        """
        super().__init__()

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

        # If the key already exists, remove it to update its position
        if key in self.cache_data:
            self.cache_data.pop(key)

        # Check if we need to discard an item
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Get the last key added to cache (LIFO)
            last_key = next(reversed(self.cache_data))
            discarded_item = self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")

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
