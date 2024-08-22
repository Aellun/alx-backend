#!/usr/bin/python3
BaseCaching = __import__('base_caching').BaseCaching

'''class BasicCache that inherits from BaseCaching and is a caching system
    Requirement:
            must use self.cache_data -
            dictionary from the parent class BaseCaching
            This caching system doesn’t have limit
            def put(self, key, item):
            Must assign to the dictionary self.cache_data
            the item value for the key key.
            If key or item is None, this method should not do anything.
            def get(self, key):
            Must return the value in self.cache_data linked to key.
            If key is None or if the key doesn’t exist in self.cache_data
            return None.
'''


class BasicCache(BaseCaching):
    '''
    This class implements a simple caching system
    with no limit on the number of items it can store.
    The cache is stored in a dictionary, with methods
    to add items to the cache and retrieve them.
    '''

    def __init__(self):
        '''Initialize the BasicCache instance by calling
            the parent class initializer.'''
        super().__init__()

    def put(self, key, item):

        '''
        Add an item to the cache.

        Args:
            key (str): The key under which the item should be stored.
            item (any): The item to store in the cache.
        Returns:
            None: If either key or item is None, the method does nothing.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Retrieve an item from the cache by key.
        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The value associated with the key,
            or None if the key is None
            or does not exist in the cache.
        '''
        if key is None:
            return None
        return self.cache_data.get(key)
