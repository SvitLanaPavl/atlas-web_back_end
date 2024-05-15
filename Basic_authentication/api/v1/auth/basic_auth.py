#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''Basic Auth class'''
    def extract_base64_authorization_header(
        self, authorization_header: str
            ) -> str:
        '''Returns Base64 of Authorization'''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]
