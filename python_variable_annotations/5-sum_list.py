#!/usr/bin/env python3
"""
A type-annotated function sum_list which takes a list input_list of floats as
argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all numbers in the provided list.
    """

    return sum(input_list)
