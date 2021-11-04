import requests

from server_config import SERVER_IP

url = SERVER_IP
class UserModel:

    @staticmethod
    def create_user(username, password):
        options = {"user": username, "password": password}
        response = requests.post(f"{url}/auth/register", data=options)
        return response.json()

    @staticmethod
    def authenticate(username, password):
        options = {"user": username, "password": password}
        response = requests.post(f"{url}/auth/login", data=options)
        return response.json()

    @staticmethod
    def get_user_info(username):
        response = requests.get(f"{url}/auth/user/{username}")
        return response.json()

    @staticmethod
    def get_all_users():
        response = requests.get(f"{url}/auth/users")
        return response.json()
