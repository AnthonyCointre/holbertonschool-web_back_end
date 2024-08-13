#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
"""

import asyncio
from typing import List
import importlib

task_wait_random = importlib.import_module('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Schedule and run n asynchronous tasks that wait for random delays,
    and return their results in the order of completion.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
