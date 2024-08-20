#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.
"""

import importlib


async_generator_module = importlib.import_module('0-async_generator')
async_generator = async_generator_module.async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using an asynchronous
    comprehension over the async_generator coroutine.
    """

    return [number async for number in async_generator()]
