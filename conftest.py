import pytest
import os
from selenium import webdriver

from src.ukr_net import UkrNet
# from utils.logger import WebDrLogger


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default='https://ukr.net/', help="Url for navigate to")
    parser.addoption("--elogin", action="store", default=None, help="User email to login")
    parser.addoption("--epass", action="store", default=None, help="User password to login")


def pytest_configure(config):
    os.environ['url'] = config.getoption('--url')
    os.environ['login'] = config.getoption('--elogin')
    os.environ['pwd'] = config.getoption('--epass')


@pytest.fixture(scope="class")
def driver(request):
    driver = webdriver.Chrome(os.path.join(os.path.dirname(__file__), 'chromedriver'))
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
#
#
# @pytest.fixture(scope="class")
# def logger(request):
#     logger = WebDrLogger("ukr.net")
#     request.cls.logger = logger
#     yield
