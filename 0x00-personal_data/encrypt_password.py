#!/usr/bin/env python3
"""Module containing a hash_password function"""
from bcrypt import hashpw
import bcrypt


def hash_password(password: str) -> bytes:
    """Function that returns a salted, hashed password,
    which is a byte string"""
    bc = password.encode()
    hashed = hashpw(bc, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Function checks whether the provided password matches
    the hashed password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
