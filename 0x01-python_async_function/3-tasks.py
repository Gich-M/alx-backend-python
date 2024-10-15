#!/usr/bin/env python3
"""Module Task 3"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asynchronous task for wait_random"""
    return asyncio.create_task(wait_random(max_delay))
