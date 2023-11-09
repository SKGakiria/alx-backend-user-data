#!/usr/bin/env python3
"""The Session Authentication class module"""
from .auth import Auth
from uuid import uuid4


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