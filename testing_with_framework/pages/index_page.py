from infra.base import Base


class IndexPage(Base):
    setting_button_farsi = (
        "xpath",
        "//android.view.View[@bounds='[838,1996][1036,2070]']",
    )
    setting_button_english = (
        "xpath",
        "//android.view.View[@bounds='[44,1996][242,2070]']",
    )

    add_button = (
        "xpath",
        "//android.widget.Button[@bounds='[132,76][264,208]']",
    )

    add_home_button = (
        "xpath",
        "//android.view.View[@content-desc='Add Home']",
    )

    def click_setting_button_farsi(self):
        self.click(self.setting_button_farsi)

    def click_setting_button_english(self):
        self.click(self.setting_button_english)

    def click_home_button(self):
        return self.click(self.add_home_button)

    def click_add_button(self):
        self.click(self.add_button)

    def select_home_button(self):
        return self.get_element(self.add_home_button)
