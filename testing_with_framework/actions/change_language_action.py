from pages.setting_page import SettingPage
from pages.index_page import IndexPage
from appium import webdriver


class ChangeLanguageAction:
    def __init__(self, driver: webdriver) -> None:
        self.driver = driver
        self.home_page = IndexPage(driver)
        self.setting_page = SettingPage(driver)

    def change_language_steps(self) -> None:
        home_button = self.home_page.select_home_button()
        if "خانه" in str(home_button.get_attribute("content-desc")):
            self.home_page.click_setting_button_farsi()
            self.setting_page.click_language_button_farsi()
        else:
            self.home_page.click_setting_button_english()
            self.setting_page.click_language_button_english()

        farsi_option = self.setting_page.select_farsi_option()
        english_otpion = self.setting_page.select_english_option()

        if farsi_option.is_selected():
            self.setting_page.click_english_option()
        elif english_otpion.is_selected():
            self.setting_page.click_farsi_option()
