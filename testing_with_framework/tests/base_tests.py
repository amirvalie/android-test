import pytest
from pages.index_page import IndexPage
from actions.login_action import LoginAction
from utils.setup_driver import exec_driver


class BaseTests:
    @pytest.fixture
    def init(self):
        driver = exec_driver()
        self.my_site = IndexPage(driver)
        self.login_actions = LoginAction(driver)
