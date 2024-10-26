#!/usr/bin/env python3
"""Module 1-async_comprehension"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> None:
    """Collects 10 random numbers using async comprehension"""
    return [num async for num in async_generator()]
