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
	time_now = time.time()
	await asyncio.gather(*[async_comprehension() for _ in range(4)])
	return time_now - time.time()
