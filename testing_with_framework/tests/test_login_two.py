from tests.base_tests import BaseTests
from settings import TEST_DATA


class TestLoginTwo(BaseTests):
    def test_login(self, init):
        # Fetch Data from YAML file and use it in test cases instead of hard coding
        self.login_actions.login_steps(
            username=TEST_DATA["login"]["email"],
            password=TEST_DATA["login"]["password"],
        )
        desc = self.my_site.select_home_button().get_attribute("content-desc")
        assert str(desc) == "Home"
