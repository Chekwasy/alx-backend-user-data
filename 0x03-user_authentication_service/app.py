#!/usr/bin/env python3
"""A simple Flask app with user authentication features.
"""
from flask import Flask, jsonify, request, abort, redirect

from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """GET /
    Return:
        - The home page's payload.
    """
    return jsonify({"message": "Bienvenue"})


@app_views.route('/users/<email>/<password>', methods=[
    'POST'], strict_slashes=False)
def reg_user(email: str, password: str) -> str:
    """register a user to the server"""
    if email and password:
        try:
            usr = Auth.register_user(email, password)
            return jsonify({"email": usr.email,
                            "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
