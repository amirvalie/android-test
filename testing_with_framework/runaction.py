from actions.change_language_action import LanguageActions
from utils.setup_driver import exec_driver
from actions.create_home_action import CreateHome
from actions.logout_action import LogoutAction
from actions.login_action import LoginAction

driver = exec_driver()

login = LoginAction(driver)
login.login_steps("test", "test@$A")
