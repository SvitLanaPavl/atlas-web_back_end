#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from api.v1.auth.auth import Auth
import uuid




class SessionAuth(Auth):
    '''Session authentication'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Generates session id using uuid'''
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''Returns user id based on the session id'''
        if session_id is None:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''Returns user instance based on the cookie value'''
        if request is None:
            return None
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        from models.user import User
        user = User().get(user_id)
        return user
