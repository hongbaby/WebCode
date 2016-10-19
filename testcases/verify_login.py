from frontend_test_case import FrontendTestCase
from business.verify_login import verify_login


class VerifyLogin(FrontendTestCase):
    def run_test(self):
        self.browser = self.create_web_browser()
        verify_login(self.browser, "stest42410", "1")

if __name__ == '__main__':
    VerifyLogin().run_test()
