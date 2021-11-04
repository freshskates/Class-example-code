import requests
from server_config import SERVER_IP

url = SERVER_IP

class RoomModel:
    @staticmethod
    def create_room(username):
        options = {"user": username}
        response = requests.post(f"{url}/auth/create_room", data=options)
        return response.json()

    @staticmethod
    def join_room(id, username):
        options = {"id": id, "user": username}
        response = requests.post(f"{url}/auth/join_room", data=options)
        return response.json()

    @staticmethod
    def get_all_rooms():
        response = requests.get(f"{url}/auth/rooms")
        return response.json()
    