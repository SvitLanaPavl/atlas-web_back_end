#!/usr/bin/env python3
'''Password encyption'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''Returned hashed'''
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=15)
    return bcrypt.hashpw(bytes, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''Validates provided password matches hashed'''
    pass_bytes = password.encode('utf-8')
    return bcrypt.checkpw(pass_bytes, hashed_password)
