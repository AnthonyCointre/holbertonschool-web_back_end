#!/usr/bin/env python3
"""
Write a coroutine called async_generator that takes no arguments.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that generates a sequence of 10 random floating-point numbers
    between 0 and 10.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
