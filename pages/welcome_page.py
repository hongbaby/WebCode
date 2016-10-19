from pages.pagebase import PageBase


class WelcomePage(PageBase):
    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://qa.englishtown.com/school/englishcenters/welcome"
