from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    LOGIN_BUTTON = (By.ID, "login")
    driver = None

    def __init__(self, driver):
        self.driver = driver

    def login_to_jira(self):
        self.driver.find_element(*self.LOGIN_INPUT).clear()
        self.driver.find_element(*self.LOGIN_INPUT).send_keys("webinar5")
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("webinar5")
        self.driver.find_element(*self.LOGIN_BUTTON).submit()

    def at_page(self):
        return "System Dashboard - Hillel IT School JIRA" in self.driver.title

    def open(self):
        self.driver.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")
        return self
