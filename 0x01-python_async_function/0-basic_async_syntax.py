#!/usr/bin/env python3
"""Module Task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous task that waits for a random amount of time."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
