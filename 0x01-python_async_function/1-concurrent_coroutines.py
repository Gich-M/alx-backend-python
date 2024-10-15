#!/usr/bin/env python3

import asyncio
from typing import List
from heapq import heappush, heappop

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    heap = []

    async def wait_and_add():
        delay = await wait_random(max_delay)
        heappush(heap, delay)

    tasks = [asyncio.create_task(wait_and_add()) for _ in range(n)]
    await asyncio.gather(*tasks)

    while heap:
        delays.append(heappop(heap))

    return delays
