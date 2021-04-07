#!/usr/bin/env python3
"""
creating a class that inherits from Auth.
For the moment this class will be empty.
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
from base64 import b64decode
import binascii
from models.user import User


class BasicAuth(Auth):
    """Empty class right now
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, header: str) -> str:
        """
        """
        if header is None:
            return None
        if type(header) is not str:
            return None
        try:
            header = b64decode(header)
        except binascii.Error:
            return None
        return header.decode('utf-8')

    def extract_user_credentials(self, header: str) -> (str, str):
        """
        """
        if header is None or type(header) is not str:
            return None, None
        if ":" not in header:
            return None, None
        header = header.split(":")
        return header[0], header[1]

    def user_object_from_credentials(self,
                                     email: str, pwd: str) -> TypeVar('User'):
        """
        returns the User instance based
        on his email and password
        """
        if email is None or pwd is None:
            return None
        if type(email) is not str or type(pwd) is not str:
            return None
        try:
            users = User.search({'email': email})
        except KeyError:
            return None
        if len(users) == 0:
            return None
        user = users[0]
        if not user.is_valid_password(pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Method that overloads Auth and retrieves
        the User instance for a request
        """
        authorization = self.authorization_header(request=request)
        extract = self.extract_base64_authorization_header(authorization)
        decode = self.decode_base64_authorization_header(extract)
        user_credentials = self.extract_user_credentials(decode)
        user = self.user_object_from_credentials(
            email=user_credentials[0],
            pwd=user_credentials[1]
        )
        return user
