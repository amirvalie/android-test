from utils.page_utils import PageUtils
from appium.webdriver.webelement import WebElement


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.page_utils = PageUtils(self.driver)

    def get_element(self, locator) -> WebElement | Exception:
        return self.page_utils.get_element(locator)

    def get_element_by_type(self, method, value):
        self.page_utils.get_element_by_type(method, value)

    def wait_visible(self, locator, timeout=10):
        self.page_utils.wait_visible(locator, timeout)

    def click(self, locator):
        self.page_utils.click(locator)

    def tap(self, locator):
        self.page_utils.tap(locator)

    def send_keys(self, locator, text):
        self.page_utils.send_keys(locator, text)

    def clear(self, locator):
        self.page_utils.clear(locator)

    def hide_keyboard(self):
        self.page_utils.hide_keyboard()

    def wait(self, locator):
        self.page_utils.wait(locator)

    def get_text(self, locator):
        return self.page_utils.get_text(locator)

    def teardown_driver(self):
        self.teardown_driver()
