from selenium.common.exceptions import NoSuchElementException, WebDriverException
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webelement import AppiumWebElement
from appium import webdriver


class PageUtils:
    def __init__(self, driver: webdriver, use_wait_driver: bool = False):
        self.driver = driver
        if use_wait_driver:
            self.wait = WebDriverWait(self.driver, 10)
        else:
            self.driver.implicitly_wait(40)

    def get_element(self, locator: tuple) -> AppiumWebElement:
        """
        Returns element based on provided locator.

        Locator include the method and locator value in a tuple.
        :param locator:
        :return:
        """
        method = locator[0]
        values = locator[1]
        obj = self.get_element_by_type(method, values)
        print("*** Element object ***", obj)
        return obj

    def get_element_by_type(self, method: str, value: str):
        try:
            return self.driver.find_element(
                by=self.find_element_type(method), value=value
            )
        except:
            print("Can not find element")
            raise NoSuchElementException

    def find_element_type(self, method: str) -> str | Exception:
        if method == "accissibility_id":
            return AppiumBy.ACCESSIBILITY_ID
        elif method == "class":
            return AppiumBy.CLASS_NAME
        elif method == "id":
            return AppiumBy.ID
        elif method == "xpath":
            return AppiumBy.XPATH
        elif method == "name":
            return AppiumBy.NAME
        else:
            return Exception("invalid locator method")

    def wait_visible(self, locator, timeout=25) -> AppiumWebElement:
        try:
            return self.wait.until(
                EC.visibility_of_element_located(
                    (self.find_element_type(locator[0]), locator[1])
                )
            )
        except TimeoutException:
            print("Element not found within 10 seconds")
            raise NoSuchElementException

    def wait_clickable(self, locator: tuple) -> AppiumWebElement:
        try:
            return self.wait.until(
                EC.element_to_be_clickable(
                    (self.find_element_type(locator[0]), locator[1])
                )
            )
        except TimeoutException:
            print("Element not found within 10 seconds")
            raise NoSuchElementException

    def hide_keyboard(self) -> None:
        self.driver.hide_keyboard()
