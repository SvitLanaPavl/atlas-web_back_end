#!/usr/bin/env python3
'''Module Documentation'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for random delay'''
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
