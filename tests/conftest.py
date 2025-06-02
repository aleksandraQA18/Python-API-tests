import pytest
from factory.post_factory import generate_post
from lib.posts import Posts
from config import LOG
import json


@pytest.fixture
def random_product_id():
    return Posts().get_random_post_id()


@pytest.fixture(scope="module")
def add_new_post():
    payload = json.dumps(generate_post())
    response = Posts().add_new_post(payload)
    assert response.ok
    LOG.debug(response.json())
    return response.json()
