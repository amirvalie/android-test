from appium.webdriver.common.appiumby import AppiumBy
from unittest import TestCase
from driver_connection import AppiumDriverSetup
from page_utils import PageUtils


class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.appium_driver_setup = AppiumDriverSetup()
        self.driver = self.appium_driver_setup.setup_driver()
        self.page_utils = PageUtils(self.driver)

    def tearDown(self) -> None:
        self.appium_driver_setup.teardown_driver()

    def test_login(self):
        login_info = {
            "username": "test",
            "password": "test",
        }
        self.driver.implicitly_wait(30)
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Login']")
        ).click()
        username_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,905][1036,1051]']")
        )
        username_field.click()
        username_field.send_keys(login_info.get("username"))
        self.driver.hide_keyboard()
        password_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,1185][1036,1331]']")
        )
        password_field.click()
        password_field.send_keys(login_info.get("password"))
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Login']")
        ).click()
        otp_field = self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@bounds='[154,997][926,1129]']")
        )
        # otp_button.click()
        # otp_button.send_keys(user_input)
        verification_code = input("Enter your otp:")
        for digit in verification_code:
            otp_field.send_keys(digit)
            time.sleep(0.2)  # Add a 0.2 second delay between digit inputs
        # Press the enter key to submit the verification code
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Confirm']")
        ).click()

        def test_logout(self):
            self.driver.implicitly_wait(30)
            self.page_utils.get_element(
                ("xpath", "//android.view.View[@bounds='[44,1996][242,2070]']")
            ).click()
            self.page_utils.get_element(
                ("xpath", "//android.view.View[@bounds='[39,259][1042,689]']")
            ).click()
            self.page_utils.get_element(
                ("xpath", "//android.view.View[@content-desc='Log Out']")
            ).click()
            self.page_utils.get_element(
                ("xpath", "//android.view.View[@content-desc='Ok']")
            ).click()

    def signup(self):
        signup_info = {
            "username": "test",
            "password": "test",
            "email": "test",
            "phone_number": "test",
        }
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Sign up']")
        ).click()
        phone_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,960][1036,1106]']")
        ).click()
        phone_field.click()
        phone_field.send_keys(signup_info.get("phone_numbers"))
        otp_field = self.driver.find_element(
            by=AppiumBy.XPATH,
            value="//android.widget.Button[@bounds='[154,997][926,1129]']",
        )
        verification_code = input("Enter your otp:")
        for digit in verification_code:
            otp_field.send_keys(digit)
            time.sleep(0.2)  # Add a 0.2 second delay between digit inputs
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Confirm']")
        ).click()
        username_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,905][1036,1051]']")
        )
        username_field.click()
        username_field.send_keys(signup_info.get("username"))
        self.driver.hide_keyboard()
        password_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[44,1185][1036,1331]']")
        )
        password_field.click()
        password_field.send_keys(signup_info.get("password"))
        self.driver.hide_keyboard()
        email_field = self.page_utils.get_element(
            ("xpath", "//android.widget.EditText[@bounds='[50,1405][149,1447]']")
        )
        email_field.click()
        email_field.send_keys(signup_info.get("email"))
        self.driver.hide_keyboard()
        self.page_utils.get_element(
            ("xpath", "//android.widget.Button[@content-desc='Sign up']")
        ).click()
