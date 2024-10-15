#!/usr/bin/env python3

import asyncio
from typing import List
from heapq import heappush, heappop

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    heap = []

    async def wait_and_add():
        delay = await task_wait_random(max_delay)
        heappush(heap, delay)

    tasks = [asyncio.create_task(wait_and_add()) for _ in range(n)]
    await asyncio.gather(*tasks)

    while heap:
        delays.append(heappop(heap))

    return delays
