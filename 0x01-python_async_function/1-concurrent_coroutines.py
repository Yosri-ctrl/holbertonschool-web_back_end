#!/usr/bin/env python3
"""concurrent croutine"""
from random import uniform
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Wait and Return random nbr between 0 and max_delay
    """
    array: List[float] = []
    delays: List[float] = []
    for _ in range(n):
        array.append((wait_random(max_delay)))
    for delay in asyncio.as_completed(array):
        delays.append(await delay)
    return delays
