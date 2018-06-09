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

        self.new_credentials = Credentials("Max", "_Max", "maxwell_haron@icloud.com", "maxisawesome")

    def tearDown(self):
        '''
        Method that does clean up after each test case has run
        '''
        Credentials.credentials_list = []


    def test_credentials_init(self):
        '''
        Created a test that tests if the ibject has been initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name, "Max")
        self.assertEqual(self.new_credentials.user_name, "_Max")
        self.assertEqual(self.new_credentials.email, "maxwell_haron@icloud.com")
        self.assertEqual(self.new_credentials.password, "maxisawesome")
