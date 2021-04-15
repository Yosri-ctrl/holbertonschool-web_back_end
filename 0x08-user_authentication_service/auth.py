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

    def create_session(self, email: str) -> str:
        """Create a new session
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str):
        """ If the session ID is None or no user is found,
        return None.
        Otherwise return the corresponding user
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: str) -> None:
        """ Delete a session
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        self._db.update_user(user.id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)
        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id,
                                 reset_token=None,
                                 hashed_password=hashed_password)
        except NoResultFound:
            raise ValueError()


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """generate a new id
    """
    return str(uuid4())
