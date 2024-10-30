#!/usr/bin/env python3
"""MRU Caching
    """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class `MRUCache` that inherits from
       `BaseCaching` and implements a caching system
       that discards the most recently used item.
    """

    def __init__(self):
        """Initialize the cache
        """
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key to store the item.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        # If the key is already in the cache, remove it first
        if key in self.cache_data:
            del self.cache_data[key]
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the last inserted item (most recently used)
            mru_key = next(reversed(self.cache_data))  # Get the last key
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)
        # Add the new item
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The value associated with the key, or None if not found.
        """
        return self.cache_data.get(key, None)
