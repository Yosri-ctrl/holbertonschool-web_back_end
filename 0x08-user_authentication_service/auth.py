#!/usr/bin/env python3
"""Hash a password using bcrypt
"""
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


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

    def valid_login(self, email: str, password: str) -> bool:
        """Returns True if user have correct login
        False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return checkpw(password.encode('utf-8'), user.hashed_password)


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """generate a new id
    """
    return str(uuid4())
