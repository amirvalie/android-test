from actions.change_language_action import ChangeLanguageAction
from utils.setup_driver import AppiumDriverSetup
from actions.create_home_action import CreateHome
from actions.logout_action import LogoutAction
from actions.login_action import LoginAction
from actions.add_reminder_action import ReminderAction

appium_driver_setup = AppiumDriverSetup()
driver = appium_driver_setup.setup_driver()

# create_home = CreateHome(driver)
# create_home.create_home_steps()

# chaage_lang = ChangeLanguageAction(driver)
# chaage_lang.change_language_steps()

# logout = LogoutAction(driver)
# logout.logout_steps()

login = LoginAction(driver)
login.login_steps("test", "test")

# remider = ReminderAction(driver)
# remider.reminder_steps()
