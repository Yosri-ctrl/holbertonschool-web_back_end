#!/usr/bin/env python3
"""
creating a class that inherits from Auth.
For the moment this class will be empty.
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


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