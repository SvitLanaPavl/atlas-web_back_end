#!/usr/bin/env python3
'''Module Documentation'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collect 10 random numbers'''
    random_num = []
    async for num in async_generator():
        random_num.append(num)
        if len(random_num) == 10:
            break
    return random_num
