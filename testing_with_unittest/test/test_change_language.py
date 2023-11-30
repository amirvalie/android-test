from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from unittest import TestCase
from appium import webdriver
from driver_connection import AppiumDriverSetup
from page_utils import PageUtils


class TestLanguage(TestCase):
    def setUp(self) -> None:
        self.appium_driver_setup = AppiumDriverSetup()
        self.driver = self.appium_driver_setup.setup_driver()
        self.page_utils = PageUtils(self.driver)

    def tearDown(self) -> None:
        self.appium_driver_setup.teardown_driver()

    def test_change_language(self):
        self.driver.implicitly_wait(30)
        home_button = self.page_utils.get_element(
            ("xpath", "//android.view.View[@bounds='[441,1973][639,2094]']")
        )
        if "خانه" in str(home_button.get_attribute("content-desc")):
            self.page_utils.get_element(  # setting button
                ("xpath", "//android.view.View[@bounds='[838,1996][1036,2070]']")
            ).click()
            self.page_utils.get_element(  # language button
                ("xpath", "//android.view.View[@content-desc='زبان']")
            ).click()
        else:
            self.page_utils.get_element(  # setting button
                ("xpath", "//android.view.View[@bounds='[44,1996][242,2070]']")
            ).click()
            self.page_utils.get_element(  # language button
                ("xpath", "//android.view.View[@content-desc='Language']")
            ).click()
        farsi_option = self.page_utils.get_element(
            ("xpath", "//android.widget.RadioButton[@content-desc='فارسی']")
        ).click()
        english_option = self.page_utils.get_element(
            ("xpath", "//android.widget.RadioButton[@content-desc='English']")
        ).click()
        if farsi_option.is_selected():
            english_option.click()
        elif english_option.is_selected():
            farsi_option.click()
