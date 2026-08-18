from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """登录页面的元素定位和操作，统一管理"""

    # 元素定位，集中写在这里，页面改了只需要改这里
    ACCOUNT_INPUT = (By.XPATH, "//input[@placeholder='账号']")
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='密码']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-btn")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".el-message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """打开登录页面"""
        self.driver.get("http://localhost:80")

    def input_account(self, account):
        """输入账号"""
        self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_INPUT))
        self.driver.find_element(*self.ACCOUNT_INPUT).send_keys(account)

    def input_password(self, password):
        """输入密码"""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """点击登录按钮"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, account, password):
        """完整登录流程：输入账号密码并点击登录"""
        self.open()
        self.input_account(account)
        self.input_password(password)
        self.click_login()

    def get_error_message(self):
        """获取错误提示元素"""
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )

    def is_login_success(self):
            """判断是否登录成功（URL是否变化）"""
            self.wait.until(EC.url_changes("http://localhost:80"))
            print("跳转后的URL：", self.driver.current_url)  # 打印出来看看
            return self.driver.current_url != "http://localhost:80"