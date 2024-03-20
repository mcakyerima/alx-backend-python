#!/usr/bin/env/ python3
""" Task 3 """
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in paralled using asyncio.gather

       Returns:
           float: Total runtime for executing async_comprehension 4 times
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_event_loop().time()

    return end_time - start_time
