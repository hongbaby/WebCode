from pages.pagebase import PageBase


class LoginPage(PageBase):
    USERNAME_ID = "username"
    PASSWORD_ID = "password"
    LOGIN_BUTTON_XPATH = "//button[contains(.,'Sign In')]"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://qa.englishtown.com/partner/englishcenters"
        self.browser.get(self.url)

    @property
    def element_username(self):
        return self.wait_until_id_presence(self.USERNAME_ID)

    @property
    def element_password(self):
        return self.wait_until_id_presence(self.PASSWORD_ID)

    @property
    def element_login_button(self):
        return self.wait_until_xpath_presence(self.LOGIN_BUTTON_XPATH)
