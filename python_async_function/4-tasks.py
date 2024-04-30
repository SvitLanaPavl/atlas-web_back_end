#!/usr/bin/env python3
'''Module Documentation'''
from typing import List
import asyncio
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Returns list of delays in ascending order'''
    delay = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    for i in range(len(delay)):
        for j in range(i + 1, len(delay)):
            if delay[i] >= delay[j]:
                delay[i], delay[j] = delay[j], delay[i]
    return delay