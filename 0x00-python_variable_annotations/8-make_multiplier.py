#!/usr/bin/env python3
"""8-make_mult"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by nbr
    """
    def inner(mult: float) -> float:
        """multplier * mut"""
        return float(mult * multiplier)

    return inner
