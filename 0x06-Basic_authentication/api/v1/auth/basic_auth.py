#!/usr/bin/env python3
"""
creating a class that inherits from Auth.
For the moment this class will be empty.
"""
from flask import request
from typing import List, TypeVar
from auth import Auth

class BasicAuth(Auth):
    pass
