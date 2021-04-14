#!/usr/bin/env python3
"""Hash a password using bcrypt
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())
