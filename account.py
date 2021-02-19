#!/usr/bin/env python3.6
from credentials inport credentials
def create_credentials(account_name,usern,password):
    '''
    function that creates credentials
    '''
    new_credentials=Credentials(account,usern,password)
    return new_credentials
def save_credentials(credentials):
    '''
    functionto save credentials
    ''' 
    credentials.save_credentials()
def del_credentials(credentials):
    '''
    function to deletes credentials
    '''
    credentials.delete_credentials()
def  find_credentials(account_name):
    '''
    function to find credentials by account name
    '''
    return Credentials.find_by_account_name(account_name)
def  check_existing_credentials(account-name):
    '''
    function that checks if a credentials exists with that account name 
    and return a boolean
    '''
    return Credentials.credentials_exist(account_name)
def display_contacts():
    '''
    function that returns all the saved contacts
    '''
    return Credentials.display_credentials()
def main():        