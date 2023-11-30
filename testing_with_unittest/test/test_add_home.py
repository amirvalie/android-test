import random
import string
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from unittest import TestCase
from driver_connection import AppiumDriverSetup
from page_utils import PageUtils


def random_text() -> str:
    characters = string.ascii_letters
    text_length = 10
    random_text = ""
    for _ in range(text_length):
        random_index = random.randint(0, len(characters) - 1)
        random_char = characters[random_index]
        random_text += random_char
    return random_text


class TestCreateHome(TestCase):
    def setUp(self) -> None:
        self.appium_driver_setup = AppiumDriverSetup()
        self.driver = self.appium_driver_setup.setup_driver()
        self.page_utils = PageUtils(self.driver)

    def tearDown(self) -> None:
        self.appium_driver_setup.teardown_driver()

    def test_home(self):
        self.driver.implicitly_wait(30)
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@bounds='[132,76][264,208]']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.view.View[@content-desc='Add Home']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,523][1036,668]']")
        ).click()
        home_title_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,523][1036,668]']")
        )
        home_title_field.click()
        home_title_field.send_keys(f"New Home {random_text()}")
        self.driver.hide_keyboard()
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Address']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.view.View[@bounds='[72,1144][1009,1331]']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='ایران']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.view.View[@bounds='[72,1359][1009,1532]']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='اصفهان']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.view.View[@bounds='[72,1559][1009,1733]']")
        ).click()
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='ابریشم']")
        ).click()
        address_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[72,1774][1009,1920]']")
        )
        address_field.click()
        address_field.send_keys("shahin shahr maskan mehr khyaban kordad")
        self.driver.hide_keyboard()
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Confirm']")
        ).click()
        room_name = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,701][1036,847]']")
        )
        room_name.click()
        room_name.send_keys("Living room")
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Confirm']")
        ).click()
