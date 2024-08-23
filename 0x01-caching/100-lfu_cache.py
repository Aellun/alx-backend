#!/usr/bin/env python3
'''LFU caching
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    LFUCache class that provides a caching system with a Least Frequently Used
    (LFU) eviction policy. If multiple items have the same frequency, the Least
    Recently Used (LRU) item is discarded first.
    '''

    def __init__(self):
        '''
        Initialize the LFUCache instance.

        Calls the parent class initializer and sets up additional attributes
        to track the frequency of access and the order of usage of keys.
        '''
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        ''''
        Adds an item to the cache.

            If the cache exceeds the Max number of items allowed, the least
            frequently used item in the cache is discarded.
            If multiple items have the same frequency,
            the least recently used item is discarded.
            Args:
                key (str): The key under which the item should be stored.
                item (any): The item to store in the cache.
            Returns:
                None
        '''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_least_frequent()

            self.cache_data[key] = item
            self.frequency[key] = 1

        self.usage_order.append(key)

    def get(self, key):
        '''
        Retrieves an item from the cache by key.
            If the key is accessed, its frequency count is incremented, and
            it is moved to the end of the usage order list.
            Args:
                key (str): The key of the item to retrieve.
            Returns:
                any: The value associated with the key, or None if the key
                    is None or does not exist in the cache.
        '''
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]

    def _evict_least_frequent(self):
        '''
        Evicts the least frequently used item from the cache.
            If there are multiple items with the same frequency, the least
            recently used item is discarded.
        '''
        min_freq = min(self.frequency.values())
        candidates = [
            key for key in self.usage_order if self.frequency[key] == min_freq
            ]

        if candidates:
            evict_key = candidates[0]
            self.usage_order.remove(evict_key)
            del self.cache_data[evict_key]
            del self.frequency[evict_key]
            print(f"DISCARD: {evict_key}")
