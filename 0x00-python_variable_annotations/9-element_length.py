#!/usr/bin/env python3
"""return the element length"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return the Element length"""
    return [(i, len(i)) for i in lst]
