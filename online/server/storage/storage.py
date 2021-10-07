from werkzeug.security import check_password_hash
from storage.user import User
from storage.room import Room
import string
import random

class Storage:
    def __init__(self, game):
        self.game = game
        self.rooms = {}
        self.users = {}

    # utility 
    def create_random_id(self, n):
        limit = 10000
        while limit:
            id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
            if id not in self.rooms:
                return id
            limit = limit - 1

        return False
            
    def user_exists(self, user):
            return user in self.users   

    def authenticate(self, user, password):
        if not self.user_exists(user):
            return {"error": "User does not exist"}
        
        if check_password_hash(self.users[user].password, password):
            data = self.users[user].get_info()
            data["success"] = True
            return data

        return {"error": "Invalid password"}

    def user_in_room(self, user):
        for room_id, room in self.rooms.items():
            if user in room.get_players():
                return {room_id: user}
        return False

    # getters 
    def get_users(self):
        # turning class into json object
        json_object = { k: v.get_info() for (k,v) in self.users.items() }
        return json_object

    def get_rooms(self):
        # turning class into json object
        json_object = { k: v.get_info() for (k,v) in self.rooms.items() }
        return json_object

    # setters
    def create_user(self, user, password):
        if self.user_exists(user):
            return {"error": "User already exists"}
        self.users[user] = User(user, password, 300)
        return self.users[user].get_info()

    def delete_user(self, user):
        return self.users.pop(user, {"error": "User not found"})

    def update_balance(self, user, balance):
        if not self.user_exists(user):
            return {"error": "Cannot update balance: User doesnt exist"}
        self.users[user].set_balance(balance)

    def create_room(self, user):
        if not self.user_exists(user) or self.user_in_room(user):
            return {"error": f"Could not create a room for {user}"}
        
        id = self.create_random_id(6)
        self.rooms[id] = Room(id, user)
        return self.rooms[id].get_info()

    def join_room(self, id, user):
        if id not in self.rooms or self.user_in_room(user):
            return {"error": "Error joining room"}
        self.rooms[id].add_player(user)

        return self.rooms[id].get_info()

