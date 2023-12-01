from .base import Base


class ReminderPage(Base):
    assistant_button: tuple = (
        "xpath",
        "//android.view.View[@bounds='[242,1996][441,2070]']",
    )
    reminder_button: tuple = (
        "xpath",
        "//android.view.View[@bounds='[239,272][506,352]']",
    )
    food_name_field: tuple = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,501][1036,646]']",
    )

    food_category_menue: tuple = (
        "xpath",
        "//android.view.View[@bounds='[44,839][513,965]']",
    )
    food_category_option: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='Beverage']",
    )
    expire_date_button: tuple = (
        "xpath",
        "//android.view.View[@bounds='[568,839][1036,965]']",
    )
    choose_expire_date: tuple = (
        "xpath",
        "android.view.View[@bounds='[478,1333][602,1448]']",
    )

    expire_date_ok_button: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='OK']",
    )

    confirm_button: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='Confirm']",
    )

    def click_assistant_button(self) -> None:
        self.page_utils.get_element(self.assistant_button).click()

    def click_reminder_button(self) -> None:
        self.page_utils.get_element(self.reminder_button).click()

    def input_food_name_field(self, value: str) -> None:
        obj = self.page_utils.get_element(self.food_name_field)
        obj.click()
        obj.send_keys(value)

    def click_category_menue(self) -> None:
        self.page_utils.get_element(self.food_category_menue).click()

    def click_category_option(self) -> None:
        self.page_utils.get_element(self.food_category_option).click()

    def click_expire_date_button(self) -> None:
        self.page_utils.get_element(self.expire_date_button).click()

    def click_expire_date_ok_button(self) -> None:
        self.page_utils.get_element(self.expire_date_ok_button).click()

    def click_confirm_button(self) -> None:
        self.page_utils.get_element(self.confirm_button).click()
