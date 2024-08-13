#!/usr/bin/env python3
"""
An async routine called wait_n that takes in 2 int arguments: n and max_delay.
You will spawn wait_random n times with the specified max_delay.
"""

import asyncio
from typing import List
import importlib

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously wait for n random delays
    and return a list of these delays in ascending order.
    """

    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
