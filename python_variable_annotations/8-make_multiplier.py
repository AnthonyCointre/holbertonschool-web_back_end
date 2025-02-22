#!/usr/bin/env python3
"""
A type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies its input by a specified
    multiplier.
    """

    def multiply_by(x: float) -> float:
        """
        Multiply the input by the specified multiplier.
        """

        return x * multiplier
    return multiply_by
