#!/usr/bin/env python3
"""Hash a password using bcrypt
"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Add_user to database
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            password = _hash_password(password)
            user = self._db.add_user(email, password)
            return user
        else:
            raise ValueError("User {} already exists".format(email))


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())