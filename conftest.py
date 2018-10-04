import allure
import pytest
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def get_driver(request):
    driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    yield
    driver.close()
















@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:  # we only look at actual failing test calls, not setup/teardown
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)
