#!/usr/bin/env python3
"""The UserSession module"""
from models.base import Base


class UserSession(Base):
    """Class representing UserSession that inherits from Base"""
    def __init__(self, *args: list, **kwargs: dict):
        """Initializes the UserSession instance"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
