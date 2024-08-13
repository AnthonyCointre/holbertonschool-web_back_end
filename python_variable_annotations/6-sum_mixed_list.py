#!/usr/bin/env python3
"""
A type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of all numbers in the provided list, which can include
    both integers and floats.
    """

    return sum(mxd_lst)
