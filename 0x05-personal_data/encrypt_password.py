#!/usr/bin/env python3
"""
returns the log message obfuscated
"""
from bcrypt import hashpw, gensalt
from typing import List, ByteString


def hash_password(password: str) -> bytes:
    """pass"""
    return hashpw(password.encode('utf-8'), gensalt())
