#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n
wait_random = __import__('0-basic_async_syntax').wait_random


tasks = [wait_random(4) for _ in range(5)]
asyncio.gather(* tasks)

print(x)
# print(wait_random())
# print(wait_random(5))
# print(wait_random(15))

# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))
