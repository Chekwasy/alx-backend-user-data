#!/usr/bin/env python3
""" Session Auth class to handle session for users and authentication"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """The class begins"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a ssession id for a user"""
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """method to return a user_id based on a given session_id"""
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)
