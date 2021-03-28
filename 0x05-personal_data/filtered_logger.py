#!/usr/bin/env python3
"""
Main file
"""
from typing import List
import re


def filter_datum(fields: List[str]
                 / redaction: str, message: str
                 / separator: str) -> str:
    for field in fields:
        passPosition = re.search(field, message).span()
        a = re.search(separator, message[passPosition[1]:]).span()
        change = message[passPosition[1] + 1: passPosition[1] + a[1]]
        message = re.sub(change, redaction, message)
    return message
