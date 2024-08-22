#!/usr/bin/env python3
'''LIFO caching.
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''
    LIFOCache class that provides a caching system with a Last-In-First-Out
    (LIFO) eviction policy.

    When the cache reaches the Max number of items, the most recently
    added item is discarded if a new item needs to be added.
    '''

    def __init__(self):
        '''
        Initialize the LIFOCache instance.

        Calls the parent class initializer and sets up an additional attribute
        to maintain the order of keys.
        '''
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        '''
        Adds an item to the cache.
        If the cache exceeds the Maax number of items allowed, the most
        recently added item in the cache is discarded
        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to store in the cache.

        Returns:
            None
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        self.last_key = key

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
