#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
            ) -> str:
        '''Returns decoded value of Base64'''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64.b64decode(base64_authorization_header)
        except binascii.Error:
            return None
        decode_bytes = base64.b64decode(base64_authorization_header)
        return decode_bytes.decode('utf-8')

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
            ) -> (str, str):
        '''Returns the user email and password from Base64'''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if not decoded_base64_authorization_header.__contains__(':'):
            return (None, None)
        email, password = decoded_base64_authorization_header.split(':')
        return (email, password)
