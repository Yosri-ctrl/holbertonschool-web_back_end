#!/usr/bin/env python3
"""concurrent croutine"""
from random import uniform
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return a list of all delayes
    """
    array: List[float] = []
    delays: List[float] = []
    for _ in range(n):
        array.append((task_wait_random(max_delay)))
    for delay in asyncio.as_completed(array):
        delays.append(await delay)
    return delays
