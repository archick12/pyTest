import allure
import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    driver = item.instance.driver
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:
            # Make the screen-shot if test failed:
            try:
                allure.attach(driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)