#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
from bcrypt import hashpw, gensalt, checkpw
from typing import List, ByteString


def hash_password(password: str) -> bytes:
    """
    Hash a password using the bcrypt hash
    and return the hash in bytes.
    """
    return hashpw(password.encode('utf-8'), gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that the provided password
    matches the hashed password.
    """
    return checkpw(password.encode('utf-8'), hashed_password)
