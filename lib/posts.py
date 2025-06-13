from random import choice

from config import API_URL, SESSION


class Posts:

    def __init__(self):
        self.url = "/posts"

    def get_all_posts(self):
        """Retrieve all posts."""
        response = SESSION.get(f"{API_URL}{self.url}")
        return response

    def get_random_post_id(self):
        """Get a random ID from posts collection."""
        response = self.get_all_posts()
        response_json = response.json()
        random_post = choice(response_json)
        return random_post["id"]

    def get_post_by_id(self, id):
        """Get a post resource by ID."""
        response = SESSION.get(f"{API_URL}{self.url}/{id}")
        return response

    def add_new_post(self, payload):
        """Add a new post."""
        response = SESSION.post(f"{API_URL}{self.url}", json=payload)
        return response

    def update_post(self, id, payload):
        """Update an existing post."""
        response = SESSION.put(f"{API_URL}{self.url}/{id}", json=payload)
        return response

    def delete_post(self, id):
        """Delete a post by ID."""
        response = SESSION.delete(f"{API_URL}{self.url}/{id}")
        return response
