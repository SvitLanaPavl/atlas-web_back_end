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
        try:
            search_usr = User.search({'email': user_email})
        except Exception:
            return None
        for user in search_usr:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''Overloads Auth and retrieves the user instance'''
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(auth_header)
        if base64_auth_header is None:
            return None

        decode_64 = self.decode_base64_authorization_header(base64_auth_header)
        if decode_64 is None:
            return None

        usr_email, usr_pwd = self.extract_user_credentials(decode_64)
        if usr_email is None or usr_pwd is None:
            return None

        return self.user_object_from_credentials(usr_email, usr_pwd)
