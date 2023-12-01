from unittest import TestCase
from actions.login_action import LoginAction
from pages.index_page import IndexPage
from testing_with_framework.actions.logout_action import LogoutAction
from testing_with_framework.pages.login_page import LoginPage
from utils.setup_driver import AppiumDriverSetup


class AuthenticationTest(TestCase):
    def setUp(self) -> None:
        self.appium_driver_setup = AppiumDriverSetup()
        self.driver = self.appium_driver_setup.setup_driver()

    def tearDown(self) -> None:
        self.appium_driver_setup.teardown_driver()

    def test_login(self):
        login_info = {"username": "test", "password": "test"}
        login_action = LoginAction(self.driver)
        index_page = IndexPage(self.driver)
        login_action.login_steps(login_info["username"], login_info["password"])
        self.assertTrue(index_page.select_home_button().is_displayed())

    def test_logout(self):
        logout_action = LogoutAction(self.driver)
        logout_action.logout_steps()
        login_page = LoginPage(self.driver)
        self.assertTrue(login_page.select_login_button().is_displayed())
