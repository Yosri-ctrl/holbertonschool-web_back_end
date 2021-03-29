#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum.
        Values for fields in fields should be filtered
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Take str message and return it obfuscated
    fields contain the field to obfuscated by redaction
    """
    for field in fields:
        pas = re.search(field, message).span()
        a = re.search(separator, message[pas[1] + 1:]).span()
        message = re.sub(message[pas[1] + 1: pas[1] + a[1]],
                         redaction, message)
    return message
