from base_test_Case import BaseTestCase
from selenium_helper import SeleniumHelper


class FrontendTestCase(BaseTestCase):

    def create_web_browser(self):
        self.driver = SeleniumHelper().open_browser()
        return self.driver

    def close_web_browser(self):
        self.driver.quit()
