#!/usr/bin/env python3
"""Module 1-async_comprehension"""

from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers using async comprehension"""
    return [num async for num in async_generator()]
