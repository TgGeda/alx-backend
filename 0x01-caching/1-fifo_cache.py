#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache implements a First-In-First-Out (FIFO) caching system.
    """

    def __init__(self):
        """
        Initializes the FIFOCache class by calling the parent class's __init__ method.
        It also initializes an empty list to keep track of the order of keys in the cache.
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Caches a key-value pair in the cache.

        Args:
            key: The key to cache.
            item: The value associated with the key.
        """
        if key is None or item is None:
            # If either key or item is None, do nothing.
            return
        else:
            cache_size = len(self.cache_data)
            if cache_size >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                # If the cache is full and the new key is not already in the cache, remove the oldest item.
                oldest_key = self.key_order[0]
                print("DISCARD: {}".format(oldest_key))
                del self.cache_data[oldest_key]
                del self.key_order[0]
            self.key_order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with a given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is None or doesn't exist in the cache.
        """
        if key is not None and key in self.cache_data:
            # If the key exists in the cache_data dictionary, return the corresponding value.
            return self.cache_data[key]
        else:
            # If the key is None or doesn't exist in the cache, return None.
            return None
