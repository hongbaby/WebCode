from settings import set_logger
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from data.objects import Container

logger = set_logger()

instance = Container()


def initialize_env(func):
    def wrapper(*args):
        if len(args) != 0:
            if hasattr(args[0], 'browser'):
                browser = getattr(args[0], 'browser')
            else:
                browser = webdriver.Chrome()
        else:
            browser = webdriver.Chrome()

        assert isinstance(browser, WebDriver)
        func(*args)
    return wrapper


def get_browser():
    if hasattr(instance, 'browser') and isinstance(instance.browser, WebDriver):
        return instance.browser
    else:
        raise EnvironmentError("You must initialize business at first!")

