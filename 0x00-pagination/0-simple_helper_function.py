#!/usr/bin/env python3
""" Module Pagination """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Function should return a tuple of size two containing a
        start index and an end index corresponding to the range of
        indexes to return in a list for those particular pagination parameters
    """
    end_idx = page * page_size
    start_idx = end_idx - page_size
    return (start_idx, end_idx)
