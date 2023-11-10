#!/usr/bin/env python3
"""The SessionDBAuth class module"""
from models.user_session import UserSession
from .session_exp_auth import SessionExpAuth


class SessionDBAuth(SessionExpAuth):
    """Class representing SessionDBAuth that inherits from SessionExpAuth"""
    def create_session(self, user_id=None):
        """Creates and stores new instance of a UserSession and returns
        the Session ID"""
        ses_id = super().create_session(user_id)
        if not ses_id:
            return None
        kwargs = {
            "user_id": user_id,
            "session_id": session_id
        }
        usr_session = UserSession(**kwargs)
        usr_session.save()
        return ses_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieves a User ID based on a Session ID"""
        user_id = UserSession.search({"session_id": session_id})
        if user_id:
            return user_id
        return None

    def destroy_session(self, request=None):
        """Destroys the UserSession based on the Session ID from the
        request cookie"""
        if request is None:
            return False
        ses_id = self.session_cookie(request)
        if not ses_id:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False
