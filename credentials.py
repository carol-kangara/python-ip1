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
        This is a method for deleting an aaccount that is no longer used
        '''  

    def __init__(self,account_name,account_user_name,account_password):
        '''
        we have created 4 arguments,the first argument is self.
        Args:
        self.account_name=account_name
        self.account_user_name=account_user_name
        self.account_password=account_password
        '''