from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from src.pages.login_page import LoginPage

driver = None
login_page = None

def test_login_to_jira():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    login_page = LoginPage(driver)
    driver.get("http://jira.hillel.it:8080/secure/Dashboard.jspa")
    assert "System Dashboard - Hillel IT School JIRA" in driver.title
    login_page.login_to_jira()

    profile_logo_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header-details-user-fullname")))
    assert profile_logo_element.is_displayed() == True
    driver.close()
