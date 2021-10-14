# import socketio

# sio = socketio.Client()

# # game_state = []

# @sio.on("connect")
# def connect():
#     print('connection established')
    
# @sio.on("disconnect")
# def disconnect():
#     print('disconnected from server')
#     sio.disconnect()
#     # sio.eio.disconnect(True)

# @sio.on("move")
# def move_received(data):
#     # game_state = data["response"]
#     # print(game_state)
#     print("data received")
#     return data

# @sio.on("join")
# def join_game(data):
#     # game_state = data["response"]
#     # print(game_state)
#     print("data received")
#     return data


# def send_game_state(board, player_turn):
#     # print('message received with ', data)
#     sio.emit('move', {'board': board, "current_turn": player_turn})

# def join_game(player_id):
#     # print('message received with ', data)
#     sio.emit('join', {})

# def init_socket():
#     sio.connect('http://127.0.0.1:5000')
# # sio.wait()
