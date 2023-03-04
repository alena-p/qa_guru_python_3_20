import allure
import pytest
from selene.support.shared import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv

from qa_guru_python_3_20.utils import attachments


@pytest.fixture(scope="function", autouse=True)
def driver_config():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities(
        {
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": os.getenv("app_id"),
            "bstack:options": {
                "projectName": "Wiki mibile",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack session",
                "userName": os.getenv("b_user_name"),
                "accessKey": os.getenv("b_access_key"),
            },
        }
    )

    with allure.step("Define driver"):
        browser.config.driver = webdriver.Remote(
            os.getenv("remote_url"), options=options
        )

    yield
    attachments.add_video(browser)
    browser.quit()
