#!/usr/bin/env python3
"""The API authentication module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks whether a given path requires authentication or not"""
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for p in excluded_paths:
                if p.startswith(path):
                    return False
                if path.startswith(p):
                    return False
                if p[-1] == "*":
                    if path.startswith(p[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """Retrieves the authorization header field from the request"""
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current user from the request"""
        return None
