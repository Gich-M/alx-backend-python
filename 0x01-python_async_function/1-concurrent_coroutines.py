#!/usr/bin/env python3
"""Module Task 1"""

import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for n random tasks and returns their delays."""
    waits = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(waits)
