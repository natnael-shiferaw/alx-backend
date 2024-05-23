#!/usr/bin/env python3
"""
FIFO Caching Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and implements
    a First-In-First-Out (FIFO) caching system.
    """

    def __init__(self):
        """
        Initialize the FIFOCache.
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
        the first added item (FIFO) will be discarded.
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                item_discarded = self.key_indexes.pop(0)
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
