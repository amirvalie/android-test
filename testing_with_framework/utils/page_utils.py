from time import sleep
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.webelement import WebElement


class PageUtils:
    def __init__(self, driver):
        self.driver = driver

    # get elements
    # posts_icon = ('accessibility_id', 'Posts') > Sample Locator Value
    def get_element(self, locator: tuple) -> WebElement | Exception:
        """
        Returns element based on provided locator.

        Locator include the method and locator value in a tuple.
        :param locator:
        :return:
        """

        method = locator[0]
        values = locator[1]
        try:
            return self.get_element_by_type(method, values)
        except:
            raise NoSuchElementException

    def get_element_by_type(self, method: str, value: str):
        if method == "accissibility_id":
            return self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=value)
        elif method == "class":
            return self.driver.find_element(by=AppiumBy.CLASS_NAME, value=value)
        elif method == "id":
            return self.driver.find_element(by=AppiumBy.ID, value=value)
        elif method == "xpath":
            print(value)
            print(method)
            return self.driver.find_element(by=AppiumBy.XPATH, value=value)
        elif method == "name":
            return self.driver.find_element(by=AppiumBy.NAME, value=value)
        else:
            return Exception("invalid locator method")

    # element visible
    # def is_visible(self, locator):
    #     try:
    #         self.get_element(locator).is_displayed()
    #         return True
    #     except NoSuchElementException:
    #         return False

    def wait_visible(self, locator, timeout=25):
        i = 0
        while i != timeout:
            try:
                return self.get_element(locator)
            except NoSuchElementException:
                sleep(1)
                i += 1
        raise Exception(
            "Element never became visible: %s (%s)" % (locator[0], locator[1])
        )

    # clicks and taps
    def click(self, locator):
        element = self.wait_visible(locator)
        element.click()

    def tap(self, locator):
        element = self.wait_visible(locator)
        element.tap()

    def hide_keyboard(self):
        try:
            sleep(1)
            self.driver.hide_keyboard()
        except WebDriverException:
            pass

    def send_keys(self, locator, text):
        element = self.wait_visible(locator)
        element.send_keys(text)
        # sleep(0.5)

    def clear(self, locator):
        element = self.wait_visible(locator)
        element.clear()
        sleep(0.5)

    # get text
    def get_text(self, locator):
        element = self.wait_visible(locator)
        return element.text

    def teardown_driver(self):
        self.driver.quite()
