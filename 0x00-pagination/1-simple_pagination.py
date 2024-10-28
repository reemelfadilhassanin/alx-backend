#!/usr/bin/env python3
"""
Module to define the Server class
for paginating a dataset of popular baby names.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size must be greater than 0")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The page of the dataset.
        """
        assert isinstance(page, int) and page > 0,
        "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0,
        "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        # Return the relevant slice of the dataset
        return data[start_index:end_index] if start_index < len(data) else []
