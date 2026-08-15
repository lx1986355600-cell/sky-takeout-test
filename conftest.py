import pytest
import requests

BASE_URL = "http://localhost:8080"

@pytest.fixture(scope="session")
def token():
    res = requests.post(f"{BASE_URL}/admin/employee/login", json={
        "username": "admin",
        "password": "123456"
    })
    return res.json()["data"]["token"]