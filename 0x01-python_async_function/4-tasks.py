#!/usr/bin/env python3
'''Task 4 module '''

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple coroutines concurrently using asyncio.Tasks.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        List[float]: List of delays (float values) in asc order.
    """

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
