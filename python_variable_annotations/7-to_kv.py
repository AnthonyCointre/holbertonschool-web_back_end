#!/usr/bin/env python3
"""
A type-annotated function to_kv that takes a string k and an int OR float v as
arguments and returns a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Transform a key-value pair into a tuple where the key remains the same and
    the value is the square of the input value.
    """

    return (k, float(v ** 2))
