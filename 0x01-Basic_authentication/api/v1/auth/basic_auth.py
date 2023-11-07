#!/usr/bin/env python3
"""The Basic Authentication class module"""
from .auth import Auth
import base64


class BasicAuth(Auth):
    """Class representing the Basic Authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the Base64 portion of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        credentials = authorization_header.split(" ")[-1]
        return credentials
