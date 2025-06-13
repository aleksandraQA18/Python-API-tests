from random import choice

from config import API_URL, SESSION

from .utils import build_request_headers


class Users:

    def __init__(self):
        self.url = "/users"

    def get_all_users(self):
        response = SESSION.get(f"{API_URL}{self.url}")
        return response

    def get_random_user_id(self):
        response = self.get_all_users()
        response_json = response.json()
        random_user = choice(response_json)
        return random_user["id"]

    def get_user_by_id(self, id):
        response = SESSION.get(f"{API_URL}{self.url}/{id}")
        return response

    def add_new_user(self, payload):
        request_headers = build_request_headers()
        response = SESSION.post(
            f"{API_URL}{self.url}", headers=request_headers, data=payload
        )
        return response

    def update_user(self, id, payload):
        request_headers = build_request_headers()
        response = SESSION.put(
            f"{API_URL}{self.url}/{id}", headers=request_headers, data=payload
        )
        return response

    def delete_user(self, id):
        response = SESSION.delete(f"{API_URL}{self.url}/{id}")
        return response
