#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Take str message and return it obfuscated
    fields contain the field to obfuscated by redaction
    """
    for field in fields:
        pas = re.search(field, message).span()
        a = re.search(separator, message[pas[1]:]).span()
        message = re.sub(message[pas[1] + 1: pas[1] + a[1]], redaction, message)
    return message
