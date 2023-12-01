from pages.assistant_page import ReminderPage


class ReminderAction:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.reminder_page = ReminderPage(driver)

    def reminder_steps(self):
        self.reminder_page.click_assistant_button()
        self.reminder_page.click_reminder_button()
        self.reminder_page.input_food_name_field("Gormeh sabzi")
        self.reminder_page.click_category_menue()
        self.reminder_page.click_category_option()
        self.reminder_page.click_expire_date_button()
        self.reminder_page.click_expire_date_ok_button()
        self.reminder_page.click_confirm_button()
