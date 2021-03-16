#!/usr/bin/env python3
"""task 3"""
from asyncio import run, create_task, Task
from time import time
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> Task:
    return (create_task(wait_random(max_delay)))
