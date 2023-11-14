#!/usr/bin/env python3
"""The authentication module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password string"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
