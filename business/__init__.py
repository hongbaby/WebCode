from selenium.webdriver.remote.webdriver import WebDriver

from data.objects import Container
from selenium_helper import SeleniumHelper
from settings import set_logger

logger = set_logger()

instance = Container()


def initialize_env(func):
    def wrapper(*args):
        browser = SeleniumHelper().open_browser()

        instance.browser = browser
        func(*args)
    return wrapper


def get_browser():
    if hasattr(instance, 'browser') and isinstance(instance.browser, WebDriver):
        return instance.browser
    else:
        raise EnvironmentError("You must initialize business at first!")
