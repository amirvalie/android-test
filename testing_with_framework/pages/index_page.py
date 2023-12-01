from .base import Base


class IndexPage(Base):
    setting_button_farsi = (
        "xpath",
        "//android.view.View[@bounds='[838,1996][1036,2070]']",
    )
    setting_button_english = (
        "xpath",
        "//android.view.View[@bounds='[44,1996][242,2070]']",
    )
    home_button = ("xpath", "//android.view.View[@bounds='[441,1973][639,2094]']")
    add_button = (
        "xpath",
        "//android.widget.Button[@bounds='[132,76][264,208]']",
    )

    add_home_button = (
        "xpath",
        "//android.view.View[@content-desc='Add Home']",
    )

    add_device_button = (
        "xpath",
        "//android.view.View[@bounds='[242,1996][441,2070]']",
    )

    def click_setting_button_farsi(self):
        self.page_utils.get_element(self.setting_button_farsi).click()

    def click_setting_button_english(self):
        self.page_utils.get_element(self.setting_button_english).click()

    def click_home_button(self):
        self.page_utils.get_element(self.add_home_button).click()

    def click_add_button(self):
        self.page_utils.get_element(self.add_button).click()

    def select_home_button(self):
        return self.page_utils.get_element(self.home_button)

    def select_add_device_button(self):
        self.page_utils.get_element(self.add_device_button).click()
