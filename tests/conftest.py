import json

import pytest

from config import LOG
from factory.post_factory import generate_post
from factory.user_factory import generate_user
from lib.posts import Posts
from lib.users import Users


@pytest.fixture
def random_product_id():
    return Posts().get_random_post_id()


@pytest.fixture
def add_new_post():
    payload = json.dumps(generate_post())
    response = Posts().add_new_post(payload)
    assert response.ok
    LOG.debug(response.json())
    return response.json()


@pytest.fixture
def random_user_id():
    return Users().get_random_user_id()


@pytest.fixture
def add_new_user():
    payload = json.dumps(generate_user())
    response = Users().add_new_user(payload)
    assert response.ok
    LOG.debug(response.json())
    return response.json()
