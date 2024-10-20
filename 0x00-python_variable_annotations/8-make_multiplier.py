#!/usr/bin/env python3
"""Module make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier and returns a function
        that multiplies a float by a multiplier.

    args:
        multiplier: Float to multiply by

    return:
        Function that multiplies a float by a multiplier
    """
    return lambda x: x * multiplier
