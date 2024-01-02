#!/usr/bin/env python3
"""returns their sum as a float."""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Sum mxd_lst"""

    return sum(mxd_lst)
