import pytest
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASS')
    url = os.getenv('SELENOID_URL')

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()