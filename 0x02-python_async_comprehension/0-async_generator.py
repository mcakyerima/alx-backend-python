#!/usr/bin/evn python3
""" Task 0 """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Generates a random sequence of 10 numbers. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
