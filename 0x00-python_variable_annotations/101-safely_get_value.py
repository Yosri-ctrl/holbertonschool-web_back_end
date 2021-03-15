#!/usr/bin/env python3
"""First Element"""
from typing import Mapping, Any, Union, TypeVar


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar('T'),
                                    None]=None) -> Union[Any, TypeVar('T')]:

    """Returns The value"""
    if key in dct:
        return dct[key]
    else:
        return default
