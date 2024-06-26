#!/usr/bin/env python3
'''Manage the API authentication'''
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    '''Retrieves parameters'''
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({'error': 'email missing'}), 400

    if not password:
        return jsonify({'error': 'password missing'}), 400

    try:
        search_user = User.search({'email': email})
        user = search_user[0]
    except Exception:
        return jsonify({'error': 'no user found for this email'}), 404

    if not user.is_valid_password(password):
        return jsonify({'error': 'wrong password'}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    response.set_cookie(getenv('SESSION_NAME'), session_id)

    return response


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    '''Log out delete the session'''
    from api.v1.app import auth
    destroy = auth.destroy_session(request)

    if not destroy:
        abort(404)
    return jsonify({}), 200
