from time import sleep
from .base import Base


class LoginPage(Base):
    login_button: tuple = ("xpath", "//android.widget.Button[@content-desc='Login']")
    username_field: tuple = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,905][1036,1051]']",
    )
    password_field: tuple = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,1185][1036,1331]']",
    )
    otp_field: tuple = ("class", "android.widget.EditText")

    submit_button: tuple = ("xpath", "//android.widget.Button[@content-desc='Confirm']")

    def click_login_button(self) -> None:
        self.page_utils.get_element(self.login_button).click()

    def select_login_button(self):
        return self.page_utils.get_element(self.login_button)

    def click_username_field(self) -> None:
        self.page_utils.get_element(self.username_field).click()

    def click_password_field(self) -> None:
        self.page_utils.get_element(self.login_button).click()

    def click_otp_button(self) -> None:
        self.page_utils.get_element(self.otp_field).click()

    def click_submit_button(self) -> None:
        self.page_utils.get_element(self.submit_button)

    def input_username_field(self, data: str) -> None:
        obj = self.page_utils.get_element(self.username_field)
        obj.click()
        obj.send_keys(data)
        self.page_utils.hide_keyboard()

    def input_password(self, data: str) -> None:
        obj = self.page_utils.get_element(self.password_field)
        obj.click()
        obj.send_keys(data)
        self.page_utils.hide_keyboard()

    def input_otp(self) -> None:
        otp_code = input("OTP code:")
        obj = self.page_utils.get_element(self.otp_field)
        self.page_utils.hide_keyboard()
        sleep(2)
        obj.click()
        obj.send_keys(otp_code)
        self.page_utils.hide_keyboard()
