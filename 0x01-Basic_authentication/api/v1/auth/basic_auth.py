#!/usr/bin/env python3
"""The Basic Authentication class module"""
from .auth import Auth
import base64


class BasicAuth(Auth):
    """Class representing the Basic Authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """Extracts the Base64 portion of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        s_token = authorization_header.split(" ")[-1]
        return s_token

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decodes a Base64-encoded string of the Authorization header"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(decoded)
            return decoded.decode('utf-8')
        except Exception:
            return None
