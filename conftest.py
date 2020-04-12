import pytest
import os
from selenium import webdriver

from src.ukr_net import UkrNet


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


@pytest.fixture(scope="class")
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    if os.getenv('headless') == 'true':
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)
    driver.set_window_size(1366, 900)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("driver")
@pytest.fixture(scope="class")
def ukr_net(request):
    ukr_net = UkrNet(request.cls.driver, request.config.option.url)
    request.cls.ukr_net = ukr_net
    yield
