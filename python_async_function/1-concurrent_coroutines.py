#!/usr/bin/env python3
"""" multiple coroutines at the same time with async """


import asyncio
import typing


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Return n time wait for max delay"""

    delay_n = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])

    return sorted(delay_n)
