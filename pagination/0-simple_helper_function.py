#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments page
and page_size.
"""


def index_range(page, page_size):
    """
    Calculate start and end indexes for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
