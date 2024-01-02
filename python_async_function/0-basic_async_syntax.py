#!/usr/bin/env python3
"""asynchronous coroutine"""


import asyncio
import random


async def wait_random(max_delay=10):
    """Method to return the delay"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
