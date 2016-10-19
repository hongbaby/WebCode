from frontend_test_case import FrontendTestCase
from business.verify_login import verify_login
from business import initialize_env


class VerifyLogin(FrontendTestCase):

    @initialize_env
    def run_test(self):
        # self.browser = self.create_web_browser()
        verify_login("stest42410", "1")

if __name__ == '__main__':
    VerifyLogin().run_test()
