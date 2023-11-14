#!/usr/bin/env python3
"""The authentication module"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password string"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user to the database"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            n_user = self._db.add_user(email, hashed_pwd)
            return n_user
        raise ValueError(f"User {email} already exists")
