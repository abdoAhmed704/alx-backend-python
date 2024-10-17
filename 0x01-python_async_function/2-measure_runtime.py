#!/usr/bin/env python3
""" time of runtime"""
from typing import List
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ takes n int and max dalay and deal with the
    wait_n function"""
    time1: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    time2: float = time.time()
    return (time2 - time1) / n
