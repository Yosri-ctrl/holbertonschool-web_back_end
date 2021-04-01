#!/usr/bin/env python3
"""
This class is the template for all
authentication system you will implement.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    This class is the template for all
    authentication system you will implement.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Validate if path exist in excluded_paths
        and return bool
        """
        if path is not None and not path.endswith("/"):
            path += "/"

        if path is None or excluded_paths is None or
        path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        """
        return None
