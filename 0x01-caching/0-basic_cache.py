#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Defines a basic caching class that stores information in key-value pairs.
    """

    def __init__(self):
        """
        Initializes the BasicCache class by calling the parent class's __init__ method.
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Stores a key-value pair in the cache.

        Args:
            key: The key to store.
            item: The value associated with the key.
        """
        if key is None or item is None:
            # If key or item is None, do nothing.
            return
        else:
            # Add the key-value pair to the cache_data dictionary.
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves the value associated with a given key from the cache.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the key, or None if the key is None or doesn't exist.
        """
        if key is not None and key in self.cache_data.keys():
            # If the key exists in the cache_data dictionary, return the corresponding value.
            return self.cache_data[key]
        else:
            # If the key is None or doesn't exist, return None.
            return None