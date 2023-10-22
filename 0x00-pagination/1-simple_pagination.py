#!/usr/bin/env python3
"""
Defines class Server that paginates a database of popular baby names
"""
import csv
import math
from typing import List, Tuple


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

class Server:
    """
    Server class that paginates a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self._dataset = None

    def _load_dataset(self) -> List[List]:
        """
        Loads the dataset from a CSV file and caches it.

        Returns:
            List[List]: The loaded dataset.

        """
        if self._dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self._dataset = dataset[1:]  # Skip the header row
        return self._dataset

    def get_page(self, page_number: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the requested page from the dataset.

        Args:
            page_number (int): The page number to retrieve (1-indexed).
            page_size (int): The number of records per page.

        Returns:
            List[List]: The data corresponding to the requested page.

        Raises:
            AssertionError: If page_number or page_size is not a positive integer.

        """
        assert isinstance(page_number, int) and page_number > 0, "Page number must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self._load_dataset()
        data_length = len(dataset)
        try:
            start_index, end_index = calculate_index_range(page_number, page_size)
            return dataset[start_index:end_index]
        except IndexError:
            return []
