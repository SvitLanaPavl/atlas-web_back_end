#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from typing import TypeVar, List


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
        if not path.endswith('/'):
            path += '/'
        for excl_path in excluded_paths:
            if path in excluded_paths and excl_path.endswith('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        '''Auth header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current user public method'''
        return None
