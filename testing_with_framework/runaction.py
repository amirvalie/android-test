from actions.change_language_action import ChangeLanguageAction
from utils.setup_driver import exec_driver
from actions.create_home_action import CreateHome
from actions.logout_action import LogoutAction
from actions.login_action import LoginAction
from actions.add_reminder_action import ReminderAction

driver = exec_driver()

# create_home = CreateHome(driver)
# create_home.create_home_steps()

# chaage_lang = ChangeLanguageAction(driver)
# chaage_lang.change_language_steps()

# logout = LogoutAction(driver)
# logout.logout_steps()

login = LoginAction(driver)
login.login_steps("AmirValiee", "amir12@$A")

# remider = ReminderAction(driver)
# remider.reminder_steps()
