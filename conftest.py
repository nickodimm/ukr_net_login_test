import pytest
import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default='https://ukr.net/', help="Url for navigate to")
    parser.addoption("--headless", action="store", default='true', help="Send any value, differ from 'true' to run "
                                                                        "test without chrome window opening")
    parser.addoption("--elogin", action="store", default=None, help="User email to login")
    parser.addoption("--epass", action="store", default=None, help="User password to login")


def pytest_configure(config):
    os.environ['url'] = config.getoption('--url')
    os.environ['headless'] = config.getoption('--headless')
    os.environ['login'] = config.getoption('--elogin')
    os.environ['pwd'] = config.getoption('--epass')


@pytest.yield_fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    if os.getenv('headless') == 'true':
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    driver.set_window_size(1366, 900)
    yield driver
    driver.quit()
