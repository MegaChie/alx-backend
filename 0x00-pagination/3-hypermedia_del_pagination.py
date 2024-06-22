#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Implement an improved Hypermedia Pagination"""
        data = self.indexed_dataset()
        assert index is not None and 0 <= index <= max(data.keys())
        pageData = []
        count = 0
        nextIndex = None
        start = index if index else 0
        for pos, elem in data.items():
            if pos >= start and count < page_size:
                pageData.append(elem)
                count += 1
                continue
            if count == page_size:
                nextIndex = pos
                break
        intel = {"index": index, "next_index": nextIndex,
                 "page_size": len(pageData), "data": pageData}
        return intel
