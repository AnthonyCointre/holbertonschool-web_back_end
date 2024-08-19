#!/usr/bin/env python3
import asyncio
import time
import importlib


async_comprehension_module = importlib.import_module('1-async_comprehension')
async_comprehension = async_comprehension_module.async_comprehension


async def measure_runtime():
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel.
    """

    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
