import random
import string
from .base import Base


class AddHomePage(Base):
    home_title_field: tuple = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,523][1036,668]']",
    )
    address_menue: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='Address']",
    )
    country_menue: tuple = (
        "xpath",
        "//android.view.View[@bounds='[72,1144][1009,1331]']",
    )
    country_option: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='ایران']",
    )
    province_menue: tuple = (
        "xpath",
        "//android.view.View[@bounds='[72,1359][1009,1532]']",
    )
    province_option: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='اصفهان']",
    )
    city_menue: tuple = (
        "xpath",
        "//android.view.View[@bounds='[72,1559][1009,1733]']",
    )
    city_option: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='ابریشم']",
    )
    address_field: tuple = (
        "xpath",
        "//android.widget.EditText[@bounds='[72,1774][1009,1920]']",
    )
    confirm_button: tuple = (
        "xpath",
        "//android.widget.Button[@content-desc='Confirm']",
    )
    room_name_field: tuple = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,701][1036,847]']",
    )

    def click_home_title(self) -> None:
        self.page_utils.get_element(self.home_title_field).click()

    def input_home_title(self, value: str) -> None:
        obj = self.page_utils.get_element(self.home_title_field)
        obj.click()
        obj.send_keys(value)
        self.page_utils.hide_keyboard()

    def click_address_menue(self) -> None:
        self.page_utils.get_element(self.address_menue).click()

    def click_country_menue(self) -> None:
        self.page_utils.get_element(self.country_menue).click()

    def click_country_option(self) -> None:
        self.page_utils.get_element(self.country_option).click()

    def click_province_menue(self) -> None:
        self.page_utils.get_element(self.province_menue).click()

    def click_province_option(self) -> None:
        self.page_utils.get_element(self.province_option).click()

    def click_city_menue(self) -> None:
        self.page_utils.get_element(self.city_menue).click()

    def click_city_option(self) -> None:
        self.page_utils.get_element(self.city_option).click()

    def input_address_field(self, value: str) -> None:
        obj = self.page_utils.get_element(self.address_field)
        obj.click()
        obj.send_keys(value)
        self.page_utils.hide_keyboard()

    def click_confirm_button(self) -> None:
        self.page_utils.get_element(self.confirm_button).click()

    def click_room_name_field(self) -> None:
        self.page_utils.get_element(self.room_name_field).click()

    def input_room_name_field(self, value: str) -> None:
        obj = self.page_utils.get_element(self.room_name_field)
        obj.click()
        obj.send_keys(value)
        self.page_utils.hide_keyboard()

    def random_text(self) -> str:
        characters = string.ascii_letters
        text_length = 10
        random_text = ""
        for _ in range(text_length):
            random_index = random.randint(0, len(characters) - 1)
            random_char = characters[random_index]
            random_text += random_char
        return random_text
