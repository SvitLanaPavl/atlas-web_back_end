#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import Flask, jsonify, abort, request
from api.v1.auth.auth import Auth
from api.v1.views import app_views
from os import getenv


@app_views.route('/auth_session/login', methods=[POST], strict_slashes=False)
def login() -> str:
    '''Retrieves parameters'''
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None:
        return jsonify({'error': 'email missing'}), 400

    if password is None:
        return jsonify({'error': 'passowrd missing'}), 400

    from api.v1.models.user import User
    search_user = User.search({'email', email})
    if search_user is None:
        return jsonify({'error': 'no user found for this email'}), 404
    if not search_user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401

    from api.v1.app import auth
    session_id = auth.create_session(search_user.id)
    response = jsonify(search_user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)

    return response
