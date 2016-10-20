import os
from testcases.verify_login import VerifyLogin

working_dir = os.path.dirname(os.path.abspath(__file__))
tests_dir = os.path.join(working_dir, 'testcases')

if __name__ == '__main__':
    VerifyLogin().run_test()
