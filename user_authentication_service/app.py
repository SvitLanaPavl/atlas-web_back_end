#!/usr/bin/env python3
'''Route module for the API'''
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def basic() -> str:
    '''Returns a JSON payload of the form'''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    '''Register a user'''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        new_usr = AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login() -> str:
    '''Log in'''
    email = request.form.get('email')
    password = request.form.get('password')
    if not email or not password:
        abort(401)
    session_id = AUTH.create_session(email)
    set_cookie('session_id', session_id)
    return jsonify({"email": f"{email}", "message": "logged in"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
