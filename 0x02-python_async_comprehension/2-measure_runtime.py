#!/usr/bin/env python3

""" Async Comprehensions """

from time import time
from asyncio import gather


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ parallel comprehension """
    start = time()
    tasks = [async_comprehension() for x in range(4)]
    await gather(*tasks)
    end = time()
    return (end - start)
