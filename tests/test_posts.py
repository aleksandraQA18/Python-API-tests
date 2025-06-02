from pytest_schema import schema
from factory.post_factory import generate_post
from lib.posts import Posts
from schemas.posts_schema import *
from config import LOG
import json


def test_get_all_posts():
    LOG.info("test_get_all_posts")
    response = Posts().get_all_posts()
    response_json = response.json()
    LOG.debug(response_json[:2])
    assert response.ok
    assert response_json == schema(POSTS_SCHEMA)


def test_post_by_id(random_product_id):
    LOG.info("test_post_by_id")
    response = Posts().get_post_by_id(random_product_id)
    response_json = response.json()
    LOG.debug(response_json)
    assert response.ok
    assert response.json()["id"] == random_product_id
    assert response_json == schema(POST_SCHEMA)


def test_add_post(add_new_post):
    LOG.info("test_add_post")
    LOG.debug(add_new_post)
    assert add_new_post["id"] is not None


# not working for created post
def test_update_post(random_product_id):
    LOG.info("test_update_post")
    payload = generate_post()
    payload_json = json.dumps(payload)
    LOG.debug(payload)
    response = Posts().update_post(random_product_id, payload_json)
    assert response.ok

    response_json = response.json()
    LOG.debug(response_json)

    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]


def test_delete_post(add_new_post):
    LOG.info("test_delete_post")
    id = add_new_post["id"]
    response = Posts().delete_post(id)
    LOG.debug(response)
    assert response.ok

    response = Posts().get_post_by_id(id)
    assert response.status_code == 404
