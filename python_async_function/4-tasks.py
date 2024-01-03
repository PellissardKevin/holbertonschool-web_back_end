#!/usr/bin/env python3
"""Tasks"""


import asyncio
import typing


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Return n time wait for max delay"""

    delay_n = await asyncio.gather(*[task_wait_random(
                                   max_delay) for _ in range(n)])

    return sorted(delay_n)
