from business import initialize_env
from business.verify_login import verify_login
from frontend_test_case import FrontendTestCase


class VerifyLogin(FrontendTestCase):

    @initialize_env
    def run_test(self):
        verify_login("stest42410", "1")

if __name__ == '__main__':
    VerifyLogin().run_test()
