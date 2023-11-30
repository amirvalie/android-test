from pages.add_home_page import AddHomePage
from pages.index_page import IndexPage


class CreateHome:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.add_home = AddHomePage(driver)
        self.index = IndexPage(driver)

    def create_home(self):
        self.index.click_add_button()
        self.index.click_home_button()
        self.add_home.click_home_title()
        self.add_home.send_keys(
            self.add_home.home_title_field, f"Home {self.add_home.random_text()}"
        )
        self.driver.hide_keyboard()
        self.add_home.click_address_menue()
        self.add_home.click_country_menue()
        self.add_home.click_country_option()
        self.add_home.click_province_menue()
        self.add_home.click_province_option()
        self.add_home.click_city_menue()
        self.add_home.click_city_option()
        self.add_home.click_address_field()
        self.add_home.send_keys(self.add_home.address_field, "Test")
        self.driver.hide_keyboard()
        self.add_home.click_confirm_button()
        self.add_home.click_room_name_field()
        self.add_home.send_keys(self.add_home.room_name_field, "Room Four")
        self.add_home.click_confirm_button()
