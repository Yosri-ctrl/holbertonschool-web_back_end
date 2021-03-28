#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
from typing import List
import re


def filter_datum(fields, redaction, message, separator):
    """
    Take str message and return it obfuscated
    fields contain the field to obfuscated by redaction
    print(message[pas[0]:pas[1] + a[1] -1])
    """
    for field in fields:
        pas = re.search(field, message).span()
        a = re.search(separator, message[pas[1]:]).span()
        change = message[pas[1] + 1: pas[1] + a[1] - 1]
        message = re.sub(change, redaction, message)
    return message
