#!/usr/bin/env python3
"""Task 0"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start index and end index
    corresponding to the range of indexes
    for those particular pagination parameters.
    """
    temp = page * page_size
    return (temp - page_size, temp)
