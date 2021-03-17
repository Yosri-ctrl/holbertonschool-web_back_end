#!/usr/bin/env python3
"""
Wait for 1 second
And generat a float between 0 and 10
"""
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
	"""
	Generate a float between 0 and 10
	And return it
	"""
	for _ in range(10):
		await asyncio.sleep(1)
		yield random.uniform(0, 10)
