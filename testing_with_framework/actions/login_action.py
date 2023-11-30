from pages.login_page import LoginPage


class LoginAction:
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginPage(driver)

    def login_steps(self, username: str, password: str):
        self.login.click_login_button()
        self.login.click_username_field()
        self.login.input_username_field(username)
        self.login.click_password_field()
        self.login.input_password(password)
        self.login.click_submit_button()
        self.login.input_otp()
        self.login.click_submit_button()
        self.login.teardown_driver()
