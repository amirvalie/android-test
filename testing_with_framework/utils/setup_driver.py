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
    # Initialize the Appium driver
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(30)
    return driver
