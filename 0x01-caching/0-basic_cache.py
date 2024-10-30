#!/usr/bin/env python3
"""BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BaseCaching and implements
       a simple caching system with no item limit.
    """

    def put(self, key, item):
        """Assign an item to the cache.

        Args:
            key: The key to store the item under.
            item: The item to store in the cache.

        If key or item is None, this method does not do anything.
        """
        if key is None or item is None:
            return
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
