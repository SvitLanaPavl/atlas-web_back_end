#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from typing import TypeVar, List


class Auth():
    '''API authentication management'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''Require authentication'''
        return False

    def authorization_header(self, request=None) -> str:
        '''Auth header'''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Current user public method'''
        return None
