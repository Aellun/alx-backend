#!/usr/bin/env python3
'''function named index_range that takes two integer arguments
    page and page_size. The function should return
    a tuple of size two containing a start index and an
    end index corresponding to the range of indexes
    to return in a list for thoseparticular pagination parameters.
'''


def index_range(page, page_size):
    ''''
    Calculate the start and end index for pagination.
        Args:
            - page (int): The page number (1-indexed).
            - page_size (int): The number of items per page.
        Returns:
            -tuple: A tuple containing the start index and end index.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
