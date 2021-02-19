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
        self.new_credentials=Credentials("twitter","karolk","uiaggscvbn")
    def _init(self):
         '''
        Tests if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name,'twitter')
        self.assertEqual(self.new_credentials.account_user_name,'karolk')
        self.assertEqual(self.new_credentials.account_password,'uiaggscvbn')
    def test_save_credentials(self):
        '''
        Case test to checkif the account is saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertTrue(len(Credentials.credentials-list),1)


if __name__ == '__main__':
    unittest.main()
          