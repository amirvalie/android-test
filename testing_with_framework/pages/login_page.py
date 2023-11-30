from infra.base import Base


class LoginPage(Base):
    login_button = ("xpath", "//android.widget.Button[@content-desc='Login']")
    username_field = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,905][1036,1051]']",
    )
    password_field = (
        "xpath",
        "//android.widget.EditText[@bounds='[44,1185][1036,1331]']",
    )
    otp_field = ("xpath", "//android.widget.Button[@bounds='[154,997][926,1129]']")
    submit_button = ("xpath", "//android.widget.Button[@content-desc='Confirm']")

    def click_login_button(self):
        self.click(self.login_button)

    def click_username_field(self):
        self.click(self.username_field)

    def click_password_field(self):
        self.click(self.login_button)

    def click_otp_button(self):
        self.click(self.otp_field)

    def click_submit_button(self):
        self.click(self.submit_button)

    def input_username_field(self, data: str):
        self.send_keys(self.username_field, data)
        self.hide_keyboard()

    def input_password(self, data: str):
        self.send_keys(self.password_field, data)
        self.hide_keyboard()

    def input_otp(self):
        otp_code = input("Etner your OTP:")
        self.send_keys(self.otp_field, otp_code)
