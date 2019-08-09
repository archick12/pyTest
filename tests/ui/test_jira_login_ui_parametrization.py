import pytest
from src.pages.header_page import HeaderPage
from src.pages.login_page import LoginPage


@pytest.mark.usefixtures("get_driver")
class TestLogin:

    @pytest.mark.parametrize("login, passwd, rez",
                             [
                                 ("admin", "changeme", "please try again."),
                                 ("admin", "wrongPass", "please try again"),
                                 ("wrongLogin", "changeme", "System Dashboard"),
                             ]
                             )
    def test_login_to_jira_page_object(self, login, passwd, rez):
        self.login_page = LoginPage(self.driver)
        self.header_page = HeaderPage(self.driver)
        self.login_page.open()
        assert self.login_page.at_page()
        self.login_page.enter_name(login)
        self.login_page.enter_password(passwd)
        self.login_page.click_login_button()
        assert self.login_page.wait_for_text_to_appear(rez)
