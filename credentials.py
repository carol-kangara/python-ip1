import pyperclip
class Credentials:
    '''
    This is a class that generates new instances of account credential storage
    '''
    credentials_list=[] #empty account list
    def save_credentials(self):
        '''
        This is a method for saving added account
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        This is a method for deleting an account that is no longer used
        '''  
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_account_name(cls,account_name): 
        '''
        This is a method for finding an account using the account name
        which now displays credentials details that matches the account
        ''' 
        for credentials in cls.credentials_list:
            if credentials.account_name==account_name:
                return credentials
    @classmethod
    def credentials_exist(cls,account_name): 
         '''
        This is a method for finding an account using the account name
        which now displays credentials details that matches the account
        ''' 
        for credentials in cls.credentials_list:
            if credentials.account_name==account_name:
                return True

        return False 
    @classmethod
    def display_credentials:
        '''
        method that returns credentials list
        '''
        return cls.credentials_list
    @classmethod
    def copy_account_password(cls,account_name):
        Credentials_found=Credentials.find_by_account_name(account_name)
        pyperclip.copy(contact_found.account_password)

    def __init__(self,account_name,account_user_name,account_password):
        '''
        we have created 4 arguments,the first argument is self.
        Args:
        self.account_name=account_name
        self.account_user_name=account_user_name
        self.account_password=account_password
        '''