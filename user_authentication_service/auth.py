#!/usr/bin/env python3
'''Module doc hash password'''
import bcrypt


def _hash_password(password: str) -> bytes:
    '''Hashes password'''
    byte_repr = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=15)
    return bcrypt.hashpw(byte_repr, salt)
