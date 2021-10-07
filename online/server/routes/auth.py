from flask import Blueprint, request, jsonify
from storage.storage import Storage
from werkzeug.security import generate_password_hash

auth = Blueprint("auth", __name__)

storage = Storage("tic tac toe")

@auth.route("/users")
def get_users():
    return jsonify(storage.get_users())

@auth.route("/rooms")
def get_rooms():
    return jsonify(storage.get_rooms())

@auth.route("/register", methods=["POST"])
def create_user():
    user = request.form['user']
    password = request.form['password']
    password = generate_password_hash(password)
    return jsonify(storage.create_user(user, password))

@auth.route("/login", methods=["POST"])
def login():
    user = request.form['user']
    password = request.form['password']
    return jsonify(storage.authenticate(user, password))

@auth.route("/create_room", methods=["POST"])
def create_room():
    user = request.form['user']
    return jsonify(storage.create_room(user))

@auth.route("/join_room", methods=["POST"])
def join_room():
    room_id = request.form['id']
    user = request.form['user']
    return jsonify(storage.join_room(room_id, user))
