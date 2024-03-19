#!/usr/bin/env python3
'''Task 2 '''


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int, wait_n: Callable) -> float:
    """Measures the total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay for each coroutine.
        wait_n (Callable): Function to execute.

    Returns:
        float: Total execution time divided by n.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
