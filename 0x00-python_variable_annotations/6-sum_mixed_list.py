#!/usr/bin/env python3
"""return the sum of the list"""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Return the sum of a mixed list
    """
    return sum(mxd_lst)
