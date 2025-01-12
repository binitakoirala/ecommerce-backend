import pytest
import requests

BASE_URL = "http://127.0.0.1:5000/users"


@pytest.fixture(scope="module")
def user_payload():
    return {
        "first_name": "Stephen",
        "last_name": "Hawkin",
        "email": "stephenhawkin@gmail.com",
        "password": "stephen123",
    }


@pytest.fixture(scope="module")
def created_user(user_payload):
    response = requests.post(BASE_URL, json=user_payload)
    response_data = response.json()
    assert response.status_code == 201
    return response_data


def test_create_user(user_payload):

    user_payload["email"] = "hstephen@gmail.com"
    response = requests.post(BASE_URL, json=user_payload)

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["first_name"] == user_payload["first_name"]
    assert response_data["last_name"] == user_payload["last_name"]
    assert response_data["email"] == user_payload["email"]

    requests.delete(f"{BASE_URL}/{response_data['user_id']}")


def test_get_user_by_id(created_user):
    user_id = created_user["user_id"]
    response = requests.get(f"{BASE_URL}/{user_id}")

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["user_id"] == user_id


def test_get_users():
    response = requests.get(BASE_URL)

    assert response.status_code == 200
    response_data = response.json()
    assert isinstance(response_data, list)


def test_delete_user(created_user):
    user_id = created_user["user_id"]

    response = requests.delete(f"{BASE_URL}/{user_id}")

    assert response.status_code == 204

    response = requests.get(f"{BASE_URL}/{user_id}")
    assert response.status_code == 404
