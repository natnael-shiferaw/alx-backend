#!/usr/bin/env python3
"""
LIFO Caching Module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching and implements
    a Last-In-First-Out (LIFO) caching system.
    """

    def __init__(self):
        """
        Initialize the LIFOCache.
        """
        super().__init__()
        self.key_indexes = []

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.

        If the cache exceeds the limit set by BaseCaching.MAX_ITEMS,
        the most recently added item will be discarded.
        """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key in self.cache_data:
                    del self.cache_data[key]
                    self.key_indexes.remove(key)
                else:
                    item_discarded = self.key_indexes.pop()
                    del self.cache_data[item_discarded]
                    print("DISCARD:", item_discarded)

            self.cache_data[key] = item
            self.key_indexes.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item stored under the key, or None if the key does not exist.
        """
        return self.cache_data.get(key)
