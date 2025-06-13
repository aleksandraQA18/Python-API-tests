from random import choice

from config import API_URL, SESSION


class Users:

    def __init__(self):
        self.url = "/users"

    def get_all_users(self):
        """Retrieve all users."""
        response = SESSION.get(f"{API_URL}{self.url}")
        return response

    def get_random_user_id(self):
        """Get a random ID from users collection."""
        response = self.get_all_users()
        response_json = response.json()
        random_user = choice(response_json)
        return random_user["id"]

    def get_user_by_id(self, id):
        """Get a user resource by ID."""
        response = SESSION.get(f"{API_URL}{self.url}/{id}")
        return response

    def add_new_user(self, payload):
        """Add a new user."""
        response = SESSION.post(f"{API_URL}{self.url}", json=payload)
        return response

    def update_user(self, id, payload):
        """Update an existing user."""
        response = SESSION.put(f"{API_URL}{self.url}/{id}", json=payload)
        return response

    def delete_user(self, id):
        """Delete a user by ID."""
        response = SESSION.delete(f"{API_URL}{self.url}/{id}")
        return response
