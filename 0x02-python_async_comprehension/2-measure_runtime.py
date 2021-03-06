#!/usr/bin/env python3
"""
Generat a ranf=do float
and return it in a list
"""
import asyncio
import random
from typing import List, Generator
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Run async_comprehension four times
    Return the time it took to execute
    """
    time_now = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.perf_counter() - time_now
