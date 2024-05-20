#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from typing import TypeVar, List
import os


class Auth():
    '''API authentication management'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Require authentication'''
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path in excluded_paths:
            return False
        if not path.endswith('/'):
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Auth header'''
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current user public method'''
        return None

    def session_cookie(self, request=None):
        '''Returns cookie value from request'''
        if request is None:
            return None
        session_cookie = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_cookie)
