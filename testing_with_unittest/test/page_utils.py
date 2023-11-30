from selenium.common.exceptions import NoSuchElementException, WebDriverException
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

    def get_element_by_type(self, method: str, value: str) -> WebElement | Exception:
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
