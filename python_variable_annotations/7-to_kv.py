#!/usr/bin/python3
"""Definition of add """

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Return k and v mul by v"""

    return (k, (v * v))
