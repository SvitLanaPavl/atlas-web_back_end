#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth
import base64
import binascii
from models.user import User


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

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        '''Returns user instance based on his email and password'''
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        search_usr = User.search({'email': user_email})
        for user in search_usr:
            if not user.is_valid_password(user_pwd):
                return None
            return user
