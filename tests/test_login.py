# test_login.py

from tests.base_test import BaseTest
from pages.login_page import LoginPage

class TestLogin(BaseTest):
    def test_login_with_valid_user(self):
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_user()
        self.assertIn("logged-in-successfully", self.driver.current_url)

    def test_login_with_invalid_username(self):
        login_page = LoginPage(self.driver)
        result = login_page.login_with_invalid_username()
        self.assertIn("Your username is invalid!", result)
        
    def test_login_with_invalid_password(self):
        login_page = LoginPage(self.driver)
        result = login_page.login_with_invalid_password()
        self.assertIn("Your password is invalid!", result)


