import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from src.pages.header_page import HeaderPage
from src.pages.login_page import LoginPage


class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.login_page = LoginPage(self.driver)
        self.header_page = HeaderPage(self.driver)

    @pytest.mark.regression
    @pytest.mark.P1
    @pytest.mark.skip(reason="NMB-12222 User authorization is blocked by advertisement")
    def test_login_to_jira_page_object(self):
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login_to_jira()
        assert self.header_page.at_page()

    def teardown_method(self):
        self.driver.close()