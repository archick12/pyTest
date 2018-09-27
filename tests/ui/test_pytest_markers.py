import random

import allure
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

    @allure.title("Create issue UI")
    @pytest.mark.regression
    @pytest.mark.P1
    def test_login_to_jira_page_object(self):
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.login_to_jira()
        assert self.header_page.at_page()

    @allure.title("Test to be skipped")
    @pytest.mark.feature
    @pytest.mark.skip(reason="NMB-12222 User authorization is blocked by advertisement")
    def test_to_be_skipped(self):
        # TODO: implement this test
        pass

    @allure.title("Unstable test")
    @pytest.mark.flaky(reruns=3, reruns_delay=1)
    def test_unstable(self):
        assert random.randint(1, 2) == 2

    def teardown_method(self):
        self.driver.close()