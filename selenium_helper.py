from selenium import webdriver


class SeleniumHelper(object):
    def open_browser(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(60)

        return self.browser

