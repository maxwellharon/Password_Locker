import unittest
from userdata import  Userdata

class TestUserdata(unittest.TestCase):
    '''
    Test for user information
    '''
    def setUp(self):
        '''
        Set up method to run before each test
        '''
        self.new_userdata = Userdata("Max","Haron","maxwell_haron@icloud.com","0711223344")

    def test_init(self):

        self.assertEqual(self.new_userdata.first_name,"Max")
        self.assertEqual(self.new_userdata.last_name,"Haron")
        self.assertEqual(self.new_userdata.email,"maxwell_haron@icloud.com" )
        self.assertEqual(self.new_userdata.number,"0711223344")

if __name__ == '__main__':
    unittest.main()
