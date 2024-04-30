#!/usr/bin/env python3
'''Module Documentation'''
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Yields a random number in asynchronous operation'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
