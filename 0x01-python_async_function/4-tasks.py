#!/usr/bin/env python3
"""Delay many times"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Delay many times"""

    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for task in tasks:
        delays.append(await task)
    return delays
