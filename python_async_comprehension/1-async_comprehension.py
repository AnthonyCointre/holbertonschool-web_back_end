#!/usr/bin/env python3
import importlib


async_generator_module = importlib.import_module('0-async_generator')
async_generator = async_generator_module.async_generator


async def async_comprehension():
    """
    Coroutine that collects 10 random numbers using an asynchronous
    comprehension over the async_generator coroutine.
    """

    return [number async for number in async_generator()]
