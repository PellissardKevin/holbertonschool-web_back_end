#!/usr/bin/env python3
"""Element length of sequence"""


import typing


def element_length(
    lst: typing.Iterable[typing.Sequence],
) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """return lst"""

    return [(i, len(i)) for i in lst]
