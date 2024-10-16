#!/usr/bin/env python3
""" Takes int, waits for a random delay """

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """make a random delay"""
    actual_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
