#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a
    database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i]
                                      for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset with
        deletion-resilient hypermedia information.

        Args:
            index (int): The starting index (0-indexed).
            page_size (int): The number of items per page.

        Returns:
            dict: A dictionary containing hypermedia pagination details.
        """
        assert index is None or (0 <= index < len(self.__indexed_dataset)),
        "index out of range"

        if index is None:
            index = 0

        data = []
        current_index = index

        for _ in range(page_size):
            while current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
                current_index += 1
                if len(data) == page_size:
                    break
            if len(data) == page_size:
                break

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': current_index
            if current_index in self.__indexed_dataset else None
        }
