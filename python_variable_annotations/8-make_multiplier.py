#!/usr/bin/env python3
'''Module documentation'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Multiples a float by multiplier'''
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func
