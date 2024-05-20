#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import request
from typing import TypeVar, List
from api.v1.auth.auth import Auth
import base64
import binascii
from models.user import User


class SessionAuth(Auth):
    '''Session authentication'''
    pass
