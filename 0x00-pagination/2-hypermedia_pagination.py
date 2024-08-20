#!/usr/bin/env python3
'''Implement a get_hyper method that takes the same arguments
    (and defaults) as get_page and returns a dictionary
    containing the following key-value pairs:

        --page_size: the length of the returned dataset page
        --page: the current page number
        --data: the dataset page (equivalent to return from previous task)
        --next_page: number of the next page, None if no next page
        --prev_page: number of the previous page, None if no previous page
        --total_pages: the total number of pages in the dataset as an integer
        --Make sure to reuse get_page in your implementation.
'''

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Calculate the start and end index for pagination.
        Args:
        - page (int): The page number (1-indexed).
        - page_size (int): The number of items per page.
        Returns:
        - tuple: A tuple containing the start index and end index.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    '''Server class to paginate a database of popular baby names.'''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''Initializes a new Server instance.'''
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset.'''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Get a specific page of the dataset.
            Args:
            - page (int): The page number (1-indexed). Defaults to 1.
            - page_size (int): The number of items per page. Defaults to 10.
            Returns:
            - List[List]: A list of rows for the specified page.
        '''
        # Validate input arguments
        if not isinstance(page, int) or not isinstance(page_size, int):
            raise ValueError("Both page and page_size must be integers.")
        if page <= 0 or page_size <= 0:
            raise ValueError("Both page and page_size must be greater than 0.")

        # Get the dataset
        dataset = self.dataset()

        # Calculate the index range
        start_index, end_index = index_range(page, page_size)

        # Return the appropriate page of the dataset
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        '''
        Get a specific page of data with additional pagination info.
            Args:
            - page (int): The page number (1-indexed). Defaults to 1.
            - page_size (int): The number of items per page. Defaults to 10.
            Returns:
            - Dict[str, Any]: A dictionary containing pagination info and data.
        '''
        # Get the current page data using get_page
        data = self.get_page(page, page_size)

        # Calculate the total number of pages
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        # Determine next and previous page numbers
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Return the hypermedia pagination info
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
