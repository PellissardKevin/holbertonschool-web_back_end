#!/usr/bin/env python3
"""Tasks """


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ takes an integer max_delay and returns a asyncio.Task."""

    async def wrapped_task():
        """async def pour une coroutine de wait_random"""
        return await wait_random(max_delay)

    return asyncio.create_task(wrapped_task())
