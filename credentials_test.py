import unittest
import pyperclip
from credentials import Credentials
from user import User

class TestCredentials(unittest.TestCase):
    '''
    This is a Yest class   that defines test cases for our credentials class behaviours.

    Args:
        unittest.TestCase: Testcase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method to before each test case.
        '''

        self.new_credentials = Credentials("IG", "_thrills", "jkodhe@gmail.com", "password")

    def tearDown(self):
        '''
        Method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []
