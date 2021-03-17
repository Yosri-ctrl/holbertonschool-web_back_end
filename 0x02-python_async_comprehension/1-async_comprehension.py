#!/usr/bin/env python3
"""
Generat a ranf=do float
and return it in a list
"""
import asyncio
import random
from typing import List, Generator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Return a list of
    Containig a generated float
    """
    return [i async for i in async_generator()]
