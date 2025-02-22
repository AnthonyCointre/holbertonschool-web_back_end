#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.
"""

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an asynchronous
    comprehension over the async_generator coroutine.
    """

    return [number async for number in async_generator()]
