#!/usr/bin/env python3
'''MRU caching.
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    '''
    MRUCache class that provides a caching system with a Most Recently Used
    (MRU) eviction policy.

    When the cache reaches the Max number of items, the most recently
    used item is discarded if a new item needs to be added.
    '''

    def __init__(self):
        '''
        Initialize the MRUCache instance.

        Calls the parent class initializer and sets up an additional attribute
        to maintain the order of usage of keys.
        '''
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        '''
        Adds an item to the cache.
            If the cache exceeds the maximum number of items allowed, the most
            recently used item in the cache is discarded.
        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to store in the cache.

        Returns:
            None
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        '''
        Retrieves an item from the cache by key.
            If the key is accessed, it is considered recently used and moved
            to the end of the access order list.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The value associated with the key, or None if the key
                 is None or does not exist in the cache.
        '''
        if key is None or key not in self.cache_data:
            return None

        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data.get(key)
