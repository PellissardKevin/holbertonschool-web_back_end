#!/usr/bin/python3
"""make a multiplyer"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """return multiplier"""

    def multi(y: float):
        """return multiplier by one number"""

        return (multiplier * y)

    return multi
