from pages.add_home_page import AddHomePage
from pages.index_page import IndexPage


class CreateHome:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.add_home = AddHomePage(driver)
        self.index = IndexPage(driver)

    def create_home_steps(self):
        self.index.click_add_button()
        self.index.click_home_button()
        self.add_home.input_home_title(f"Home {self.add_home.random_text()}")
        self.add_home.click_address_menue()
        self.add_home.click_country_menue()
        self.add_home.click_country_option()
        self.add_home.click_province_menue()
        self.add_home.click_province_option()
        self.add_home.click_city_menue()
        self.add_home.click_city_option()
        self.add_home.input_address_field("shahin shahr maskan mehr khyaban kordad")
        self.add_home.click_confirm_button()
        self.add_home.input_room_name_field("Room Four")
        self.add_home.click_confirm_button()
