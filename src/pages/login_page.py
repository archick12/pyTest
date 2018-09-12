from selenium.webdriver.common.by import By

class LoginPage:
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def login_to_jira(self):
        self.driver.LOGIN_INPUT.clear()
        self.driver.LOGIN_INPUT.send_keys("webinar5")
        self.driver.PASSWORD_INPUT("login-form-password").clear()
        self.driver.PASSWORD_INPUT("login-form-password").send_keys("webinar5")
        self.driver.LOGIN_BUTTON("login").submit()