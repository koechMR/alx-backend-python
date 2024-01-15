#!/usr/bin/env python3
""" async here """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ Tasks to wait in randome """
    task = create_task(wait_random(max_delay))
    return task
