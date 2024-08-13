#!/usr/bin/env python3
"""
A function task_wait_random that takes an integer max_delay
and returns a asyncio.Task.
"""

import asyncio
import importlib

wait_random = importlib.import_module('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio Task that runs the wait_random function.
    """

    return asyncio.create_task(wait_random(max_delay))
