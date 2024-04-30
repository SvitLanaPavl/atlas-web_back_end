#!/usr/bin/env python3
'''Module Documentation'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Collect 10 random numbers'''
    return [num async for num in async_generator()]
