#!/usr/bin/env python3
"""
Caching System Module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching and implements
    a Least Frequently Used (LFU) caching system.
    """

    def __init__(self) -> None:
        """Initialize the LFUCache."""
        super().__init__()
        self.temp_list = {}

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.

        If the cache exceeds the limit set by BaseCaching.MAX_ITEMS,
        the least frequently used item will be discarded.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                least_frequent_key = min(self.temp_list,
                                         key=self.temp_list.get)
                self.temp_list.pop(least_frequent_key)
                self.cache_data.pop(least_frequent_key)
                print(f"DISCARD: {least_frequent_key}")
            if key not in self.temp_list:
                self.temp_list[key] = 0
            else:
                self.temp_list[key] += 1

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item stored under the key, or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.temp_list[key] += 1
        return self.cache_data.get(key)
