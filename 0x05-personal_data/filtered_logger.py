#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
from typing import List
import re
import logging
import os
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    """
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
    database = os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
    user = os.environ.get('PERSONAL_DATA_DB_USERNAME'),
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    return mysql.connector.connect(host, database, user, password)

def main():
    """
    """
    data_base = get_db()
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM users;")
    all = cursor.fetchall()
    for data in all:
        message = "name={}; email={}; phone={}; \
            ssn={}; password={};".format(data[0],
                                         data[1],
                                         data[2],
                                         data[3],
                                         data[4])
        print(message)
        log_record = logging.LogRecord("my_logger", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    cursor.close()
    data_base.close()
if __name__ == "__main__":
    main()