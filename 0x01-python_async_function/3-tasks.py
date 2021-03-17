#!/usr/bin/env python3
"""task 3"""
from asyncio import run, create_task, Task
from time import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Take the max_delay and pass it tp wait_random
    and Return it
    """
    return (create_task(wait_random(max_delay)))
