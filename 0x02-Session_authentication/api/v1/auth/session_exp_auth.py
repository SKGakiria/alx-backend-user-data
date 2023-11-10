#!/usr/bin/env python3
"""The SessionExpAuth class module"""
import os
from datetime import datetime, timedelta

from .session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """Class representing SessionExpAuth"""
    def __init__(self):
        """Initializes the class"""
        try:
            ses_duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            ses_duration = 0
        self.session_duration = ses_duration

    def create_session(self, user_id=None):
        """Creates a Session ID for the User"""
        ses_id = super().create_session(user_id)
        if ses_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[ses_id] = session_dictionary
        return ses_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieves a User ID based on a Session ID"""
        if session_id is None:
            return None
        user_info = self.user_id_by_session_id.get(session_id)
        if user_info is None:
            return None
        if "created_at" not in user_info.keys():
            return None
        if self.session_duration <= 0:
            return user_info.get("user_id")
        created_at = user_info.get("created_at")
        exp_time = created_at + timedelta(seconds=self.session_duration)
        if exp_time < datetime.now():
            return None
        return user_info.get("user_id")
