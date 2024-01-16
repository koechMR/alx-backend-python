#!/usr/bin/env python3

""" Comprehensions """

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Async """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
