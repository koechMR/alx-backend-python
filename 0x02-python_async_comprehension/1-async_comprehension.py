#!/usr/bin/env python3

""" Comprehension """

from typing import List
from asyncio import sleep
from random import uniform


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ async   """
    x = [j async for j in async_generator()]
    return x
