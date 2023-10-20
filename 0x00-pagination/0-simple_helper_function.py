#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for a given page and page size in a paginated list.

    Args:
        page (int): The page number to return (pages are 1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indices of the range.

    """

    # Calculate the start and end indices for the given page and page size
    start_index = 0  # The start index of the range
    end_index = 0  # The end index of the range

    # Iterate over each page to calculate the indices
    for current_page in range(page):
        start_index = end_index  # Update the start index to be the previous end index
        end_index += page_size  # Increment the end index by the page size to move the range

    # Return the calculated start and end indices as a tuple
    return (start_index, end_index)
