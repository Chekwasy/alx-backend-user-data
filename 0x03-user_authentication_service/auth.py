#!/usr/bin/env python3
"""A module for authentication-related routines.
"""
import bcrypt
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """method to hash pwd, create user and return user"""
        hsh_pwd = _hash_password(password)
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, hsh_pwd)
        raise ValueError("User " + email + " already exists")