#!/usr/bin/env python3
"""Task 1"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start index and end index
    corresponding to the range of indexes
    for those particular pagination parameters.
    """
    temp = page * page_size
    return (temp - page_size, temp)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement Simple Pagination"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if end > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Implement Hypermedia Pagination"""
        start, end = index_range(page, page_size)
        data = self.get_page(page, page_size)
        pageCount = math.ceil(len(self.__dataset) / page_size)
        intel = {"page_size": len(data), "page": page,
                 "data": data, "total_pages": pageCount,
                 "next_page": page + 1 if end < len(self.__dataset) else None,
                 "prev_page": page - 1 if start > 0 else None,
                 }
        return intel
