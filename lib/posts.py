from random import choice
from urllib import response
from config import API_URL, SESSION
from .utils import build_request_headers


class Posts:

    def __init__(self):
        self.url = "/posts"

    def get_all_posts(self):
        response = SESSION.get(f"{API_URL}{self.url}")
        return response

    def get_random_post_id(self):
        response = self.get_all_posts()
        response_json = response.json()
        random_post = choice(response_json)
        return random_post["id"]

    def get_post_by_id(self, id):
        response = SESSION.get(f"{API_URL}{self.url}/{id}")
        return response

    def add_new_post(self, payload):
        request_headers = build_request_headers()
        response = SESSION.post(
            f"{API_URL}{self.url}", headers=request_headers, data=payload
        )
        return response

    def update_post(self, id, payload):
        request_headers = build_request_headers()
        response = SESSION.put(
            f"{API_URL}{self.url}/{id}", headers=request_headers, data=payload
        )
        return response

    def delete_post(self, id):
        response = SESSION.delete(f"{API_URL}{self.url}/{id}")
        return response
