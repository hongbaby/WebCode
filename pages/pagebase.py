from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class PageBase(object):
    def __init__(self, browser):
        self._browser = browser
        self._url = ''

    @property
    def browser(self):
        return self._browser

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url

    @property
    def get(self):
        return self.browser.get(self.url)

    def wait_until(self, method, message='', timeout=60,):
        return WebDriverWait(self.browser, timeout).until(method, message)

    def wait_until_xpath_presence(self, xpath):
        return self.wait_until(ec.presence_of_element_located((By.XPATH, xpath)))

    def wait_until_id_presence(self, element_id):
        return self.wait_until(ec.presence_of_element_located((By.ID, element_id)))

    def wait_until_element_visible(self, element):
        return self.wait_until(ec.visibility_of(element))

    def verify_current_page_url(self, page_url=None, exact_match=False):
        if page_url is None:
            page_url = self.url

        if exact_match:
            assert page_url == self.browser.current_url
        else:
            assert page_url in self.browser.current_url, "%s is not in %s" % (page_url, self.browser.current_url)
