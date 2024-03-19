#!/usr/bin/env python3
'''Task 1 '''


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple coroutines concurrently.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: List of delays (float values) in asc order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return sorted(await gather(*tasks))
