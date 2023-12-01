from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


def exec_driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "14",
        "deviceName": "Android Emulator",
        "app": "/home/amir/Downloads/Programs/Smartboom.apk",
        "noReset": True,
    }
    print("**************************** Driver Setup ****************************")
    # Initialize the Appium driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(30)
    return driver


class AppiumDriverSetup:
    def __init__(self) -> None:
        self.driver = None

    def setup_driver(self) -> webdriver:
        print("**************************** Driver Setup ****************************")
        desired_caps: dict = {
            "platformName": "Android",
            "platformVersion": "14",
            "deviceName": "Android Emulator",
            "app": "/home/amir/Downloads/Programs/Smartboom.apk",
            "noReset": True,
        }
        # Initialize the Appium driver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return self.driver

    def teardown_driver(self) -> None:
        # Quit the driver
        if self.driver:
            self.driver.quit()
