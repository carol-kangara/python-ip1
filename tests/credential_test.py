import unittest#importing the unit test module
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviour
    '''
    def setUp(self):
        '''
        the set up method to run before each code
        '''
        self.new_account=Credentials("twitter","karolk","uiaggscvbn")
    def _init(self):
         '''
        Tests if the object is initialized properly
        '''
        self.assertEqual(self.new_account.account_name,'twitter')
        self.assertEqual(self.new_account.account_user_name,'karolk')
        self.assertEqual(self.new_account.account_password,'uiaggscvbn')
if __name__ == '__main__':
    unittest.main()
          