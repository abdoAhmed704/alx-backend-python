#!/usr/bin/env python3
"""Delay many times"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Delay many times"""

    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    print("tasks===========", tasks)
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
