#!/usr/bin/env python3
"""The Basic Authentication class module"""
from .auth import Auth
import base64
from typing import TypeVar

from models.user import User


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Extracts user credentials from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        usr_email = decoded_base64_authorization_header.split(":")[0]
        usr_password = decoded_base64_authorization_header[len(usr_email)
                                                           + 1:]
        return (usr_email, usr_password)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Returns a User instance based on the user's authentication
        credentials"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for usr in users:
                if usr.is_valid_password(user_pwd):
                    return usr
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns a User instance for a request"""
        auth_header = self.authorization_header(request)
        if auth_header is not None:
            token = self.extract_base64_authorization_header(auth_header)
            if token is not None:
                decoded = self.decode_base64_authorization_header(token)
                if decoded is not None:
                    u_email, u_psword = self.extract_user_credentials(decoded)
                    if u_email is not None:
                        return self.user_object_from_credentials(u_email,
                                                                 u_psword)
        return None
