#!/usr/bin/env python3
'''FIFO caching.
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    FIFOCache class that provides a caching system with a First-In-First-Out
    eviction policy.

    When the cache reaches the maximum number of items, the oldest item
    (the first one added) is discarded.
    '''

    def __init__(self):
        '''
        Initialize the FIFOCache instance.

        Calls the parent class initializer and sets up an additional attribute
        to maintain the order of keys.
        '''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''
        Adds an item to the cache.
        If the cache exceeds the max number of items allowed, the oldest
        item in the cache is discarded.
        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to store in the cache.

        Returns:
            None
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        '''
        Retrieves an item from the cache by key.
        Args:
            key (str): The key of the item to retrieve.
        Returns:
            any: The value associated with the key, or None if the key
                 is None or does not exist in the cache.
        '''
        return self.cache_data.get(key, None)
