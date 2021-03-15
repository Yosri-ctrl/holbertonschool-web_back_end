#!/usr/bin/env python3
"""First Element"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Take unknown type input
    and returns it's type or None
    """
    if lst:
        return lst[0]
    else:
        return None
