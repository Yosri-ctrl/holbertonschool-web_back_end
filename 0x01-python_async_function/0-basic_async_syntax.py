#!/usr/bin/env python3
"""basic async sytax"""
from random import uniform
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait and Return random nbr between 0 and max_delay
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
