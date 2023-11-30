from appium import webdriver


class AppiumDriverSetup:
    def __init__(self):
        self.driver = None

    def setup_driver(self):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "14",
            "deviceName": "Android Emulator",
            "app": "/home/amir/Downloads/Programs/Smartboom.apk",
            "noReset": True,
        }
        # Initialize the Appium driver
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return self.driver

    def teardown_driver(self):
        # Quit the driver
        if self.driver:
            self.driver.quit()
