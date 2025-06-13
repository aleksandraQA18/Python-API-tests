from pytest_schema import schema

from config import LOG
from factory.post_factory import generate_post
from lib.posts import Posts
from schemas.posts_schema import *

# Note: JSONPlaceholder does not persist changes.
# After POST, UPDATE, or DELETE, further tests with GET are not possible.


def test_get_all_posts():
    LOG.info("test_get_all_posts")
    response = Posts().get_all_posts()
    response_json = response.json()
    LOG.debug(response_json[:2])
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    assert response_json == schema(POSTS_SCHEMA)


def test_post_by_id(random_post_id):
    LOG.info("test_post_by_id")
    response = Posts().get_post_by_id(random_post_id)
    response_json = response.json()
    LOG.debug(response_json)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    assert response.json()["id"] == random_post_id
    assert response_json == schema(POST_SCHEMA)


def test_add_post(add_new_post):
    LOG.info("test_add_post")
    LOG.debug(add_new_post)
    assert add_new_post["id"] is not None


def test_update_post(random_post_id):
    LOG.info("test_update_post")
    payload = generate_post()
    LOG.debug(payload)
    response = Posts().update_post(random_post_id, payload)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    response_json = response.json()
    LOG.debug(response_json)
    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]


def test_delete_post(add_new_post):
    LOG.info("test_delete_post")
    id = add_new_post["id"]
    response = Posts().delete_post(id)
    LOG.debug(response)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
