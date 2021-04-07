#!/usr/bin/env python3
"""
creating a class to manage the API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    This class is the template for all
    authentication system you will implement
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Validate if path exist in excluded_paths
        and return bool
        """
        if path is not None and not path.endswith("/"):
            path += "/"
        if path is None:
            return True
        if excluded_paths is None or path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object
        """
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None - request will be the Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """returns None - request will be the Flask request object
        """
        if request is None: return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)