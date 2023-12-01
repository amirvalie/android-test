from .base import Base


class SettingPage(Base):
    language_button_english = ("xpath", "//android.view.View[@content-desc='Language']")
    language_button_farsi = ("xpath", "//android.view.View[@content-desc='زبان']")
    farsi_option = ("xpath", "//android.widget.RadioButton[@content-desc='فارسی']")
    english_option = ("xpath", "//android.widget.RadioButton[@content-desc='English']")
    profile_button = ("xpath", "//android.view.View[@bounds='[39,259][1042,689]']")
    logout_button = ("xpath", "//android.view.View[@content-desc='Log Out']")
    confirm_logout_button = ("xpath", "//android.view.View[@content-desc='ok']")

    def click_language_button_farsi(self):
        self.page_utils.get_element(self.language_button_farsi).click()

    def click_language_button_english(self):
        self.page_utils.get_element(self.language_button_english).click()

    def click_english_option(self):
        self.page_utils.get_element(self.english_option).click()

    def click_farsi_option(self):
        self.page_utils.get_element(self.farsi_option).click()

    def select_farsi_option(self):
        return self.page_utils.get_element(self.farsi_option)

    def select_english_option(self):
        return self.page_utils.get_element(self.english_option)

    def click_profile_button(self):
        self.page_utils.get_element(self.profile_button).click()

    def click_logout_button(self):
        self.page_utils.get_element(self.logout_button).click()

    def click_confirm_logout_button(self):
        self.page_utils.get_element(self.confirm_logout_button).click()
