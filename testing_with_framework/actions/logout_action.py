from pages.setting_page import SettingPage
from pages.index_page import IndexPage
from appium import webdriver


class LogoutAction:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.settings = SettingPage(driver)
        self.index = IndexPage(driver)

    def logout_steps(self) -> None:
        self.index.click_setting_button_english()
        self.settings.click_profile_button()
        self.settings.click_logout_button()
        self.settings.click_confirm_logout_button()
