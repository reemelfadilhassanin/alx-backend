#!/usr/bin/env python3
"""
Module to
calculate the index range for pagination.
"""

from typing import Tuple


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
