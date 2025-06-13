import json

from pytest_schema import schema

from config import LOG
from factory.user_factory import generate_user
from lib.users import Users
from schemas.users_schema import *

# Note: JSONPlaceholder does not persist changes.
# After POST, UPDATE, or DELETE, further tests with GET are not possible.


def test_get_all_users():
    LOG.info("test_get_all_users")
    response = Users().get_all_users()
    response_json = response.json()
    LOG.debug(response_json[:2])
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    assert response_json == schema(USERS_SCHEMA)


def test_user_by_id(random_user_id):
    LOG.info("test_user_by_id")
    response = Users().get_user_by_id(random_user_id)
    response_json = response.json()
    LOG.debug(response_json)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    assert response.json()["id"] == random_user_id
    assert response_json == schema(USER_SCHEMA)


def test_add_user(add_new_user):
    LOG.info("test_add_user")
    LOG.debug(add_new_user)
    assert add_new_user["id"] is not None


def test_update_user(random_user_id):
    LOG.info("test_update_user")
    payload = generate_user()
    LOG.debug(payload)
    response = Users().update_user(random_user_id, payload)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
    response_json = response.json()
    LOG.debug(response_json)
    assert response_json["name"] == payload["name"]
    assert response_json["username"] == payload["username"]


def test_delete_user(add_new_user):
    LOG.info("test_delete_user")
    id = add_new_user["id"]
    response = Users().delete_user(id)
    LOG.debug(response)
    assert response.ok, f"Request failed: {response.status_code} {response.text}"
