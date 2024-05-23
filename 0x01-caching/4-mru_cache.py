#!/usr/bin/env python3
"""
MRU Caching Module
"""

from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements
    a Most Recently Used (MRU) caching system.
    """

    def __init__(self):
        """
        Initialize the MRUCache.
        """
        super().__init__()
        self.mru_order = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key (str): The key under which the item is stored.
            item (any): The item to store in the cache.

        If the cache exceeds the limit set by BaseCaching.MAX_ITEMS,
        the most recently used item will be discarded.
        """
        if not key or not item:
            return

        self.cache_data[key] = item
        self.mru_order[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.mru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.mru_order) > BaseCaching.MAX_ITEMS:
            self.mru_order.popitem(last=False)

        self.mru_order.move_to_end(key, last=False)

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The item stored under the key, or None if the key does not exist.
        """
        if key in self.cache_data:
            self.mru_order.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
