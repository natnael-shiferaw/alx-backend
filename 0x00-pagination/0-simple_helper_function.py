#!/usr/bin/env python3
"""Contains a simple helper function for pagination."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing start and end indexes for pagination.

    Args:
        page: The current page number.
        page_size: The number of items per page.

    Returns:
        A tuple containing the start and end indexes for
        the given pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
