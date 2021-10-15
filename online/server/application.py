from flask import Flask, jsonify
from routes.auth import auth
from flask_socketio import SocketIO, send, emit, join_room, leave_room

application = Flask(__name__)
application.config["SECRET_KEY"] = "ASLJKDKALSD!"

socketio = SocketIO(application)

rooms = {}
application.register_blueprint(auth, url_prefix="/auth")


@application.route("/", methods=["GET"])
def home_page():
    return jsonify({"success": "HELLO CLASS"})

@socketio.on("move")
def handleMove(data):
    print("Got message:", data)
    room = data["channel"]
    emit("move", data, room=room)

@socketio.on("join")
def syncGame(data):
    room = data["channel"]
    if room not in rooms:
        rooms[room] = {"players": {}, "symbols": ["X", "O"]}

    temp_symbol = rooms[room]["symbols"].pop()
    rooms[room]["players"][data["player_name"]] = temp_symbol
    rooms[room]["channel"] = room

    join_room(room)

    # emit("sync_game", game_state, broadcast=True)
    emit("sync_game", rooms[room], room=room)

if __name__ == "__main__":
    
    # host='0.0.0.0'
    
    # production
    # socketio.run(application, host='0.0.0.0', debug=True)
    
    socketio.run(application, debug=True)
