#!/usr/bin/env python3
"""Task 5: Least Frequently Used caching module.
"""
from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = {}
        self.freq_map = defaultdict(list)  # Maps frequencies to keys
        self.key_freq = {}  # Maps keys to their frequencies
        self.min_freq = 0  # Tracks the minimum frequency

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing item
            self.cache_data[key] = item
            self.__update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove least frequently used item
                lfu_key = self.freq_map[self.min_freq].pop(0)
                if not self.freq_map[self.min_freq]:
                    del self.freq_map[self.min_freq]
                self.cache_data.pop(lfu_key)
                self.key_freq.pop(lfu_key)
                print("DISCARD:", lfu_key)

            # Add new item
            self.cache_data[key] = item
            self.key_freq[key] = 1
            self.freq_map[1].append(key)
            self.min_freq = 1

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the accessed key
        self.__update_frequency(key)
        return self.cache_data[key]

    def __update_frequency(self, key):
        """Updates the frequency of a key when accessed or modified."""
        freq = self.key_freq[key]
        self.key_freq[key] += 1
        new_freq = freq + 1

        # Update frequency maps
        self.freq_map[freq].remove(key)
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        self.freq_map[new_freq].append(key)
