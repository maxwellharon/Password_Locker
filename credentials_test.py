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


    def test_save_credentials(self):
        '''
        Test case to test if the contact object is saved into the credentials
        list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test", "t_un", "t_u@gmail", "pwd")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)


    def test_delete_credentials(self):
        '''
        Test if we can remove credentials from our credentials contact_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test", "t_un", "t_u@gmail", "pwd")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)


    def test_find_credentials_by_account_name(self):
        '''
        this will check if we can find a contact by phone number and display
        information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "t_uname", "t_uname@gmail", "passwd")
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_account_name("Twitter")

        self.assertEqual(found_credentials.email, test_credentials.email)


    def test_credentials_exist(self):
        '''
        Check if a credentials exist and return a boolean
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "t_uname", "t_uname@gmail", "passwd")
        test_credentials.save_credentials()

        credentials_exist = Credentials.credentials_exist
        self.assertTrue(credentials_exist)


    def test_display_all_credentials(self):
        '''
        test method that returns a list of all the credentials saved.
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)


    def test_copy_account(self):
        '''
        Test to confirm that we are copying account credentials found
        '''

        self.new_credentials.save_credentials()
        Credentials.copy_username("Max")

        self.assertEqual(self.new_credentials.account_name, pyperclip.paste())

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method run before each test case
        '''
        self.new_user = User("KimaniNjoroge", "passwd")


    def tearDown(self):
        '''
        Method to give an empty array before each test for more accurate results
        '''
        User.user_list = []
    
