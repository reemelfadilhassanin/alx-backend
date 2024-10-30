#!/usr/bin/env python3
"""LRUCache module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache inherits from BaseCaching and implements
       an LRU caching system.
    """

    def __init__(self):
        """Initialize the LRU cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.

        Args:
            key: The key to store the item.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item  # Update existing item
        self.cache_data.move_to_end(key)  # Mark as recently used

    def get(self, key):
        """Retrieves an item by key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The value associated with the key, or None if not found.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)  # Mark as recently used
            return self.cache_data[key]
        return None
