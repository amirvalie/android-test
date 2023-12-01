from .base import Base
from appium.webdriver.webelement import AppiumWebElement


class IndexPage(Base):
    setting_button_farsi: tuple = (
        "xpath",
        "//android.view.View[@bounds='[838,1996][1036,2070]']",
    )
    setting_button_english: tuple = (
        "xpath",
        "//android.view.View[@bounds='[44,1996][242,2070]']",
    )
    home_button: tuple = (
        "xpath",
        "//android.view.View[@bounds='[441,1973][639,2094]']",
    )
    add_button: tuple = (
        "xpath",
        "//android.widget.Button[@bounds='[132,76][264,208]']",
    )

    add_home_button: tuple = (
        "xpath",
        "//android.view.View[@content-desc='Add Home']",
    )

    add_device_button: tuple = (
        "xpath",
        "//android.view.View[@bounds='[242,1996][441,2070]']",
    )

    def click_setting_button_farsi(self) -> None:
        self.page_utils.get_element(self.setting_button_farsi).click()

    def click_setting_button_english(self) -> None:
        self.page_utils.get_element(self.setting_button_english).click()

    def click_home_button(self) -> None:
        self.page_utils.get_element(self.add_home_button).click()

    def click_add_button(self) -> None:
        self.page_utils.get_element(self.add_button).click()

    def select_home_button(self) -> AppiumWebElement:
        return self.page_utils.get_element(self.home_button)

    def select_add_device_button(self) -> None:
        self.page_utils.get_element(self.add_device_button).click()
