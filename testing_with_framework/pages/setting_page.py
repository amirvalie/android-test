from infra.base import Base


class SettingPage(Base):
    language_button = ("xpath", "//android.view.View[@content-desc='Language']")
    language_button = ("xpath", "//android.view.View[@content-desc='زبان']")
    farsi_option = ("xpath", "//android.widget.RadioButton[@content-desc='فارسی']")
    english_option = ("xpath", "//android.widget.RadioButton[@content-desc='English']")
    profile_button = ("xpath", "//android.view.View[@bounds='[39,259][1042,689]']")
    logout_button = ("xpath", "//android.view.View[@content-desc='Log Out']")
    confirm_logout_button = ("xpath", "//android.view.View[@content-desc='Ok']")

    def click_language_button_farsi(self):
        self.click(self.language_button)

    def click_language_button_english(self):
        self.click(self.language_button)

    def click_english_option(self):
        self.click(self.english_option)

    def click_farsi_option(self):
        self.click(self.farsi_option)

    def select_farsi_option(self):
        self.get_element(self.farsi_option)

    def select_english_option(self):
        self.get_element(self.english_option)

    def click_profile_button(self):
        self.click(self.profile_button)

    def click_logout_button(self):
        self.click(self.logout_button)

    def click_confirm_logout_button(self):
        self.click(self.confirm_logout_button)
