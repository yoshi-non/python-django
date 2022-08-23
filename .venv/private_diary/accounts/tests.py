from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver

import environ
env = environ.Env()
env.read_env('.env')


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver(
            executable_path="C:/Users/TACHI/chromedriver.exe")

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get("http://localhost:8000" +
                          str(reverse_lazy("account_login")))

        # ログイン
        username_input = self.selenium.find_element_by_name("login")
        username_input.send_keys(env("TEST_USER_MAIL"))
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(env("TEST_USER_PASS"))
        elem = self.selenium.find_element_by_class_name("testBtn")
        elem.click()

        # ページタイトルの検証
        self.assertEquals("日記一覧 | Private Diary", self.selenium.title)
