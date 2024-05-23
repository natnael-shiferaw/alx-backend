#!/usr/bin/env python3
"""
Basic dictionary caching module
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.

    This cache does not have a limit on the number of items it can store.
    """

    def put(self, key, item):
        """
        Add an item to the cache.
        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.
        If either key or item is None, this method does nothing.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            The item stored under the key, or None if the key does not exist.
        """
        return self.cache_data.get(key)
