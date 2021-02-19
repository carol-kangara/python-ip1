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
    def tearDown(self):
        '''
        This method cleans up after  every test has run
        '''
    def test_save_multiple-credentials:
        '''
        test_save_multiple_credentials to check if we can save multiple contact
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials=Credentials("instagram", "ckas", "!#$@*@)__+(*&*^%!")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    def test delete_credentials():
        '''
        This is a test  if we can removed the accounts we no longer need
        '''
        self.new_credentials.save_credentials()
        test_credentials=Credentials("instagram", "ckas", "!#$@*@)__+(*&*^%!")
        self.new_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_credentials_by_account_name(self):
        '''
        This is a test  to check if we can find credential using
        account name and display information
        ''' 
        self.new_credentials.save_credentials()
        test_credentials=Credentials("instagram", "ckas", "!#$@*@)__+(*&*^%!")
        self.new_credentials.save_credentials() 

        found_credentials=Credentials.find_by_account_name("instagram")

        self.assertEqual(found_credentials.account_user_name,test_credentials.account_user_name) 



if __name__ == '__main__':
    unittest.main()
          