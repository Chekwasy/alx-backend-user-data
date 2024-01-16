#!/usr/bin/env python3
"""auth file"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require auth method - that returns False - path and excluded_paths
        will be used later, now, you don’t need to take care of them"""
        return False


    def authorization_header(self, request=None) -> str:
        """returns None - request will be the Flask request object"""
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """that returns None - request will be the Flask request object"""
        return None
