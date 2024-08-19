#!/usr/bin/env python3
'''Implement a method named get_page that takes two integer arguments
    page with default value 1 and page_size with default value 10.
    Use assert to verify that both arguments are integers greater than 0.
    Use index_range to find the correct indexes to paginate the dataset
    correctly and return the appropriate page of the dataset
    If the input arguments are out of range for the dataset,
    an empty list should be returned.
'''

import csv
import math
from typing import List


def index_range(page, page_size):
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
    '''Server class to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''Cached dataset
        '''
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
