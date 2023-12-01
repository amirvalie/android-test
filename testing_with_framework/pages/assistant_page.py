from .base import Base


class ReminderPage(Base):
    assistant_button = (
        "xpath",
        "//android.view.View[@bounds='[242,1996][441,2070]']",
    )
    reminder_button = (
        "xpath",
        "//android.view.View[@bounds='[239,272][506,352]']",
    )
    food_name_field = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,501][1036,646]']",
    )

    food_category_menue = (
        "xpath",
        "//android.view.View[@bounds='[44,839][513,965]']",
    )
    food_category_option = (
        "xpath",
        "//android.widget.Button[@content-desc='Beverage']",
    )
    expire_date_button = (
        "xpath",
        "//android.view.View[@bounds='[568,839][1036,965]']",
    )
    choose_expire_date = (
        "xpath",
        "android.view.View[@bounds='[478,1333][602,1448]']",
    )

    expire_date_ok_button = ("xpath", "//android.widget.Button[@content-desc='OK']")

    confirm_button = ("xpath", "//android.widget.Button[@content-desc='Confirm']")

    # [86,398][994,1822]
    # //android.view.View[@content-desc="SELECT DATE Fri, Dec 1"]

    def click_assistant_button(self):
        self.page_utils.get_element(self.assistant_button).click()

    def click_reminder_button(self):
        self.page_utils.get_element(self.reminder_button).click()

    def input_food_name_field(self, value: str):
        obj = self.page_utils.get_element(self.food_name_field)
        obj.click()
        obj.send_keys(value)

    def click_category_menue(self):
        self.page_utils.get_element(self.food_category_menue).click()

    def click_category_option(self):
        self.page_utils.get_element(self.food_category_option).click()

    def click_expire_date_button(self):
        self.page_utils.get_element(self.expire_date_button).click()

    def click_expire_date_ok_button(self):
        self.page_utils.get_element(self.expire_date_ok_button).click()

    def click_confirm_button(self):
        self.page_utils.get_element(self.confirm_button).click()


# for testing
# //android.widget.ImageView[@content-desc="Gormeh sabzi Expire 2023-12-01"]
# [44,1521][1036,1713]
