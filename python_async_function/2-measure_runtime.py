#!/usr/bin/env python3
"""
A measure_time function with integers n
and max_delay as arguments thatnmeasures the total execution time for wait_n,
and returns total_time / n.
"""

import time
import asyncio
import importlib

wait_n = importlib.import_module('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average time it takes to run wait_n function.
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
