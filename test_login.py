import requests
import pytest

BASE_URL = "http://localhost:8080"

def test_login_success():
    """正常登录"""
    res = requests.post(f"{BASE_URL}/admin/employee/login", json={
        "username": "admin",
        "password": "123456"
    })
    assert res.status_code == 200
    assert res.json()["code"] == 1
    assert "token" in res.json()["data"]

def test_login_wrong_password():
    """密码错误"""
    res = requests.post(f"{BASE_URL}/admin/employee/login", json={
        "username": "admin",
        "password": "wrongpassword"
    })
    assert res.status_code == 200
    assert res.json()["code"] == 0

def test_login_wrong_username():
    """账号不存在"""
    res = requests.post(f"{BASE_URL}/admin/employee/login", json={
        "username": "notexist",
        "password": "123456"
    })
    assert res.status_code == 200
    assert res.json()["code"] == 0

@pytest.mark.parametrize("username, password, expected_code", [
    ("admin", "123456", 1),
    ("admin", "wrongpwd", 0),
    ("notexist", "123456", 0),
    ("", "", 0),
])
def test_login_parametrize(username, password, expected_code):
    """参数化登录测试"""
    res = requests.post(f"{BASE_URL}/admin/employee/login", json={
        "username": username,
        "password": password
    })
    assert res.json()["code"] == expected_code