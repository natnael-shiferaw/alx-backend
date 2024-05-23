#!/usr/bin/env python3
"""
LRU Caching Module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that inherits from BaseCaching and implements
    a Least Recently Used (LRU) caching system.
    """

    def __init__(self):
        """
        Initialize the LRUCache.
        """
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.

        If the cache exceeds the limit set by BaseCaching.MAX_ITEMS,
        the least recently used item will be discarded.
        """
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                item_discarded = next(iter(self.lru_order))
                del self.cache_data[item_discarded]
                self.lru_order.popitem(last=False)
                print("DISCARD:", item_discarded)

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item stored under the key, or None if the key does not exist.
        """
        if key in self.cache_data:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
        return None
