import requests

BASE_URL = "http://localhost:8080"

def test_dish_list_success(token):
    """正常查询菜品列表，携带token"""
    headers = {"token": token}
    res = requests.get(
        f"{BASE_URL}/admin/dish/page",
        params={"page": 1, "pageSize": 10},
        headers=headers
    )
    assert res.status_code == 200
    assert res.json()["code"] == 1
    # 验证返回的数据里有records字段（菜品列表）
    assert "records" in res.json()["data"]

def test_dish_list_no_token():
    """不带token直接请求，验证鉴权是否生效"""
    res = requests.get(
        f"{BASE_URL}/admin/dish/page",
        params={"page": 1, "pageSize": 10}
    )
    # 服务器直接返回401，说明鉴权生效了
    assert res.status_code == 401

def test_dish_list_page2(token):
    """查询第二页"""
    headers = {"token": token}
    res = requests.get(
        f"{BASE_URL}/admin/dish/page",
        params={"page": 2, "pageSize": 10},
        headers=headers
    )
    assert res.status_code == 200
    assert res.json()["code"] == 1