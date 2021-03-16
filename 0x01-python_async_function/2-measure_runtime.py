#!/usr/bin/env python3
"""mesure runtime"""
from asyncio import run
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Calculate the time wait_n take to complete
    and return it
    """
    time_prev = time()
    run(wait_n(n, max_delay))
    return (time() - time_prev) / n
