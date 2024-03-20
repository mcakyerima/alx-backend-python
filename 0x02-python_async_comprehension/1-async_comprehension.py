#!/usr/bin/env python 3
""" Task 2 """
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """ Collects 10 random numbers using async comprehension over async_generator 

        Returns:
            List[float]:  list of 10 random numbers.
    """

    return [ i async for i in async_generator() ][:10]
