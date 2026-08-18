import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    """返回一个LoginPage实例"""
    return LoginPage(driver)

def test_login_success(login_page):
    """正常登录，验证跳转到首页"""
    login_page.login("admin", "123456")
    assert login_page.is_login_success()

def test_login_wrong_password(login_page):
    """错误密码，验证弹出错误提示"""
    login_page.login("admin", "wrongpassword")
    error = login_page.get_error_message()
    assert error.is_displayed()