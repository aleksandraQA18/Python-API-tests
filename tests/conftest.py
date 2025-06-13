import pytest

from config import LOG
from factory.post_factory import generate_post
from factory.user_factory import generate_user
from lib.posts import Posts
from lib.users import Users


@pytest.fixture
def random_post_id():
    """Return a random post ID from posts collection"""
    return Posts().get_random_post_id()


@pytest.fixture
def add_new_post():
    """Create and return a new post"""
    payload = generate_post()
    response = Posts().add_new_post(payload)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    LOG.debug(response.json())
    return response.json()


@pytest.fixture
def random_user_id():
    """Return a random user ID from users collection"""
    return Users().get_random_user_id()


@pytest.fixture
def add_new_user():
    """Create and return a new user"""
    payload = generate_user()
    response = Users().add_new_user(payload)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    LOG.debug(response.json())
    return response.json()
