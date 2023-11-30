from infra.base import Base
import random
import string


class AddHomePage(Base):
    home_title_field = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,523][1036,668]']",
    )
    address_menue = (
        "xpath",
        "//android.widget.Button[@content-desc='Address']",
    )
    country_menue = (
        "xpath",
        "//android.view.View[@bounds='[72,1144][1009,1331]']",
    )
    country_option = (
        "xpath",
        "//android.widget.Button[@content-desc='ایران']",
    )  # selecting Iran country
    province_menue = (
        "xpath",
        "//android.view.View[@bounds='[72,1359][1009,1532]']",
    )
    province_option = (
        "xpath",
        "//android.widget.Button[@content-desc='اصفهان']",
    )
    city_menue = (
        "xpath",
        "//android.view.View[@bounds='[72,1559][1009,1733]']",
    )
    city_option = (
        "xpath",
        "//android.widget.Button[@content-desc='ابریشم']",
    )
    address_field = (
        "xpath",
        "//android.widget.EditText[@bounds='[72,1774][1009,1920]']",
    )
    confirm_button = ("xpath", "//android.widget.Button[@content-desc='Confirm']")
    room_name_field = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,701][1036,847]']",
    )

    def click_home_title(self):
        self.click(self.home_title_field)

    def click_address_menue(self):
        self.click(self.address_menue)

    def click_country_menue(self):
        return self.click(self.country_menue)

    def click_country_option(self):
        return self.click(self.country_option)

    def click_province_menue(self):
        return self.click(self.province_menue)

    def click_province_option(self):
        return self.click(self.province_option)

    def click_city_menue(self):
        return self.click(self.city_menue)

    def click_city_option(self):
        return self.click(self.city_option)

    def click_address_field(self):
        return self.click(self.address_field)

    def click_confirm_button(self):
        return self.click(self.confirm_button)

    def click_room_name_field(self):
        return self.click(self.room_name_field)

    def random_text(self) -> str:
        characters = string.ascii_letters
        text_length = 10
        random_text = ""
        for _ in range(text_length):
            random_index = random.randint(0, len(characters) - 1)
            random_char = characters[random_index]
            random_text += random_char
        return random_text
