#!/usr/bin/env python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used (LFU) caching system.
    """

    def __init__(self):
        """
        Initializes the LFUCache class by calling the parent class's __init__ method.
        It also initializes an empty list to keep track of the usage order of keys in the cache,
        and an empty dictionary to keep track of the frequency of each key.
        """
        super().__init__()
        self.usage = []
        self.frequency = {}

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
                # If the cache is full and the new key is not already in the cache, remove the least frequently used item.
                least_frequency = min(self.frequency.values())
                least_frequency_keys = [k for k, v in self.frequency.items() if v == least_frequency]
                if len(least_frequency_keys) > 1:
                    # If there are multiple keys with the same least frequency, select the least recently used among them.
                    lru_lfu = {k: self.usage.index(k) for k in least_frequency_keys}
                    discard = min(lru_lfu, key=lru_lfu.get)
                else:
                    discard = least_frequency_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.usage[self.usage.index(discard)]
                del self.frequency[discard]

            # Update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1

            if key in self.usage:
                # If the key is already in the cache, remove it from the current position.
                del self.usage[self.usage.index(key)]
            self.usage.append(key)
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
            # If the key exists in the cache_data dictionary, update its usage position and frequency, and return the corresponding value.
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        else:
            # If the key is None or doesn't exist in the cache, return None.
            return None
