#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using the bcrypt hash
    and return the hash in bytes.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that the provided password
    matches the hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
