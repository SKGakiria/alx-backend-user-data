#!/usr/bin/env python3
"""The Session Authentication class module"""
import base64
from uuid import uuid4

from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Class representing Session Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        s_id = uuid4()
        self.user_id_by_session_id[str(s_id)] = user_id
        return str(s_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> User:
        """Returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)
        return user
