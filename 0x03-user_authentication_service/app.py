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


@app.route('/users', methods=[
    'POST'], strict_slashes=False)
def reg_user() -> str:
    """register a user to the server"""
    email = request.form.get("email")
    password = request.form.get("password")
    if email and password:
        try:
            usr = AUTH.register_user(email, password)
            return jsonify({"email": usr.email,
                            "message": "user created"})
        except ValueError:
            return jsonify({"message": "email already registered"}), 400

@app.route('/sessions', methods=[
    'POST'], strict_slashes=False)
def login() -> str:
    """method to comfirm logged in"""
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        uid = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", uid)
        return response
    else:
        abort(401)

@app.route('/sessions', methods=[
    'DELETE'], strict_slashes=False)
def logout() -> str:
    """method to delete session. same as logout"""
    cooki = request.cookies.get("session_id")
    if cooki is None:
        abort(403)
    usr = AUTH.get_user_from_session_id(cooki)
    if usr is None:
        abort(403)
    AUTH.destroy_session(usr.id)
    redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
