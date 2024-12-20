#!/usr/bin/env python3
"""Module async_generator"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields 10 random numbers between 0 and 10,
    with a 1-second delay between each yield.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
